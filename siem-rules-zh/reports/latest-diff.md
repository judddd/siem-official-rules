# SIEM 规则汉化 diff

- 生成时间: `2026-09-22T06:43:13Z`
- 官方 commit: `11e144f` (2026-09-21 14:38:07 +0000) [Docs] Restore rule tag taxonomy guidance dropped in #6839 (#6849)
- 官方规则: **2117** | 已汉化: **1229** | 同步: 1229 | 过期: **0** | 未汉化: **888**
- 自定义: 21 | 官方已删/失配: 0

## 分类汇总（integrations 按子目录展开前的顶层）

| 分类 | 官方 | 已汉化 | 同步 | 过期 | 未汉化 | 覆盖率 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `integrations` | 750 | 2 | 2 | 0 | 748 | 0.3% |
| `cross-platform` | 132 | 1 | 1 | 0 | 131 | 0.8% |
| `threat_intel` | 6 | 0 | 0 | 0 | 6 | 0.0% |
| `apm` | 3 | 0 | 0 | 0 | 3 | 0.0% |
| `building_block` | 129 | 129 | 129 | 0 | 0 | 100.0% |
| `linux` | 372 | 372 | 372 | 0 | 0 | 100.0% |
| `macos` | 100 | 100 | 100 | 0 | 0 | 100.0% |
| `ml` | 45 | 45 | 45 | 0 | 0 | 100.0% |
| `network` | 61 | 61 | 61 | 0 | 0 | 100.0% |
| `promotions` | 26 | 26 | 26 | 0 | 0 | 100.0% |
| `windows` | 493 | 493 | 493 | 0 | 0 | 100.0% |
| `custom` | — | 21 | — | — | — | 自写 |

## 尚未开始汉化的官方分类

- `threat_intel`
- `apm`

## 有 diff 的分类明细

### `apm`

未汉化 3 条：
- `d49cc73f-7a16-4def-89ce-9fc7127d7820` Web Application Suspicious Activity: sqlmap User Agent (`rules/apm/apm_sqlmap_user_agent.toml`)
- `75ee75d8-c180-481c-ba88-ee50129a6aef` Web Application Suspicious Activity: Unauthorized Method (`rules/apm/apm_405_response_method_not_allowed.toml`)
- `a87a4e42-1d82-44bd-b0bf-d9b7f91fb89e` Web Application Suspicious Activity: POST Request Declined (`rules/apm/apm_403_response_to_a_post.toml`)

### `cross-platform`

未汉化 131 条：
- `0871a5d8-6b5f-4a12-a568-fd7bc05bd8db` Node.js Pre or Post-Install Script Execution (`rules/cross-platform/execution_nodejs_pre_or_post_install_script_execution.toml`)
- `55be0398-e72d-4c02-a916-b11d62af0e29` Uncommon DNS Request via Bun or Node.js (`rules/cross-platform/command_and_control_uncommon_dns_request_via_bun_or_nodejs.toml`)
- `f7d588ba-e4b0-442e-879d-7ec39fbd69c5` Potential SAP NetWeaver WebShell Creation (`rules/cross-platform/execution_sap_netweaver_jsp_webshell.toml`)
- `a87d49f0-24ae-4d6e-a0b4-5fd2f6188d6a` Kubectl Secrets Enumeration Across All Namespaces (`rules/cross-platform/discovery_kubectl_secrets_all_namespaces.toml`)
- `da4f56b8-9bc5-4003-a46c-d23616fbc691` PANW and Elastic Defend - Command and Control Correlation (`rules/cross-platform/command_and_control_pan_elastic_defend_c2.toml`)
- `6fa3abe3-9cd8-41de-951b-51ed8f710523` Web Server Potential Spike in Error Response Codes (`rules/cross-platform/reconnaissance_web_server_unusual_spike_in_error_response_codes.toml`)
- `b53f1d73-150d-484d-8f02-222abeb5d5fa` Kubernetes Direct API Request via Curl or Wget (`rules/cross-platform/execution_kubernetes_direct_api_request_via_curl_or_wget.toml`)
- `25a4207c-5c05-4680-904c-6e3411b275fa` Multiple Elastic Defend Alerts from a Single Process Tree (`rules/cross-platform/multiple_alerts_edr_elastic_same_process_tree.toml`)
- `7d02c440-52a8-4854-ad3f-71af7fbb4fc6` Alerts From Multiple Integrations by Source Address (`rules/cross-platform/multiple_alerts_from_different_modules_by_srcip.toml`)
- `c85eb82c-d2c8-485c-a36f-534f914b7663` Virtual Machine Fingerprinting via Grep (`rules/cross-platform/discovery_virtual_machine_fingerprinting_grep.toml`)
- `8d4d0a23-19d3-4186-a6f1-6f0760d2e070` Multiple External EDR Alerts by Host (`rules/cross-platform/multiple_external_edr_alerts_by_host.toml`)
- `f9de0949-94d8-441d-ae9a-8eb1e040acf2` Newly Observed Process Exhibiting High CPU Usage (`rules/cross-platform/impact_newly_observed_process_with_high_cpu.toml`)
- `08933236-b27a-49f6-b04a-a616983f04b9` Alerts From Multiple Integrations by Destination Address (`rules/cross-platform/multiple_alerts_from_different_modules_by_dstip.toml`)
- `ecc0cd54-608e-11ef-ab6d-f661ea17fbce` Suspicious Instance Metadata Service (IMDS) API Command Line Execution (`rules/cross-platform/credential_access_suspicious_instance_metadata_service_api_cli.toml`)
- `29531d20-0e80-41d4-9ec6-d6b58e4a475c` Alerts in Different ATT&CK Tactics by Host (`rules/cross-platform/multiple_alerts_risky_host_esql.toml`)
- `665e7a4f-c58e-4fc6-bc83-87a7572670ac` WebServer Access Logs Deleted (`rules/cross-platform/defense_evasion_deleting_websvr_access_logs.toml`)
- `8670bf41-cb64-4d65-a0d6-78af17cf8f30` Web Server Cloud Metadata SSRF Request (`rules/cross-platform/credential_access_web_server_cloud_imds_ssrf_request.toml`)
- `0d160033-fab7-4e72-85a3-3a9d80c8bff7` Multiple Alerts Involving a User (`rules/cross-platform/multiple_alerts_involving_user.toml`)
- `02275e05-57a1-46ab-a443-7fb444da6b28` Direct Interactive Kubernetes API Request by Unusual Utilities (`rules/cross-platform/execution_d4c_k8s_mda_kubernetes_api_activity_by_unusual_utilities.toml`)
- `a640ef5b-e1da-4b17-8391-468fdbd1b517` Execution via GitHub Actions Runner (`rules/cross-platform/execution_via_github_actions_runner.toml`)
- `45d099b4-a12e-4913-951c-0129f73efb41` Web Server Potential Remote File Inclusion Activity (`rules/cross-platform/discovery_web_server_remote_file_inclusion_activity.toml`)
- `6631a759-4559-4c33-a392-13f146c8bcc4` Potential Spike in Web Server Error Logs (`rules/cross-platform/reconnaissance_web_server_unusual_spike_in_error_logs.toml`)
- `b2c3d4e5-f6a7-8901-bcde-f123456789ab` GenAI Process Compiling or Generating Executables (`rules/cross-platform/defense_evasion_genai_process_compiling_executables.toml`)
- `a1b2c3d4-e5f6-7890-abcd-ef1234567890` GenAI Process Connection to Suspicious Top Level Domain (`rules/cross-platform/command_and_control_genai_process_suspicious_tld_connection.toml`)
- `482a5584-4ce4-4838-b806-0839a39b004f` Potential Tunneling via Tailscaled (`rules/cross-platform/command_and_control_tunneling_via_tailscaled.toml`)
- `58ac2aa5-6718-427c-a845-5f3ac5af00ba` Zoom Meeting with no Passcode (`rules/cross-platform/initial_access_zoom_meeting_with_no_passcode.toml`)
- `84b81b96-58dd-4c0d-9b2e-35023ab5ee88` Suspicious Process Execution by Zoom (`rules/cross-platform/execution_suspicious_process_execution_by_zoom.toml`)
- `cf2b8cf5-3364-4396-b551-42aae9b6d37e` AWS SSM Session Manager Child Process Execution (`rules/cross-platform/execution_aws_ssm_session_manager_child_process.toml`)
- `f0cc239b-67fa-46fc-89d4-f861753a40f5` M365 or Entra ID Identity Sign-in from a Suspicious Source (`rules/cross-platform/initial_access_azure_o365_with_network_alert.toml`)
- `2fc14da3-03d1-4d8e-b42b-942566bf69b4` LLM-Based Wget Activity Triage (`rules/cross-platform/command_and_control_wget_activity_llm_triage.toml`)
- `cf6995ec-32a9-4b2d-9340-f8e61acf3f4e` Trap Signals Execution (`rules/cross-platform/privilege_escalation_trap_execution.toml`)
- `f236cca1-e887-4d14-9ba9-bb8dd3e16cf1` LLM-Based Attack Chain Triage by Host (`rules/cross-platform/multiple_alerts_llm_attack_chain_triage_by_host.toml`)
- `877cc04a-3320-411d-bbe9-53266fa5e107` Kubectl Network Configuration Modification (`rules/cross-platform/command_and_control_kubectl_networking_modification.toml`)
- `590fc62d-7386-4c75-92b0-af4517018da1` Unusual Process Modifying GenAI Configuration File (`rules/cross-platform/defense_evasion_genai_config_modification.toml`)
- `4bd306f9-ee89-4083-91af-e61ed5c42b9a` Service Account Token or Certificate Access Followed by Kubernetes API Request (`rules/cross-platform/execution_d4c_k8s_mda_service_account_token_access_followed_by_kubernetes_api_request.toml`)
- `c371e9fc-6a10-11ef-a0ac-f661ea17fbcc` AWS SSM `SendCommand` with Run Shell Command Parameters (`rules/cross-platform/execution_aws_ssm_sendcommand_with_command_parameters.toml`)
- `344e6c7d-ceb0-4f20-ba04-7c75569a7e38` Elastic Defend Alert from Package Manager Install Ancestry (`rules/cross-platform/initial_access_elastic_defend_alert_package_manager_ancestor.toml`)
- `0c093569-dff9-42b6-87b1-0242d9f7d9b4` Processes with Trailing Spaces (`rules/cross-platform/defense_evasion_processes_with_trailing_spaces.toml`)
- `2b9a3b7a-0891-4a89-abbe-dca753c403cd` Multi-Cloud CLI Token and Credential Access Commands (`rules/cross-platform/credential_access_multi_cloud_cli_token_harvesting.toml`)
- `c0136397-f82a-45e5-9b9f-a3651d77e21a` GenAI Process Accessing Sensitive Files (`rules/cross-platform/credential_access_genai_process_sensitive_file_access.toml`)
- … 另有 91 条，用 `sync.py next --category cross-platform` 查看

### `integrations/aws`

未汉化 210 条：
- `c61fee20-4d00-4b39-a6e6-acddcc4433e2` AWS Cognito Unauthenticated Identity Pool Credentials Issued (`rules/integrations/aws/credential_access_cognito_unauthenticated_identity_pool_credentials_issued.toml`)
- `e71ae602-bf44-4834-a4ea-b5c87047d426` AWS Backup Resource Enumeration via Long-Term Access Key (`rules/integrations/aws/discovery_backup_enumeration_via_long_term_access_key.toml`)
- `2d7822a5-418c-4cde-a96e-e337d77b67e7` AWS Bedrock Automated Reasoning Safety Policy Tampering (`rules/integrations/aws/defense_evasion_bedrock_automated_reasoning_safety_policy_tampering.toml`)
- `d4e8f0a1-2b3c-4d5e-a6f7-8b9c0d1e2f3a` AWS IAM Customer Managed Policy Version Created or Default Version Set (`rules/integrations/aws/privilege_escalation_iam_customer_managed_policy_version_created_or_set_default.toml`)
- `9550ec87-e73c-4baa-ad44-e448a33fbc3d` AWS EKS Access Entry Granted Cluster Admin Policy (`rules/integrations/aws/privilege_escalation_eks_access_entry_granted_cluster_admin_policy.toml`)
- `ea248a02-bc47-4043-8e94-2885b19b2636` AWS IAM Principal Enumeration via UpdateAssumeRolePolicy (`rules/integrations/aws/discovery_iam_principal_enumeration_via_update_assume_role_policy.toml`)
- `5301ac83-7a43-4c92-95e7-c372afea807d` AWS IAM User Console Login from Multiple Geolocations (`rules/integrations/aws/initial_access_console_login_iam_user_multiple_geolocations.toml`)
- `453183fa-f903-11ee-8e88-f661ea17fbce` AWS Route 53 Resolver Query Log Configuration Deleted (`rules/integrations/aws/defense_evasion_route53_dns_query_resolver_config_deletion.toml`)
- `e515aeb2-3d47-4925-b6fc-3f92b0d40d5b` AWS GuardDuty Detection Suppression (`rules/integrations/aws/defense_evasion_guardduty_finding_suppression.toml`)
- `536997f7-ae73-447d-a12d-bff1e8f5f0a0` AWS EFS File System Deleted (`rules/integrations/aws/impact_efs_filesystem_deleted.toml`)
- `523116c0-d89d-4d7c-82c2-39e6845a78ef` AWS GuardDuty Detector Deletion (`rules/integrations/aws/defense_evasion_guardduty_detector_deletion.toml`)
- `2d8f6e1a-4b7c-4f9d-8e3a-1c5d2f8b9a0e` AWS Bedrock AgentCore Resource Created with IAM Execution Role (`rules/integrations/aws/privilege_escalation_bedrock_agentcore_resource_created_with_role.toml`)
- `594e0cbf-86cc-45aa-9ff7-ff27db27d3ed` AWS CloudTrail Log Created (`rules/integrations/aws/collection_cloudtrail_logging_created.toml`)
- `e12c0318-99b1-44f2-830c-3a38a43207ca` AWS EC2 Route Table Created (`rules/integrations/aws/persistence_route_table_created.toml`)
- `9f8e3c5e-f72e-4e91-93f6-e98a4fae3e4f` AWS IAM Long-Term Access Key First Seen from Source IP (`rules/integrations/aws/credential_access_iam_long_term_access_key_first_seen_from_source_ip.toml`)
- `618bb351-00f0-467b-8956-8cace8b81f07` AWS S3 Bucket Policy Added to Allow Public Access (`rules/integrations/aws/exfiltration_s3_bucket_policy_added_for_public_access.toml`)
- `042b35f3-afa6-4441-92b2-ef41976b48a3` AWS Backup Recovery Point Deleted (`rules/integrations/aws/impact_backup_recovery_point_deleted.toml`)
- `f7a1c536-9ac0-11ef-9911-f661ea17fbcd` AWS IAM Create User via Assumed Role on EC2 Instance (`rules/integrations/aws/persistence_iam_create_user_via_assumed_role_on_ec2_instance.toml`)
- `ab8f074c-5565-4bc4-991c-d49770e19fc9` AWS S3 Object Encryption Using External KMS Key (`rules/integrations/aws/impact_s3_object_encryption_with_external_key.toml`)
- `f4a82031-9c8e-4b23-a7d5-6e1094b2c539` AWS IAM Permission Boundary or Guardrail Policy Deleted by Unusual Identity (`rules/integrations/aws/defense_evasion_iam_managed_policy_deleted_unusual_identity.toml`)
- `42b5e06d-b297-4286-a004-ae0da92c5b81` AWS Bedrock Provisioned Model Throughput Tampering (`rules/integrations/aws/impact_bedrock_provisioned_model_throughput_tampering.toml`)
- `444c8fad-874f-4f59-b0ea-cf26cea478bd` AWS Account Discovery By Rare User (`rules/integrations/aws/discovery_organization_discovery_by_rare_user.toml`)
- `8e4bde35-125d-4eb3-9a2e-d7e77a053a08` AWS SES Email Identity Verified Then Deleted (`rules/integrations/aws/resource_development_ses_identity_verified_then_deleted.toml`)
- `f4dc90eb-e77e-4f0e-b18b-eb50da9e827e` AWS IAM Login Profile Created or Modified for an IAM User (`rules/integrations/aws/persistence_iam_login_profile_created_or_modified.toml`)
- `df919b5e-a0f6-4fd8-8598-e3ce79299e3b` AWS IAM AdministratorAccess Policy Attached to Group (`rules/integrations/aws/privilege_escalation_iam_administratoraccess_policy_attached_to_group.toml`)
- `119c8877-8613-416d-a98a-96b6664ee73a` AWS RDS Snapshot Export (`rules/integrations/aws/exfiltration_rds_snapshot_export.toml`)
- `a17f2e5f-de52-49e8-9d86-ccfe91cd54d4` AWS Bedrock Foundation Model Enumeration Followed by Invocation via Long-Term Key (`rules/integrations/aws/discovery_bedrock_model_recon_and_invocation_via_long_term_key.toml`)
- `a6788d4b-b241-4bf0-8986-a3b4315c5b70` AWS S3 Bucket Server Access Logging Disabled (`rules/integrations/aws/defense_evasion_s3_bucket_server_access_logging_disabled.toml`)
- `cdf7b922-909c-440c-8df0-0efe72aa7bea` AWS Bedrock Guardrail Deleted or Weakened (`rules/integrations/aws/defense_evasion_bedrock_guardrail_deleted_or_weakened.toml`)
- `ae32268b-bfd0-4c35-b002-13461b5830ca` AWS AssumeRoleWithWebIdentity from Kubernetes SA and External ASN (`rules/integrations/aws/initial_access_assume_role_with_web_identity_kubernetes_sa_from_external_asn.toml`)
- `90c0ce77-3fb4-484f-a8ad-4648e12b35b1` AWS EKS Access Entry Modified (`rules/integrations/aws/persistence_eks_access_entry_modified.toml`)
- `4ddac6c1-e4be-4e2b-95b5-0654cb8d423c` AWS Backup Vault Deleted or Vault Lock Removed (`rules/integrations/aws/impact_backup_vault_deleted_or_lock_removed.toml`)
- `873b5452-074e-11ef-852e-f661ea17fbcc` AWS EC2 Instance Connect SSH Public Key Uploaded (`rules/integrations/aws/lateral_movement_ec2_instance_connect_ssh_public_key_uploaded.toml`)
- `ca8c2751-5507-44f2-b58d-08958200cde9` AWS SageMaker Execution Role Passed by Unusual Principal (`rules/integrations/aws/privilege_escalation_sagemaker_execution_role_passed_by_unusual_principal.toml`)
- `9ebd48ac-a0e2-430a-a219-fe072a50146b` AWS CloudTrail Log Evasion (`rules/integrations/aws/defense_evasion_cloudtrail_logging_evasion.toml`)
- `962a71ae-aac9-11ef-9348-f661ea17fbce` AWS STS AssumeRoot by Rare User and Member Account (`rules/integrations/aws/privilege_escalation_sts_assume_root_from_rare_user_and_member_account.toml`)
- `4577ef08-61d1-4458-909f-25a4b10c87fe` AWS RDS DB Snapshot Shared with Another Account (`rules/integrations/aws/exfiltration_rds_snapshot_shared_with_another_account.toml`)
- `a80ffc40-a256-475a-a86a-74361930cdb1` AWS IAM SAML Provider Created (`rules/integrations/aws/persistence_iam_saml_provider_created.toml`)
- `1aa8fa52-44a7-4dae-b058-f3333b91c8d7` AWS CloudTrail Log Suspended (`rules/integrations/aws/defense_evasion_cloudtrail_logging_suspended.toml`)
- `55260656-76d6-427b-bd02-7acdde131b64` AWS Lambda Function High-Frequency Invocation by a Single Principal (`rules/integrations/aws/impact_lambda_high_frequency_invocation.toml`)
- … 另有 170 条，用 `sync.py next --category integrations/aws` 查看

### `integrations/aws_bedrock`

未汉化 12 条：
- `17261da3-a6d0-463c-aac8-ea1718afcd20` AWS Bedrock Detected Multiple Attempts to use Denied Models by a Single User (`rules/integrations/aws_bedrock/aws_bedrock_multiple_attempts_to_use_denied_models_by_user.toml`)
- `f4c2515a-18bb-47ce-a768-1dc4e7b0fe6c` AWS Bedrock Guardrails Detected Multiple Policy Violations Within a Single Blocked Request (`rules/integrations/aws_bedrock/aws_bedrock_guardrails_multiple_violations_in_single_request.toml`)
- `f2c653b7-7daf-4774-86f2-34cdbd1fc528` AWS Bedrock Invocations without Guardrails Detected by a Single User Over a Session (`rules/integrations/aws_bedrock/aws_bedrock_execution_without_guardrails.toml`)
- `b1773d05-f349-45fb-9850-287b8f92f02d` Potential Abuse of Resources by High Token Count and Large Response Sizes (`rules/integrations/aws_bedrock/aws_bedrock_high_resource_consumption_detection.toml`)
- `4f855297-c8e0-4097-9d97-d653f7e471c4` Unusual High Confidence Content Filter Blocks Detected (`rules/integrations/aws_bedrock/aws_bedrock_high_confidence_misconduct_blocks_detected.toml`)
- `68521f99-9b4f-40ef-a4e7-4d74794852b2` AWS Bedrock Model Prompt or Completion Containing Credentials (`rules/integrations/aws_bedrock/credential_access_aws_bedrock_credentials_in_model_prompt_or_completion.toml`)
- `0e1af929-42ed-4262-a846-55a7c54e7c84` Unusual High Denied Sensitive Information Policy Blocks Detected (`rules/integrations/aws_bedrock/aws_bedrock_multiple_sensitive_information_policy_blocks_detected.toml`)
- `51d50385-aa3d-448c-bc48-7d6bc39108a3` AWS Bedrock High Risk Filesystem or Execution Tool Invocation (`rules/integrations/aws_bedrock/execution_bedrock_high_risk_tool_invocation.toml`)
- `266bbea8-fcf9-4b0e-ba7b-fc00f6b1dc73` Unusual High Denied Topic Blocks Detected (`rules/integrations/aws_bedrock/aws_bedrock_multiple_topic_policy_blocks_detected.toml`)
- `0cd2f3e6-41da-40e6-b28b-466f688f00a6` AWS Bedrock Guardrails Detected Multiple Violations by a Single User Over a Session (`rules/integrations/aws_bedrock/aws_bedrock_guardrails_multiple_violations_by_single_user.toml`)
- `3216949c-9300-4c53-b57a-221e364c6457` Unusual High Word Policy Blocks Detected (`rules/integrations/aws_bedrock/aws_bedrock_multiple_word_policy_blocks_detected.toml`)
- `725a048a-88c5-4fc7-8677-a44fc0031822` AWS Bedrock Detected Multiple Validation Exception Errors by a Single User (`rules/integrations/aws_bedrock/aws_bedrock_multiple_validation_exception_errors_by_single_user.toml`)

### `integrations/aws_bedrock_agentcore`

未汉化 2 条：
- `b3e1f7a2-9d4c-4e8a-8f2b-1c6d5a0e3f77` AWS Bedrock AgentCore Runtime Prompt Containing Credentials (`rules/integrations/aws_bedrock_agentcore/credential_access_bedrock_agentcore_runtime_prompt_containing_credentials.toml`)
- `9c2f1d6a-4e8b-4c7a-9f3d-2b6e1a0c5d44` AWS Bedrock AgentCore Runtime Prompt Targeting Credentials or Instance Metadata (`rules/integrations/aws_bedrock_agentcore/credential_access_bedrock_agentcore_runtime_prompt_credential_harvesting.toml`)

### `integrations/azure`

未汉化 143 条：
- `fd9d2933-f0f9-4aac-810c-a31f6a4a7890` Azure AD Graph Access with Unusual Client and User (`rules/integrations/azure/discovery_aad_graph_unusual_client_for_user.toml`)
- `c8e5f6a2-1234-4d5e-9f8a-b7c6d5e4f3a2` Entra ID OAuth Authorization Code Grant for Unusual User, App, and Resource (`rules/integrations/azure/initial_access_entra_id_oauth_auth_code_grant_unusual_app_resource_user.toml`)
- `c22f89d9-b674-4650-8454-02242c8b35eb` Entra ID Microsoft Authentication Broker Sign-In with Non-Standard User Agent (`rules/integrations/azure/initial_access_entra_id_microsoft_auth_broker_nonstandard_user_agent.toml`)
- `a3cc60d8-2701-11f0-accf-f661ea17fbcd` Entra ID Sharepoint or OneDrive Accessed by Unusual Client (`rules/integrations/azure/collection_entra_id_sharepoint_access_from_unusual_application.toml`)
- `97266eb4-b8c3-4e3e-9417-7d0ace6b3dfe` Azure VM Serial Console Connection with Unusual User and ASN (`rules/integrations/azure/lateral_movement_azure_vm_serial_console_connect.toml`)
- `b6dce542-2b75-4ffb-b7d6-38787298ba9d` Azure Event Hub Authorization Rule Created or Updated (`rules/integrations/azure/persistence_event_hub_created_or_updated.toml`)
- `9563dace-5822-11f0-b1d3-f661ea17fbcd` Entra ID OAuth user_impersonation Scope for Unusual User and Client (`rules/integrations/azure/initial_access_entra_id_oauth_user_impersonation_scope.toml`)
- `a1b2c3d4-5e6f-7a8b-9c0d-1e2f3a4b5c6d` Azure Storage Account Deletion by Unusual User (`rules/integrations/azure/impact_azure_storage_account_deletion.toml`)
- `e842d39d-ead1-48c6-97f1-6b055476c2f3` Azure VM Extension Deployment by User (`rules/integrations/azure/persistence_azure_vm_extension_deployment_by_interactive_user.toml`)
- `763b0a74-2961-4396-bb4b-8cd850e1ebe4` Entra ID Windows Hello or Passkey Sign-in from Unregistered Device (`rules/integrations/azure/defense_evasion_entra_id_whfb_key_from_unregistered_device.toml`)
- `9bc14983-fabc-4a3e-896d-3632a902f17c` Azure AKS Kubernetes Events Deleted (`rules/integrations/azure/defense_evasion_azure_aks_events_deleted.toml`)
- `d8f4e3b0-8a1b-11ef-9b4a-f661ea17fbce` Azure Compute Restore Point Collections Deleted (`rules/integrations/azure/impact_azure_compute_restore_point_collections_deleted.toml`)
- `38e5acdd-5f20-4d99-8fe4-f0a1a592077f` Entra ID User Added as Service Principal Owner (`rules/integrations/azure/persistence_entra_id_user_added_as_owner_for_azure_service_principal.toml`)
- `60884af6-f553-4a6c-af13-300047455491` Azure Compute VM Command Executed (`rules/integrations/azure/execution_compute_vm_command_executed.toml`)
- `a1b2c3d4-e5f6-7890-a1b2-c3d4e5f67890` Entra ID Protection Admin Confirmed Compromise (`rules/integrations/azure/initial_access_entra_id_protection_confirmed_compromise.toml`)
- `d79c4b2a-6134-4edd-86e6-564a92a933f9` Azure Blob Storage Permissions Modified (`rules/integrations/azure/defense_evasion_storage_blob_permissions_modified.toml`)
- `d4e5f6a7-8b9c-0d1e-2f3a-4b5c6d7e8f9a` Azure Compute Snapshot Deletions by User (`rules/integrations/azure/impact_azure_compute_vm_snapshot_deletions.toml`)
- `5370d4cd-2bb3-4d71-abf5-1e1d0ff5a2de` Azure Diagnostic Settings Deleted (`rules/integrations/azure/defense_evasion_insights_diagnostic_settings_deletion.toml`)
- `aa04377a-19b5-4940-952f-aad173790d23` Entra ID OAuth Device Code Sign-in to Azure AD Graph Enumeration (`rules/integrations/azure/credential_access_device_code_signin_aad_graph_enum.toml`)
- `498e4094-60e7-11f0-8847-f661ea17fbcd` Entra ID Federated Identity Credential Issuer Modified (`rules/integrations/azure/persistence_entra_id_service_principal_federated_issuer_modified.toml`)
- `c07f7898-5dc3-11f0-9f27-f661ea17fbcd` Azure Key Vault Excessive Secret or Key Retrieved (`rules/integrations/azure/credential_access_key_vault_excessive_retrieval.toml`)
- `8ddab73b-3d15-4e5d-9413-47f05553c1d7` Azure Automation Runbook Deleted (`rules/integrations/azure/defense_evasion_automation_runbook_deleted.toml`)
- `42c97e6e-60c3-11f0-832a-f661ea17fbcd` Entra ID External Authentication Methods (EAM) Modified (`rules/integrations/azure/persistence_graph_eam_addition_or_modification.toml`)
- `04c5a96f-19c5-44fd-9571-a0b033f9086f` Entra ID Global Administrator Role Assigned (`rules/integrations/azure/persistence_entra_id_global_administrator_role_assigned.toml`)
- `7882cebf-6cf1-4de3-9662-213aa13e8b80` Entra ID Privileged Identity Management (PIM) Role Modified (`rules/integrations/azure/persistence_entra_id_privileged_identity_management_role_modified.toml`)
- `8d9c4128-372a-11f0-9d8f-f661ea17fbcd` Entra ID Elevated Access to User Access Administrator (`rules/integrations/azure/privilege_escalation_entra_id_elevate_to_user_administrator_access.toml`)
- `ce08cdb8-e6cb-46bb-a7cc-16d17547323f` Unusual City for an Azure Activity Logs Event (`rules/integrations/azure/ml_azure_rare_method_by_city.toml`)
- `d4695889-0410-4e7b-a4aa-59be525a11a6` Entra ID Register Device with Unusual User Agent (Azure AD Join) (`rules/integrations/azure/persistence_entra_id_register_device_unusual_user_agent.toml`)
- `a605c51a-73ad-406d-bf3a-f24cc41d5c97` Entra ID PowerShell Sign-in (`rules/integrations/azure/initial_access_entra_id_powershell_signin.toml`)
- `a222b46e-eba8-492f-a376-b7f5f397a34f` Entra ID ROPC Authentication with Unknown Client ID (`rules/integrations/azure/credential_access_entra_id_ropc_unknown_client_id.toml`)
- `2636aa6c-88b5-4337-9c31-8d0192a8ef45` Azure Blob Storage Container Access Level Modified (`rules/integrations/azure/discovery_storage_blob_container_access_modification.toml`)
- `c17ffbf9-595a-4c0b-a126-aacedb6dd179` Rare Azure Activity Logs Event Failures (`rules/integrations/azure/ml_azure_rare_event_failures.toml`)
- `323cb487-279d-4218-bcbd-a568efe930c6` Azure VNet Network Watcher Deleted (`rules/integrations/azure/defense_evasion_network_watcher_deletion.toml`)
- `921544bd-e2aa-44a6-9fb9-98629c342adf` Entra ID Conditional Access MFA Bypass with Unusual User, Client and Source ASN (`rules/integrations/azure/defense_evasion_entra_id_ca_mfa_bypass_first_party_graph.toml`)
- `30090d40-cdfd-4750-a281-0125fdf22045` Entra ID Guest Account Promoted to Member (`rules/integrations/azure/persistence_entra_id_guest_account_promoted_to_member.toml`)
- `cca64114-fb8b-11ef-86e2-f661ea17fbce` Entra ID User Sign-in Brute Force Attempted (`rules/integrations/azure/credential_access_entra_id_brute_force_activity.toml`)
- `82629eed-5516-446e-ad73-03b8c4f4d571` Entra ID Device Registration with Phishing Kit Default OS Build (`rules/integrations/azure/persistence_entra_id_phishing_kit_default_os_build_device_registration.toml`)
- `4f95e0f8-18b7-459a-b8b5-b2f5c94bf6eb` Entra ID Microsoft Authentication Broker Sign-In to Unusual Resource (`rules/integrations/azure/initial_access_entra_id_microsoft_auth_broker_unusual_resource.toml`)
- `16280f1e-57e6-4242-aa21-bb4d16f13b2f` Azure Automation Runbook Created or Modified (`rules/integrations/azure/execution_automation_runbook_created_or_modified.toml`)
- `ed9ecd27-e3e6-4fd9-8586-7754803f7fc8` Entra ID Global Administrator Role Assigned (PIM User) (`rules/integrations/azure/persistence_entra_id_pim_user_added_global_admin.toml`)
- … 另有 103 条，用 `sync.py next --category integrations/azure` 查看

### `integrations/azure_openai`

未汉化 3 条：
- `fb16f9ef-cb03-4234-adc2-44641f3b71ee` Azure OpenAI Insecure Output Handling (`rules/integrations/azure_openai/azure_openai_insecure_output_handling_detection.toml`)
- `b0450411-46e5-46d2-9b35-8b5dd9ba763e` Potential Denial of Azure OpenAI ML Service (`rules/integrations/azure_openai/azure_openai_denial_of_ml_service_detection.toml`)
- `4021e78d-5293-48d3-adee-a70fa4c18fab` Potential Azure OpenAI Model Theft (`rules/integrations/azure_openai/azure_openai_model_theft_detection.toml`)

### `integrations/beaconing`

未汉化 2 条：
- `5397080f-34e5-449b-8e9c-4c8083d7ccc6` Statistical Model Detected C2 Beaconing Activity (`rules/integrations/beaconing/command_and_control_beaconing.toml`)
- `0ab319ef-92b8-4c7f-989b-5de93c852e93` Statistical Model Detected C2 Beaconing Activity with High Confidence (`rules/integrations/beaconing/command_and_control_beaconing_high_confidence.toml`)

### `integrations/cloud_defend`

未汉化 49 条：
- `0398c0a2-1237-478e-84c4-84510f1925e6` Suspicious Container Runtime CLI Execution (`rules/integrations/cloud_defend/execution_container_runtime_cli_suspicious_args.toml`)
- `342f834b-21a6-41bf-878c-87d116eba3ee` Dynamic Linker Modification Detected via Defend for Containers (`rules/integrations/cloud_defend/defense_evasion_ld_preload_shared_object_modified_inside_a_container.toml`)
- `1a289854-5b78-49fe-9440-8a8096b1ab50` Suspicious Network Tool Launch Detected via Defend for Containers (`rules/integrations/cloud_defend/discovery_suspicious_network_tool_launched_inside_a_container.toml`)
- `d0b0f3ed-0b37-44bf-adee-e8cb7de92767` Cloud Credential Search Detected via Defend for Containers (`rules/integrations/cloud_defend/credential_access_cloud_creds_search_inside_a_container.toml`)
- `f66a6869-d4c7-4d20-ab13-beefd03b63b4` Environment Variable Enumeration Detected via Defend for Containers (`rules/integrations/cloud_defend/discovery_environment_enumeration.toml`)
- `47661529-15ed-4848-93da-9fbded7a3a0e` Chroot Execution Detected via Defend for Containers (`rules/integrations/cloud_defend/privilege_escalation_chroot_execution_detected_inside_container.toml`)
- `4b4e9c99-27ea-4621-95c8-82341bc6e512` Container Workload Protection (`rules/integrations/cloud_defend/container_workload_protection.toml`)
- `41f7da9e-4e9f-4a81-9b58-40d725d83bc0` Mount Execution Detected via Defend for Containers (`rules/integrations/cloud_defend/privilege_escalation_mount_launched_inside_a_privileged_container.toml`)
- `97697a52-4a76-4f0a-aa4f-25c178aae6eb` DebugFS Execution Detected via Defend for Containers (`rules/integrations/cloud_defend/privilege_escalation_debugfs_launched_inside_a_privileged_container.toml`)
- `a52a9439-d52c-401c-be37-2785235c6547` Netcat File Transfer or Listener Detected via Defend for Containers (`rules/integrations/cloud_defend/execution_netcat_listener_established_inside_a_container.toml`)
- `1dc56174-5d02-4ca4-af92-e391f096fb21` Ingress Tool Transfer Followed by Execution and Deletion Detected via Defend for Containers (`rules/integrations/cloud_defend/defense_evasion_file_creation_execution_deletion_cradle.toml`)
- `f7c64a1b-9d00-4b92-9042-d3bb4196899a` Service Account Namespace Read Detected via Defend for Containers (`rules/integrations/cloud_defend/discovery_service_account_namespace_read.toml`)
- `cd24c340-b778-44bd-ab69-2f739bd70ce1` Suspicious Interpreter Execution Detected via Defend for Containers (`rules/integrations/cloud_defend/execution_suspicious_interactive_interpreter_command_execution.toml`)
- `420e5bb4-93bf-40a3-8f4a-4cc1af90eca1` Exec Into Container Detected via Defend for Containers (`rules/integrations/cloud_defend/execution_interactive_exec_to_container.toml`)
- `39029450-8e2d-4034-81b0-15af8e4e3a4e` Nsenter Execution with Target Flag Inside Container (`rules/integrations/cloud_defend/privilege_escalation_nsenter_execution_inside_container.toml`)
- `f246e70e-5e20-4006-8460-d72b023d6adf` Modification of Persistence Relevant Files Detected via Defend for Containers (`rules/integrations/cloud_defend/persistence_modification_of_persistence_relevant_files.toml`)
- `f596175f-b8fd-43ac-b9e9-ea2a96bb55d8` Kubelet Pod Discovery Detected via Defend for Containers (`rules/integrations/cloud_defend/discovery_kubelet_pod_discovery_via_builtin_utilities.toml`)
- `160896de-b66f-42cb-8fef-20f53a9006ea` Potential release_agent Container Escape Detected via Defend for Containers (`rules/integrations/cloud_defend/privilege_escalation_potential_container_escape_via_modified_release_agent_file.toml`)
- `227cf26a-88d1-4bcb-bf4c-925e5875abcf` Encoded Payload Detected via Defend for Containers (`rules/integrations/cloud_defend/defense_evasion_potential_evasion_via_encoded_payload.toml`)
- `475b42f0-61fb-4ef0-8a85-597458bfb0a1` Sensitive File Compression Detected via Defend for Containers (`rules/integrations/cloud_defend/credential_access_collection_sensitive_files_compression_inside_a_container.toml`)
- `ef65e82c-d8b4-4895-9824-5f6bc6166804` Potential notify_on_release Container Escape Detected via Defend for Containers (`rules/integrations/cloud_defend/privilege_escalation_potential_container_escape_via_modified_notify_on_release_file.toml`)
- `74ee9a2d-5ed3-40c8-9e6c-523d2e6a17ef` DNS Enumeration Detected via Defend for Containers (`rules/integrations/cloud_defend/discovery_dns_enumeration.toml`)
- `6c6bb7ea-0636-44ca-b541-201478ef6b50` Container Management Utility Execution Detected via Defend for Containers (`rules/integrations/cloud_defend/execution_container_management_binary_launched_inside_a_container.toml`)
- `66229f32-c460-410d-bc37-4b32322cd4bb` Service Account Token or Certificate Read Detected via Defend for Containers (`rules/integrations/cloud_defend/credential_access_service_account_token_or_cert_read.toml`)
- `cebabc1e-1145-4e39-b04b-34d621ee1e2c` Shell Command-Line History Deletion Detected via Defend for Containers (`rules/integrations/cloud_defend/defense_evasion_deletion_of_shell_cmdline_history.toml`)
- `279e272a-91d9-4780-878c-bfcac76e6e31` Suspicious Process Execution Detected via Defend for Containers (`rules/integrations/cloud_defend/defense_evasion_interactive_process_execution_from_suspicious_directory.toml`)
- `33ff31e9-3872-4944-8394-81dae76c12d9` Potential Cluster Enumeration via jq Detected via Defend for Containers (`rules/integrations/cloud_defend/discovery_potential_cluster_enumeration_via_jq.toml`)
- `9d94d61b-9476-41ff-a8d3-3d24b4bb8158` Tunneling and/or Port Forwarding Detected via Defend for Containers (`rules/integrations/cloud_defend/command_and_control_tunneling_and_port_forwarding.toml`)
- `0fb83aa0-3d17-41e9-b09c-56397bf7a7d9` Decoded Payload Piped to Interpreter Detected via Defend for Containers (`rules/integrations/cloud_defend/defense_evasion_decoded_payload_piped_to_interpreter.toml`)
- `26a989d2-010e-4dae-b46b-689d03cc22b3` Direct Kubernetes API Request Detected via Defend for Containers (`rules/integrations/cloud_defend/execution_direct_interactive_kubernetes_api_request.toml`)
- `8d3d0794-c776-476b-8674-ee2e685f6470` Interactive Shell Spawn Detected via Defend for Containers (`rules/integrations/cloud_defend/execution_interactive_shell_spawned_from_inside_a_container.toml`)
- `85d9c573-ad77-461b-8315-9a02a280b20b` Process Killing Detected via Defend for Containers (`rules/integrations/cloud_defend/impact_process_killing.toml`)
- `d9bfa475-270d-4b07-93cb-b1f49abe13da` Suspicious Echo or Printf Execution Detected via Defend for Containers (`rules/integrations/cloud_defend/persistence_suspicious_echo_or_printf_execution.toml`)
- `737626a2-4dca-4195-8ecd-68ef96fd1bad` Privilege Boundary Enumeration Detected via Defend for Containers (`rules/integrations/cloud_defend/discovery_privilege_boundary_enumeration_from_interactive_process.toml`)
- `eb958cb3-dead-42b6-94ff-b9de6721fab2` Curl SOCKS Proxy Detected via Defend for Containers (`rules/integrations/cloud_defend/command_and_control_curl_socks_proxy_detected_inside_container.toml`)
- `b799720e-40d0-4dd6-9c9c-4f193a6ed643` File Creation and Execution Detected via Defend for Containers (`rules/integrations/cloud_defend/execution_interactive_file_creation_followed_by_execution.toml`)
- `42de0740-8ed8-4b8b-995c-635b56a8bbf4` Kubelet Certificate File Access Detected via Defend for Containers (`rules/integrations/cloud_defend/discovery_kubelet_certificate_file_access.toml`)
- `05a50000-9886-4695-ad33-3f990dc142e2` System Path File Creation and Execution Detected via Defend for Containers (`rules/integrations/cloud_defend/execution_interactive_file_creation_in_system_binary_locations.toml`)
- `9e5dbd3b-5e19-4648-a1cf-c2649c91b015` Namespace Manipulation Using Unshare in a Container (`rules/integrations/cloud_defend/privilege_escalation_unshare_namespace_manip.toml`)
- `a750bbcc-863f-41ef-9924-fd8224e23694` Payload Execution via Shell Pipe Detected by Defend for Containers (`rules/integrations/cloud_defend/execution_payload_downloaded_and_piped_to_shell.toml`)
- … 另有 9 条，用 `sync.py next --category integrations/cloud_defend` 查看

### `integrations/cyberarkpas`

未汉化 2 条：
- `c5f81243-56e0-47f9-b5bb-55a5ed89ba57` CyberArk Privileged Access Security Recommended Monitor (`rules/integrations/cyberarkpas/privilege_escalation_cyberarkpas_recommended_events_to_monitor_promotion.toml`)
- `3f0e5410-a4bf-4e8c-bcfc-79d67a285c54` CyberArk Privileged Access Security Error (`rules/integrations/cyberarkpas/privilege_escalation_cyberarkpas_error_audit_event_promotion.toml`)

### `integrations/ded`

未汉化 7 条：
- `bfba5158-1fd6-4937-a205-77d96213b341` Potential Data Exfiltration Activity to an Unusual Region (`rules/integrations/ded/exfiltration_ml_high_bytes_destination_region_name.toml`)
- `4b95ecea-7225-4690-9938-2a2c0bad9c99` Unusual Process Writing Data to an External Device (`rules/integrations/ded/exfiltration_ml_rare_process_writing_to_external_device.toml`)
- `35a3b253-eea8-46f0-abd3-68bdd47e6e3d` Spike in Bytes Sent to an External Device (`rules/integrations/ded/exfiltration_ml_high_bytes_written_to_external_device.toml`)
- `e1db8899-97c1-4851-8993-3a3265353601` Potential Data Exfiltration Activity to an Unusual ISO Code (`rules/integrations/ded/exfiltration_ml_high_bytes_destination_geo_country_iso_code.toml`)
- `ef8cc01c-fc49-4954-a175-98569c646740` Potential Data Exfiltration Activity to an Unusual Destination Port (`rules/integrations/ded/exfiltration_ml_high_bytes_destination_port.toml`)
- `cc653d77-ddd2-45b1-9197-c75ad19df66c` Potential Data Exfiltration Activity to an Unusual IP Address (`rules/integrations/ded/exfiltration_ml_high_bytes_destination_ip.toml`)
- `e92c99b6-c547-4bb6-b244-2f27394bc849` Spike in Bytes Sent to an External Device via Airdrop (`rules/integrations/ded/exfiltration_ml_high_bytes_written_to_external_device_airdrop.toml`)

### `integrations/dga`

未汉化 4 条：
- `bcaa15ce-2d41-44d7-a322-918f9db77766` Machine Learning Detected DGA activity using a known SUNBURST DNS domain (`rules/integrations/dga/command_and_control_ml_dga_activity_using_sunburst_domain.toml`)
- `f3403393-1fd9-4686-8f6e-596c58bc00b4` Machine Learning Detected a DNS Request Predicted to be a DGA Domain (`rules/integrations/dga/command_and_control_ml_dns_request_predicted_to_be_a_dga_domain.toml`)
- `ff0d807d-869b-4a0d-a493-52bc46d2f1b1` Potential DGA Activity (`rules/integrations/dga/command_and_control_ml_dga_high_sum_probability.toml`)
- `da7f5803-1cd4-42fd-a890-0173ae80ac69` Machine Learning Detected a DNS Request With a High DGA Probability Score (`rules/integrations/dga/command_and_control_ml_dns_request_high_dga_probability.toml`)

### `integrations/endpoint`

未汉化 9 条：
- `017de1e4-ea35-11ee-a417-f661ea17fbce` Memory Threat - Detected - Elastic Defend (`rules/integrations/endpoint/defense_evasion_elastic_memory_threat_detected.toml`)
- `9a1a2dae-0b5f-4c3d-8305-a268d404c306` Endpoint Security (Elastic Defend) (`rules/integrations/endpoint/elastic_endpoint_security.toml`)
- `f2c3caa6-ea34-11ee-a417-f661ea17fbce` Malicious File - Detected - Elastic Defend (`rules/integrations/endpoint/execution_elastic_malicious_file_detected.toml`)
- `06f3a26c-ea35-11ee-a417-f661ea17fbce` Memory Threat - Prevented- Elastic Defend (`rules/integrations/endpoint/defense_evasion_elastic_memory_threat_prevented.toml`)
- `10f3d520-ea35-11ee-a417-f661ea17fbce` Ransomware - Prevented - Elastic Defend (`rules/integrations/endpoint/impact_elastic_ransomware_prevented.toml`)
- `f87e6122-ea34-11ee-a417-f661ea17fbce` Malicious File - Prevented - Elastic Defend (`rules/integrations/endpoint/execution_elastic_malicious_file_prevented.toml`)
- `0f615fe4-eaa2-11ee-ae33-f661ea17fbce` Behavior - Detected - Elastic Defend (`rules/integrations/endpoint/elastic_endpoint_security_behavior_detected.toml`)
- `0c74cd7e-ea35-11ee-a417-f661ea17fbce` Ransomware - Detected - Elastic Defend (`rules/integrations/endpoint/impact_elastic_ransomware_detected.toml`)
- `eb804972-ea34-11ee-a417-f661ea17fbce` Behavior - Prevented - Elastic Defend (`rules/integrations/endpoint/elastic_endpoint_security_behavior_prevented.toml`)

### `integrations/entityanalytics_entra_id`

未汉化 2 条：
- `10b63b69-9f08-4767-b318-12208f97ad41` Entra ID Device with ROADtools Default OS Build (Entity Analytics) (`rules/integrations/entityanalytics_entra_id/persistence_entra_id_device_roadtools_default_os_build.toml`)
- `47f1d35c-8ee2-43c9-9651-90f840a0630f` Entra ID Phishing Kit Default OS Build (Entity Analytics) (`rules/integrations/entityanalytics_entra_id/persistence_entra_id_device_phishing_kit_default_os_build.toml`)

### `integrations/fim`

未汉化 1 条：
- `192657ba-ab0e-4901-89a2-911d611eee98` Potential Persistence via File Modification (`rules/integrations/fim/persistence_suspicious_file_modifications.toml`)

### `integrations/gcp`

未汉化 74 条：
- `f20d1782-e783-4ed0-a0c4-946899a98a7c` Unusual City For a GCP Event (`rules/integrations/gcp/ml_gcp_rare_method_by_city.toml`)
- `fde4efad-9cd0-4fa4-84c8-0e3b6fc957b4` GKE Pod Created With HostIPC (`rules/integrations/gcp/privilege_escalation_gcp_gke_pod_host_ipc.toml`)
- `80528e81-949f-4d38-b0c7-aef4b160212e` GKE CoreDNS or Kube-DNS Configuration Modified (`rules/integrations/gcp/impact_gcp_gke_coredns_or_kube_dns_configuration_modified.toml`)
- `bca7d28e-4a48-47b1-adb7-5074310e9a61` GCP Service Account Disabled (`rules/integrations/gcp/impact_gcp_service_account_disabled.toml`)
- `642ac343-e7d6-4cf2-bb0b-7db412e614ad` GCP Secret Manager ListSecrets Across Multiple Projects (`rules/integrations/gcp/discovery_gcp_secret_manager_listsecrets_across_multiple_projects.toml`)
- `c58c3081-2e1d-4497-8491-e73a45d1a6d6` GCP Virtual Private Cloud Network Deletion (`rules/integrations/gcp/defense_evasion_gcp_virtual_private_cloud_network_deleted.toml`)
- `00c2a946-bbe8-4345-941d-9ea13da91600` GKE API Request Impersonating Privileged Identity (`rules/integrations/gcp/privilege_escalation_gcp_gke_api_request_impersonating_privileged_identity.toml`)
- `e155e658-3dcd-4d27-a4e5-1d8da6704b0e` GKE Certificate Signing Request Self-Approved (`rules/integrations/gcp/persistence_gcp_gke_certificate_signing_request_self_approved.toml`)
- `0c04d82f-6def-4659-aa62-ed6355a51f39` GKE Secret get or list with Suspicious User Agent (`rules/integrations/gcp/credential_access_gcp_gke_secret_access_suspicious_user_agent.toml`)
- `0e5acaae-6a64-4bbc-adb8-27649c03f7e1` GCP Service Account Key Creation (`rules/integrations/gcp/persistence_gcp_key_created_for_service_account.toml`)
- `e2fb5b18-e33c-4270-851e-c3d675c9afcd` GCP IAM Role Deletion (`rules/integrations/gcp/impact_gcp_iam_role_deletion.toml`)
- `bedab6b4-f195-45d1-8f97-7d300eb79671` GKE Secret Access from Node or Denied Service Account (`rules/integrations/gcp/credential_access_gcp_gke_secret_access_from_node_or_denied_service_account.toml`)
- `647ae821-a80d-4f07-bb12-d40dd433f6b4` GKE Pod Created with a Sensitive hostPath Volume (`rules/integrations/gcp/privilege_escalation_gcp_gke_sensitive_hostpath_volume.toml`)
- `4780a3d6-e6a7-490c-9afb-9c5fbb220b9a` GKE Rapid Secret GET Activity Against Multiple Objects (`rules/integrations/gcp/credential_access_gcp_gke_rapid_secret_get_activity_against_multiple_objects.toml`)
- `d52e2418-978c-4184-9eab-e084af1f76b7` GKE Ephemeral Container Added to Pod (`rules/integrations/gcp/privilege_escalation_gcp_gke_ephemeral_container_added_to_pod.toml`)
- `1e58e0a0-7674-4aa9-9409-f72f100a8b5e` GKE Creation of a RoleBinding Referencing a ServiceAccount (`rules/integrations/gcp/persistence_gcp_gke_role_binding_referencing_service_account.toml`)
- `8d97dfa3-3c51-45fb-8621-bde800c47b22` GKE Unusual Sensitive Workload Modification (`rules/integrations/gcp/privilege_escalation_gcp_gke_unusual_sensitive_workload_modification.toml`)
- `9890ee61-d061-403d-9bf6-64934c51f638` GCP IAM Service Account Key Deletion (`rules/integrations/gcp/persistence_gcp_iam_service_account_key_deletion.toml`)
- `7ceb2216-47dd-4e64-9433-cddc99727623` GCP Service Account Creation (`rules/integrations/gcp/persistence_gcp_service_account_created.toml`)
- `d62b64a8-a7c9-43e5-aee3-15a725a794e7` GCP Pub/Sub Subscription Creation (`rules/integrations/gcp/collection_gcp_pub_sub_subscription_creation.toml`)
- `3a68325b-6169-44c1-a5f0-0102ef82b6f1` GKE Pod Exec with Curl or Wget to HTTPS (`rules/integrations/gcp/execution_gcp_gke_pod_exec_curl_wget_https.toml`)
- `e2f60d42-e0ea-4a03-a151-942bb5b86c0b` GKE Suspicious Assignment of Controller Service Account (`rules/integrations/gcp/privilege_escalation_gcp_gke_suspicious_assignment_of_controller_service_account.toml`)
- `854e89c1-f70c-4180-bc53-65999df9d3c3` GKE Secret Access via Unusual User Agent (`rules/integrations/gcp/credential_access_gcp_gke_secret_access_via_unusual_user_agent.toml`)
- `1e344fba-a2f7-462b-aaec-d6c8f80d5a28` GKE Certificate Signing Request API Client Signer Requested (`rules/integrations/gcp/privilege_escalation_gcp_gke_certificate_signing_request_api_client_signer_requested.toml`)
- `ff9b571e-61d6-4f6c-9561-eb4cca3bafe1` GCP Firewall Rule Deletion (`rules/integrations/gcp/defense_evasion_gcp_firewall_rule_deleted.toml`)
- `2302fb59-5201-46ec-b433-6044adb37b0b` GKE Suspicious Self-Subject Review via Service Account (`rules/integrations/gcp/discovery_gcp_gke_suspicious_self_subject_review.toml`)
- `9180ffdf-f3d0-4db3-bf66-7a14bcff71b8` GCP Virtual Private Cloud Route Creation (`rules/integrations/gcp/defense_evasion_gcp_virtual_private_cloud_route_created.toml`)
- `97359fd8-757d-4b1d-9af1-ef29e4a8680e` GCP Storage Bucket Configuration Modification (`rules/integrations/gcp/defense_evasion_gcp_storage_bucket_configuration_modified.toml`)
- `5378a829-30c2-435a-a0f2-e3d794bd6f80` Rare GCP Audit Failure Event Code (`rules/integrations/gcp/ml_gcp_rare_error_code.toml`)
- `a4fa2bf0-1cf9-4803-bed0-1f9c6e57af3c` GKE API Server Proxying Request to Kubelet (`rules/integrations/gcp/privilege_escalation_gcp_gke_api_proxy_to_node.toml`)
- `51859fa0-d86b-4214-bf48-ebb30ed91305` GCP Logging Sink Deletion (`rules/integrations/gcp/defense_evasion_gcp_logging_sink_deletion.toml`)
- `a7b984e4-16ff-405b-80be-31a94a03e929` GKE Privileged Pod Created (`rules/integrations/gcp/privilege_escalation_gcp_gke_privileged_pod_created.toml`)
- `2af7f1d7-d02c-476f-a130-e17ea4e556e6` GKE Creation or Modification of Sensitive Role (`rules/integrations/gcp/persistence_gcp_gke_sensitive_role_created_or_modified.toml`)
- `4159bec9-76ad-4cdc-a797-4a8572073bbe` GKE Certificate Signing Request for Privileged Identity (`rules/integrations/gcp/privilege_escalation_gcp_gke_certificate_signing_request_privileged_identity_requested.toml`)
- `4df2e3ae-3553-4194-b22e-3e5a6f71466e` GKE Secrets List from Unusual Source AS Organization (`rules/integrations/gcp/credential_access_gcp_gke_secrets_list_unusual_source_asn.toml`)
- `92980750-3373-4f0c-aebd-c2a8563d8e8a` GKE Anonymous Pod Create/Update/Patch (`rules/integrations/gcp/execution_gcp_gke_anonymous_pod_create_update_patch.toml`)
- `184dfe52-2999-42d9-b9d1-d1ca54495a61` GCP Logging Sink Modification (`rules/integrations/gcp/exfiltration_gcp_logging_sink_modification.toml`)
- `ec67ab57-945a-4edb-84f8-1d7a51f46544` GKE Client Certificate Signing Request Created or Approved (`rules/integrations/gcp/persistence_gcp_gke_client_certificate_signing_request_created_or_approved.toml`)
- `189f0f31-8f31-48eb-bb3e-c0db8c8b8c4c` GKE Anonymous Request Authorized by Unusual User Agent (`rules/integrations/gcp/initial_access_gcp_gke_anonymous_request_authorized.toml`)
- `2783d84f-5091-4d7d-9319-9fceda8fa71b` GCP Firewall Rule Modification (`rules/integrations/gcp/defense_evasion_gcp_firewall_rule_modified.toml`)
- … 另有 34 条，用 `sync.py next --category integrations/gcp` 查看

### `integrations/github`

未汉化 19 条：
- `daf2e0e0-0bab-4672-bfa1-62db0ee5ec22` Github Activity on a Private Repository from an Unusual IP (`rules/integrations/github/impact_github_repository_activity_from_unusual_ip.toml`)
- `fd01b949-81be-46d5-bcf8-284395d5f56d` GitHub App Deleted (`rules/integrations/github/execution_github_app_deleted.toml`)
- `19f3674c-f4a1-43bb-a89c-e4c6212275e0` GitHub Exfiltration via High Number of Repository Clones by User (`rules/integrations/github/exfiltration_high_number_of_cloning_by_user.toml`)
- `21c3536f-b674-43db-9bfc-dcf4cf9dcc37` GitHub Secret Scanning Disabled (`rules/integrations/github/defense_evasion_secret_scanning_disabled.toml`)
- `8c707e4c-bd20-4ff4-bda5-4dc3b34ce298` GitHub Private Repository Turned Public (`rules/integrations/github/exfiltration_github_private_repository_turned_public.toml`)
- `345889c4-23a8-4bc0-b7ca-756bd17ce83b` GitHub Repository Deleted (`rules/integrations/github/impact_github_repository_deleted.toml`)
- `0428c618-27f5-4d94-99e6-b254585aba69` High Number of Protected Branch Force Pushes by User (`rules/integrations/github/impact_high_number_of_protected_branch_force_pushes_by_user.toml`)
- `03245b25-3849-4052-ab48-72de65a82c35` GitHub Actions Unusual Bot Push to Repository (`rules/integrations/github/initial_access_github_actions_bot_first_push_to_repo.toml`)
- `e8b37f18-4804-4819-8602-4aba1169c9f4` GitHub Actions Workflow Modification Blocked (`rules/integrations/github/initial_access_github_actions_workflow_injection_blocked.toml`)
- `07639887-da3a-4fbf-9532-8ce748ff8c50` GitHub Protected Branch Settings Changed (`rules/integrations/github/defense_evasion_github_protected_branch_settings_changed.toml`)
- `fb0afac5-bbd6-49b0-b4f8-44e5381e1587` High Number of Cloned GitHub Repos From PAT (`rules/integrations/github/execution_github_high_number_of_cloned_repos_from_pat.toml`)
- `214d4e03-90b0-4813-9ab6-672b47158590` New GitHub Personal Access Token (PAT) Added (`rules/integrations/github/persistence_new_pat_created.toml`)
- `40c34c8a-b0bc-43bc-83aa-d2b76bf129e1` New GitHub Self Hosted Action Runner (`rules/integrations/github/initial_access_github_register_self_hosted_runner.toml`)
- `9b343b62-d173-4cfd-bd8b-e6379f964ca4` GitHub Owner Role Granted To User (`rules/integrations/github/persistence_organization_owner_role_granted.toml`)
- `929223b4-fba3-4a1c-a943-ec4716ad23ec` GitHub UEBA - Multiple Alerts from a GitHub Account (`rules/integrations/github/execution_github_ueba_multiple_behavior_alerts_from_account.toml`)
- `1ca62f14-4787-4913-b7af-df11745a49da` New GitHub App Installed (`rules/integrations/github/execution_new_github_app_installed.toml`)
- `8bd1c36a-2c4f-4801-a43d-ba696c13ffc2` Several Failed Protected Branch Force Pushes by User (`rules/integrations/github/impact_high_number_of_failed_protected_branch_force_pushes_by_user.toml`)
- `098bd5cc-fd55-438f-b354-7d6cd9856a08` High Number of Closed Pull Requests by User (`rules/integrations/github/impact_high_number_of_closed_pull_requests_by_user.toml`)
- `24401eca-ad0b-4ff9-9431-487a8e183af9` New GitHub Owner Added (`rules/integrations/github/persistence_github_org_owner_added.toml`)

### `integrations/google_workspace`

未汉化 27 条：
- `9510add4-3392-11ed-bd01-f661ea17fbce` Google Workspace Gmail Routing or Forwarding Rule Created or Modified (`rules/integrations/google_workspace/collection_google_workspace_custom_gmail_route_created_or_modified.toml`)
- `f1a6d0f4-95b8-11ed-9517-f661ea17fbcc` Forwarded Google Workspace Security Alert (`rules/integrations/google_workspace/google_workspace_alert_center_promotion.toml`)
- `cc6a8a20-2df2-11ed-8378-f661ea17fbce` Google Workspace User Organizational Unit Changed (`rules/integrations/google_workspace/persistence_google_workspace_user_organizational_unit_changed.toml`)
- `cf549724-c577-4fd6-8f9b-d1b8ec519ec0` Domain Added to Google Workspace Trusted Domains (`rules/integrations/google_workspace/defense_evasion_domain_added_to_google_workspace_trusted_domains.toml`)
- `e0916edd-ea8c-49d2-882e-2cf6af161dd7` Google Workspace User Sign-in from Atypical Device Type (`rules/integrations/google_workspace/persistence_google_workspace_device_registration_atypical_device.toml`)
- `5e161522-2545-11ed-ac47-f661ea17fbce` Google Workspace 2SV Policy Disabled By User (`rules/integrations/google_workspace/persistence_google_workspace_2sv_policy_disabled.toml`)
- `1f489c86-d9c4-40de-9316-931721ca9b45` Google Workspace User Login with Unusual ASN (`rules/integrations/google_workspace/initial_access_google_workspace_login_from_atypical_asn.toml`)
- `acbc8bb9-2486-49a8-8779-45fb5f9a93ee` Google Workspace API Access Granted via Domain-Wide Delegation (`rules/integrations/google_workspace/persistence_google_workspace_api_access_granted_via_dwd.toml`)
- `00678712-b2df-11ed-afe9-f661ea17fbcc` Google Workspace Suspended User Account Renewed (`rules/integrations/google_workspace/initial_access_google_workspace_suspended_user_renewed.toml`)
- `aff74d85-5bfa-4ff1-ace2-4e3995a37cfa` Google Workspace Impossible Travel Login (`rules/integrations/google_workspace/initial_access_google_workspace_login_impossible_travel.toml`)
- `bea0589d-c7a4-4dc6-a931-9fecaa8689fb` Google Workspace Device Registration Burst for Single User (`rules/integrations/google_workspace/persistence_google_workspace_device_registration_burst.toml`)
- `a99f82f5-8e77-4f8b-b3ce-10c0f6afbc73` Google Workspace Password Policy Modified (`rules/integrations/google_workspace/persistence_google_workspace_password_policy_modified.toml`)
- `785a404b-75aa-4ffd-8be5-3334a5a544dd` Application Added to Google Workspace Domain (`rules/integrations/google_workspace/persistence_application_added_to_google_workspace_domain.toml`)
- `495e5f2e-2480-11ed-bea8-f661ea17fbce` Application Removed from Blocklist in Google Workspace (`rules/integrations/google_workspace/defense_evasion_application_removed_from_blocklist_in_google_workspace.toml`)
- `7caa8e60-2df0-11ed-b814-f661ea17fbce` Google Workspace Bitlocker Setting Disabled (`rules/integrations/google_workspace/defense_evasion_google_workspace_bitlocker_setting_disabled.toml`)
- `07b5f85a-240f-11ed-b3d9-f661ea17fbce` Google Workspace Drive Data Transfer or Takeout Export Initiated (`rules/integrations/google_workspace/collection_google_drive_ownership_transferred_via_google_workspace.toml`)
- `68994a6c-c7ba-4e82-b476-26a26877adf6` Google Workspace Admin Role Assigned to a User or Group (`rules/integrations/google_workspace/persistence_google_workspace_admin_role_assigned_to_user.toml`)
- `cad4500a-abd7-4ef3-b5d3-95524de7cfe1` Google Workspace MFA Enforcement Disabled For Organization (`rules/integrations/google_workspace/impact_google_workspace_mfa_enforcement_disabled.toml`)
- `012bfca7-45cb-4507-a3ba-3777167f8b81` Google Workspace Device Registration After OAuth from Suspicious ASN (`rules/integrations/google_workspace/persistence_google_workspace_device_registered_after_oauth_from_suspicious_asn.toml`)
- `a2795334-2499-11ed-9e1a-f661ea17fbce` Google Workspace Restrictions for Marketplace Modified to Allow Any App (`rules/integrations/google_workspace/defense_evasion_restrictions_for_marketplace_modified_to_allow_any_app.toml`)
- `f33e68a4-bd19-11ed-b02f-f661ea17fbcc` Google Workspace Object Copied from External Drive with App Consent (`rules/integrations/google_workspace/initial_access_object_copied_to_external_drive_with_app_consent.toml`)
- `ad3f2807-2b3e-47d7-b282-f84acbbe14be` Google Workspace Custom Admin Role Created (`rules/integrations/google_workspace/persistence_google_workspace_custom_admin_role_created.toml`)
- `6f435062-b7fc-4af9-acea-5b1ead65c5a5` Google Workspace Role Modified (`rules/integrations/google_workspace/persistence_google_workspace_role_modified.toml`)
- `38f384e0-aef8-11ed-9a38-f661ea17fbcc` External User Added to Google Workspace Group (`rules/integrations/google_workspace/initial_access_external_user_added_to_google_workspace_group.toml`)
- `980b70a0-c820-11ed-8799-f661ea17fbcc` Google Workspace Drive Encryption Key(s) Accessed from Anonymous User (`rules/integrations/google_workspace/credential_access_google_workspace_drive_encryption_key_accessed_by_anonymous_user.toml`)
- `21bafdf0-cf17-11ed-bd57-f661ea17fbcc` First Time Seen Google Workspace OAuth Login from Third-Party Application (`rules/integrations/google_workspace/defense_evasion_google_workspace_new_oauth_login_from_third_party_application.toml`)
- `93e63c3e-4154-4fc6-9f86-b411e0987bbf` Google Workspace Admin Role Deletion (`rules/integrations/google_workspace/impact_google_workspace_admin_role_deletion.toml`)

### `integrations/kubernetes`

未汉化 43 条：
- `c9d4e8f1-2a3b-4c5d-8e9f-0a1b2c3d4e5f` Kubernetes Pod Exec with Curl or Wget to HTTPS (`rules/integrations/kubernetes/execution_kubernetes_pod_exec_curl_wget_https.toml`)
- `78c6559d-47a7-4f30-91fe-7e2e983206c2` Unusual Kubernetes Sensitive Workload Modification (`rules/integrations/kubernetes/privilege_escalation_sensitive_workload_modification_by_user_agent.toml`)
- `4f8f7c08-ffb5-443f-86c6-0884c964df7b` Kubernetes Admission Webhook Created or Modified (`rules/integrations/kubernetes/persistence_kubernetes_admission_webhook_created_or_modified.toml`)
- `f8a31c62-0d4e-4b9a-b7e1-6c2a9d4e8f10` Kubernetes Secret Get or List from Node or Pod Service Account (`rules/integrations/kubernetes/credential_access_kubernetes_secret_read_by_node_or_pod_service_account.toml`)
- `3a01e5c6-ce01-46d7-ac9f-52dc349695fb` Kubernetes Anonymous User Create/Update/Patch Pods Request (`rules/integrations/kubernetes/execution_anonymous_create_update_patch_pod_request.toml`)
- `f1a2b3c4-d5e6-4789-a012-3456789abc01` Kubernetes Pod Exec Potential Reverse Shell (`rules/integrations/kubernetes/execution_kubernetes_pod_exec_potential_reverse_shell.toml`)
- `a8e7d6c5-b4a3-2918-0f9e-8d7c6b5a4032` Kubernetes Pod Exec Cloud Instance Metadata Access (`rules/integrations/kubernetes/credential_access_kubernetes_pod_exec_cloud_instance_metadata.toml`)
- `ec81962e-4bc8-48e6-bfb0-545fc97d8f6a` Kubernetes Forbidden Creation Request (`rules/integrations/kubernetes/execution_forbidden_creation_request.toml`)
- `33c27b4e-8ec6-406f-b8e5-345dc024aa97` Kubernetes Events Deleted (`rules/integrations/kubernetes/defense_evasion_events_deleted.toml`)
- `7e3f9a2b-1c4d-5e6f-8a0b-9c8d7e6f5a4b` Kubernetes Secrets List Across Cluster or Sensitive Namespaces (`rules/integrations/kubernetes/credential_access_kubernetes_secrets_list_cluster_and_sensitive_namespaces.toml`)
- `4b77d382-b78e-4aae-85a0-8841b80e4fc4` Kubernetes Forbidden Request from Unusual User Agent (`rules/integrations/kubernetes/execution_forbidden_request_from_unsual_user_agent.toml`)
- `5202697c-313b-4bf0-9029-73fe78cd4b6d` EKS Authentication Configuration Modified (`rules/integrations/kubernetes/persistence_kubernetes_eks_aws_auth_configmap_modified.toml`)
- `0fb25791-d8d4-42ab-8fc7-4954642de85f` Kubernetes Creation or Modification of Sensitive Role (`rules/integrations/kubernetes/persistence_sensitive_role_creation_or_modification.toml`)
- `a643e6b8-ba2a-45f1-8d71-d265bfe2ae43` Kubernetes CoreDNS or Kube-DNS Configuration Modified (`rules/integrations/kubernetes/impact_kubernetes_coredns_or_kube_dns_configuration_modified.toml`)
- `b2c3d4e5-f6a7-4890-b1c2-d3e4f5a60789` Kubernetes Pod Exec Sensitive File or Credential Path Access (`rules/integrations/kubernetes/credential_access_kubernetes_pod_exec_sensitive_file_access.toml`)
- `764c8437-a581-4537-8060-1fdb0e92c92d` Kubernetes Pod Created With HostIPC (`rules/integrations/kubernetes/privilege_escalation_pod_created_with_hostipc.toml`)
- `63c057cc-339a-11ed-a261-0242ac120002` Kubernetes Anonymous Request Authorized by Unusual User Agent (`rules/integrations/kubernetes/initial_access_anonymous_request_authorized.toml`)
- `220d92c6-479d-4a49-9cc0-3a29756dad0c` Kubernetes Secret or ConfigMap Access via Azure Arc Proxy (`rules/integrations/kubernetes/credential_access_azure_arc_proxy_secret_configmap_access.toml`)
- `65f9bccd-510b-40df-8263-334f03174fed` Kubernetes Exposed Service Created With Type NodePort (`rules/integrations/kubernetes/persistence_exposed_service_created_with_type_nodeport.toml`)
- `a337c3f8-e264-4eb4-9998-22669ca52791` Kubernetes Potential Endpoint Permission Enumeration Attempt Detected (`rules/integrations/kubernetes/discovery_endpoint_permission_enumeration_by_user_and_srcip.toml`)
- `c8f4a2e1-9b3d-4c7e-8f2a-1d0e5b6c7a89` Kubernetes RBAC Wildcard Elevation on Existing Role (`rules/integrations/kubernetes/privilege_escalation_role_patch_wildcard_verbs_resources_response.toml`)
- `c62733ff-9373-4fdf-9733-3d992e148c93` Kubernetes Ephemeral Container Added to Pod (`rules/integrations/kubernetes/privilege_escalation_kubernetes_ephemeral_container_added_to_pod.toml`)
- `c7908cac-337a-4f38-b50d-5eeb78bdb531` Kubernetes Privileged Pod Created (`rules/integrations/kubernetes/privilege_escalation_privileged_pod_created.toml`)
- `f2e21713-1eac-4908-a782-1b49c7e9d53b` Kubernetes Service Account Modified RBAC Objects (`rules/integrations/kubernetes/privilege_escalation_service_account_rbac_write_operation.toml`)
- `2dd0d4fd-0cc9-4d18-8b46-1a507e28bbc0` Kubernetes Potential Endpoint Permission Enumeration Attempt by Anonymous User Detected (`rules/integrations/kubernetes/discovery_endpoint_permission_enumeration_by_anonymous_user.toml`)
- `0f5941c6-3db9-4d2f-91df-06c7c292ba45` Kubernetes Client Certificate Signing Request Created or Approved (`rules/integrations/kubernetes/persistence_kubernetes_client_certificate_signing_request_created_or_approved.toml`)
- `b4c8e2a1-9f3d-4e7c-a2b1-0d5e6f7a8b9c` Kubernetes Rapid Secret GET Activity Against Multiple Objects (`rules/integrations/kubernetes/credential_access_kubernetes_multiple_secret_retrieval_burst.toml`)
- `332ecb5b-08b6-47e9-885b-3cee1de74bac` Kubernetes API Server Proxying Request to Kubelet (`rules/integrations/kubernetes/privilege_escalation_api_proxy_to_node.toml`)
- `abb7bc31-b865-4318-80a9-b9ee4edd57b6` Kubernetes API Request Impersonating Privileged Identity (`rules/integrations/kubernetes/privilege_escalation_kubernetes_api_request_impersonating_privileged_identity.toml`)
- `a2951930-dd35-438c-b10e-1bbdc5881cb4` Kubernetes Cluster-Admin Role Binding Created (`rules/integrations/kubernetes/persistence_cluster_admin_rolebinding_created.toml`)
- `63c05204-339a-11ed-a261-0242ac120002` Kubernetes Suspicious Assignment of Controller Service Account (`rules/integrations/kubernetes/privilege_escalation_suspicious_assignment_of_controller_service_account.toml`)
- `c2a91e88-4f4b-4e1d-9c7b-8fde112a9403` Kubernetes Multi-Resource Discovery (`rules/integrations/kubernetes/discovery_kubernetes_multi_resource_setup_recon.toml`)
- `2abda169-416b-4bb3-9a6b-f8d239fd78ba` Kubernetes Pod Created with a Sensitive hostPath Volume (`rules/integrations/kubernetes/privilege_escalation_pod_created_with_sensitive_hostpath_volume.toml`)
- `a4c8e901-2b7f-4d6e-9a3c-8e1f0d5b6c2a` Kubernetes Secret Get or List with Suspicious User Agent (`rules/integrations/kubernetes/credential_access_kubernetes_secret_access_scripting_http_clients.toml`)
- `7164081a-3930-11ed-a261-0242ac120002` Kubernetes Container Created with Excessive Linux Capabilities (`rules/integrations/kubernetes/privilege_escalation_container_created_with_excessive_linux_capabilities.toml`)
- `fd00769d-b18d-450a-a844-7a9f9c71995e` Kubernetes Creation of a RoleBinding Referencing a ServiceAccount (`rules/integrations/kubernetes/persistence_service_account_bound_to_clusterrole.toml`)
- `3c82bf84-5941-495b-ac41-0302f28e1a90` Kubernetes Sensitive RBAC Change Followed by Workload Modification (`rules/integrations/kubernetes/privilege_escalation_sensitive_rbac_change_followed_by_workload_modification.toml`)
- `12cbf709-69e8-4055-94f9-24314385c27e` Kubernetes Pod Created With HostNetwork (`rules/integrations/kubernetes/privilege_escalation_pod_created_with_hostnetwork.toml`)
- `cbda9a0e-2be4-4eaa-9571-8d6a503e9828` Kubernetes Secret Access via Unusual User Agent (`rules/integrations/kubernetes/credential_access_get_secrets_access.toml`)
- `df7fda76-c92b-4943-bc68-04460a5ea5ba` Kubernetes Pod Created With HostPID (`rules/integrations/kubernetes/privilege_escalation_pod_created_with_hostpid.toml`)
- … 另有 3 条，用 `sync.py next --category integrations/kubernetes` 查看

### `integrations/lmd`

未汉化 11 条：
- `36c48a0c-c63a-4cbc-aee1-8cac87db31a9` High Mean of Process Arguments in an RDP Session (`rules/integrations/lmd/lateral_movement_ml_high_mean_rdp_process_args.toml`)
- `e9b0902b-c515-413b-b80b-a8dcebc81a66` Spike in Remote File Transfers (`rules/integrations/lmd/lateral_movement_ml_spike_in_remote_file_transfers.toml`)
- `a8d35ca0-ad8d-48a9-9f6c-553622dca61a` High Variance in RDP Session Duration (`rules/integrations/lmd/lateral_movement_ml_high_variance_rdp_session_duration.toml`)
- `19e9daf3-f5c5-4bc2-a9af-6b1e97098f03` Spike in Number of Processes in an RDP Session (`rules/integrations/lmd/lateral_movement_ml_spike_in_rdp_processes.toml`)
- `3e0561b5-3fac-4461-84cc-19163b9aaa61` Spike in Number of Connections Made from a Source IP (`rules/integrations/lmd/lateral_movement_ml_spike_in_connections_from_a_source_ip.toml`)
- `a74c60cb-70ee-4629-a127-608ead14ebf1` High Mean of RDP Session Duration (`rules/integrations/lmd/lateral_movement_ml_high_mean_rdp_session_duration.toml`)
- `3f4e2dba-828a-452a-af35-fe29c5e78969` Unusual Time or Day for an RDP Session (`rules/integrations/lmd/lateral_movement_ml_unusual_time_for_an_rdp_session.toml`)
- `18a5dd9a-e3fa-4996-99b1-ae533b8f27fc` Spike in Number of Connections Made to a Destination IP (`rules/integrations/lmd/lateral_movement_ml_spike_in_connections_to_a_destination_ip.toml`)
- `814d96c7-2068-42aa-ba8e-fe0ddd565e2e` Unusual Remote File Extension (`rules/integrations/lmd/lateral_movement_ml_rare_remote_file_extension.toml`)
- `0678bc9c-b71a-433b-87e6-2f664b6b3131` Unusual Remote File Size (`rules/integrations/lmd/lateral_movement_ml_high_remote_file_size.toml`)
- `be4c5aed-90f5-4221-8bd5-7ab3a4334751` Unusual Remote File Directory (`rules/integrations/lmd/lateral_movement_ml_rare_remote_file_directory.toml`)

### `integrations/macos`

未汉化 2 条：
- `3751cc17-6e7e-4356-86d5-c8f44aab9a28` Potential SSH Brute Force Detected via macOS Security Events (`rules/integrations/macos/credential_access_potential_macos_ssh_bruteforce_via_security_events.toml`)
- `f5898b1e-3071-4597-b066-43d298c7b415` Potential Successful SSH Brute Force Attack via macOS Security Events (`rules/integrations/macos/credential_access_potential_successful_macos_ssh_bruteforce_via_security_events.toml`)

### `integrations/microsoft_exchange_online_message_trace`

未汉化 1 条：
- `a6129187-c47b-48ab-a412-67a44836d918` M365 Azure Monitor Alert Email with Financial or Billing Theme (`rules/integrations/microsoft_exchange_online_message_trace/initial_access_azure_monitor_callback_phishing_email.toml`)

### `integrations/o365`

未汉化 48 条：
- `d68eb1b5-5f1c-4b6d-9e63-5b6b145cd4aa` M365 Exchange Anti-Phish Policy Deleted (`rules/integrations/o365/defense_evasion_exchange_anti_phish_policy_deletion.toml`)
- `0c3c80de-08c2-11f0-bd11-f661ea17fbcc` M365 Identity OAuth Illicit Consent Grant by Rare Client and User (`rules/integrations/o365/initial_access_identity_illicit_consent_grant_via_registered_application.toml`)
- `40fe11c2-376e-11f0-9a82-f661ea17fbcd` M365 Exchange Inbox Phishing Evasion Rule Created (`rules/integrations/o365/defense_evasion_exchange_new_inbox_rule_delete_or_move.toml`)
- `bba1b212-b85c-41c6-9b28-be0e5cdfc9b1` M365 OneDrive Malware File Upload (`rules/integrations/o365/lateral_movement_onedrive_malware_uploaded.toml`)
- `1c3d9346-4591-4894-935c-dad2824850f2` M365 Exchange Inbox Rule with Obfuscated Name (`rules/integrations/o365/defense_evasion_exchange_inbox_rule_obfuscated_name.toml`)
- `3896d4c0-6ad1-11ef-8c7b-f661ea17fbcc` M365 Identity Login from Impossible Travel Location (`rules/integrations/o365/initial_access_entra_id_portal_login_impossible_travel.toml`)
- `60f3adec-1df9-4104-9c75-b97d9f078b25` Deprecated - M365 Exchange DLP Policy Deleted (`rules/integrations/o365/defense_evasion_exchange_dlp_policy_removed.toml`)
- `ff4dd44a-0ac6-44c4-8609-3f81bc820f02` M365 Exchange Mail Flow Transport Rule Created (`rules/integrations/o365/exfiltration_exchange_transport_rule_creation.toml`)
- `b2951150-658f-4a60-832f-a00d1e6c6745` Deprecated - M365 Security Compliance Unusual Volume of File Deletion (`rules/integrations/o365/impact_security_compliance_unusual_volume_of_file_deletion.toml`)
- `2de10e77-c144-4e69-afb7-344e7127abd0` M365 Identity Unusual SSO Authentication Errors for User (`rules/integrations/o365/initial_access_identity_unusual_sso_errors_for_user.toml`)
- `c9636a6e-125e-11f1-9cd3-f661ea17fbce` M365 Exchange MFA Notification Email Deleted or Moved (`rules/integrations/o365/defense_evasion_mfa_notification_email_deleted.toml`)
- `0136b315-b566-482f-866c-1d8e2477ba16` Deprecated - M365 Security Compliance User Restricted from Sending Email (`rules/integrations/o365/initial_access_security_compliance_user_restricted_from_sending_email.toml`)
- `7fc95782-4bd1-11f0-9838-f661ea17fbcd` M365 Exchange Mailbox Items Accessed Excessively (`rules/integrations/o365/collection_exchange_excessive_mail_items_accessed.toml`)
- `491651da-125b-11f1-af7d-f661ea17fbce` M365 SharePoint/OneDrive File Access via PowerShell (`rules/integrations/o365/collection_sharepoint_file_download_via_powershell.toml`)
- `721999d0-7ab2-44bf-b328-6e63367b9b29` Deprecated - M365 Security Compliance Potential Ransomware Activity (`rules/integrations/o365/impact_security_compliance_potential_ransomware_activity.toml`)
- `bbd1a775-8267-41fa-9232-20e5582596ac` M365 Teams Custom Application Interaction Enabled (`rules/integrations/o365/defense_evasion_teams_custom_app_interaction_allowed.toml`)
- `0e524fa6-eed3-11ef-82b4-f661ea17fbce` M365 OneDrive/SharePoint Excessive File Downloads (`rules/integrations/o365/collection_onedrive_excessive_file_downloads.toml`)
- `ca79768e-40e1-4e45-a097-0e5fbc876ac2` M365 Exchange Malware Filter Rule Modified (`rules/integrations/o365/defense_evasion_exchange_malware_filter_rule_mod.toml`)
- `a989fa1b-9a11-4dd8-a3e9-f0de9c6eb5f2` M365 Exchange Email Safe Link Policy Disabled (`rules/integrations/o365/defense_evasion_exchange_exchange_safelinks_disabled.toml`)
- `48819484-9826-4083-9eba-1da74cd0eaf2` M365 Exchange Mailbox Accessed by Unusual Client (`rules/integrations/o365/collection_exchange_mailbox_access_by_unusual_client_app_id.toml`)
- `929d0766-204b-11f0-9c1f-f661ea17fbcd` M365 Identity OAuth Phishing via First-Party Microsoft Application (`rules/integrations/o365/initial_access_identity_oauth_phishing_via_first_party_microsoft_application.toml`)
- `5e552599-ddec-4e14-bad1-28aa42404388` Deprecated - M365 Teams Guest Access Enabled (`rules/integrations/o365/persistence_teams_guest_access_enabled.toml`)
- `98ebd6a1-77db-4fe1-b4fd-1bd3c737b780` M365 SharePoint Site Administrator Added (`rules/integrations/o365/privilege_escalation_sharepoint_site_collection_admin_added.toml`)
- `36188365-f88f-4f70-8c1d-0b9554186b9c` M365 Identity OAuth Flow by First-Party Microsoft App from Multiple IPs (`rules/integrations/o365/defense_evasion_entra_id_susp_oauth2_authorization.toml`)
- `98995807-5b09-4e37-8a54-5cae5dc932d7` M365 Exchange Management Group Role Assigned (`rules/integrations/o365/persistence_exchange_management_role_assignment.toml`)
- `3d753eb2-68c4-404a-9279-91a3ad490765` M365 Identity OAuth ROPC Grant via Legacy Authentication Client (`rules/integrations/o365/initial_access_identity_ropc_grant_via_legacy_authenticated_client.toml`)
- `03024bd9-d23f-4ec1-8674-3cf1a21e130b` M365 Exchange Email Safe Attachment Rule Disabled (`rules/integrations/o365/defense_evasion_exchange_safe_attach_rule_disabled.toml`)
- `4f2654e4-125b-11f1-af7d-f661ea17fbce` M365 SharePoint Search for Sensitive Content (`rules/integrations/o365/discovery_sharepoint_sensitive_term_search.toml`)
- `275b972d-2fed-44fc-9214-08603b3318e3` M365 Potential AiTM UserLoggedIn via Office App (Tycoon2FA) (`rules/integrations/o365/initial_access_tycoon_o365.toml`)
- `514121ce-c7b6-474a-8237-68ff71672379` M365 Exchange DKIM Signing Configuration Disabled (`rules/integrations/o365/defense_evasion_exchange_dkim_signing_config_disabled.toml`)
- `0e52157a-8e96-4a95-a6e3-5faae5081a74` M365 SharePoint Malware File Detected (`rules/integrations/o365/lateral_movement_sharepoint_malware_uploaded.toml`)
- `7e2abdb3-c7b0-4e11-ba2f-6657602800a1` M365 Identity Device Code Grant by an Unusual User (Non-Compliant Device) (`rules/integrations/o365/initial_access_identity_oauth_device_code_grant_unusual_user_noncompliant_device.toml`)
- `272a6484-2663-46db-a532-ef734bf9a796` M365 Exchange Mail Flow Transport Rule Modified (`rules/integrations/o365/exfiltration_exchange_transport_rule_modification.toml`)
- `88671231-6626-4e1b-abb7-6e361a171fbb` M365 Identity Global Administrator Role Assigned (`rules/integrations/o365/persistence_entra_id_global_administrator_role_assign.toml`)
- `27f7c15a-91f8-4c3d-8b9e-1f99cc030a51` Deprecated - M365 Teams External Access Enabled (`rules/integrations/o365/defense_evasion_teams_external_access_enabled.toml`)
- `fcd2e4be-6ec4-482f-9222-6245367cd738` M365 Identity OAuth Flow by User Sign-in to Device Registration (`rules/integrations/o365/credential_access_entra_id_device_reg_via_oauth_redirection.toml`)
- `ec8efb0c-604d-42fa-ac46-ed1cfbc38f78` M365 Exchange Inbox Forwarding Rule Created (`rules/integrations/o365/collection_exchange_new_inbox_rule.toml`)
- `d743ff2a-203e-4a46-a3e3-40512cfe8fbb` M365 Exchange Malware Filter Policy Deleted (`rules/integrations/o365/defense_evasion_exchange_malware_filter_policy_deletion.toml`)
- `32d3ad0e-6add-11ef-8c7b-f661ea17fbcc` M365 Identity Login from Atypical Region (`rules/integrations/o365/initial_access_entra_id_portal_login_atypical_travel.toml`)
- `26f68dba-ce29-497b-8e13-b4fde1db5a2d` M365 Identity User Brute Force Attempted (`rules/integrations/o365/credential_access_entra_id_potential_user_account_brute_force.toml`)
- … 另有 8 条，用 `sync.py next --category integrations/o365` 查看

### `integrations/okta`

未汉化 50 条：
- `ee39a9f7-5a79-4b0a-9815-d36b3cf28d3e` Okta FastPass Phishing Detection (`rules/integrations/okta/initial_access_okta_fastpass_phishing.toml`)
- `5889760c-9858-4b4b-879c-e299df493295` Potential Okta Brute Force (Multi-Source) (`rules/integrations/okta/credential_access_okta_brute_force_multi_source.toml`)
- `cdbebdc1-dc97-43c6-a538-f26a20c0a911` Okta User Session Impersonation (`rules/integrations/okta/credential_access_user_impersonation_access.toml`)
- `50887ba8-7ff7-11ee-a038-f661ea17fbcd` Multiple Okta User Auth Events with Same Device Token Hash Behind a Proxy (`rules/integrations/okta/credential_access_multiple_auth_events_from_single_device_behind_proxy.toml`)
- `6f1bb4b2-7dc8-11ee-92b2-f661ea17fbcd` First Occurrence of Okta User Session Started via Proxy (`rules/integrations/okta/initial_access_first_occurrence_user_session_started_via_proxy.toml`)
- `23f18264-2d6d-11ef-9413-f661ea17fbce` Potential Okta Brute Force (Device Token Rotation) (`rules/integrations/okta/credential_access_okta_brute_force_device_token_rotation.toml`)
- `8a0fbd26-867f-11ee-947c-f661ea17fbcd` Potential Okta MFA Bombing via Push Notifications (`rules/integrations/okta/credential_access_okta_mfa_bombing_via_push_notifications.toml`)
- `af2d8e4c-3b7c-4e91-8f5a-6c9d0e1f2a3b` Okta Alerts Following Unusual Proxy Authentication (`rules/integrations/okta/initial_access_okta_suspicious_activity_after_proxy_authentication.toml`)
- `6649e656-6f85-11ef-8876-f661ea17fbcc` Unauthorized Scope for Public App OAuth2 Token Grant with Client Credentials (`rules/integrations/okta/defense_evasion_first_occurence_public_app_client_credential_token_exchange.toml`)
- `f994964f-6fce-4d75-8e79-e16ccc412588` Suspicious Activity Reported by Okta User (`rules/integrations/okta/initial_access_suspicious_activity_reported_by_okta_user.toml`)
- `29b53942-7cd4-11ee-b70e-f661ea17fbcd` New Okta Identity Provider (IdP) Added by Admin (`rules/integrations/okta/persistence_new_idp_successfully_added_by_admin.toml`)
- `cc92c835-da92-45c9-9f29-b4992ad621a0` Attempt to Deactivate an Okta Policy Rule (`rules/integrations/okta/defense_evasion_okta_attempt_to_deactivate_okta_policy_rule.toml`)
- `50742e15-c5ef-49c8-9a2d-31221d45af58` Okta Successful Login After Credential Attack (`rules/integrations/okta/credential_access_okta_successful_login_after_credential_attack.toml`)
- `000047bb-b27a-47ec-8b62-ef1a5d2c9e19` Attempt to Modify an Okta Policy Rule (`rules/integrations/okta/defense_evasion_okta_attempt_to_modify_okta_policy_rule.toml`)
- `621e92b6-7e54-11ee-bdc0-f661ea17fbcd` Multiple Okta Sessions Detected for a Single User (`rules/integrations/okta/lateral_movement_multiple_sessions_for_single_user.toml`)
- `c74fd275-ab2c-4d49-8890-e2943fa65c09` Attempt to Modify an Okta Application (`rules/integrations/okta/impact_okta_attempt_to_modify_okta_application.toml`)
- `95b99adc-2cda-11ef-84e1-f661ea17fbce` Multiple Okta User Authentication Events with Same Device Token Hash (`rules/integrations/okta/credential_access_okta_authentication_for_multiple_users_with_the_same_device_token_hash.toml`)
- `e6e3ecff-03dd-48ec-acbd-54a04de10c68` Possible Okta DoS Attack (`rules/integrations/okta/impact_possible_okta_dos_attack.toml`)
- `2e56e1bc-867a-11ee-b13e-f661ea17fbcd` Okta User Sessions Started from Different Geolocations (`rules/integrations/okta/initial_access_okta_user_sessions_started_from_different_geolocations.toml`)
- `c749e367-a069-4a73-b1f2-43a3798153ad` Attempt to Delete an Okta Network Zone (`rules/integrations/okta/defense_evasion_attempt_to_delete_okta_network_zone.toml`)
- `3805c3dc-f82c-4f8d-891e-63c24d3102b0` Attempted Bypass of Okta MFA (`rules/integrations/okta/credential_access_attempted_bypass_of_okta_mfa.toml`)
- `8a5c1e5f-ad63-481e-b53a-ef959230f7f1` Attempt to Deactivate an Okta Network Zone (`rules/integrations/okta/defense_evasion_attempt_to_deactivate_okta_network_zone.toml`)
- `edb91186-1c7e-4db8-b53e-bfa33a1a0a8a` Attempt to Deactivate an Okta Application (`rules/integrations/okta/impact_okta_attempt_to_deactivate_okta_application.toml`)
- `e48236ca-b67a-4b4e-840c-fdc7782bc0c3` Attempt to Modify an Okta Network Zone (`rules/integrations/okta/defense_evasion_okta_attempt_to_modify_okta_network_zone.toml`)
- `9ed5d08f-aad6-4c03-838c-d686da887c2c` Okta AiTM Session Cookie Replay (`rules/integrations/okta/credential_access_okta_aitm_session_cookie_replay.toml`)
- `e90ee3af-45fc-432e-a850-4a58cf14a457` High Number of Okta User Password Reset or Unlock Attempts (`rules/integrations/okta/defense_evasion_suspicious_okta_user_password_reset_or_unlock_attempts.toml`)
- `42bf698b-4738-445b-8231-c834ddefd8a0` Potential Okta Password Spray (Single Source) (`rules/integrations/okta/credential_access_okta_password_spray_single_source.toml`)
- `94e734c0-2cda-11ef-84e1-f661ea17fbce` Potential Okta Credential Stuffing (Single Source) (`rules/integrations/okta/credential_access_okta_credential_stuffing_single_source.toml`)
- `676cff2b-450b-4cf1-8ed2-c0c58a4a2dd7` Attempt to Revoke Okta API Token (`rules/integrations/okta/impact_attempt_to_revoke_okta_api_token.toml`)
- `d5d86bf5-cf0c-4c06-b688-53fdc072fdfd` Attempt to Delete an Okta Policy Rule (`rules/integrations/okta/defense_evasion_okta_attempt_to_delete_okta_policy_rule.toml`)
- `cd89602e-9db0-48e3-9391-ae3bf241acd8` MFA Deactivation with no Re-Activation for Okta User Account (`rules/integrations/okta/persistence_mfa_deactivation_with_no_reactivation.toml`)
- `d48e1c13-4aca-4d1f-a7b1-a9161c0ad86f` Attempt to Delete an Okta Application (`rules/integrations/okta/impact_okta_attempt_to_delete_okta_application.toml`)
- `97a8e584-fd3b-421f-9b9d-9c9d9e57e9d7` Potentially Successful Okta MFA Bombing via Push Notifications (`rules/integrations/okta/credential_access_okta_potentially_successful_okta_bombing_via_push_notifications.toml`)
- `729aa18d-06a6-41c7-b175-b65b739b1181` Attempt to Reset MFA Factors for an Okta User Account (`rules/integrations/okta/persistence_attempt_to_reset_mfa_factors_for_okta_user_account.toml`)
- `b8075894-0b62-46e5-977c-31275da34419` Administrator Privileges Assigned to an Okta Group (`rules/integrations/okta/persistence_administrator_privileges_assigned_to_okta_group.toml`)
- `2d3c27d5-d133-4152-8102-8d051619ec4a` Potential Okta Password Spray (Multi-Source) (`rules/integrations/okta/credential_access_okta_password_spray_multi_source.toml`)
- `1ceb05c4-7d25-11ee-9562-f661ea17fbcd` Okta Sign-In Events via Third-Party IdP (`rules/integrations/okta/initial_access_sign_in_events_via_third_party_idp.toml`)
- `1502a836-84b2-11ef-b026-f661ea17fbcc` Successful Application SSO from Rare Unknown Client Device (`rules/integrations/okta/initial_access_successful_application_sso_from_unknown_client_device.toml`)
- `e08ccd49-0380-4b2b-8d71-8000377d6e49` Attempts to Brute Force an Okta User Account (`rules/integrations/okta/credential_access_attempts_to_brute_force_okta_user_account.toml`)
- `b4bb1440-0fcb-4ed1-87e5-b06d58efc5e9` Attempt to Delete an Okta Policy (`rules/integrations/okta/defense_evasion_okta_attempt_to_delete_okta_policy.toml`)
- … 另有 10 条，用 `sync.py next --category integrations/okta` 查看

### `integrations/pad`

未汉化 19 条：
- `fbb10f1e-77cb-42f9-994e-5da17fc3fc15` Unusual Source IP for Okta Privileged Operations Detected (`rules/integrations/pad/privileged_access_ml_okta_rare_source_ip_by_user.toml`)
- `178770e0-5c20-4246-b430-e216a2888b23` Spike in User Lifecycle Management Change Events (`rules/integrations/pad/privileged_access_ml_okta_spike_in_user_lifecycle_management_changes.toml`)
- `8c9ae3e2-f0b1-4b2c-9eba-bd87c2db914f` Unusual Host Name for Okta Privileged Operations Detected (`rules/integrations/pad/privileged_access_ml_okta_rare_host_name_by_user.toml`)
- `138520d2-11ff-4288-a80e-a45b36dca4b1` Spike in Group Membership Events (`rules/integrations/pad/privileged_access_ml_okta_spike_in_group_membership_changes.toml`)
- `08be5599-3719-4bbd-8cbc-7e9cff556881` Unusual Source IP for Windows Privileged Operations Detected (`rules/integrations/pad/privileged_access_ml_windows_rare_source_ip_by_user.toml`)
- `bd1eadf6-3ac6-4e66-91aa-4a1e6711915f` Spike in Privileged Command Execution by a User (`rules/integrations/pad/privileged_access_ml_linux_high_count_privileged_process_events_by_user.toml`)
- `27569131-560e-441e-b556-0b9180af3332` Unusual Privilege Type assigned to a User (`rules/integrations/pad/privileged_access_ml_windows_rare_privilege_assigned_to_user.toml`)
- `0cbbb5e0-f93a-47fe-ab72-8213366c38f1` High Command Line Entropy Detected for Privileged Commands (`rules/integrations/pad/privileged_access_ml_linux_high_median_process_command_line_entropy_by_user.toml`)
- `6fb2280a-d91a-4e64-a97e-1332284d9391` Spike in Special Privilege Use Events (`rules/integrations/pad/privileged_access_ml_windows_high_count_special_privilege_use_events.toml`)
- `5eac16ab-6d4f-427b-9715-f33e1b745fc7` Unusual Process Detected for Privileged Commands by a User (`rules/integrations/pad/privileged_access_ml_linux_rare_process_executed_by_user.toml`)
- `fb5d91d0-3b94-4f91-bf20-b6fbc4b2480a` Unusual Group Name Accessed by a User (`rules/integrations/pad/privileged_access_ml_windows_rare_group_name_by_user.toml`)
- `097ef0b8-fb21-4e45-ad89-d81666349c6a` Spike in Special Logon Events (`rules/integrations/pad/privileged_access_ml_windows_high_count_special_logon_events.toml`)
- `a8f7187f-76d6-4c1d-a1d5-1ff301ccc120` Unusual Region Name for Okta Privileged Operations Detected (`rules/integrations/pad/privileged_access_ml_okta_rare_region_name_by_user.toml`)
- `2bca4fcd-5228-4472-9071-148903a31057` Unusual Host Name for Windows Privileged Operations Detected (`rules/integrations/pad/privileged_access_ml_windows_rare_device_by_user.toml`)
- `a300dea6-e228-40e1-9123-a339e207378b` Unusual Spike in Concurrent Active Sessions by a User (`rules/integrations/pad/privileged_access_ml_okta_high_sum_concurrent_sessions_by_user.toml`)
- `3278313c-d6cd-4d49-aa24-644e1da6623c` Spike in Group Application Assignment Change Events (`rules/integrations/pad/privileged_access_ml_okta_spike_in_group_application_assignment_changes.toml`)
- `aa28f01d-bc93-4c8f-bc01-6f67f2a0a833` Spike in Group Lifecycle Change Events (`rules/integrations/pad/privileged_access_ml_okta_spike_in_group_lifecycle_changes.toml`)
- `d2703b82-f92c-4489-a4a7-62aa29a62542` Unusual Region Name for Windows Privileged Operations Detected (`rules/integrations/pad/privileged_access_ml_windows_rare_region_name_by_user.toml`)
- `02b4420d-eda2-4529-9e46-4a60eccb7e2d` Spike in Group Privilege Change Events (`rules/integrations/pad/privileged_access_ml_okta_spike_in_group_privilege_changes.toml`)

### `integrations/problemchild`

未汉化 8 条：
- `f5d9d36d-7c30-4cdb-a856-9f653c13d4e0` Parent Process Detected with Suspicious Windows Process(es) (`rules/integrations/problemchild/defense_evasion_ml_suspicious_windows_process_cluster_from_parent_process.toml`)
- `1224da6c-0326-4b4f-8454-68cdc5ae542b` User Detected with Suspicious Windows Process(es) (`rules/integrations/problemchild/defense_evasion_ml_suspicious_windows_process_cluster_from_user.toml`)
- `56004189-4e69-4a39-b4a9-195329d226e9` Unusual Process Spawned by a Host (`rules/integrations/problemchild/defense_evasion_ml_rare_process_for_a_host.toml`)
- `994e40aa-8c85-43de-825e-15f665375ee8` Machine Learning Detected a Suspicious Windows Event with a High Malicious Probability Score (`rules/integrations/problemchild/defense_evasion_ml_suspicious_windows_event_high_probability.toml`)
- `40155ee4-1e6a-4e4d-a63b-e8ba16980cfb` Unusual Process Spawned by a User (`rules/integrations/problemchild/defense_evasion_ml_rare_process_for_a_user.toml`)
- `bdfebe11-e169-42e3-b344-c5d2015533d3` Host Detected with Suspicious Windows Process(es) (`rules/integrations/problemchild/defense_evasion_ml_suspicious_windows_process_cluster_from_host.toml`)
- `ea09ff26-3902-4c53-bb8e-24b7a5d029dd` Unusual Process Spawned by a Parent Process (`rules/integrations/problemchild/defense_evasion_ml_rare_process_for_a_parent_process.toml`)
- `13e908b9-7bf0-4235-abc9-b5deb500d0ad` Machine Learning Detected a Suspicious Windows Event with a Low Malicious Probability Score (`rules/integrations/problemchild/defense_evasion_ml_suspicious_windows_event_low_probability.toml`)

### `threat_intel`

未汉化 6 条：
- `0c41e478-5263-4c69-8f9e-7dfd2c22da64` Threat Intel IP Address Indicator Match (`rules/threat_intel/threat_intel_indicator_match_address.toml`)
- `f3e22c8b-ea47-45d1-b502-b57b6de950b3` Threat Intel URL Indicator Match (`rules/threat_intel/threat_intel_indicator_match_url.toml`)
- `a61809f3-fb5b-465c-8bff-23a8a068ac60` Threat Intel Windows Registry Indicator Match (`rules/threat_intel/threat_intel_indicator_match_registry.toml`)
- `aab184d3-72b3-4639-b242-6597c99d8bca` Threat Intel Hash Indicator Match (`rules/threat_intel/threat_intel_indicator_match_hash.toml`)
- `fcf18de8-ad7d-4d01-b3f7-a11d5b3883af` Threat Intel Email Indicator Match (`rules/threat_intel/threat_intel_indicator_match_email.toml`)
- `3a657da0-1df2-11ef-a327-f661ea17fbcc` Rapid7 Threat Command CVEs Correlation (`rules/threat_intel/threat_intel_rapid7_threat_command.toml`)

## 自定义 / 未匹配

- `custom-win-gpo-change` 【自定义】Windows组策略对象变更
- `custom-linux-usermod-attribute` 【自定义】Linux账号属性修改
- `custom-linux-group-membership-change` 【自定义】Linux群组成员变更
- `custom-win-logon-success` 【自定义】Windows登录成功审计
- `custom-win-group-membership` 【自定义】Windows安全组成员变更
- `custom-linux-ssh-login-failure` 【自定义】Linux登录失败
- `custom-linux-useradd-account-create` 【自定义】Linux本地账号创建
- `custom-win-stale-computer-reuse` 【自定义】Windows疑似僵尸计算机账号重新活动
- `custom-win-computer-account-created` 【自定义】Windows计算机账号创建
- `custom-win-account-lockout` 【自定义】Windows账号锁定
- `custom-win-password-reset` 【自定义】Windows用户密码重置或修改
- `custom-win-user-disabled` 【自定义】Windows用户账号禁用
- `custom-win-special-privileges` 【自定义】Windows特殊特权登录
- `custom-linux-ssh-login-success-audit` 【自定义】Linux登录成功审计
- `custom-linux-passwd-reset` 【自定义】Linux账号密码重置
- `custom-win-user-attr-changed` 【自定义】Windows用户账号属性修改
- `custom-win-logon-failure` 【自定义】Windows域登录失败
- `custom-win-user-enabled` 【自定义】Windows用户账号启用
- `custom-linux-account-frequent-lock` 【自定义】Linux账号频繁锁定
- `custom-win-user-account-created` 【自定义】Windows用户账号创建
- `custom-linux-account-lock-unlock` 【自定义】Linux账号锁定或解锁

