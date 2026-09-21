---
name: siem-official-rules-zh
description: >
  Syncs Elastic official SIEM detection rules with Chinese localization records
  in siem-rules-zh/. Use whenever the user mentions SIEM 规则, 官方规则, 汉化,
  detection-rules, linux_windows_chinese_rule, 双端, custom 规则, 同步分类,
  stale/missing 规则, or asks to compare/translate Elastic Security prebuilt
  rules. On every such turn, run the sync program first, list diffs vs official,
  then ask which category (or all) to sync before localizing.
---

# SIEM 官方规则汉化同步

每次找你的时候，你都要运行程序看看同步状态，列出与官方的不同，然后询问我要同步什么分类，或者是所有分类。

官方源：https://github.com/elastic/detection-rules  
程序根目录：仓库内 `siem-rules-zh/`（需要 **Python 3.12**）。

未得到用户明确分类（或「所有分类」）之前，**禁止开始汉化**。

## 每次必做（先于回答）

1. 若当前不在仓库根，先定位含 `siem-rules-zh/sync.py` 的项目。
2. 带代理跑 diff（用户本机 Clash 端口，已写入 `siem-rules-zh/config.yaml`）：

```bash
export https_proxy=http://127.0.0.1:7890 http_proxy=http://127.0.0.1:7890 all_proxy=socks5://127.0.0.1:7890
cd siem-rules-zh
python3.12 sync.py diff
```

代理失败时改 `python3.12 sync.py diff --offline`，并说明用的是本地缓存、未拉到最新官方。

3. 读 `siem-rules-zh/reports/latest-diff.md`（或命令 stdout 的分类表）。
4. 在回复里列出与官方的不同（至少：官方 commit、已汉化/过期/未汉化总数、按分类覆盖率、尚未开始的分类、`stale` 条数）。明细太长时只贴汇总表 + 各分类 missing/stale 数量，完整列表指向该 markdown。
5. **停住询问**：要同步哪个分类，还是所有分类。用选择题时选项对齐报告里的顶层分类（`linux` / `windows` / `macos` / `ml` / `cross-platform` / `integrations` / `network` / `apm` / `promotions` / `threat_intel` / `building_block` / `custom`）并加「所有分类」。用户已在本轮写明分类则可跳过询问，仍须先跑 diff。

## 用户选定分类之后

1. `python3.12 sync.py next --category <cat>`（`integrations` 会列出所有集成子目录）。先处理 **stale**（官方已变，重跟汉化），再处理 **missing**。已在 `localized/` 且 hash 未变的不要重做。
2. 汉化写入 `localized/rules/<官方分类>/<stem>.ndjson`（一行一条），`rule_id` 对齐官方；自写规则进 `custom/`。
3. 每条用 `python3.12 sync.py record <rule_id> zh.json` 或等价调用 `record_official_zh`（落盘是 `.ndjson`）。
4. 一批结束后再 `diff --offline`，更新报告。

分类跟官方文件夹，不是跟中文标签：

| 用户说法 | 落盘 |
| --- | --- |
| 双端 / 跨平台认证 ML | `localized/rules/ml/`（官方 `rules/ml/`） |
| 查询类跨平台（如 sudoers） | `localized/rules/cross-platform/` |
| 【自定义】 | `localized/rules/custom/` |

汉化体例见 [zh-style.md](zh-style.md)。
