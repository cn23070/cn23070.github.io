---
layout: post
title: Module 3 Security and Risk Management April 2024
subtitle: How Security and Risk overlap and interact. 
categories: Module_3
tags: [Module 3]
---

*Module 3 will cover the various areas where security and risk overlap and interact with each other. It will review the various methods of risk assessment, looking at both qualitative and quantitative methods.*


## Module 3: Learning Scope & Objectives

*“All human endeavors involve uncertainty and risk.”(Olson, D.L. & Desheng D.W, 2020)*

- Discuss the difference between qualitative and quantitative risk assessments.
- Describe how to carry out both kinds of assessments.
	- Objective: Ability to describe when to use qualitative and quantitative risk assessments.
- Explain what is meant by and how to create threat models.
	- Objective: Ability to create threat models for various scenarios.
- Demonstrate how to create quantitative risk models.
	- Objective: Ability to create quantitative risk models.
- Discuss and design DR solutions.
	- Objective: Design and explain DR strategies and solutions.
	
### Unit 1&2: An Introduction to Security and Risk Management, & Users, Assessments and the Risk Management Process

#### Unit 1&2: Learning Objectives

- Understand the various definitions of risk.
- Ability to explain how to assess, qualify and mitigate risks.
- Describe various approaches to quantify and qualify risks.
- List common security and risk standards and select the appropriate one(s) for a given situation.
- Explain the importance of user participation in the risk management process.
- Discuss the implications of any recommended mitigations.

#### Unit 1&2: Reflections

Unit 1 provided a lecturecast that covered each learning objective in detail. Through the lecturecast I learnt a number of key terminology used in risk, and further developed my understanding on risk definitions by looking at the evolution of the definition over time and how context and situation influences the definition.The Lecturecast also introduced myself to the OpenFAIR and OCTAVE Framework's.
We also reviewed our first case study, a paper by Kovaitė and Stankevičienė (2019),that illustrates some of the risks introduced by industry 4.0 when applying digitalisation to more traditional business processes. The study also covered a methodology for carrying out the risk assessment of the digitalisation process as well as some common definitions of risk.
Industry 4.0. it refers to the fourth industrial revolution and embodies the use of new technologies like the Internet of things (IoT), big data, cloud computing, robotics, and artificial intelligence, to transform traditional and manufacturing processes.
It aims to enhance and optimize manufacturing and industrial operations by decentralising communication between humans and machines and enabling autonomous collaboration between machines, devices and systems. (Kovaitė and Stankevičienė, 2019).


#### Understand the various definitions of risk.

- **1**: Learning about Risk Definition

![Risk Definition During Lecturecast1](/Modules/3/img/1.png)

On completion of unit 1 I came away with a good understanding of what risk is, including the various definitions it known by.

A key takeaway is that risk is not easy to define, as the definition if often dependant on context and situation. One of the challenges of risk management is ensuring that all key stakeholders share a common understanding of risk.

Reim, Parida, and Sjödin (2016) define risk “as a combination of the probability of loss and the impact of the loss for a number of events and risks”. 

My simplified version of this is that risk is the probability that something may occur, and is based on the impact an likelihood of the occurrence.

![Risk Definition During Lecturecast1](/Modules/3/img/2.png)

#### Ability to explain how to assess, qualify and mitigate risks

![Risk Definition During Lecturecast1](/Modules/3/img/4.png)

In order for a company to assess, qualify and mitigate risks appropriately, a risk management system program should be implemented made up of:
- appropriatte governance, buy-in and contribution from senior management and involve the senior leaders of all major departments within the company
- all known appropriate standards and certifications that the company is required to be compliant with from both a legal and regulatory perspective
- continous improvmenet following the PDCA model
- be integrated with the companys information security management system


#### Describe various approaches to quantify and qualify risks.

- **1**: Learning about qualitative vs. quantative

![Qualitative vs. Quantative During Lecturecast1](/Modules/3/img/3.png)

**Qualatitive:**
- Used for lower value assets, or numerical data is missing, or when risk stakeholders do not have quatative assessment skillsets
- Threats and vulnerabilities are ususally assigned a value of high, medium or low

**Quantative:**
- Well defined mathematical calculation that often uses proability and game theory

Hubbard(2009) argues that quantative assessments are more useful then qualitative assessments and should be preferred. 

However Busch(n.d.) points out not all risks can be evaluated numerically. This is becuase risk is subjective, and precluding qualitative assessment may exclude useful input from less numerically oriented staff. 

#### List common security and risk standards and select the appropriate one(s) for a given situation.

The Lecturecast also introduced myself to a number of standards including the OpenFAIR and OCTAVE Framework's.

**OpenFAIR**
Open FAIR is a standard produced by the Open Group  
FAIR is an acronym for "Factor Analysis of Information Risk" (Josey et al, 2014). 
It consists of two documents, the open risk taxonomy (O-RT) which defines the taxonomy for the factors driving information risk; and the open risk analysis (O-RA) which describes the process and procedures associated with performing risk analysis.

**OCTAVE**
OCTAVE stands for Operationally Critical Threat, Asset and Vulnerability Evaluation (OCTAVE) framework standard 
The standard was created at Carnegie Mellon University (CMU) in 1999 (Alberts et al, 1999)
Made up of three phases: 1 Build enterprise wide security requirements, 2 Identify infrastructure vulnerabilties, and 3 determine the security risk management strategy

#### Unit 3,4 & 5: Reflections

Unit 3 provided an introduction to threat modelling. the lecturecast we learnt the difference between threats and vulnerabilities and reviewed a number of common threat modelling techniques.

![Key Terminology](/Modules/3/img/5.png)

#### Common Threat Models and Features (Shevchenko et al, 2018)

To further support my uderstanding of the different threat models and their features, I also reviewed a paper by Shevchenko et al (2018) that summarised the most common threat management and modelling methods currently in use which is summarised in the table below.

| Threat Modelling Method                        | Features|
| :--------                                      | :-------|
| STRIDE										 | Helps identify relevant mitigating techniques, Is the most mature, Is easy to use but is time consuming|      
| PASTA 									     | Helps identify relevant mitigating techniques, Directly contributes to risk management, Encourages collaboration among stakeholders, Contains built-in prioritization of threat mitigation, Is laborious but has rich documentation|
| LINDDUN   									 | Helps identify relevant mitigation techniques, Contains built-in prioritization of threat mitigation, Can be labor intensive and time consuming |
| CVSS 											 | Contains built-in prioritization of threat mitigation, Has consistent results when repeated, Automated components, Has score calculations that are not transparent |      
| Attack Trees									 | Helps identify relevant mitigation techniques, Has consistent results when repeated, Is easy to use if you already have a thorough understanding of the system |
| Persona non Grata 							 | Helps identify relevant mitigation techniques, Directly contributes to risk management, Has consistent results when repeated, Tends to detect only some subsets of threats |
| Security Cards 								 | Encourages collaboration among stakeholders, Targets out-of-the-ordinary threats, Leads to many false positives |
| hTMM	                                         | Contains built-in prioritization of threat mitigation, Encourages collaboration among stakeholders, Has consistent results when repeated |
| Quantitative TMM							     | Contains built-in prioritization of threat mitigation, Has automated components, Has consistent results when repeated |
| Trike											 | Helps identify relevant mitigation techniques, Directly contributes to risk management , Contains built-in prioritization of threat mitigation, Encourages collaboration among stakeholders, Has automated components, Has vague, insufficient documentation |
| VAST Modeling 								 | Helps identify relevant mitigation techniques, Directly contributes to risk management, Contains built-in prioritization of threat mitigation, Encourages collaboration among stakeholders, Has consistent results when repeated, Has automated components, Is explicitly designed to be scalable, Has little publicly available documentation|
| OCTAVE 	                                     | Helps identify relevant mitigation techniques, Directly contributes to risk management, Contains built-in prioritization of threat mitigation, Encourages collaboration among stakeholders, Has consistent results when repeated, Is explicitly designed to be scalable, Is time consuming and has vague documentation |

####  Intial Threat Modeling with STRIDE, DREAD, and Attack Trees

Unit 4 allowed us to gain experiance of the some of the more common threat modelling techniques (STRIDE and DREAD, Attack Trees), by researching them in more detail, attempting to apply them to a scenario, and then discussing them during the uniit 4 group seminar. 

I decided to perform a rapid threat assessment with the aid of ChatGPT. I generated a couple threat models using STRIDE, DREAD, and attack trees for the following **scenario: *a large medical device manufacturer based in the United States of America.*** 

Example results are shown below and were discussed with my lecturer and peers. 

Each node shown represents a threat actors goal or method to achieve that goal. This helps to identify where security measures should be implemented to mitigate risks, and aids in understanding and prioritizing risks.

![Example Attack Tree Exercise Results](/Modules/3/img/7.png)

**STRIDE Threat Model Exercise Results**

**1. Spoofing Identity**
- **Threat:** An attacker impersonates an authorized user or system.
- **Example:** Attacker uses stolen credentials to access the network.
- **Mitigation:** Implement multi-factor authentication (MFA) and strong access controls.
 
**2. Tampering with Data**
- **Threat:** An attacker tampers with data, compromising its integrity.
- **Example:** An insider modifies patient records or medical device calibration data.
- **Mitigation:** Use encryption, digital signatures, audit log reviews, and regular integrity checks.
 
**3. Repudiation**
- **Threat:** Actions or transactions can be denied by users.
- **Example:** An employee denies making changes to sensitive patient data after changing it.
- **Mitigation:** Implement audit logging including log reviews.
 
**4. Information Disclosure**
- **Threat:** Unauthorized disclosure of sensitive information.
- **Example:** An attacker exploits a known vulnerability to access confidential patient data.
- **Mitigation:** Use encryption, access controls, and regular security assessments.
 
**5. Denial of Service (DoS)**
- **Threat:** An attacker disrupts services to make them unavailable.
- **Example:** A DDoS attack on the company's servers disrupts manufacturing operations.
- **Mitigation:** Deploy DoS protection mechanisms like firewalls and redundancy.
 
**6. Elevation of Privilege**
- **Threat:** An attacker gains unauthorized elevated privileges.
- **Example:** An attacker exploits a vulnerability to gain administrative access to the system.
- **Mitigation:** Implement least privilege access controls and regular patching.

Taking the experiance gained, I began building out proposed content for the intial group assignment for review by my team members.

![Risk Proccess based on ISO 31000](/Modules/3/img/6.png)

![Risk Proccess Step 1: Establish Context](/Modules/3/img/8.png)




## Module 3: Artefacts


| Parameter                                      | Type                        | Description                                                                                                       | References                 |
| :--------                                      | :-------                    | :--------------------------                                                                                       | :------------------------- |
| `Collaborative Discussion Forum 1 - Units 1-3` | `Student Forum Posts`       | Discuss why Cyber Security is now a global issue and why it is important for companies to invest in Cyber Security|[All Forum Posts](https://www.my-course.co.uk/mod/forum/view.php?id=907384) , [My Initial Post](https://www.my-course.co.uk/mod/forum/discuss.php?d=196152), [My Summary Post](https://www.my-course.co.uk/mod/forum/discuss.php?d=199496)|
| `Collaborative Discussion Forum 2 - Units 4-6` | `Student Forum Posts`       | Identify and discuss two security technologies and the context in which they can be employed. | [All Forum Posts](https://www.my-course.co.uk/mod/forum/view.php?id=907417) , [My Initial Post](https://www.my-course.co.uk/mod/forum/discuss.php?d=203142), [My Summary Post](https://www.my-course.co.uk/mod/forum/discuss.php?d=205078)|
| `Individual Essay - Unit 9`                    | `Essay`                    | Apply the Cyber Security methods and techniques studied during the module to develop a solution to a business problemInclude two UML diagrams showing aspects of the system and at least two threat modelling techniques used to identify potential cyber threats and how these are to be mitigated. | [View Essay](https://essexuniversity-my.sharepoint.com/:w:/g/personal/cn23070_essex_ac_uk/EeQPvWOq43lAkEEXqabnWHMBmYsS2LwWj4ARxk9hUIiKFg) 
| `End of Module Assignment - Unit 12`           | `Python Code` | Using Python code, implement at least one solution recommended as part of the proposal submitted in the individual essay.         | [(1) View Solution **Read Me** File](https://cn23070.github.io/module_1/2024/02/12/Module-1EOMA-Python-ReadMe.html) , [(2) Run **Code**](https://colab.research.google.com/github/cn23070/cn23070.github.io/blob/main/CraigNorris_LCS_EoMA.ipynb)



## Module 3: Reflections

*Information about what I learnt during this module and how*

Unit 1
Definition of a risk


## Module 3: Meeting Notes

*Notes from various meetings, as well as feedback from team members and tutors.*

#### Professional Skills Matrix and Action Plan

*What skills have I gained or enhanced as a result of this module and how can I use it? What else do I need to learn?*

## Module 3: Citations

*Information about what I learnt during this module and how*

Olson, D.L. & Desheng D.W (2020) Enterprise risk management models. Berlin, Germany: Springer.

(Kovaitė & Stankevičienė, 2019) - Kovaite, Kristina & Stankevičienė, Jelena. (2019). Risks of digitalisation of business models. 10.3846/cibmee.2019.039.

Bitten Thorgaard Sørensen, Digitalisation: An Opportunity or a Risk?, Journal of European Competition Law & Practice, Volume 9, Issue 6, June 2018, Pages 349–350, https://doi.org/10.1093/jeclap/lpy038

Reim, W., Parida, V., & Sjödin, D. R. (2016). Risk management for product-service system operation. International Journal of Operations & Production Management, 36(6), 665-686. https://doi.org/10.1108/IJOPM-10-2014-0498

*Tupa, J., Simota, J., & Steiner, F. (2017). Aspects of risk management implementation for Industry 4.0. Procedia Manufacturing,11, 1223-1230. https://doi.org/10.1016/j.promfg.2017.07.248* 

*Soltovski, R. et al. (2022) Theoretical framework of the Industry 4.0 risks from sustainability perspective. Revista Competitividade e Sustentabilidade. [Online]*

Shevchenko, N., Chick, T. A., O'Riordan, P., Scanlon, T. P., & Woody, C. (2018). Threat modeling: a summary of available methods. Carnegie Mellon University Software Engineering Institute Pittsburgh United States. Available from: https://apps.dtic.mil/sti/pdfs/AD1084024.pdf


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://cn23070.github.io/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/craig-norris-3b787610/)


