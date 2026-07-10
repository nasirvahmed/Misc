# 🛡️ GuardDuty Independent Threat Intelligence Validation

> **Report Date:** 2026-07-10 17:46  
> **Methodology:** Cross-reference GuardDuty IOCs against GreyNoise, AbuseIPDB, and URLhaus

---

## 1. Executive Summary

GuardDuty generated **295,626 findings** referencing:
- **5** unique public IP addresses
- **40,908** unique domains (sample of 0 validated)

### IP Validation Results

| Category | Count | Percentage |
|----------|------:|-----------:|
| ✅ Confirmed Malicious | 0 | 0.0% |
| ⚠️ Likely Noise/Benign | 5 | 100.0% |
| ❓ Unverifiable | 0 | 0.0% |

---

## 🏢 Known Infrastructure: Excluded from Threat Analysis

**Total IPs excluded:** 72 / 724 (9.9% of all public IPs)

### Ericsson Infrastructure (Intentional Monitoring)

> **Context:** Ericsson IPs were **intentionally added** to the GuardDuty custom threat list for **visibility/tracking purposes**, not because they represent a real threat. This is a deliberate use of GuardDuty's custom threat list as a network activity monitor for partner traffic.

| Detail | Value |
|---|---|
| Ericsson IPs on custom list | 67 |
| Findings generated | ~5,400+ |
| Purpose | Traffic visibility / partner monitoring |
| Threat level | None — known partner infrastructure |

**⚠️ Implication for this analysis:** These findings are **not threats** and inflate GuardDuty's alert count. They have been excluded from external validation to avoid skewing results. However, this practice contributes to alert fatigue — SOC analysts cannot distinguish intentional tracking alerts from genuine threats without additional context.

**Recommendation:** Consider tagging these findings with a custom label or using GuardDuty **suppression rules with auto-archiving** to separate Ericsson tracking alerts from genuine threats — keeps the visibility without polluting SOC queues.

### Vonage Infrastructure (Known Service Provider)

> Vonage/Vonage Business (UCaaS provider) IPs flagged by GuardDuty as `NetworkPortUnusual` or `UnusualDNSResolver` — expected behavior from VoIP infrastructure.

| IP | Service | Finding Type |
|---|---|---|
| `104.192.48.6` | Vonage UCaaS | Behavior:EC2/NetworkPortUnusual |
| `216.147.7.132` | Vonage UCaaS | Behavior:EC2/NetworkPortUnusual |
| `216.9.65.2` | Vonage UCaaS | Behavior:EC2/NetworkPortUnusual |
| `72.5.150.10` | Vonage UCaaS | Behavior:EC2/NetworkPortUnusual |
| `72.5.150.11` | Vonage UCaaS | Behavior:EC2/NetworkPortUnusual |

**Action:** Suppress GuardDuty findings for known Vonage CIDR ranges.

### Exclusion Summary

| Source | IPs | Reason for Exclusion | Recommendation |
|---|---:|---|---|
| Ericsson | 67 | Intentional tracking (not a threat) | Suppression rules + auto-archive |
| Vonage | 5 | Known UCaaS provider | Add to GuardDuty suppression rules |

---

## 2. GuardDuty Noise: False Positives & Benign Indicators

> These IPs were flagged by GuardDuty but external sources indicate they are **benign, whitelisted, or have zero abuse history**.

### B. Zero External Reports (5 IPs)

No abuse reports in 90 days — likely stale or low-confidence alerts.

| IP | ISP | Country |
|---|---|---|
| `100.31.30.153` | Amazon Data Services Northern Virginia | US |
| `100.48.57.28` | Amazon Data Services Northern Virginia | US |
| `1.0.0.1` | APNIC and Cloudflare DNS Resolver projec | AU |
| `100.24.102.134` | Amazon Data Services Northern Virginia | US |
| `100.20.125.19` | Amazon.com, Inc. | US |

**📊 Impact:** 100.0% of GuardDuty IP indicators are likely noise, generating alert fatigue without actionable intelligence.

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

### Custom Threat List: Intentional Tracking vs Security Alerts

| Source | Purpose | Findings Generated | Impact on SOC |
|---|---|---:|---|
| Ericsson (67 IPs) | Partner traffic monitoring | ~5,400 | Alerts indistinguishable from real threats |
| Vonage (5 IPs) | UCaaS provider (not intentional) | ~80 | Behavioral false positives |

**Issue:** Using the threat intelligence list for operational monitoring mixes security signals with tracking data, making it impossible for analysts to prioritize without manual investigation.

### Alert Fatigue

- **100.0%** of IP indicators are unconfirmed/benign
- **295,626** total findings with limited prioritization guidance
- SOC teams cannot distinguish critical from informational

### Response Gap

- GuardDuty tells you **WHAT** happened but not **WHO/WHY**
- No malware family = no ability to scope the campaign
- No community consensus = no confidence in blocking decisions

---

## 6. Recommendations

### 🟠 P1. Reduce Monitoring Noise from Intentional Tracking

- **Ericsson (67 IPs):** Currently using custom threat list for partner traffic visibility. This inflates alert counts by ~5,400 findings. Use **GuardDuty suppression rules with auto-archive** to keep visibility without flooding SOC — findings still exist for audit but don't trigger analyst workflows.
- **Vonage (5 IPs):** UCaaS provider traffic triggering behavioral findings. Add to **GuardDuty trusted IP list** or suppression rules.

This reduces noise by **~5,400+ findings** without losing visibility (move to appropriate monitoring tool instead).

### 1. Integrate External Threat Intel Feeds

- Add AbuseIPDB/GreyNoise enrichment to SIEM correlation rules
- Auto-suppress GuardDuty alerts for known benign IPs (RIOT list)
- Use URLhaus for malware family attribution on DNS findings
- Add VirusTotal for multi-vendor consensus scoring
- Use AlienVault OTX for campaign/threat actor attribution

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
