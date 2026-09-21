"""Official Elastic SIEM rule catalog + Chinese localization records."""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import tomllib
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parent
HASH_FIELDS = (
    "name",
    "description",
    "note",
    "setup",
    "query",
    "false_positives",
    "tags",
    "severity",
    "risk_score",
    "from",
    "interval",
    "type",
    "language",
)
ZH_FIELDS = (
    "name",
    "description",
    "note",
    "setup",
    "false_positives",
    "tags",
    "investigation_fields",
)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_config(path: Path | None = None) -> dict[str, Any]:
    cfg_path = path or ROOT / "config.yaml"
    text = cfg_path.read_text(encoding="utf-8")
    try:
        return tomllib.loads(text)
    except tomllib.TOMLDecodeError:
        return _parse_simple_yaml(text)


def _parse_simple_yaml(text: str) -> dict[str, Any]:
    data: dict[str, Any] = {}
    section: str | None = None
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].rstrip()
        if not line.strip():
            continue
        if not line.startswith(" ") and line.endswith(":") and ":" == line.strip()[-1]:
            key = line[:-1].strip()
            section = key
            data[key] = {}
            continue
        if ":" not in line:
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        value = value.strip()
        parsed: Any
        if value.lower() in {"true", "false"}:
            parsed = value.lower() == "true"
        elif value.startswith(("http://", "https://", "socks5://")) or value:
            parsed = value
        else:
            parsed = value
        if line.startswith("  ") and section:
            data[section][key] = parsed
        else:
            section = None
            data[key] = parsed
    return data


def apply_proxy(cfg: dict[str, Any]) -> None:
    proxy = cfg.get("proxy") or {}
    mapping = {
        "http": "http_proxy",
        "https": "https_proxy",
        "all": "all_proxy",
    }
    for src, env in mapping.items():
        val = proxy.get(src)
        if val and not os.environ.get(env) and not os.environ.get(env.upper()):
            os.environ[env] = str(val)
            os.environ[env.upper()] = str(val)


def cache_dir(cfg: dict[str, Any]) -> Path:
    return ROOT / cfg.get("cache_dir", ".cache/detection-rules")


def localized_dir(cfg: dict[str, Any]) -> Path:
    return ROOT / cfg.get("localized_dir", "localized")


def reports_dir(cfg: dict[str, Any]) -> Path:
    return ROOT / cfg.get("reports_dir", "reports")


def content_hash(payload: dict[str, Any]) -> str:
    subset = {k: payload.get(k) for k in HASH_FIELDS}
    blob = json.dumps(subset, ensure_ascii=False, sort_keys=True, default=str)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()


def category_from_official_relpath(relpath: str) -> str:
    parts = Path(relpath).parts
    if parts and parts[0] == "rules_building_block":
        return "building_block"
    if len(parts) >= 2 and parts[0] == "rules":
        if parts[1] == "integrations" and len(parts) >= 3:
            return f"integrations/{parts[2]}"
        return parts[1]
    return "unknown"


def official_relpaths(cfg: dict[str, Any]) -> Iterable[Path]:
    cache = cache_dir(cfg)
    yield from (cache / "rules").rglob("*.toml")
    if cfg.get("include_building_block", True):
        bb = cache / "rules_building_block"
        if bb.exists():
            yield from bb.rglob("*.toml")


def parse_official_toml(path: Path, cache: Path) -> dict[str, Any] | None:
    raw = path.read_bytes()
    data = tomllib.loads(raw.decode("utf-8"))
    meta = data.get("metadata") or {}
    rule = data.get("rule") or {}
    rule_id = rule.get("rule_id")
    if not rule_id:
        return None
    relpath = path.relative_to(cache).as_posix()
    snapshot = {
        "name": rule.get("name"),
        "description": rule.get("description"),
        "note": rule.get("note"),
        "setup": rule.get("setup"),
        "query": rule.get("query"),
        "false_positives": rule.get("false_positives") or [],
        "tags": rule.get("tags") or [],
        "severity": rule.get("severity"),
        "risk_score": rule.get("risk_score"),
        "from": rule.get("from"),
        "interval": rule.get("interval"),
        "type": rule.get("type"),
        "language": rule.get("language"),
    }
    return {
        "rule_id": str(rule_id),
        "relpath": relpath,
        "category": category_from_official_relpath(relpath),
        "maturity": meta.get("maturity"),
        "updated_date": meta.get("updated_date"),
        "creation_date": meta.get("creation_date"),
        "integration": meta.get("integration"),
        "stem": path.stem,
        "official": snapshot,
        "content_hash": content_hash(snapshot),
        "filename": path.name,
        "raw_rule": rule,
        "raw_meta": meta,
    }


def load_official_catalog(cfg: dict[str, Any]) -> dict[str, dict[str, Any]]:
    cache = cache_dir(cfg)
    catalog: dict[str, dict[str, Any]] = {}
    include_deprecated = bool(cfg.get("include_deprecated", False))
    for path in official_relpaths(cfg):
        if path.name == "README.md":
            continue
        parsed = parse_official_toml(path, cache)
        if not parsed:
            continue
        if not include_deprecated and parsed["category"] == "_deprecated":
            continue
        catalog[parsed["rule_id"]] = parsed
    return catalog


def git_head(cfg: dict[str, Any]) -> dict[str, str]:
    cache = cache_dir(cfg)
    if not (cache / ".git").exists():
        return {"commit": "", "date": "", "subject": ""}
    commit = subprocess.check_output(
        ["git", "rev-parse", "--short", "HEAD"], cwd=cache, text=True
    ).strip()
    meta = subprocess.check_output(
        ["git", "log", "-1", "--format=%ci%x09%s"], cwd=cache, text=True
    ).strip()
    date, _, subject = meta.partition("\t")
    return {"commit": commit, "date": date, "subject": subject}


def fetch_official(cfg: dict[str, Any]) -> dict[str, str]:
    apply_proxy(cfg)
    cache = cache_dir(cfg)
    cache.parent.mkdir(parents=True, exist_ok=True)
    repo = cfg.get("official_repo", "https://github.com/elastic/detection-rules")
    ref = cfg.get("official_ref", "main")
    env = os.environ.copy()
    sparse_paths = ["rules", "rules_building_block", "detection_rules/etc"]
    if cache.exists() and (cache / ".git").exists():
        subprocess.check_call(["git", "fetch", "--depth", "1", "origin", ref], cwd=cache, env=env)
        subprocess.check_call(["git", "sparse-checkout", "set", *sparse_paths], cwd=cache, env=env)
        subprocess.check_call(["git", "checkout", "-q", "FETCH_HEAD"], cwd=cache, env=env)
    else:
        if cache.exists():
            raise RuntimeError(f"cache path exists but is not a git repo: {cache}")
        subprocess.check_call(
            [
                "git",
                "clone",
                "--filter=blob:none",
                "--sparse",
                "--depth",
                "1",
                "--branch",
                ref,
                repo,
                str(cache),
            ],
            env=env,
        )
        subprocess.check_call(["git", "sparse-checkout", "set", *sparse_paths], cwd=cache, env=env)
    return git_head(cfg)


_VERSION_LOCK: dict[str, Any] | None = None


def version_lock_path(cfg: dict[str, Any] | None = None) -> Path:
    if cfg is None:
        return ROOT / ".cache/detection-rules/detection_rules/etc/version.lock.json"
    return cache_dir(cfg) / "detection_rules/etc/version.lock.json"


def load_version_lock(cfg: dict[str, Any] | None = None) -> dict[str, Any]:
    global _VERSION_LOCK
    if _VERSION_LOCK is not None:
        return _VERSION_LOCK
    path = version_lock_path(cfg)
    if not path.exists():
        _VERSION_LOCK = {}
        return _VERSION_LOCK
    data = json.loads(path.read_text(encoding="utf-8"))
    _VERSION_LOCK = data if isinstance(data, dict) else {}
    return _VERSION_LOCK


def prebuilt_version(rule_id: str, cfg: dict[str, Any] | None = None) -> int | None:
    entry = load_version_lock(cfg).get(str(rule_id))
    if isinstance(entry, dict) and entry.get("version") is not None:
        return int(entry["version"])
    return None


def zh_from_kibana(obj: dict[str, Any]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key in ZH_FIELDS:
        if key in obj:
            out[key] = obj[key]
    return out


KIBANA_TYPES = (
    "eql",
    "query",
    "saved_query",
    "threshold",
    "threat_match",
    "machine_learning",
    "new_terms",
    "esql",
)
DEFAULT_LANGUAGE = {
    "eql": "eql",
    "esql": "esql",
    "query": "kuery",
    "threshold": "kuery",
    "new_terms": "kuery",
    "threat_match": "kuery",
    "saved_query": "kuery",
}
TOML_SKIP = {"threat", "new_terms"}
# Kibana 从检测引擎导出时每条规则都有的外壳（最后一行导出统计除外）。
# 不含 id / created_* / updated_*：那是集群 Saved Object，导入时由 Kibana 生成。
KIBANA_ENVELOPE_DEFAULTS: dict[str, Any] = {
    "actions": [],
    "exceptions_list": [],
    "risk_score_mapping": [],
    "severity_mapping": [],
    "required_fields": [],
    "related_integrations": [],
    "output_index": "",
    "revision": 1,
    "enabled": True,
    "max_signals": 100,
    "to": "now",
    "false_positives": [],
    "references": [],
    "threat": [],
}
KIBANA_EXPORT_MARKERS = (
    "immutable",
    "rule_source",
    "version",
    "actions",
    "exceptions_list",
    "risk_score_mapping",
    "severity_mapping",
    "required_fields",
    "output_index",
    "revision",
)
LEDGER_KEYS = (
    "kind",
    "category",
    "stem",
    "official_relpath",
    "official_snapshot",
    "query_override",
    "localized_at",
    "source",
)


def ledger_path(cfg: dict[str, Any]) -> Path:
    return localized_dir(cfg) / "ledger.json"


def load_ledger(cfg: dict[str, Any]) -> dict[str, Any]:
    path = ledger_path(cfg)
    if not path.exists():
        return {"rules": {}}
    data = json.loads(path.read_text(encoding="utf-8"))
    if "rules" not in data:
        data = {"rules": data}
    return data


def save_ledger(cfg: dict[str, Any], ledger: dict[str, Any]) -> None:
    path = ledger_path(cfg)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def drop_nones(obj: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in obj.items() if v is not None}


def is_wrapper_record(obj: dict[str, Any]) -> bool:
    return obj.get("kind") in {"official_zh", "custom", "unmatched"} and isinstance(obj.get("zh"), dict)


def flatten_false_positives(values: Any) -> list[str]:
    out: list[str] = []
    for item in values or []:
        text = str(item).strip()
        if text:
            out.append(text)
    return out


def coerce_history_window_start(value: Any) -> str | None:
    """Kibana import expects a date-math string, e.g. now-5d — same as 样例 ndjson."""
    if value is None:
        return None
    if isinstance(value, str):
        return value
    if isinstance(value, dict):
        return value.get("value") or value.get("history_window_start")
    if isinstance(value, list) and value:
        return coerce_history_window_start(value[0])
    return str(value)


def is_full_kibana_export(obj: Any) -> bool:
    return isinstance(obj, dict) and all(k in obj for k in KIBANA_EXPORT_MARKERS)


def convert_new_terms(nt: Any) -> tuple[list[str] | None, str | None]:
    if not isinstance(nt, dict):
        return None, None
    fields = nt.get("value") if nt.get("field") == "new_terms_fields" else nt.get("value") or nt.get("new_terms_fields")
    if isinstance(fields, str):
        fields = [fields]
    hist = coerce_history_window_start(nt.get("history_window_start"))
    return fields, hist


def apply_kibana_envelope(
    obj: dict[str, Any],
    zh: dict[str, Any] | None = None,
    cfg: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """补齐 Kibana 检测引擎导出外壳，与 linux_windows_chinese_rule.ndjson 同形。"""
    out = dict(obj)
    zh = zh or {}
    rid = str(out.get("rule_id") or "")
    locked = prebuilt_version(rid, cfg) if rid else None
    if not isinstance(out.get("version"), int):
        if out.get("version") is not None:
            out["version"] = int(out["version"])
        else:
            out["version"] = locked if locked is not None else 1
    prebuilt = locked is not None
    if "immutable" not in out:
        out["immutable"] = bool(prebuilt)
    if "rule_source" not in out:
        if prebuilt:
            customized = [{"field_name": k} for k in ZH_FIELDS if k in zh and zh[k] is not None]
            out["rule_source"] = {
                "type": "external",
                "is_customized": True,
                "customized_fields": customized,
                "has_base_version": True,
            }
        else:
            out["rule_source"] = {"type": "internal"}
    for key, default in KIBANA_ENVELOPE_DEFAULTS.items():
        if key not in out:
            out[key] = list(default) if isinstance(default, list) else default
    if isinstance(out.get("machine_learning_job_id"), str):
        out["machine_learning_job_id"] = [out["machine_learning_job_id"]]
    if "investigation_fields" not in out:
        out["investigation_fields"] = {"field_names": []}
    elif isinstance(out["investigation_fields"], list):
        out["investigation_fields"] = {"field_names": out["investigation_fields"]}
    if out.get("author") and isinstance(out["author"], str):
        out["author"] = [out["author"]]
    if out.get("references") is None:
        out["references"] = []
    if "note" not in out:
        out["note"] = ""
    if "setup" not in out:
        out["setup"] = ""
    if "history_window_start" in out:
        coerced = coerce_history_window_start(out.get("history_window_start"))
        if coerced:
            out["history_window_start"] = coerced
        else:
            out.pop("history_window_start", None)
    return drop_nones(out)


def normalize_kibana_import(
    obj: dict[str, Any],
    cfg: dict[str, Any] | None = None,
    zh: dict[str, Any] | None = None,
) -> dict[str, Any]:
    return apply_kibana_envelope(obj, zh=zh, cfg=cfg)


def kibana_from_toml(
    official_hit: dict[str, Any],
    zh: dict[str, Any],
    query_override: str | None = None,
    cfg: dict[str, Any] | None = None,
) -> dict[str, Any]:
    rule = dict(official_hit.get("raw_rule") or {})
    meta = official_hit.get("raw_meta") or {}
    out: dict[str, Any] = {}
    for key, value in rule.items():
        if key in TOML_SKIP:
            continue
        out[key] = value
    if "threat" in rule and rule["threat"]:
        out["threat"] = rule["threat"]
    fields, hist = convert_new_terms(rule.get("new_terms"))
    if fields:
        out["new_terms_fields"] = fields
    if hist:
        out["history_window_start"] = hist
    rule_type = out.get("type") or "query"
    out["type"] = rule_type
    if not out.get("language"):
        out["language"] = DEFAULT_LANGUAGE.get(str(rule_type))
    if query_override:
        out["query"] = query_override
    out["false_positives"] = flatten_false_positives(out.get("false_positives"))
    if not out.get("from"):
        out["from"] = "now-9m"
    if not out.get("interval"):
        out["interval"] = "5m" if rule_type != "machine_learning" else "15m"
    integration = meta.get("integration")
    if integration and not out.get("related_integrations"):
        pkgs = integration if isinstance(integration, list) else [integration]
        out["related_integrations"] = [{"package": p, "version": "*"} for p in pkgs]
    for key in ZH_FIELDS:
        if key in zh and zh[key] is not None:
            out[key] = zh[key]
    if out.get("false_positives") is not None:
        out["false_positives"] = flatten_false_positives(out.get("false_positives"))
    return normalize_kibana_import(out, cfg, zh)


def overlay_zh_on_kibana(
    kibana: dict[str, Any],
    zh: dict[str, Any],
    query_override: str | None = None,
    cfg: dict[str, Any] | None = None,
) -> dict[str, Any]:
    out = dict(kibana)
    for key in ZH_FIELDS:
        if key in zh and zh[key] is not None:
            out[key] = zh[key]
    if query_override:
        out["query"] = query_override
    return normalize_kibana_import(out, cfg, zh)


def validate_kibana_rule(obj: dict[str, Any]) -> None:
    missing = [k for k in ("name", "description", "rule_id", "type", "severity", "risk_score") if obj.get(k) in (None, "")]
    if missing:
        raise ValueError(f"检测规则缺少必填字段: {', '.join(missing)}")
    if obj["type"] not in KIBANA_TYPES:
        raise ValueError(f"非法 type: {obj['type']}")
    if obj["severity"] not in {"low", "medium", "high", "critical"}:
        raise ValueError(f"非法 severity: {obj['severity']}")
    if not isinstance(obj["risk_score"], (int, float)):
        raise ValueError("risk_score 必须是数字")
    if obj["type"] != "machine_learning" and not obj.get("query"):
        raise ValueError("非机器学习规则必须有 query")
    if "history_window_start" in obj and not isinstance(obj["history_window_start"], str):
        raise ValueError("history_window_start 必须是字符串，例如 now-5d")
    if not isinstance(obj.get("version"), int):
        raise ValueError("检测规则必须有整数 version（预置规则用官方 version.lock.json）")
    missing_env = [k for k in KIBANA_EXPORT_MARKERS if k not in obj]
    if missing_env:
        raise ValueError(f"缺少 Kibana 导出外壳字段: {', '.join(missing_env)}")


def build_kibana_payload(
    record: dict[str, Any],
    official: dict[str, dict[str, Any]] | None = None,
    cfg: dict[str, Any] | None = None,
) -> dict[str, Any]:
    zh = record.get("zh") or zh_from_kibana(record)
    query_override = record.get("query_override")
    existing = record.get("kibana_export")
    rid = record["rule_id"]
    hit = (official or {}).get(rid)
    if is_full_kibana_export(existing):
        return overlay_zh_on_kibana(existing, zh, query_override, cfg)
    if hit and hit.get("raw_rule"):
        return kibana_from_toml(hit, zh, query_override, cfg)
    if existing and existing.get("name") and existing.get("type"):
        return overlay_zh_on_kibana(existing, zh, query_override, cfg)
    raise ValueError(f"{rid} 无法生成可导入规则：既无 Kibana 导出，也无官方 TOML")


def localized_record_path(cfg: dict[str, Any], category: str, stem: str) -> Path:
    return localized_dir(cfg) / "rules" / category / f"{stem}.ndjson"


def write_localized(cfg: dict[str, Any], record: dict[str, Any], official: dict[str, dict[str, Any]] | None = None) -> Path:
    stem = record.get("stem") or re.sub(r"[^a-zA-Z0-9._-]+", "-", record["rule_id"])
    record["stem"] = stem
    if official is None:
        official = load_official_catalog(cfg)
    kibana = build_kibana_payload(record, official, cfg)
    kibana = normalize_kibana_import(kibana, cfg, record.get("zh"))
    validate_kibana_rule(kibana)
    path = localized_record_path(cfg, record["category"], stem)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(kibana, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    old_json = path.with_suffix(".json")
    if old_json.exists():
        old_json.unlink()
    ledger = load_ledger(cfg)
    ledger.setdefault("rules", {})
    entry = {k: record.get(k) for k in LEDGER_KEYS if record.get(k) is not None}
    entry["rule_id"] = record["rule_id"]
    if not entry.get("official_snapshot") and official.get(record["rule_id"]):
        hit = official[record["rule_id"]]
        entry["official_snapshot"] = {
            "name": hit["official"]["name"],
            "updated_date": hit["updated_date"],
            "maturity": hit["maturity"],
            "content_hash": hit["content_hash"],
        }
        entry["official_relpath"] = hit["relpath"]
        entry.setdefault("kind", "official_zh")
    ledger["rules"][record["rule_id"]] = entry
    save_ledger(cfg, ledger)
    return path


def _read_record_file(path: Path) -> dict[str, Any] | None:
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return None
    try:
        obj = json.loads(text)
    except json.JSONDecodeError:
        obj = json.loads(text.splitlines()[0])
    if isinstance(obj, list):
        obj = obj[0] if obj else None
    if not isinstance(obj, dict) or not obj.get("rule_id"):
        return None
    obj["_path"] = path.relative_to(ROOT).as_posix()
    return obj


def _category_from_localized_path(path: Path, cfg: dict[str, Any]) -> str:
    rel = path.relative_to(localized_dir(cfg) / "rules")
    parts = rel.parts[:-1]
    return "/".join(parts) if parts else "unknown"


def load_localized(cfg: dict[str, Any]) -> dict[str, dict[str, Any]]:
    base = localized_dir(cfg) / "rules"
    found: dict[str, dict[str, Any]] = {}
    if not base.exists():
        return found
    ledger = load_ledger(cfg).get("rules") or {}
    for path in list(base.rglob("*.ndjson")) + list(base.rglob("*.json")):
        obj = _read_record_file(path)
        if not obj:
            continue
        rid = obj["rule_id"]
        if rid in found and path.suffix == ".json":
            continue
        meta = dict(ledger.get(rid) or {})
        if is_wrapper_record(obj):
            kibana = obj.get("kibana_export") or {}
            zh = obj.get("zh") or zh_from_kibana(kibana)
            rec = {
                "kind": obj.get("kind") or meta.get("kind") or "official_zh",
                "rule_id": rid,
                "category": obj.get("category") or meta.get("category") or _category_from_localized_path(path, cfg),
                "official_relpath": obj.get("official_relpath") or meta.get("official_relpath"),
                "stem": obj.get("stem") or path.stem,
                "official_snapshot": obj.get("official_snapshot") or meta.get("official_snapshot"),
                "zh": zh,
                "query_override": obj.get("query_override") or meta.get("query_override"),
                "kibana_export": kibana or None,
                "localized_at": obj.get("localized_at") or meta.get("localized_at"),
                "source": obj.get("source") or meta.get("source"),
                "_path": obj["_path"],
            }
        else:
            rec = {
                "kind": meta.get("kind") or ("custom" if _category_from_localized_path(path, cfg) == "custom" else "official_zh"),
                "rule_id": rid,
                "category": meta.get("category") or _category_from_localized_path(path, cfg),
                "official_relpath": meta.get("official_relpath"),
                "stem": meta.get("stem") or path.stem,
                "official_snapshot": meta.get("official_snapshot"),
                "zh": zh_from_kibana(obj),
                "query_override": meta.get("query_override"),
                "kibana_export": {k: v for k, v in obj.items() if not str(k).startswith("_")},
                "localized_at": meta.get("localized_at"),
                "source": meta.get("source"),
                "_path": obj["_path"],
            }
        found[rid] = rec
    return found


def rewrite_localized_kibana(cfg: dict[str, Any]) -> dict[str, int]:
    official = load_official_catalog(cfg)
    localized = load_localized(cfg)
    stats = {"ok": 0, "failed": 0}
    errors: list[str] = []
    for rid, rec in localized.items():
        try:
            write_localized(cfg, rec, official)
            stats["ok"] += 1
        except Exception as exc:
            stats["failed"] += 1
            errors.append(f"{rid}: {exc}")
    stats["errors"] = errors  # type: ignore[assignment]
    return stats


def import_ndjson(cfg: dict[str, Any], ndjson_path: Path, official: dict[str, dict[str, Any]]) -> dict[str, int]:
    stats = {"official_zh": 0, "custom": 0, "unmatched": 0, "skipped": 0}
    localized_dir(cfg).mkdir(parents=True, exist_ok=True)
    for line in ndjson_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        obj = json.loads(line)
        rule_id = obj.get("rule_id")
        if not rule_id or not obj.get("name"):
            stats["skipped"] += 1
            continue
        official_hit = official.get(rule_id)
        kind = (obj.get("rule_source") or {}).get("type")
        name = obj.get("name") or ""
        is_custom = (
            str(rule_id).startswith("custom-")
            or name.startswith("【自定义】")
            or kind == "internal"
        ) and not official_hit
        if official_hit:
            record = {
                "kind": "official_zh",
                "rule_id": rule_id,
                "category": official_hit["category"],
                "official_relpath": official_hit["relpath"],
                "stem": official_hit["stem"],
                "official_snapshot": {
                    "name": official_hit["official"]["name"],
                    "updated_date": official_hit["updated_date"],
                    "maturity": official_hit["maturity"],
                    "content_hash": official_hit["content_hash"],
                },
                "zh": zh_from_kibana(obj),
                "query_override": None,
                "kibana_export": obj,
                "localized_at": obj.get("updated_at") or utc_now(),
                "source": ndjson_path.name,
            }
            customized = [
                x.get("field_name")
                for x in ((obj.get("rule_source") or {}).get("customized_fields") or [])
            ]
            if "query" in customized:
                record["query_override"] = obj.get("query")
            write_localized(cfg, record, official)
            stats["official_zh"] += 1
        elif is_custom:
            record = {
                "kind": "custom",
                "rule_id": rule_id,
                "category": "custom",
                "official_relpath": None,
                "stem": str(rule_id),
                "zh": zh_from_kibana(obj),
                "kibana_export": obj,
                "localized_at": obj.get("updated_at") or utc_now(),
                "source": ndjson_path.name,
            }
            write_localized(cfg, record, official)
            stats["custom"] += 1
        else:
            record = {
                "kind": "unmatched",
                "rule_id": rule_id,
                "category": "custom",
                "official_relpath": None,
                "stem": str(rule_id),
                "zh": zh_from_kibana(obj),
                "kibana_export": obj,
                "localized_at": obj.get("updated_at") or utc_now(),
                "source": ndjson_path.name,
            }
            write_localized(cfg, record, official)
            stats["unmatched"] += 1
    return stats


def record_official_zh(
    cfg: dict[str, Any],
    official_hit: dict[str, Any],
    zh: dict[str, Any],
    query_override: str | None = None,
) -> Path:
    record = {
        "kind": "official_zh",
        "rule_id": official_hit["rule_id"],
        "category": official_hit["category"],
        "official_relpath": official_hit["relpath"],
        "stem": official_hit["stem"],
        "official_snapshot": {
            "name": official_hit["official"]["name"],
            "updated_date": official_hit["updated_date"],
            "maturity": official_hit["maturity"],
            "content_hash": official_hit["content_hash"],
        },
        "zh": zh,
        "query_override": query_override,
        "localized_at": utc_now(),
        "source": "manual",
    }
    return write_localized(cfg, record, {official_hit["rule_id"]: official_hit})


def diff_catalog(
    cfg: dict[str, Any],
    official: dict[str, dict[str, Any]],
    localized: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    by_cat: dict[str, dict[str, list]] = {}

    def bucket(cat: str) -> dict[str, list]:
        if cat not in by_cat:
            by_cat[cat] = {
                "synced": [],
                "stale": [],
                "missing": [],
                "orphan": [],
                "custom": [],
                "unmatched": [],
            }
        return by_cat[cat]

    official_ids = set(official)
    for rid, off in official.items():
        cat = off["category"]
        loc = localized.get(rid)
        item = {
            "rule_id": rid,
            "official_name": off["official"]["name"],
            "official_relpath": off["relpath"],
            "updated_date": off["updated_date"],
            "maturity": off["maturity"],
        }
        if not loc:
            bucket(cat)["missing"].append(item)
            continue
        item["zh_name"] = (loc.get("zh") or {}).get("name")
        snap = loc.get("official_snapshot") or {}
        stale_reasons = []
        if snap.get("content_hash") and snap.get("content_hash") != off["content_hash"]:
            stale_reasons.append("content_hash")
        if snap.get("updated_date") and snap.get("updated_date") != off["updated_date"]:
            stale_reasons.append("updated_date")
        if stale_reasons:
            item["stale_reasons"] = stale_reasons
            item["localized_updated_date"] = snap.get("updated_date")
            bucket(cat)["stale"].append(item)
        else:
            bucket(cat)["synced"].append(item)

    for rid, loc in localized.items():
        cat = loc.get("category") or "custom"
        kind = loc.get("kind")
        if rid in official_ids:
            continue
        row = {
            "rule_id": rid,
            "zh_name": (loc.get("zh") or {}).get("name"),
            "path": loc.get("_path"),
        }
        if kind == "custom":
            bucket("custom")["custom"].append(row)
        else:
            bucket(cat if cat else "custom")["unmatched" if kind == "unmatched" else "orphan"].append(row)

    def summarize(cat: str, b: dict[str, list]) -> dict[str, Any]:
        official_n = len(b["synced"]) + len(b["stale"]) + len(b["missing"])
        zh_n = len(b["synced"]) + len(b["stale"])
        return {
            "category": cat,
            "official": official_n,
            "localized": zh_n,
            "synced": len(b["synced"]),
            "stale": len(b["stale"]),
            "missing": len(b["missing"]),
            "orphan": len(b["orphan"]),
            "custom": len(b["custom"]),
            "unmatched": len(b["unmatched"]),
            "coverage": round(100.0 * zh_n / official_n, 1) if official_n else (100.0 if b["custom"] else 0.0),
        }

    categories = [summarize(cat, b) for cat, b in sorted(by_cat.items())]
    totals = {
        "official": sum(c["official"] for c in categories),
        "localized": sum(c["localized"] for c in categories),
        "synced": sum(c["synced"] for c in categories),
        "stale": sum(c["stale"] for c in categories),
        "missing": sum(c["missing"] for c in categories),
        "custom": sum(c["custom"] for c in categories),
        "orphan": sum(c["orphan"] for c in categories),
        "unmatched": sum(c["unmatched"] for c in categories),
    }
    unsynced_cats = [
        c["category"]
        for c in categories
        if c["official"] and (c["missing"] or c["stale"])
    ]
    empty_cats = [
        c["category"]
        for c in categories
        if c["official"] and c["localized"] == 0 and c["category"] != "custom"
    ]
    return {
        "generated_at": utc_now(),
        "totals": totals,
        "categories": categories,
        "unsynced_categories": unsynced_cats,
        "never_started_categories": empty_cats,
        "by_category": by_cat,
    }


def parent_category(cat: str) -> str:
    if cat.startswith("integrations/"):
        return "integrations"
    return cat


def rollup_integrations(diff: dict[str, Any]) -> list[dict[str, Any]]:
    groups: dict[str, dict[str, int]] = {}
    for row in diff["categories"]:
        parent = parent_category(row["category"])
        g = groups.setdefault(
            parent,
            {
                "category": parent,
                "official": 0,
                "localized": 0,
                "synced": 0,
                "stale": 0,
                "missing": 0,
                "custom": 0,
            },
        )
        for k in ("official", "localized", "synced", "stale", "missing", "custom"):
            g[k] += row[k]
    out = []
    for g in groups.values():
        g["coverage"] = round(100.0 * g["localized"] / g["official"], 1) if g["official"] else 100.0
        out.append(g)
    return sorted(
        out,
        key=lambda x: (
            1 if x["category"] == "custom" else 0,
            -(x["missing"] or 0),
            x["category"],
        ),
    )


def render_diff_markdown(head: dict[str, str], diff: dict[str, Any]) -> str:
    t = diff["totals"]
    lines = [
        f"# SIEM 规则汉化 diff",
        "",
        f"- 生成时间: `{diff['generated_at']}`",
        f"- 官方 commit: `{head.get('commit')}` ({head.get('date')}) {head.get('subject')}",
        f"- 官方规则: **{t['official']}** | 已汉化: **{t['localized']}** | 同步: {t['synced']} | 过期: **{t['stale']}** | 未汉化: **{t['missing']}**",
        f"- 自定义: {t['custom']} | 官方已删/失配: {t['orphan'] + t['unmatched']}",
        "",
        "## 分类汇总（integrations 按子目录展开前的顶层）",
        "",
        "| 分类 | 官方 | 已汉化 | 同步 | 过期 | 未汉化 | 覆盖率 |",
        "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
    ]
    for row in rollup_integrations(diff):
        if row["category"] == "custom" and not row["official"]:
            lines.append(f"| `custom` | — | {row['custom']} | — | — | — | 自写 |")
            continue
        lines.append(
            f"| `{row['category']}` | {row['official']} | {row['localized']} | {row['synced']} | {row['stale']} | {row['missing']} | {row['coverage']}% |"
        )
    lines += [
        "",
        "## 尚未开始汉化的官方分类",
        "",
    ]
    never = [
        row["category"]
        for row in rollup_integrations(diff)
        if row["official"] and row["localized"] == 0
    ]
    if never:
        for cat in never:
            lines.append(f"- `{cat}`")
    else:
        lines.append("- （无）")
    lines += ["", "## 有 diff 的分类明细", ""]
    for cat in diff["unsynced_categories"]:
        b = diff["by_category"][cat]
        if not (b["missing"] or b["stale"]):
            continue
        lines.append(f"### `{cat}`")
        lines.append("")
        if b["stale"]:
            lines.append(f"过期 {len(b['stale'])} 条（官方已更新，需重跟汉化）：")
            for item in b["stale"][:30]:
                lines.append(
                    f"- `{item['rule_id']}` {item.get('zh_name')} ← {item['official_name']} ({','.join(item.get('stale_reasons') or [])})"
                )
            if len(b["stale"]) > 30:
                lines.append(f"- … 另有 {len(b['stale']) - 30} 条")
            lines.append("")
        if b["missing"]:
            lines.append(f"未汉化 {len(b['missing'])} 条：")
            for item in b["missing"][:40]:
                lines.append(f"- `{item['rule_id']}` {item['official_name']} (`{item['official_relpath']}`)")
            if len(b["missing"]) > 40:
                lines.append(f"- … 另有 {len(b['missing']) - 40} 条，用 `sync.py next --category {cat}` 查看")
            lines.append("")
    custom = diff["by_category"].get("custom", {})
    if custom.get("custom") or custom.get("unmatched"):
        lines += ["## 自定义 / 未匹配", ""]
        for item in (custom.get("custom") or []) + (custom.get("unmatched") or []):
            lines.append(f"- `{item['rule_id']}` {item.get('zh_name')}")
        lines.append("")
    return "\n".join(lines) + "\n"


def write_reports(cfg: dict[str, Any], head: dict[str, str], diff: dict[str, Any]) -> tuple[Path, Path]:
    out = reports_dir(cfg)
    out.mkdir(parents=True, exist_ok=True)
    slim = {k: v for k, v in diff.items() if k != "by_category"}
    slim["stale_ids"] = [
        item["rule_id"]
        for b in diff["by_category"].values()
        for item in b["stale"]
    ]
    md = out / "latest-diff.md"
    js = out / "latest-diff.json"
    md.write_text(render_diff_markdown(head, diff), encoding="utf-8")
    payload = {"official": head, **slim}
    js.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return md, js


IDENTITY_HINTS = re.compile(
    r"account|logon|login|password|passwd|shadow|brute.?force|spray|"
    r"dcsync|kerberos|pre-?auth|as-?rep|credential dump|ntds|\bsam\b|"
    r"group policy|\bgpo\b|privileged group|user account|authentication|"
    r"账号|登录|密码|爆破|凭据|组策略|域控",
    re.I,
)


def list_next(
    official: dict[str, dict[str, Any]],
    localized: dict[str, dict[str, Any]],
    category: str | None = None,
    limit: int = 40,
    identity_only: bool = False,
) -> list[dict[str, Any]]:
    rows = []
    for rid, off in official.items():
        if rid in localized:
            continue
        if category:
            if category == "integrations":
                if not off["category"].startswith("integrations/"):
                    continue
            elif off["category"] != category:
                continue
        name = off["official"]["name"] or ""
        desc = off["official"]["description"] or ""
        if identity_only and not IDENTITY_HINTS.search(f"{name}\n{desc}\n{off['relpath']}"):
            continue
        rows.append(off)
    rows.sort(key=lambda x: (x["category"], x["relpath"]))
    return rows[:limit]


def export_ndjson(cfg: dict[str, Any], dest: Path) -> int:
    localized = load_localized(cfg)
    official = load_official_catalog(cfg)
    n = 0
    dest.parent.mkdir(parents=True, exist_ok=True)
    with dest.open("w", encoding="utf-8") as fh:
        for rec in sorted(localized.values(), key=lambda r: (r.get("category") or "", r.get("rule_id") or "")):
            obj = rec.get("kibana_export")
            if not is_full_kibana_export(obj):
                obj = build_kibana_payload(rec, official, cfg)
            obj = normalize_kibana_import(obj, cfg, rec.get("zh"))
            validate_kibana_rule(obj)
            fh.write(json.dumps(obj, ensure_ascii=False) + "\n")
            n += 1
    return n


def github_blob_url(relpath: str, commit: str) -> str:
    host = "https://github.com/elastic/detection-rules/blob"
    ref = commit or "main"
    return f"{host}/{ref}/{relpath}"
