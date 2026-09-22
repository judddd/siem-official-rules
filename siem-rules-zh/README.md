# SIEM 官方规则同步比对（汉化）

对照 [elastic/detection-rules](https://github.com/elastic/detection-rules) 的 `rules/` 分类，记录已经汉化/丰富过的规则，并按分类做 diff。比官方多一个 **`custom`** 分类（自写规则，样例 `linux_windows_chinese_rule.ndjson` 里的 `【自定义】`）。

汉化不只是翻译：规则名要按 SOC 场景**重新定义**（`【默认】…` / `【自定义】…`），`description` / `note` / `tags` / `setup` 要补调查步骤和对应需求。

需要 Python **3.12**（解析官方 TOML）。官方 detection-rules 缓存在 `.cache/`（不入库），克隆后先 `fetch` 再 `diff`。拉官方仓库走 `config.yaml` 里的代理。

```bash
git clone https://github.com/judddd/siem-official-rules.git
cd siem-official-rules
export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890

cd siem-rules-zh
python3.12 sync.py fetch
python3.12 sync.py diff                 # 默认同步官方后再 diff
python3.12 sync.py diff --offline       # 只用本地缓存
python3.12 sync.py import-ndjson samples/linux_windows_chinese_rule.ndjson --offline
python3.12 sync.py next --category linux --identity
python3.12 sync.py record <rule_id> zh.json   # 输入可仍是多行 JSON；落盘为 .ndjson
python3.12 sync.py pack --list
python3.12 sync.py pack -c linux
python3.12 sync.py pack -c linux -c windows -c custom
python3.12 sync.py pack -c linux,ml -o reports/kibana-import-linux-ml.ndjson
python3.12 sync.py export-ndjson -o reports/kibana-import.ndjson          # 全部
python3.12 sync.py export-ndjson -o reports/kibana-import-linux.ndjson -c linux
python3.12 sync.py rebuild              # 按 Kibana 导入格式重写 localized ndjson
```

| 目录 | 含义 |
| --- | --- |
| `localized/rules/<官方分类>/<stem>.ndjson` | 已汉化预置规则：一文件一行，文件名对齐官方 toml |
| `localized/rules/integrations/<集成>/` | 对齐 `rules/integrations/` |
| `localized/rules/building_block/` | 对齐仓库根上的 `rules_building_block/` |
| `localized/rules/custom/` | 自写规则 |
| `reports/latest-diff.md` | 每次 `diff` 覆盖写入 |

比对账本在 `localized/ledger.json`。`localized/rules/**/*.ndjson` 必须是 Kibana **检测规则导入**格式（含 `name`/`type`/`severity`/`risk_score`），不是汉化包装对象。
