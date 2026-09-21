#!/usr/bin/env python3.12
"""Sync Elastic official SIEM rules and Chinese localization records."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from siem_rules import (
    diff_catalog,
    export_ndjson,
    fetch_official,
    git_head,
    github_blob_url,
    import_ndjson,
    list_next,
    load_config,
    load_localized,
    load_official_catalog,
    record_official_zh,
    rewrite_localized_kibana,
    write_reports,
)


def cmd_fetch(cfg) -> int:
    head = fetch_official(cfg)
    print(f"official {head['commit']} {head['date']} {head['subject']}")
    return 0


def cmd_diff(cfg, fetch: bool) -> int:
    if fetch:
        head = fetch_official(cfg)
    else:
        head = git_head(cfg)
        if not head.get("commit"):
            print("官方仓库尚未下载，先执行: python3.12 sync.py fetch", file=sys.stderr)
            return 1
    official = load_official_catalog(cfg)
    localized = load_localized(cfg)
    diff = diff_catalog(cfg, official, localized)
    md, js = write_reports(cfg, head, diff)
    print(md.read_text(encoding="utf-8"))
    print(f"报告: {md}")
    print(f"JSON: {js}")
    t = diff["totals"]
    return 0 if t["stale"] == 0 else 2


def cmd_import(cfg, ndjson: Path, fetch: bool) -> int:
    if fetch:
        fetch_official(cfg)
    official = load_official_catalog(cfg)
    stats = import_ndjson(cfg, ndjson, official)
    print(json.dumps(stats, ensure_ascii=False))
    return cmd_diff(cfg, fetch=False)


def cmd_next(cfg, category: str | None, limit: int, identity: bool) -> int:
    official = load_official_catalog(cfg)
    localized = load_localized(cfg)
    head = git_head(cfg)
    rows = list_next(official, localized, category=category, limit=limit, identity_only=identity)
    print(f"# 下一步汉化候选  {len(rows)} 条  commit={head.get('commit')}")
    for off in rows:
        print(
            f"{off['category']}\t{off['rule_id']}\t{off['official']['name']}\t"
            f"{github_blob_url(off['relpath'], head.get('commit') or 'main')}"
        )
    return 0


def cmd_record(cfg, rule_id: str, zh_json: Path) -> int:
    official = load_official_catalog(cfg)
    hit = official.get(rule_id)
    if not hit:
        print(f"官方目录中没有 rule_id={rule_id}", file=sys.stderr)
        return 1
    payload = json.loads(zh_json.read_text(encoding="utf-8"))
    query_override = payload.pop("query_override", None)
    path = record_official_zh(cfg, hit, payload, query_override=query_override)
    print(path)
    return 0


def cmd_export(cfg, dest: Path) -> int:
    n = export_ndjson(cfg, dest)
    print(f"exported {n} rules -> {dest}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="比对 elastic/detection-rules 与本地汉化记录（按官方分类 + custom）"
    )
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("fetch", help="拉取/更新官方仓库（走 config.yaml 代理）")
    d = sub.add_parser("diff", help="按分类输出汉化 diff（默认先 fetch）")
    d.add_argument("--offline", action="store_true", help="不访问网络，只用本地缓存")
    im = sub.add_parser("import-ndjson", help="导入 Kibana 导出的汉化 ndjson 并记账")
    im.add_argument("ndjson", type=Path)
    im.add_argument("--offline", action="store_true")
    n = sub.add_parser("next", help="列出尚未汉化的官方规则，避免重复")
    n.add_argument("--category", help="如 linux / windows / ml / integrations / integrations/okta")
    n.add_argument("--limit", type=int, default=40)
    n.add_argument("--identity", action="store_true", help="只列出账号/登录/凭据相关")
    r = sub.add_parser("record", help="把一条已汉化官方规则写入 localized/")
    r.add_argument("rule_id")
    r.add_argument("zh_json", type=Path, help="含 name/description/note/tags/setup/false_positives/investigation_fields")
    e = sub.add_parser("export-ndjson", help="合并可导入的检测规则 ndjson")
    e.add_argument("-o", "--output", type=Path, required=True)
    sub.add_parser("rebuild", help="把汉化记录重写成 Kibana 可导入的检测规则 ndjson")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    cfg = load_config()
    if args.cmd == "fetch":
        return cmd_fetch(cfg)
    if args.cmd == "diff":
        return cmd_diff(cfg, fetch=not args.offline)
    if args.cmd == "import-ndjson":
        return cmd_import(cfg, args.ndjson.resolve(), fetch=not args.offline)
    if args.cmd == "next":
        return cmd_next(cfg, args.category, args.limit, args.identity)
    if args.cmd == "record":
        return cmd_record(cfg, args.rule_id, args.zh_json)
    if args.cmd == "export-ndjson":
        return cmd_export(cfg, args.output)
    if args.cmd == "rebuild":
        stats = rewrite_localized_kibana(cfg)
        print(json.dumps({k: v for k, v in stats.items() if k != "errors"}, ensure_ascii=False))
        for err in stats.get("errors") or []:
            print(err, file=sys.stderr)
        return 0 if not stats.get("failed") else 1
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
