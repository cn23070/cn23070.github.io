---
layout: post
title: Module 8 Assignment 1 DRAFT: Literature Review and Research on Cybersecurity Threats in IoT in the Healthcare Sector
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

#### Methodology (Approx. 200 words)

*Conduct a comprehensive systematic literature review*

This project uses a qualitative, exploratory approach based on a systematic literature review (SLR) to identify cyber threats in healthcare IoT (H-IoT) and assess mitigation strategies using threat intelligence and vulnerability databases. It aligns with CyBOK's Cyber-Physical Systems Security and Cyber Threat Intelligence areas and meets BCS-aligned MSc academic and ethical standards.

- Databases: IEEE Xplore, Scopus, PubMed, ACM Digital Library, ScienceDirect, PubMed Central, SpringerLink, Google Scholar.
- Inclusion criteria: Peer-reviewed publications (2018–2025), peer reviewed papers, in english, focusing on healthcare IoT threats, vulnerabilities and defences 
- Search strategy: “Healthcare IoT cyber threats,” “H-IoT vulnerabilities,” “medical IoT security,” “threat intelligence healthcare,” “CVE medical devices,” "Healthcare IoT" or "H-IoT" and "cyber threats" and "attack vectors" or "vulnerabilities" or "security risks" and "mitigation" or "cybersecurity countermeasures" etc.
- Exclusion criteria include studies not related to healthcare, papers focusing only on general IoT and not healthcare IoT, articles with insufficient technical detail on threats and countermeasures

*Data Extraction and Synthesis*

- Threat Intelligence and Vulnerability Data Analysis
- Structured data extracted from reputable threat intelligence sources, including MITRE ATT&CK for ICS/IoT, Nist National Vulnerability Database (NVD), Common Vulnerabilities and Exposures (CVE) records, and CISA Healthcare Cybersecurity Bulletins.
- Threat instances will be classified by: Type, Impact, Affected device and / or system, Mitigation
- Data will be organised into a Threat / Mitigation Table, which will form a key project artifact.



#### Review of Literature (Approx. 800 words)

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

#### Critical Evaluation (Approx. 400 words)


#### Conclusion and Future Directions (Approx. 150 words)

- Conclusions 
- Recommendations 


#### References

*List of all cited resources*

ElSayed, Z., Abdelgawad, A. and Elsayed, N. (2025). Cybersecurity and Frequent Cyber Attacks on IoT Devices in Healthcare: Issues and Solutions. arXiv preprint arXiv:2501.11250. Available at: https://arxiv.org/abs/2501.11250

Mejía-Granda, C.M., Fernández-Alemán, J.L., Carrillo-de-Gea, J.M. and García-Berná, J.A. (2023). Security vulnerabilities in healthcare: an analysis of medical devices and software. Medical & Biological Engineering & Computing, 62, pp.257–273. Available at: https://link.springer.com/article/10.1007/s11517-023-02912-0