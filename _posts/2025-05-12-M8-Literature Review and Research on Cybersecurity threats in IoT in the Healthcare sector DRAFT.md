---
layout: post
title: Module 8 Literature Review and Research on Cybersecurity Threats in IoT in the Healthcare Sector
subtitle: Overview of IoT technology use in Healthcare and the importance of cybersecurity and protecting patient data. 
categories: Module_8
tags: [Module 8]
---

## Project Title: Securing the Healthcare Internet of Things (IoT): A Critical Review of Prevalent Cyber Threats and Mitigation Strategies Based on Threat Intelligence and Vulnerability Data

#### Introduction (Approx. 250 words)

*Aim of the review and Target Audience*

The aim of the review is to identify and critically assess the leading cyber threats targeting Healthcare IoT (H-IoT) systems, and examine current mitigation strategies using threat intelligence and vulnerability data

The target audience for this research paper include academics, cybersecurity researchers, healthcare IT professionals, and policy-makers interested in healthcare cybersecurity. 

*Significance of the research problem*

The rapid integration of IoT devices in healthcare—such as insulin pumps and patient monitors—has significantly expanded the attack surface, making Healthcare IoT (H-IoT) systems attractive targets for cybercriminals. A comprehensive understanding of emerging threats and existing mitigation strategies is crucial to safeguarding patient safety and ensuring data confidentiality, integrity and availability.


#### Context, Perspective, and Theoretical Framework (Approx. 250 words)

*Context*

Healthcare organizations are increasingly dependent on Internet of Things (IoT) technologies to deliver critical services such as real-time patient monitoring, smart diagnostics, and automated treatment systems. While these innovations enhance operational efficiency and patient outcomes, they also introduce significant cybersecurity risks. Many Healthcare IoT (H-IoT) devices are deployed with minimal or no built-in security features, making them highly susceptible to cyber threats such as ransomware attacks, unauthorized data access, and device hijacking (ElSayed et al., 2025).

The lack of standardized security protocols and the diversity of device manufacturers further exacerbate these vulnerabilities. For instance, poor credential management, hard-coded passwords, and unencrypted communication channels are common weaknesses exploited by attackers (Mejía-Granda et al., 2023). These security gaps not only threaten the confidentiality and integrity of sensitive patient data but also pose direct risks to patient safety, especially when life-sustaining devices are compromised (ElSayed et al., 2025).

A growing body of research emphasizes the urgent need for robust, scalable, and adaptive security frameworks tailored to the unique constraints of H-IoT environments. Threat intelligence and vulnerability data must be systematically leveraged to inform proactive defence mechanisms and policy development.

This review takes a security risk management perspective when attempting to address the following research question: 

*Research Question*

What are the most prevelant cyber threats targeting healthcare Internet of Things (IoT) systems, and how can these threats be best mitigated using current threat intelligence and vulnerability data?


#### Methodology (Approx. 200 words)

*Conduct a comprehensive systematic literature review*

This project uses a qualitative, exploratory approach based on a systematic literature review (SLR) to identify cyber threats in healthcare IoT (H-IoT) and assess mitigation strategies using threat intelligence and vulnerability databases. It aligns with CyBOK's Cyber-Physical Systems Security and Cyber Threat Intelligence areas and meets BCS-aligned MSc academic and ethical standards.

*Search strategy*

A structured SLR protocol will be followed using guidelines adapted from Kitchenham’s framework for software engineering research:

- Databases to be searched include: IEEE Xplore, ACM Digital Library, ScienceDirect, PubMed Central, SpringerLink, Google Scholar
- Search terms will include a combination of : "Healthcare IoT" or "H-IoT" and "cyber threats" and "attack vectors" or "vulnerabilities" or "security risks" and "mitigation" or "cybersecurity countermeasures"
- Inclusion criteria is peer reviewed papers published betweeen 2018 and 2025, in english, focusing on healthcare IoT threats, vulnerabilities and defences 
- Exclusion criteria include studies not related to healthcare, papers focusing only on general IoT and not healthcare IoT, articles with insufficient technical detail on threats and countermeasures

*Threat Intelligence and Vulnerability Data Analysis*

To complement the literature review, structured data will be extracted from reputable threat intelligence sources, including MITRE ATT&CK for ICS/IoT, Nist National Vulnerability Database (NVD), Common Vulnerabilities and Exposures (CVE) records, and CISA Healthcare Cybersecurity Bulletins.

- Threat instances will be classified by: Type, Impact, Affected device and / or system, Mitigation
- Data will be organised into a Threat / Mitigation Table, which will form a key project artifact.

*Ethical Considerations*

Using insights from both the literature and intelligence data, the project will develop a A Risk Assessment Matrix that categorizes common threats by impact and likelihood which will form a key project artefact.

*Risk and Mitigation Framework Development*

An ethical self-assessment form covering ethical considerations and response to be submitted to the University Ethics Board for approval

#### Theoretical Framework

*Cybersecurity concepts*

- Definitions and key concepts related to cybersecurity
- Specific theories and models relevant to IoT security


*IoT in Healthcare*

- Overview of IoT applications / technologies used in Healthcare
- Benefits and challenges of IoT adoption in Healthcare


#### Review of Literature

*Types of Cybersecurity Threats*

	
- Malware: prevalence and impact in healthcare IoT
- Denial of Service (DoS) Attacks: prevalence and impact in healthcare IoT
- Man-in-the-Middle (MitM) Attacks: prevalence and impact in healthcare IoT
- Other Attacks: prevalence and impact in healthcare IoT

ElSayed, Z., Abdelgawad, A. and Elsayed, N., 2025. Cybersecurity and Frequent Cyber Attacks on IoT Devices in Healthcare: Issues and Solutions. arXiv preprint arXiv:2501.11250.

	-- Key Ideas: Survey major attack vectors (Malware / Ransomware, DDoS ...) affecting IoT in heatlhcare
	-- Strengths: Up to date with recent examples and covers both oerational and technical security areas. COvers real world medical devices 
    -- Limitations: Mitigation solutions are high level and do not cover detailed implementation guidance or metrics.
	-- Gaps: Lacks empirical testing or data-driven models. No threat intelligence data use for things like systemic classification of threats.
	
*Vulnerabilities in IoT Devices*

- Device Security Flaws: Studies covering common security flaws in IoT devices
- Network Security Issues: Studies covering common network security flaws relevant to IoT Healthcare devices
	
Dzamesi, L. and Elsayed, N., 2025. A Review on the Security Vulnerabilities of the IoMT against Malware Attacks and DDoS. arXiv preprint arXiv:2501.07703.	

	-- Key Ideas: Focused research on vulnerabilities (especially malware an ddistributed attacks) affecting IoT in heatlhcare. Explores device and network level.
	-- Strengths: Detailed breakdown of attack types specific to Healthcare IoT, highlighting interdependancies between systems and networks. 
    -- Limitations: Focused on types of attack rather then detection or mitifation strategies.
	-- Gaps: No discussion of threat intelligence usage and does not integrate into existing frameworks or tools (e.g. CVE, MITRE ...) for mitigation


*Impact on Healthcare*

- Patient Safety: Impact analysis from cyber threats
- Operational / Regulatory / Other: Studies covering impacts caused by cyberattacks on IoT devices
- Financial Implications: Financial impact analysis covering cybersecurity data breeches in Healthcare

Luna, R., Rhine, E., Myhra, M., Sullivan, R. and Kruse, C.S., 2016. Cyber threats to health information systems: A systematic review. Technology and Health Care, 24(1), pp.1-9.

	-- Key Ideas: Focused on electronic health records and data integrity, not device-level IoT. Provides a summary of prior studies that cover healthcare cybersecurity threats.
	-- Strengths: Strong systemic review methodology and highlights key / relevant risk vectors  
    -- Limitations: Old paper (2016) that does not address modern day IoT complexities and is not device specific.
	-- Gaps: No threat intelligence integation and limited applicability to IoT enviroments.
	


*Mitigation Strategies*

- Studies on impact of relevant cybersecurity technical countermeasures to address the threats and vulnerabilities
- Overview of regulations covering IoT in Healthcare and their impact
- Studies covering best practice for securing IoT devices in Healthcare
- Studies covering emerging technologies that may potentially enhance the security IoT devices in Healthcare

Khatun, M.A., Memon, S.F., Eising, C. and Dhirani, L.L., 2023. Machine learning for healthcare-iot security: A review and risk mitigation. IEEE Access, 11, pp.145869-145896.

	-- Key Ideas: This paper examines healthcare IoT fundamentals, privacy, and data security challenges with machine learning and H-IoT devices. 
		          It highlights the need to monitor healthcare IoT layers and discusses security and privacy challenges, along with risk mitigation strategies for healthcare IoT resilience.
	-- Strengths: Comprehensive view of healthcare IoT security challenges, emphasizing the role of machine learning for risk mitigation 
    -- Limitations: Lacking empirical validation of proposals
	-- Gaps: No coverage of integation with existing healthcare IT systems.

#### Ethical considerations and risk assessment

SUmmary: With no human subjects involved, the project poses minimal ethical risk. It uses data from public or academically licensed sources and adheres to responsible disclosure principles, avoiding detailed discussion of unpatched vulnerabilities.

- Concern: Published explicit, detailed exploit mechanisms might aid malicious actors.
- Response: Emphasise reponsible disclosure and avoid uneceserary technical details or breakdowns of active vulnerabilities unless already mitigated or published in advisories.
- Concern: Skewed representaiton due to undereported threats in developing countries can lead to solutions that are not applicable globally.
- Response: Acknowledge source bias, seek complementary database or litereture covering global context where possible

![Risk Assessment Matrix](/Modules/8/img/x.png)

- **Figure 1**: Risk Assessment Matrix (Norris, 2025)

#### Description of artifact(s) that will be created

*Literature Review Document (Primary Academic Output)*

- Content: A concise, critical review of peer-reviewed sources on key threats to Healthcare IoT (H-IoT), covering categories like ransomware, data breaches, and DoS attacks, along with mitigation strategies such as threat intelligence sharing, machine learning-based anomaly detection, and encryption practices.
	-- Mapped CyBOK Area: Cyber-Physical Systems Security, Security Operations & Incident Management, Risk Management & Governance.
	-- Value: Offers a scholarly basis and valuable insights for practitioners aiming to comprehend H-IoT threat patterns and the effectiveness of mitigation strategies.
	
*Threat Intelligence Mapping Dataset (Supplementary Artefact)*

- Content: A structured table or spreadsheet documenting known threats (CVE entries, known attacks), related IoT devices or systems, and associated mitigation strategies from sources like MITRE ATT&CK, NIST NVD, and peer-reviewed papers.
	-- Mapped CyBOK Area: Cyber Threat Intelligence.
	-- Value: Demonstrates application of academic and technical knowledge to collate actionable intelligence from real-world data.
	
*Risk Assessment Matrix (Supplementary Artefact)*

- Content: A risk matrix evaluating the impact and likelihoodof cyber threats on various H-IoT environments (e.g., remote patient monitoring, smart implants).
	-- Mapped CyBOK Area: Risk Management & Governance.
	-- Value: Applies theory to practical decision-making frameworks that healthcare organisations might adopt.
	
	
#### Timeline and proposed activities

![Timeline](/Modules/8/img/x.png)

- **Figure 1**: Timeline (Norris, 2025)

#### Conclusion

*Summary of Findings*

- Recap of key findings

*Implications of Practice*

- Discussion on practical implications of the findings 

*Recommendations for Future Research*

- Suggestions for areas that require further investigations


#### References

*List of all cited resources*

ElSayed, Z., Abdelgawad, A. and Elsayed, N. (2025). Cybersecurity and Frequent Cyber Attacks on IoT Devices in Healthcare: Issues and Solutions. arXiv preprint arXiv:2501.11250. Available at: https://arxiv.org/abs/2501.11250

Mejía-Granda, C.M., Fernández-Alemán, J.L., Carrillo-de-Gea, J.M. and García-Berná, J.A. (2023). Security vulnerabilities in healthcare: an analysis of medical devices and software. Medical & Biological Engineering & Computing, 62, pp.257–273. Available at: https://link.springer.com/article/10.1007/s11517-023-02912-0