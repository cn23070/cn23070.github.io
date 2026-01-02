
---
layout: post
title: Dissertation Artefact: Framework Decision Support Tool (FDST) – User Guide
subtitle: Dissertation artefact as part of my final dissertation for MSc Cybersecurity.
categories: Module_9
tags: [Module 9]
description: Evidence-based selection of cybersecurity governance frameworks for healthcare technology suppliers using CTQs and a weighted sum model.
permalink: /fdst-user-guide/
nav_order: 20
---

# Framework Decision Support Tool (FDST) – User Guide

---

## 1) Purpose

The **Framework Decision Support Tool (FDST)** helps healthcare technology suppliers and hospital procurement teams select cybersecurity governance frameworks using a transparent, evidence‑based methodology. It converts qualitative literature evidence into quantitative scores across five **Critical‑to‑Quality (CTQ)** criteria:

- Regulatory Compliance  
- Industry Acceptance  
- Scalability  
- Cost  
- Implementation & Maintenance Time

FDST’s goal is to make **trade‑offs explicit**, provide **auditable reasoning** for choices, and support **repeatable** decisions across different supplier contexts (SMB, enterprise, SaaS/service providers, regulated healthcare markets).

---

## 2) Audience & prerequisites

- **Audience**: Security leaders, governance/assurance teams, procurement/commercial managers, and technical program managers in healthcare and adjacent regulated sectors.  
- **Prerequisites**: Working knowledge of information security frameworks (e.g., ISO/IEC 27001, NIST CSF, COBIT 2019, HITRUST, SOC 2), basic Excel skills, and familiarity with risk/governance terminology.

---

## 3) Method overview & assumptions

FDST implements a **Weighted Sum Model (WSM)** across the five CTQs. It assumes:

1. Multiple frameworks may be suitable; priorities differ by stakeholder context.  
2. Evidence quality varies; the tool provides **scenario treatments** to mitigate bias.  
3. CTQ scores are derived using a 4‑level rubric (1.0 / 0.6 / 0.3 / 0.0) from structured evidence.  
4. CTQ weights are **normalized** so the total influence equals 1.0, ensuring comparability.

---

## 4) CTQs: definitions, scoring rubric & weights

### 4.1 CTQ definitions

- **Regulatory Compliance**: How well the framework aligns with mandatory laws and sector regulations (e.g., GDPR, HIPAA), and supports audits/assurance.  
- **Industry Acceptance**: Market trust signals (customer/regulator expectation, certification/attestation availability, cross‑sector adoption).  
- **Scalability**: Ability to tailor requirements across sizes/maturity levels; modular/adaptable control sets; integration potential with other frameworks.  
- **Cost**: Total cost of ownership (certification fees, consulting, audits, internal resourcing).  
- **Implementation & Maintenance Time**: Time to initial adoption/certification and ongoing upkeep.

### 4.2 Scoring rubric (row‑level evidence → numeric score)

| **Level** | **Score** | **Meaning** |
|---|---:|---|
| Strong positive (with evidence) | 1.0 | Explicit, high‑quality evidence of strong alignment/performance |
| Moderate positive (no direct evidence) | 0.6 | Implied or general alignment without explicit proof |
| Moderate negative / Weak / Mixed | 0.3 | Limited/conflicting evidence or constrained alignment |
| Strong negative (with evidence) | 0.0 | Explicit evidence of lack of alignment/performance |

> The tool averages row‑level scores per CTQ for each framework to produce CTQ averages used by WSM.

### 4.3 Default weights & normalization

**Default CTQ weights** (1‑5 scale):  
- Acceptance = 5  
- Regulatory = 5  
- Scalability = 4  
- Cost = 3  
- Time = 3  

**Normalized weights** used by WSM:  
- 0.25, 0.25, 0.20, 0.15, 0.15 (sum = 1.0)

You can change defaults in `CTQ_Scored` to reflect your context; normalization updates automatically.

---

## 5) Workbook structure & data dictionary

### 5.1 Sheets

| **Sheet** | **Purpose** |
|---|---|
| **CTQ_Scored** | Set CTQ priorities (weights 1–5) and view normalized weights. |
| **Frameworks_Scored** | Evidence register: Framework × CTQ rows with quality level and rubric score. |
| **WSM_Calc** | Core calculations: CTQ averages per framework, WSM scores/ranks, scenario blocks. |
| **Formulas_Overview** | Documentation of key formulas and ranges used in the model. |
| **Test_Scripts** | Lightweight test log confirming ranges, labels, and calculation consistency. |

### 5.2 Key fields (data dictionary)

- **Frameworks_Scored**  
  - *Framework*: ISO 27001, NIST CSF, HITRUST, SOC 2, COBIT 2019  
  - *CTQ*: Regulatory, Acceptance, Scalability, Cost, Time  
  - *Study Quality*: High / Moderate / Low  
  - *CTQ Score*: 1.0 / 0.6 / 0.3 / 0.0  
  - *Notes/Justification*: Short rationale linking score to evidence

- **CTQ_Scored**  
  - *CTQ Name*: Five CTQs listed above  
  - *Default Weight (1–5)*  
  - *Normalized Weight*: Auto‑computed (sum = 1.0)

- **WSM_Calc**  
  - *CTQ Averages per Framework*: Baseline and scenario variants  
  - *WSM Score*: Weighted sum across CTQs  
  - *Rank*: Descending rank by WSM Score  
  - *Evidence Counts*: Number of contributing rows per CTQ & framework

---

## 6) Steps to use (detailed)

1. **Set priorities**  
   Open `CTQ_Scored`. Assign 1–5 weights for each CTQ to reflect your stakeholder priorities.  
   - Compliance‑led: Keep Acceptance/Regulatory high.  
   - Agility/scale‑led: Increase Scalability; reduce Acceptance/Regulatory if assurance is secondary.  
   - Service‑assurance‑led: Increase Acceptance for attestation demand (SOC 2, ISO).

2. **Review evidence**  
   In `Frameworks_Scored`, confirm that the quotes/notes and **Study Quality** are sensible. Adjust CTQ row scores if new evidence emerges.

3. **View baseline results**  
   In `WSM_Calc`, inspect CTQ averages and baseline **WSM Score/Rank**. Use **evidence counts** to check confidence (thin coverage warrants caution).

4. **Run scenarios**  
   - **Scenario A**: Exclude Low‑quality evidence to test sensitivity.  
   - **Scenario B**: Retain only High‑quality evidence for strict decisions.  
   - **Scenario C**: Apply Quality weights (High=1.0, Moderate=0.75, Low=0.5).

5. **Interpret & decide**  
   Use Section 8 (outputs) and Section 10 (interpretation) to justify the choice. Consider hybrid adoption if a single framework doesn’t meet all CTQs.

6. **Document decision**  
   Capture chosen framework(s), CTQ weight profile, and scenario robustness notes (for audit and procurement defensibility).

---

## 7) Key formulas (Excel## 7) Key formulas (Excel)

=B2/SUM($B$2:$B$6)

**CTQ average per framework**

=IFERROR(AVERAGEIFS(Frameworks_Scored!$G$2:$G$264,
Frameworks_Scored!$A$2:$A$264,$A11,
Frameworks_Scored!$E$2:$E$264,B$10),"")

**WSM score (simple averaging)**

=IF(COUNTA(B11:F11)=0,"",
B11*$C$2 + C11*$C$3 + D11*$C$4 + E11*$C$5 + F11*$C$6)

**Optional: Dynamic normalization (avoid penalizing missing CTQs)**

=LET(
s,B11:F11,
w,$C$2:$C$6,
m,IF(s<>"",1,0),
denom,SUMPRODUCT(w,m),
IF(denom=0,"",SUMPRODUCT(s,w)/denom)
)

**Scenario A (Exclude Low)**

=IFERROR(AVERAGEIFS(Frameworks_Scored!$G$2:$G$264,
Frameworks_Scored!$A$2:$A$264,$A22,
Frameworks_Scored!$E$2:$E$264,B$21,
Frameworks_Scored!$B$2:$B$264,"<>Low"),"")

**Scenario B (High‑only)**

=IFERROR(AVERAGEIFS(Frameworks_Scored!$G$2:$G$264,
Frameworks_Scored!$A$2:$A$264,$A31,
Frameworks_Scored!$E$2:$E$264,B$30,
Frameworks_Scored!$B$2:$B$264,"High"),"")

**Scenario C (Quality‑weighted)**

=IFERROR(
($J$2SUMIFS(...,"High") + $J$3SUMIFS(...,"Moderate") + $J$4SUMIFS(...,"Low")) /
($J$2COUNTIFS(...,"High") + $J$3COUNTIFS(...,"Moderate") + $J$4COUNTIFS(...,"Low"))
,"")

---

## 8) Sample scenario outputs

> Default CTQ weighting profile: Acceptance=5, Regulatory=5, Scalability=4, Cost=3, Time=3 ⇒ normalized 0.25, 0.25, 0.20, 0.15, 0.15.

### 8.1 Baseline (All Evidence)
| **Framework** | **WSM Score** | **Rank** |
|---|---:|:---:|
| ISO 27001 | 0.7160 | 1 |
| NIST CSF | 0.5723 | 2 |
| HITRUST | 0.5626 | 3 |
| SOC 2 | 0.5600 | 4 |
| COBIT 2019 | 0.5344 | 5 |

### 8.2 Scenario A – Exclude Low Quality
| **Framework** | **WSM Score (A)** | **Rank (A)** |
|---|---:|:---:|
| ISO 27001 | 0.7149 | 1 |
| NIST CSF | 0.5713 | 2 |
| HITRUST | 0.5626 | 3 |
| SOC 2 | 0.5600 | 4 |
| COBIT 2019 | 0.5344 | 5 |

### 8.3 Scenario B – High Quality Only
| **Framework** | **WSM Score (B)** | **Rank (B)** |
|---|---:|:---:|
| ISO 27001 | 0.7093 | 1 |
| SOC 2 | 0.5767 | 2 |
| HITRUST | 0.5626 | 3 |
| NIST CSF | 0.5485 | 4 |
| COBIT 2019 | 0.5302 | 5 |

### 8.4 Scenario C – Quality Weighted
| **Framework** | **WSM Score (C)** | **Rank (C)** |
|---|---:|:---:|
| ISO 27001 | 0.7144 | 1 |
| NIST CSF | 0.5680 | 2 |
| SOC 2 | 0.5633 | 3 |
| HITRUST | 0.5626 | 4 |
| COBIT 2019 | 0.5335 | 5 |

---

## 9) How to interpret WSM scores

- **WSM Score** reflects framework performance weighted by your CTQ priorities.  
- A difference of **~0.02–0.04** can be **material** if driven by high‑priority CTQs (e.g., Acceptance/Regulatory).  
- Always cross‑check **evidence counts** and **quality** supporting each CTQ for the top‑ranked frameworks.  
- Treat **Cost/Time** signals as **indicative** when evidence is thinner (see Caveats).

---

## 10) Use‑case guidance (decision patterns)

- **Compliance & assurance‑led** (hospital procurement, cross‑border regulation):  
  Favor **ISO 27001** as anchor (top Acceptance/Regulatory). Consider **HITRUST** for US‑centric healthcare assurance.

- **Agility/scalability‑led** (rapid rollout, modular adoption):  
  Favor **NIST CSF** (strong Scalability; comparatively better Cost/Time signals). Plan a path to later certification if customers demand it.

- **Service‑assurance‑led (SaaS/cloud)**:  
  Elevate **SOC 2**; under High‑quality‑only, SOC 2 strengthens (Scenario B). Pair with ISO 27001 if customers request certification.

- **Enterprise governance overlay**:  
  Use **COBIT 2019** to align cybersecurity with IT governance, PMO, and audit programs; treat it as complementary rather than a primary certification path.

- **Hybrid adoption**:  
  Common outcome: **ISO 27001** anchor + **NIST CSF** operational overlay; optionally add **SOC 2** for services assurance reporting.

---

## 11) Validation & quality assurance (what FDST checks)

FDST includes internal checks (documented in `Test_Scripts`), such as:

- **Sheet presence & naming**  
- **Range coverage** vs formulas (`Frameworks_Scored` last row matches formulas)  
- **CTQ label consistency** across sheets  
- **Weights normalization** (sum to 1.0)  
- **WSM empty guard** (`IF(COUNTA...)=0`)  
- **Scenario blocks** compute correctly (exclude Low / High‑only / quality‑weighted)  
- **Evidence counts** and **CTQ averages** match the register

> Add your own tests for customizations (e.g., additional frameworks, alternative CTQs).

---

## 12) Caveats & limitations

- **Evidence gaps**: Cost/Time CTQs often rely on grey literature; treat quantitative claims cautiously.  
- **Representation imbalance**: ISO/NIST typically have more evidence rows than SOC 2/HITRUST—interpret mid‑tier ranks conservatively.  
- **Rubric compression**: The 4‑level scoring simplifies interpretation; subtle differences may be lost.  
- **Context dependence**: Rankings change meaningfully when weights shift—capture stakeholder priorities explicitly.  
- **No primary data collection**: Outputs are synthesis‑based, not a guarantee of certification success or risk performance.

---

## 13) Troubleshooting

- **Rank looks “off”**: Check CTQ weights; confirm normalization; verify CTQ averages are not blank (consider dynamic normalization).  
- **Scenario results don’t change**: Ensure `Study Quality` values are correctly set (High/Moderate/Low).  
- **Thin evidence**: Use **Scenario B** (High‑only) to avoid low‑quality influence; document the limitation in the decision memo.  
- **Conflicting sources**: Use **Scenario C** (quality‑weighted) to proportionally reflect quality tiers.

---

## 14) FAQ

- **Q: Can I add more CTQs?**  
  **A:** Yes; extend `CTQ_Scored`, normalization, and WSM formulas accordingly. Keep the sum = 1.0.

- **Q: Can I include more frameworks?**  
  **A:** Yes; append rows in `Frameworks_Scored` and extend WSM ranges.

- **Q: Does FDST recommend a single best framework universally?**  
  **A:** No; FDST explains **best‑fit given stated priorities** and **evidence**.

---

## 15) Change log (template)

- **v1.0** – Initial artefact; CTQs finalized; scenario blocks added.  
- **v1.1** – Dynamic normalization option; expanded data dictionary; detailed guidance.

---

## 16) Attribution & license

- Author: Craig Norris (MSc Cybersecurity).  
- FDST is provided for educational and decision‑support purposes under an open license; adapt and credit appropriately.  
- Ethical note: No personal/sensitive data used; all evidence sources are secondary and referenced in the dissertation.

---