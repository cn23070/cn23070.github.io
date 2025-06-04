# 📚 Literature Review: Evaluating the integration of AI/ML to mitigate Cyber Threats and Vulnerabilities in Healthcare IoT Systems

By: Craig Norris

# 📘 Introduction

##Focus and Aim of the Review

The swift growth of the Internet of Things (IoT) in healthcare has revolutionised clinical operations, diagnostic processes, and real time patient monitoring. However, this advancement also brings about significant cybersecurity concerns.

The guiding research question for this review is:

*What are the most significant cybersecurity threats facing Healthcare Internet of Things (H-IoT) systems, and how can the integration of Artificial Intelligence (AI) and Machine Learning (ML) be leveraged to effectively mitigate these threats?*

This review critically examines the evolving cybersecurity threat landscape within Healthcare Internet of Things (H-IoT) systems, with a particular emphasis on how the integration of Artificial Intelligence (AI) and Machine Learning (ML) can support the mitigation of emerging threats and vulnerabilities.

##Significance of the Review

This review holds significance as it systematically examines current academic literature to identify the most critical cybersecurity challenges confronting Healthcare Internet of Things (H-IoT) systems. It further explores the transformative potential of Artificial Intelligence (AI) and Machine Learning (ML) in enabling proactive threat detection, vulnerability identification, and adaptive mitigation strategies. By bridging the gap between emerging cybersecurity threats and intelligent technological solutions, this review provides a timely and comprehensive resource for researchers, developers, and healthcare stakeholders committed to securing the future of connected healthcare.

##Context, Perspective, and Theoretical Framework

###Context of the Topic

The integration of IoT in healthcare has improved diagnostics, patient monitoring, and real-time data analysis, enhancing patient outcomes. However, it has also widened the attack surface for cyber threats. Many Healthcare IoT (H-IoT) devices lack basic security features, making them vulnerable to ransomware, data breaches, and device hijacking (Badr et al., 2021; Kirubavathi et al., 2024). Weak credential practices, hard-coded passwords, and unencrypted communications are also common flaws exploited by attackers (Mejía-Granda et al., 2023). These vulnerabilities not only compromise patient data but also endanger patient safety when critical devices are targeted (O’Brien et al. ,2018).

A growing body of research emphasizes the urgent need for robust, scalable, and adaptive security frameworks tailored to the unique constraints of H-IoT environments. Threat intelligence and vulnerability data must be systematically leveraged to inform proactive defence mechanisms and policy development.

###Perspective and Framework

This review adopts a Systematic Literature Review (SLR) methodology to rigorously identify, evaluate, and analyse scholarly sources related to cybersecurity threats and AI/ML-based mitigation strategies in Healthcare Internet of Things (H-IoT) systems. The approach follows a transparent and structured process, incorporating defined inclusion and exclusion criteria, comprehensive database searches, and critical appraisal of selected studies. By focusing on peer-reviewed articles within a specified timeframe, the review ensures academic rigor and facilitates the identification of key themes, trends, and research gaps. This framework ultimately aims to inform future research directions and contribute towards the development of robust, adaptive security solutions tailored to the complex and sensitive nature of healthcare IoT systems.

# 🔍 Methodology for Literature Selection

The SLR methodology uses a qualitative, exploratory approach. The selection process considers the Preferred Reporting Items for Systematic Reviews and Meta Analyses (PRISMA) guidelines.

Relevant literature was sourced from authoritative academic databases including IEEE Xplore, PubMed, ACM Digital Library, SpringerLink, ScienceDirect, and Google Scholar.

Key search terms were derived from the research question, combining concepts such as "Healthcare Internet of Things" OR "H-IoT" OR "IoMT" (Internet of Medical Things) AND/OR "cybersecurity threats" OR "cyber threats" OR "security vulnerabilities" AND/OR "artificial intelligence" OR "AI" AND/OR "machine learning" OR "ML" AND/OR "cyberattack mitigation" OR "threat mitigation" OR "security framework".

Peer-reviewed publications in English from 2018 to 2025 were selected. Papers that were non peer reviewed or lacked applied context were excluded. The final analysis included 16 studies selected based on timeliness, relevance, and academic impact.

This review aligns closely with the CyBOK knowledge areas of Cyber-Physical Systems Security and Cyber Threat Intelligence by critically assessing the cybersecurity challenges facing Healthcare IoT (H-IoT) systems and evaluating the role of Artificial Intelligence (AI) and Machine Learning (ML) in mitigating these risks.

Conducted in accordance with BCS aligned MSc academic and ethical standards, the review upholds scholarly integrity, objectivity, and relevance. It integrates technical depth with ethical considerations, supporting evidence-based approaches to securing critical cyber physical systems in healthcare.

##Structure of the Review

This literature review is organised into four main sections:

- Section 1 identifies and critically analyses prevalent cyber threats and vulnerabilities affecting H-IoT.

- Section 2 identifies and critically analyses the impact on healthcare and patient safety.

- Section 3 analyses how AI/ML techniques are being applied for threat detection and mitigation.

- Section 4 evaluates best practices and research gaps in AI/ML-driven H-IoT security.

##Main Findings from the Literature

##Prevalent Threats and Vulnerabilities Identified

###Prevalent Threats

Several studies underscore the multifaceted nature of cyber threats facing H-IoT systems. Altulaihan et al. (2022) maps threats across architectural layers of H-IoT systems, reinforcing the need for layered defence strategies. Studies also highlight ransomware, phishing, and unauthorized access as dominant threats (Khatun et al., 2023; Kirubavathi et al., 2024). Also prominent was Distributed Denial of Service (DDoS) attacks, which can disrupt the availability of essential healthcare services (Khatun et al., 2023; Al-Hadhrami and Hussain, 2021; Rahman et al., 2024), and ransomware, which jeopardizes patient data confidentiality and system integrity (Sahu et al., 2020). Fereidouni et al. (2025) underscore vulnerabilities in communication protocols exploited via Man in the Middle (MitM) attacks. Additionally, the highly heterogeneous and resource-constrained nature of H-IoT devices exacerbates their susceptibility to exploitation through network-based attacks, such as man-in-the-middle and replay attacks (Altulaihan et al., 2022; Badr et al., 2021). Privacy breaches stemming from inadequate data protection mechanisms and insufficient regulatory compliance also emerge as critical challenges, given the sensitivity of healthcare data (Beaman et al., 2021).

###Known Vulnerabilities

During the COVID-19 pandemic, cyberattacks surged, exploiting vulnerabilities introduced by rapidly deployed digital health tools (Beaman et al., 2021). Legacy systems lacking basic encryption or authentication along with the valuable data they interact with also make healthcare networks highly attractive to cybercriminals (Beaman et al., 2021). Moreover, insider threats and insufficient user training contribute to the overall risk profile.

Research consistently highlights poor credential management, outdated firmware, and variety of devices and systems as major vulnerabilities (Khatun et al., 2023). Many devices do not consider security and privacy by design metrics, leading to inadequate password protocols and software patching, and end users continue to be the most vulnerable point in the security framework (Mejía-Granda et al., 2023).

The absence of interoperability standards further increases risk through frequent misconfigurations (Badr et al., 2021). These threats are exacerbated by the lack of universal standards in H-IoT development, creating heterogeneity in device capabilities and security configurations (Badr et al., 2021; Khatun et al., 2023).

Looking to the future, Quantum computing is anticipated to break conventional encryption, presenting a future risk (Mansoor et al., 2025).

###Impact on Healthcare

Data breaches erode patient trust and expose providers to financial and legal consequences (IBM, 2024). Attacks during COVID-19, such as ransomware in critical care units, overwhelmed already stretched healthcare systems (Beaman et al., 2021). The mishandling of sensitive patient data by healthcare providers or their associated supply chains can result in significant data breaches, leading to substantial reputational harm and financial loss. The Ponemon Institute (2023) reports that the average cost of a data breach has reached USD 4.45 million, the highest on record. However, the financial repercussions can be even more severe under regulatory frameworks such as the General Data Protection Regulation (GDPR). As highlighted by Wolford (2022), organizations found in serious violation of GDPR may face penalties of up to €20 million or 4% of their global annual turnover, whichever is greater. The risks extend beyond data breaches. Compromised devices like infusion pumps or ventilators pose direct patient safety risks (O’Brien et al., 2018).

###Mitigation Strategies and Threat Intelligence Integration

Artificial Intelligence (AI) and Machine Learning (ML) techniques are increasingly recognized as pivotal tools in advancing the cybersecurity posture of Healthcare Internet of Things (H-IoT) systems (Khatun et al., 2023; ElSayed et al., 2024), particularly for proactive threat detection and mitigation. Mohamed, 2025 proposes a multilayered artificial intelligence framework that employs machine learning classifiers to detect anomalous network behaviour in Healthcare IoT (H-IoT) systems, enhancing threat detection through adaptive, data-driven analysis across multiple security layers. Complementing this, ElSayed et al. (2024) propose a hybrid lightweight ML model that effectively predicts cyber-attacks through anomaly detection tailored to resource constrained IoT devices, addressing the unique computational limitations intrinsic to H-IoT architectures. Khatun et al. (2023) provide a comprehensive review of ML approaches, underscoring the role of supervised and unsupervised learning algorithms in recognising novel attacks, while emphasising the need for real-time processing and minimal false positives to preserve patient safety and data integrity. Furthermore, the paper from Jawahar et al., 2024 on integrated blockchain technology with deep learning to mitigate Distributed Denial of Service (DDoS) attacks showcases how AI can complement cryptographic techniques for robust defence mechanisms. Badr et al. (2021) and Veeramakali et al. (2021) also highlight the symbiotic relationship between AI and blockchain in securing H-IoT, proposing intelligent frameworks that utilize AI for continuous threat intelligence and adaptive response strategies.

However, these studies also acknowledge critical challenges. The scarcity of publicly available, high-quality datasets for model training (Khatun et al., 2023; Altulaihan et al., 2022), the risk of adversarial machine learning attacks that can subvert AI models, and the complexity of integrating AI seamlessly into heterogeneous H-IoT infrastructures without compromising latency or reliability are all highlighted as challenges (Altulaihan et al., 2022; ElSayed et al., 2024). Collectively, the literature evidence that while AI/ML methods hold significant promise in enhancing H-IoT cybersecurity, ongoing research must address scalability, model robustness, and ethical considerations to realize their full potential within patient safety critical healthcare environments.

##Critical Evaluation

###Strengths of the Literature

The literature offers a strong conceptual foundation for understanding cyber threats to H-IoT. Several studies (e.g., Altulaihan et al., 2022; Badr et al., 2021) systematically classify threat types and defences, while others explore innovations like zero trust architectures and ML based anomaly detection (ElSayed et al., 2024).

Moreover, the recognition of post pandemic cybersecurity trends adds practical urgency and real-world relevance to the research (Beaman et al., 2021). The exploration of quantum risks, while speculative, positions the literature to anticipate future challenges before they become critical (Mansoor et al., 2025).

# ✅ Conclusion and Research Gaps

## ✅ Conclusions

This review underscores the growing complexity of cybersecurity threats in Healthcare IoT (H-IoT), driven by the rapid expansion of connected medical devices and sensitive data (Mejía-Granda et al. (2023); Kirubavathi et al. (2024); Beaman et al. (2021)). AI and ML offer adaptive, real-time solutions that outperform traditional security methods, with current research highlighting hybrid models, blockchain integration, and anomaly detection (Rahman et al. (2024); ElSayed et al. (2024); Khatun et al. (2023)). Despite these advances, challenges such as data scarcity (Khatun et al. (2023); Altulaihan et al. (2022)), system heterogeneity (Fereidouni et al. (2025), latency (ElSayed et al. (2024), and adversarial risks (Beaman et al. (2021)) hinder real-world adoption. Closing the divide between technological innovation and practical implementation is crucial for protecting the healthcare infrastructures of the future.

##Identified Gaps and Future Research

The literature reveals several critical gaps that present opportunities for future research in securing Healthcare IoT (H-IoT) systems. One of the most pressing issues is the lack of large scale, labelled datasets representative of diverse healthcare environments, which are essential for training and validating effective AI/ML models (Khatun et al., 2023; Altulaihan et al., 2022). There is also a need to develop lightweight, real-time algorithms suited to the resource constraints of H-IoT devices (ElSayed et al., 2024). Adversarial machine learning remains underexplored, particularly in the context of healthcare specific threats (Beaman et al., 2021; Mansoor et al., 2025). Moreover, while AI blockchain integration shows promise, but empirical validation in real-world settings is limited (Jawahar et al., 2024; Veeramakali et al., 2021). Greater interdisciplinary focus is needed to address ethical and regulatory issues such as data privacy, governance, and algorithmic transparency. Finally, advancing adaptive architectures like AI driven Zero Trust models tailored for H-IoT represents a promising yet underdeveloped area (ElSayed et al., 2024).

# 🔖 References

Al-Hadhrami, Y. and Hussain, F.K. (2021) ‘DDoS attacks in IoT networks: A comprehensive systematic literature review’, World Wide Web, 24, pp. 971–1001. Available at: https://link.springer.com/article/10.1007/s11280-020-00855-2 (Accessed: 3 June 2025).

Altulaihan, E., Almaiah, M.A. and Aljughaiman, A. (2022) ‘Cybersecurity threats, countermeasures and mitigation techniques on the IoT: Future research directions’, Electronics, 11(20), p. 3330.

Badr, Y., Zhu, X. and Alraja, M.N. (2021) ‘Security and privacy in the Internet of Things: Threats and challenges’, Service Oriented Computing and Applications, 15, pp. 257–271. Available at: https://link.springer.com/article/10.1007/s11761-021-00327-z (Accessed: 3 June 2025).

Beaman, C., Barkworth, A., Akande, T.D., Hakak, S. and Khan, M.K. (2021) ‘Ransomware: Recent advances, analysis, challenges and future research directions’, Computers & Security, 111, p. 102490.

ElSayed, Z., Elsayed, N. and Bay, S. (2024) ‘A novel zero-trust machine learning green architecture for healthcare IoT cybersecurity: Review, analysis, and implementation’, SoutheastCon 2024, pp. 686–692.

Fereidouni, H., Fadeitcheva, O. and Zalai, M. (2025) ‘IoT and man-in-the-middle attacks’, Security and Privacy, 8(2), p. e70016.

Jawahar, A., Kaythry, P., Vinoth Kumar, C., Vinu, R., Amrish, R., Bavapriyan, K. and Gopinaath, V. (2024) ‘DDoS mitigation using blockchain and machine learning techniques’, Multimedia Tools and Applications, 83, pp. 60265–60278. Available at: https://link.springer.com/article/10.1007/s11042-023-18028-4 (Accessed: 4 June 2025).

Khatun, M.A., Memon, S.F., Eising, C. and Dhirani, L.L. (2023) ‘Machine learning for healthcare-IoT security: A review and risk mitigation’, IEEE Access, 11, pp. 145869–145896.

Kirubavathi, G., Regis Anne, W. and Sridevi, U.K. (2024) ‘A recent review of ransomware attacks on healthcare industries’, International Journal of System Assurance Engineering and Management, 15, pp. 5078–5096. Available at: https://link.springer.com/article/10.1007/s13198-024-02496-4 (Accessed: 3 June 2025).

Mansoor, K., Afzal, M., Iqbal, W. et al. (2025) ‘Securing the future: Exploring post-quantum cryptography for authentication and user privacy in IoT devices’, Cluster Computing, 28, p. 93. doi:10.1007/s10586-024-04799-4.

Mejía-Granda, C.M., Fernández-Alemán, J.L., Carrillo-de-Gea, J.M. and García-Berná, J.A. (2023) ‘Security vulnerabilities in healthcare: An analysis of medical devices and software’, Medical & Biological Engineering & Computing, 62, pp. 257–273. Available at: https://link.springer.com/article/10.1007/s11517-023-02912-0

Mohamed, N. (2025) ‘Artificial intelligence and machine learning in cybersecurity: A deep dive into state-of-the-art techniques and future paradigms’, Knowledge and Information Systems. Available at: https://link.springer.com/article/10.1007/s10115-025-02429-y (Accessed: 4 June 2025).

O’Brian, D. (2018) Securing wireless infusion pumps in healthcare delivery organizations: NIST SP 1800-8. National Institute of Standards and Technology. Available at: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1800-8.pdf (Accessed: 4 June 2025).

Ponemon Institute (2023) Cost of data breach report 2023. Sponsored by IBM. Available at: https://www.ibm.com/reports/data-breach (Accessed: 3 June 2025).

Rahman, M.A., Islam, M.T., Rahman, M.M., Hossain, M.S. and Alrajeh, N.A. (2024) ‘DoS and DDoS attack detection in IoT infrastructure using Xception model with explainability’. ResearchGate. Available at: https://www.researchgate.net/publication/391796103 (Accessed: 3 June 2025).

Veeramakali, T., Siva, R., Sivakumar, B., Arulmurugan, R., Chilamkurti, N. and Shanthini, A. (2021) ‘An intelligent internet of things-based secure healthcare framework using blockchain technology with an optimal deep learning model’, Journal of Supercomputing, 77, pp. 9576–9596. doi:10.1007/s11227-021-03637-3.

Wolford, B. (2020) What is GDPR, the EU’s new data protection law? Available at: https://gdpr.eu/what-is-gdpr/ (Accessed: 3 June 2025).

lata Sahu, M., Atulkar, M. and Ahirwal, M.K. (2020) ‘Comprehensive investigation on IoT based smart healthcare system’, in 2020 First International Conference on Power, Control and Computing Technologies (ICPC2T), pp. 325–330. IEEE.

