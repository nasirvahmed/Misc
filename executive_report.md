# 🛡️ GuardDuty Independent Threat Intelligence Validation

> **Report Date:** 2026-07-10 15:55  
> **Methodology:** Cross-reference GuardDuty IOCs against GreyNoise, AbuseIPDB, and URLhaus

---

## 1. Executive Summary

GuardDuty generated **295,626 findings** referencing:
- **50** unique public IP addresses
- **40,908** unique domains (sample of 50 validated)

### IP Validation Results

| Category | Count | Percentage |
|----------|------:|-----------:|
| ✅ Confirmed Malicious | 0 | 0.0% |
| ⚠️ Likely Noise/Benign | 45 | 90.0% |
| ❓ Unverifiable | 5 | 10.0% |

### Domain Validation Results

| Category | Count |
|----------|------:|
| 🔴 In URLhaus (known malware) | 0 |
| ⚪ Not in URLhaus | 50 |
| 🟠 Active malware hosting | 0 |

---

## 2. GuardDuty Noise: False Positives & Benign Indicators

> These IPs were flagged by GuardDuty but external sources indicate they are **benign, whitelisted, or have zero abuse history**.

### B. Zero External Reports (45 IPs)

No abuse reports in 90 days — likely stale or low-confidence alerts.

| IP | ISP | Country |
|---|---|---|
| `102.89.32.126` | MTN Nigeria | NG |
| `102.89.22.141` | MTNN-OJOTA-REGION-PREFIXES | NG |
| `103.120.6.144` | HostRoyale Technologies Pvt Ltd | AU |
| `103.162.75.75` | Team Technic | IN |
| `103.174.111.201` | 3 Way Cable Communications Private Limit | IN |
| `103.110.164.24` | Esto Broadband Pvt Ltd | IN |
| `100.31.30.153` | Amazon Data Services Northern Virginia | US |
| `103.210.134.122` | Assistive Networks and Technologies Pvt  | IN |
| `103.116.136.41` | SKYNET SERVICES | IN |
| `103.184.239.38` | Kerala Vision Broad Band Private Limited | IN |
| `103.168.81.139` | SMARTFI NETWORKS LLP | IN |
| `100.48.57.28` | Amazon Data Services Northern Virginia | US |
| `100.20.125.19` | Amazon.com, Inc. | US |
| `103.106.232.9` | Hbs Network Private Limited | IN |
| `103.16.71.230` | Gatik Business Solutions | IN |
| `103.110.164.17` | Esto Broadband Pvt Ltd | IN |
| `103.177.83.247` | Sancfil Technologies Internet Services P | IN |
| `100.8.67.93` | Verizon Business | US |
| `103.137.51.168` | Pteron Communication Pvt. Ltd. | IN |
| `103.110.165.121` | Esto Broadband Pvt Ltd | IN |

*...and 25 more*

**📊 Impact:** 90.0% of GuardDuty IP indicators are likely noise, generating alert fatigue without actionable intelligence.

---

## 3. Validated Threats: Confirmed by External Intelligence

⚠️ **No IPs were independently confirmed as malicious** by external sources.

This suggests GuardDuty may be using proprietary threat feeds not reflected in public threat intelligence, OR the indicators are stale.

---

## 4. Blind Spots: What GuardDuty Misses

External threat intel provides context that GuardDuty **does NOT** surface:

### A. Malware Family Attribution

| GuardDuty Says | External Intel Provides |
|---|---|
| "PhishingDomainRequest" | Specific malware family (Emotet, QBot, IcedID) |
| "DriveBySourceTraffic" | Active download URLs and payload hashes |
| "C&CActivity" | C2 framework identification and campaign tracking |

### B. IP Reputation Context

GuardDuty classifies by **behavior** but lacks:

| Missing Context | Why It Matters |
|---|---|
| ISP/hosting provider | Distinguish bulletproof hosting vs legitimate |
| Historical abuse patterns | Repeat offender vs first offense |
| Community consensus | How many orgs report the same IP |
| Geographic risk profiling | Identify unlikely source countries |

### C. Active Threat Status

GuardDuty findings may reference **stale indicators**. External services provide:

- **URLhaus:** Is the malware URL still serving payloads?
- **GreyNoise:** Is the IP still actively scanning?
- **AbuseIPDB:** Are reports still coming in? (`last_reported_at`)

### D. Prioritization Intelligence

| GuardDuty | External Sources |
|---|---|
| Severity 1-8 scale | AbuseIPDB: 0-100% confidence score |
| No scanner distinction | GreyNoise: mass scanner vs targeted attack |
| Generic finding type | URLhaus: ransomware vs coinminer vs botnet |

---

## 5. Cost of Sole Reliance on GuardDuty

```
┌─────────────────────────────────────────────────────────────────────────┐
│  73.8% of all findings (218,330) are DNS-based phishing domain alerts   │
│  with NO external validation available for most domains.                │
│  GuardDuty uses proprietary threat feeds that cannot be independently   │
│  verified.                                                              │
└─────────────────────────────────────────────────────────────────────────┘
```

### Alert Fatigue

- **90.0%** of IP indicators are unconfirmed/benign
- **295,626** total findings with limited prioritization guidance
- SOC teams cannot distinguish critical from informational

### Response Gap

- GuardDuty tells you **WHAT** happened but not **WHO/WHY**
- No malware family = no ability to scope the campaign
- No community consensus = no confidence in blocking decisions

---

## 6. Recommendations

### 1. Integrate External Threat Intel Feeds

- Add AbuseIPDB/GreyNoise enrichment to SIEM correlation rules
- Auto-suppress GuardDuty alerts for known benign IPs (RIOT list)
- Use URLhaus for malware family attribution on DNS findings

### 2. Reduce Noise

- Create suppression rules for known DNS resolvers (8.8.8.8, 1.1.1.1)
- Filter `UnusualDNSResolver` findings that flag legitimate resolvers
- Tune `MaliciousIPCaller.Custom` threat lists quarterly

### 3. Enhance Detection

- GuardDuty alone is **insufficient** for threat attribution
- Layer with: MISP, VirusTotal, Shodan for complete picture
- Consider GuardDuty as **detection layer**, not **intelligence layer**

### 4. Operationalize Confidence Scoring

| Action | Threshold |
|---|---|
| Auto-block | AbuseIPDB score ≥ 75% |
| Escalate to IR | GreyNoise confirmed malicious |
| Priority domain block | URLhaus status = 'online' |
| Suppress alert | GreyNoise RIOT or AbuseIPDB whitelisted |

---

*Report generated by GuardDuty Threat Intel Validator*
