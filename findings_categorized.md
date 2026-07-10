# 📊 GuardDuty Findings: Categorized by Type & Severity vs External Validation

> **Context:** This appendix categorizes the 295,626 GuardDuty findings by type and severity, overlaid with external threat intel validation results.

---

## Severity Distribution

| Severity | Label | Findings | % of Total | External Validation |
|:--------:|-------|--------:|-----------:|---------------------|
| 9 | CRITICAL | 7 | 0.002% | No IPs/domains to validate |
| 8 | HIGH | 238,036 | 80.5% | 0% confirmed by external sources |
| 5 | MEDIUM | 6,327 | 2.1% | 0% confirmed by external sources |
| 2 | LOW | 51,256 | 17.3% | Mostly internal/infrastructure |

---

## HIGH Severity (8) — DNS/Domain Based

These generate **80% of all findings** but have **zero external validation**:

| Finding Type | Findings | Unique Domains | External Status |
|---|---:|---:|---|
| Trojan:EC2/PhishingDomainRequest!DNS | 217,266 | 39,106 | ⚠️ 0/50 sample in URLhaus |
| Trojan:EC2/DriveBySourceTraffic!DNS | 16,989 | 3,761 | ⚠️ 0/50 sample in URLhaus |
| Backdoor:EC2/C&CActivity.B!DNS | 56 | 15 | 🔍 Not in public feeds |
| Trojan:EC2/DGADomainRequest.B | 14 | 14 | 🔍 DGA domains - ephemeral |
| UnauthorizedAccess:EC2/MetadataDNSRebind | 10 | 1 | ⚠️ `169.254.169.254.nip.io` |

**Key Insight:** GuardDuty's proprietary threat feed classified 234,335 DNS requests as malicious, but none appeared in URLhaus — the largest public malware URL database. These could be:
- True threats using private intelligence
- Overly broad classification of disposable domains
- False positives from domain reputation scoring

---

## HIGH Severity (8) — IP/Credential Based

| Finding Type | Findings | Unique IPs | AbuseIPDB Score | GreyNoise |
|---|---:|---:|---|---|
| Impact:IAMUser/AnomalousBehavior | 1,328 | 89 | 0% for all tested | Not observed |
| Exfiltration:IAMUser/AnomalousBehavior | 1,217 | 10 | 0% for all tested | Not observed |
| InstanceCredentialExfiltration.InsideAWS | 222 | 85 | N/A (AWS IPs) | N/A |
| InstanceCredentialExfiltration.OutsideAWS | 129 | 10 | 0% for tested | Not observed |
| UnauthorizedAccess:EC2/SSHBruteForce | 52 | 48 | Internal IPs (10.x) | N/A |
| Object:S3/MaliciousFile | 744 | 0 | No IP indicator | N/A |

**Key Insight:** The `InstanceCredentialExfiltration.InsideAWS` findings reference AWS-owned IPs (54.x, 44.x, 34.x, etc.) — these are lateral movement within AWS, not external threats. External tools can't validate these.

---

## MEDIUM Severity (5) — Custom Threat Lists & Behavior

| Finding Type | Findings | Unique IPs | AbuseIPDB | Notes |
|---|---:|---:|---|---|
| UnauthorizedAccess:EC2/MaliciousIPCaller.Custom | 2,887 | 64 | 0% score | Custom threat list IPs — **no public validation** |
| UnauthorizedAccess:IAMUser/MaliciousIPCaller.Custom | 1,682 | 12 | 0% score | Same custom list |
| Recon:IAMUser/MaliciousIPCaller.Custom | 890 | 2 | 0% score | 192.176.1.69 (656 hits), 195.235.15.200 (234 hits) |
| DefenseEvasion:EC2/UnusualDNSResolver | 300 | 185 | 0% score | **Includes 8.8.8.8 (58 hits), 1.1.1.1 (9 hits)** 🚨 |
| Recon:EC2/Portscan | 148 | 138 | N/A | All internal 10.x IPs |
| Behavior:EC2/NetworkPortUnusual | 81 | 31 | 0% score | University/corporate IPs |

**🚨 Critical Noise:** `DefenseEvasion:EC2/UnusualDNSResolver` flagged **Google DNS (8.8.8.8)** 58 times, **Cloudflare (1.1.1.1)** 9 times, and **OpenDNS (208.67.222.222)** as threats. These are definitively false positives.

**Custom Threat List Gap:** The `MaliciousIPCaller.Custom` findings reference IPs from a custom threat list that has **zero corroboration** in any public threat feed. The top offender (192.176.1.x subnet) generated 2,500+ alerts with no external evidence of malice.

---

## LOW Severity (2) — Informational

| Finding Type | Findings | Unique IPs | Actionability |
|---|---:|---:|---|
| Recon:EC2/PortProbeUnprotectedPort | 48,547 | 0 | Internet noise — no source IPs stored |
| Discovery:IAMUser/AnomalousBehavior | 753 | 233 | API enumeration — 0% AbuseIPDB score |
| Stealth:IAMUser/CloudTrailLoggingDisabled | 428 | 5 | Operational, not threat |
| UnauthorizedAccess:EC2/SSHBruteForce | 272 | 47 | Internal 10.x IPs — lateral |
| Policy:S3/BucketBlockPublicAccessDisabled | 196 | 31 | Config drift — known AWS IPs |
| Policy:IAMUser/RootCredentialUsage | 51 | 3 | Legitimate admin activity |

---

## Summary: Finding Type vs External Validation Matrix

| Category | Findings | GuardDuty Says | External Says | Verdict |
|---|---:|---|---|---|
| DNS Phishing (Sev 8) | 234,255 | Trojan/Phishing | Not in URLhaus | **UNVERIFIABLE** |
| Port Probes (Sev 2) | 48,547 | Recon | No IPs to check | **NOISE** |
| Custom IP Lists (Sev 5) | 5,459 | Malicious | 0% AbuseIPDB | **UNCONFIRMED** |
| DNS Resolvers (Sev 5) | 300 | Defense Evasion | Known services | **FALSE POSITIVE** |
| IAM Anomalous (Sev 2-8) | 4,408 | Anomalous | 0% AbuseIPDB | **UNCONFIRMED** |
| Credential Exfil (Sev 8) | 351 | Unauthorized | AWS-owned IPs | **INTERNAL** |
| S3 Policy (Sev 2-8) | 961 | Policy Violation | Known AWS IPs | **OPERATIONAL** |

---

## Recommendations by Finding Type

### Suppress Immediately
- `DefenseEvasion:EC2/UnusualDNSResolver` for 8.8.8.8, 8.8.4.4, 1.1.1.1, 1.0.0.1, 208.67.222.222
- `Policy:IAMUser/RootCredentialUsage` from known admin IPs

### Validate Custom Threat Lists
- `MaliciousIPCaller.Custom` — review 192.176.1.x and 213.160.156.x subnets
- Cross-reference with AbuseIPDB quarterly; remove if no external corroboration

### Investigate with Priority
- `Backdoor:EC2/C&CActivity.B!DNS` (15 unique domains, sev 8) — check if domains resolve
- `InstanceCredentialExfiltration.OutsideAWS` (10 IPs, sev 8) — actual data exfil risk
- `AttackSequence:IAM/CompromisedCredentials` (7 findings, sev 9) — correlated attack chains

### Accept as Operational
- `S3/BucketBlockPublicAccessDisabled` — remediate via config management, not SOC
- `Stealth:S3/ServerAccessLoggingDisabled` — feed to compliance, not security ops

---

*Appendix to GuardDuty Threat Intel Validation Executive Report*
