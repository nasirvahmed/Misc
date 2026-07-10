# 📊 GuardDuty Threat Intelligence Validation — Visual Report

> **Report Date:** 2026-07-10  
> **Scope:** 295,626 findings | 724 public IPs | 40,908 domains  
> **Validated Against:** GreyNoise, AbuseIPDB, URLhaus

---

## 🎯 Validation Results at a Glance

```mermaid
pie title IP Validation Results (50 IP Sample)
    "Likely Noise/Benign (90%)" : 45
    "Unverifiable (10%)" : 5
    "Confirmed Malicious (0%)" : 0
```

```mermaid
pie title Domain Validation Results (50 Domain Sample)
    "Not in URLhaus (100%)" : 50
    "Known Malware (0%)" : 0
```

---

## 📈 Findings by Severity

```mermaid
pie title 295,626 Findings by Severity Level
    "HIGH - Severity 8 (80.5%)" : 238036
    "LOW - Severity 2 (17.3%)" : 51256
    "MEDIUM - Severity 5 (2.1%)" : 6327
    "CRITICAL - Severity 9 (0.002%)" : 7
```

---

## 🏗️ Finding Types — Volume vs Validation

```mermaid
graph LR
    subgraph "HIGH SEVERITY (8) — 238,036 findings"
        A[Phishing DNS<br/>217,266] -->|0 confirmed| X[❌ Unverifiable]
        B[DriveBy DNS<br/>16,989] -->|0 confirmed| X
        C[IAM Impact<br/>1,328] -->|0% AbuseIPDB| X
        D[Cred Exfil<br/>351] -->|AWS IPs| Y[⚠️ Internal]
        E[C&C DNS<br/>56] --> Z[🔍 Investigate]
    end

    subgraph "MEDIUM SEVERITY (5) — 6,327 findings"
        F[Custom IP List<br/>5,459] -->|0% AbuseIPDB| X
        G[DNS Resolvers<br/>300] -->|8.8.8.8, 1.1.1.1| W[🚨 False Positive]
    end

    subgraph "LOW SEVERITY (2) — 51,256 findings"
        H[Port Probes<br/>48,547] -->|No IPs stored| X
        I[Discovery<br/>753] -->|0% AbuseIPDB| X
    end

    style X fill:#ff6b6b,color:#fff
    style Y fill:#ffa94d,color:#fff
    style Z fill:#51cf66,color:#fff
    style W fill:#ff0000,color:#fff
```

---

## 🚨 Noise Breakdown: What GuardDuty Flags vs Reality

```mermaid
graph TD
    subgraph "GuardDuty Alert: DefenseEvasion:EC2/UnusualDNSResolver"
        DNS1["8.8.8.8 — 58 alerts"] --> R1["✅ Google Public DNS"]
        DNS2["8.8.4.4 — 11 alerts"] --> R2["✅ Google Public DNS"]
        DNS3["1.1.1.1 — 14 alerts"] --> R3["✅ Cloudflare DNS"]
        DNS4["208.67.222.222 — 1 alert"] --> R4["✅ OpenDNS (Cisco)"]
    end

    style DNS1 fill:#ff6b6b,color:#fff
    style DNS2 fill:#ff6b6b,color:#fff
    style DNS3 fill:#ff6b6b,color:#fff
    style DNS4 fill:#ff6b6b,color:#fff
    style R1 fill:#51cf66,color:#fff
    style R2 fill:#51cf66,color:#fff
    style R3 fill:#51cf66,color:#fff
    style R4 fill:#51cf66,color:#fff
```

---

## 📊 Top Finding Types by Volume

| # | Finding Type | Severity | Count | Bar |
|---|---|:---:|---:|---|
| 1 | Trojan:EC2/PhishingDomainRequest!DNS | 🔴 8 | 217,266 | ![](https://img.shields.io/badge/-%E2%96%88%E2%96%88%E2%96%88%E2%96%88%E2%96%88%E2%96%88%E2%96%88%E2%96%88%E2%96%88%E2%96%88%E2%96%88%E2%96%88%E2%96%88%E2%96%88%E2%96%88%E2%96%88%E2%96%88%E2%96%88%E2%96%88%E2%96%88-red) |
| 2 | Recon:EC2/PortProbeUnprotectedPort | 🟡 2 | 48,547 | ![](https://img.shields.io/badge/-%E2%96%88%E2%96%88%E2%96%88%E2%96%88%E2%96%88-orange) |
| 3 | Trojan:EC2/DriveBySourceTraffic!DNS | 🔴 8 | 16,989 | ![](https://img.shields.io/badge/-%E2%96%88%E2%96%88-red) |
| 4 | UnauthorizedAccess:EC2/MaliciousIPCaller.Custom | 🟠 5 | 2,887 | ![](https://img.shields.io/badge/-%E2%96%88-yellow) |
| 5 | UnauthorizedAccess:IAMUser/MaliciousIPCaller.Custom | 🟠 5 | 1,682 | ![](https://img.shields.io/badge/-%E2%96%88-yellow) |

---

## 🔍 External Intelligence Gap Analysis

```mermaid
quadrantChart
    title GuardDuty Findings: Severity vs External Validation
    x-axis "No External Evidence" --> "Externally Confirmed"
    y-axis "Low Severity" --> "High Severity"
    quadrant-1 "Validated Threats"
    quadrant-2 "Blind Trust Zone"
    quadrant-3 "Acceptable Noise"
    quadrant-4 "Confirmed Low Risk"
    "DNS Phishing (217K)": [0.1, 0.9]
    "DriveBy DNS (17K)": [0.1, 0.85]
    "Port Probes (48K)": [0.15, 0.15]
    "Custom IP List (5K)": [0.1, 0.5]
    "IAM Anomalous (4K)": [0.15, 0.6]
    "DNS Resolvers (300)": [0.05, 0.5]
    "Cred Exfil (351)": [0.3, 0.9]
    "C&C Activity (56)": [0.4, 0.9]
    "Attack Sequence (7)": [0.5, 0.95]
```

---

## 💰 Cost of Noise: Alert Fatigue Impact

```mermaid
graph TD
    A[295,626 Total<br/>GuardDuty Findings] --> B{External<br/>Validation}
    B -->|90% of IPs| C[🔴 No External<br/>Evidence of Malice<br/>~266,000 findings]
    B -->|0% confirmed| D[✅ Independently<br/>Confirmed Malicious<br/>0 findings]
    B -->|10%| E[❓ Cannot Determine<br/>~29,000 findings]

    C --> F[SOC Impact:<br/>Alert Fatigue]
    D --> G[SOC Impact:<br/>Zero Actionable Intel]
    E --> H[SOC Impact:<br/>Manual Triage Required]

    style C fill:#ff6b6b,color:#fff
    style D fill:#51cf66,color:#fff
    style E fill:#ffa94d,color:#fff
    style F fill:#495057,color:#fff
    style G fill:#495057,color:#fff
    style H fill:#495057,color:#fff
```

---

## 🗂️ Finding Category Heatmap

| MITRE Tactic | Sev 9 | Sev 8 | Sev 5 | Sev 2 | External Validation |
|---|:---:|:---:|:---:|:---:|---|
| **Execution** (DNS Trojan) | | 🟥 234K | | | ❌ None |
| **Reconnaissance** (Probes) | | | 🟧 148 | 🟨 48K | ❌ None |
| **Credential Access** | | 🟥 1.2K | 🟧 32 | | ❌ 0% AbuseIPDB |
| **Exfiltration** | | 🟥 1.2K | | | ❌ 0% AbuseIPDB |
| **Impact** | | 🟥 1.3K | | | ❌ 0% AbuseIPDB |
| **Defense Evasion** | | | 🟧 325 | | 🚨 FALSE POSITIVE |
| **Initial Access** | | | 🟧 61 | | ❌ 0% AbuseIPDB |
| **Lateral Movement** (Cred Exfil) | | 🟥 351 | | | ⚠️ AWS-internal |
| **Persistence** | | | 🟧 24 | | ❌ 0% AbuseIPDB |
| **Privilege Escalation** | | | 🟧 5 | | ❌ 0% AbuseIPDB |
| **Attack Sequence** | 🟪 7 | | | | 🔍 Investigate |

---

## 📋 Actionability Matrix

```mermaid
graph LR
    subgraph "SUPPRESS (70% of findings)"
        S1[DNS Phishing<br/>217K alerts]
        S2[Port Probes<br/>48K alerts]
        S3[DNS Resolvers<br/>300 alerts]
    end

    subgraph "VALIDATE (12% of findings)"
        V1[Custom IP List<br/>5.4K alerts]
        V2[IAM Anomalous<br/>4.4K alerts]
        V3[DriveBy DNS<br/>17K alerts]
    end

    subgraph "INVESTIGATE (0.3% of findings)"
        I1[Credential Exfil<br/>351 alerts]
        I2[C&C Activity<br/>56 alerts]
        I3[Attack Sequences<br/>7 alerts]
    end

    subgraph "OPERATIONAL (17.7% of findings)"
        O1[S3 Policy<br/>961 alerts]
        O2[CloudTrail<br/>428 alerts]
        O3[Root Usage<br/>51 alerts]
    end

    style S1 fill:#868e96,color:#fff
    style S2 fill:#868e96,color:#fff
    style S3 fill:#868e96,color:#fff
    style V1 fill:#ffa94d,color:#fff
    style V2 fill:#ffa94d,color:#fff
    style V3 fill:#ffa94d,color:#fff
    style I1 fill:#ff6b6b,color:#fff
    style I2 fill:#ff6b6b,color:#fff
    style I3 fill:#ff6b6b,color:#fff
    style O1 fill:#74c0fc,color:#fff
    style O2 fill:#74c0fc,color:#fff
    style O3 fill:#74c0fc,color:#fff
```

---

## 🎯 Recommendations Summary

| Priority | Action | Impact | Effort |
|:---:|---|---|---|
| 🔴 P1 | Suppress DNS resolver false positives (8.8.8.8, 1.1.1.1) | -300 alerts | Low |
| 🔴 P1 | Review custom threat list (192.176.1.x, 213.160.156.x) | -5,459 alerts | Medium |
| 🟠 P2 | Integrate AbuseIPDB enrichment in SIEM | Better prioritization | Medium |
| 🟠 P2 | Add URLhaus lookup for DNS findings | Malware attribution | Medium |
| 🟡 P3 | Route S3/CloudTrail findings to compliance (not SOC) | -1,600 alerts from SOC | Low |
| 🟡 P3 | Deploy GreyNoise RIOT for auto-suppression | Reduce benign IP alerts | High |

---

## 📊 Bottom Line

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                             │
│   GuardDuty alone: 295,626 alerts with NO prioritization intelligence       │
│                                                                             │
│   With external TI: <500 alerts worth investigating (~0.17%)                │
│                                                                             │
│   Signal-to-noise ratio: 1:590                                              │
│                                                                             │
│   Conclusion: GuardDuty is a DETECTION engine, not an INTELLIGENCE tool.    │
│               It must be augmented with external threat feeds to be          │
│               operationally useful.                                          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

*Generated by GuardDuty Threat Intel Validator | Data: GreyNoise Community, AbuseIPDB, URLhaus*
