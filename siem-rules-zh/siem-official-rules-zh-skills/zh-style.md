# 汉化体例（对齐 linux_windows_chinese_rule.ndjson）

汉化不是直译：规则名按 SOC 场景重新定义，并丰富 `description` / `note` / `tags` / `setup` / `investigation_fields`。

## 命名

- 预置：`【默认】<中文场景名>`，ML 规则名末尾加 `（机器学习）`
- 自写：`【自定义】<中文场景名>`
- 跨 Linux+Windows 的认证 ML：名称用「双端」，目录仍是 `ml/`

## tags

从样例组合，不要照搬英官方 tags：

- `操作系统: Linux` / `Windows` / `双端`
- `主题: 身份安全`（按实际主题改）
- `来源: 默认` 或 `来源: 自定义`
- 可选：`规则类型: 机器学习`、`对应需求: …`、`用例: 身份与访问审计`

## note / setup

`note` 用「调查指引」：规则说明、为何重要、调查步骤、常见误报、响应建议。  
`setup` 用短中文「设置说明」，不要整段粘贴官方英文 Fleet 教程。

## 查询

默认保留官方 `query`。仅当 Kibana 导出里 `customized_fields` 含 `query` 时写入 `query_override`。

## 记账 ndjson

每条规则一个 `<stem>.ndjson` 文件，**一行一条**，内容是 Kibana 检测引擎可导入对象（顶层必须有 `name`、`description`、`type`、`severity`、`risk_score`、`rule_id`）。汉化字段写在这些顶层键上，不要再包 `zh`。  
官方 hash 记在 `localized/ledger.json`。`stale` = ledger 里的 `updated_date` / `content_hash` 已落后。
