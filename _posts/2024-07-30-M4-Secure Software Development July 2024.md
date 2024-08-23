---
layout: post
title: Secure Software Development July 2024
subtitle: Learn about security risks which are associated with programming languages, from the perspectives of design and architecture approaches 
categories: Module_4
tags: [Module 4]
---
	

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://cn23070.github.io/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/craig-norris-3b787610/)


![Module Introduction](/Modules/4/img/3.png)

- **Figure 1**: Module Introduction (University of Essex Online, 2024)


### Units 1

We begun the module with background core reading. Unit 1 reading covered two key topics:
- Principles of Software Architecture
- Writing Secure Code

![Module Core Reading](/Modules/4/img/1.png)

- **Figure 2**: Module Core Reading (Pillai, 2017)

#### Principles of Software Architecture
- Defining software architecture: According to Pillai (2017), software architecture is a description of the subsystems or components of a software
system, and the relationships between them.

**Software architecture versus design**

Although used interchangeably, Pillai (2017) argues that there are distinctions:
 
- Software Architecture (higher abstraction / larger scope) is about the design of the entire system.
	- It covers the higher level structures and interactions of the system and is closer to questions about the systems functional, technical, organizational, business and quality attributes, 

- Wheras Software Design covers the organization of parts of the sub system and system invovled in making the system
	 - Mostly about the details of the subsystems
	 - It is closer to questions around the code itself

• Aspects of software architecture include a System(collection of components orangazed in such a way as to achieve a specific function), Structure (set of software or hardware elements grouped together accordign to a guiding principle), Enviroment (context(technical, business, operational ...) or circumstances in which a system is built), and Stakeholders (person(s0 who is interested in or concered about the success of the system.))

**Characteristics of software architecture**

An Architecture of a system: 

- is represented as structual details. of the sytem, often depicted using a class diagram
- picks a core set of elements and does not setout to document everything about every component of the system
- captures early design decisions based on requirements and constraints of its context. These decisionsplay a major role in further development
- manages stakeholders requirements
- influences the organizational structure
- is influenced by its enviroment. The envioment often imposes limits that the architecture must function within.
- documents the system (stakeholders, requirements, decisions) and often conforms to a pattern (architecture patterns include client server, pipes and filters ect..)

**Why is software architecture important?**
- A number of reasons including technical aspects such as helping manage changes, ensuring component based design, and facilitates early prototyping. I also an architecture balances and optimizes stakeholder requirements and formalises it, helping ensure good documentation best pratice as well as producing a system that is etensible and moifiable.


**System versus Enterprise Architecture**

"Enterprise Architecture is a conceptual blueprint that defines the structure and behavior of an organization. It determines how the organization's structure,
processes, personnel and flow of information is aligned to its core goals to efficiently achieve its current and future objectives."

"A system architecture is the fundamental organization of a system, represented by its structural and behavioral views. The structure is determined by the components of the system and the behavior by the relationships between them and their interaction with external systems."

![Scope and focus of various architect roles](/Modules/4/img/2.png)

- **Figure 3**: Scope and focus of various architect roles (Pillai, 2017)

**Architectural quality attributes**

"A quality attribute is a measurable and testable property of a system which can be used to evaluate the performance of a system within its prescribed environment with respect to its non-functional aspects".(Pillai, 2017)

°° Modifiability: the ease with which changes can be made to a system, and the flexibility with which the system adjusts to the changes
°° Testability: how much a software system is amenable to demonstrating its faults through testing
°° Scalability/performance: capacity to accommodate increasing workload on demand while keeping its performance within acceptable limits
°° Availability: the property of readiness of a software system to carry out its operations when the need arises.
°° Security: in the software domain, can be defined as the degree of ability of a system to avoid damage to its data and logic from unauthenticated access, while continuing to provide services to other systems and roles that are properly authenticated.
°° Deployability: the degree of ease with which software can be taken from the development to the production environment. 


We also reviewed our first case study, a paper by Kovaitė and Stankevičienė (2019),that illustrates some of the risks introduced by industry 4.0 when applying digitalisation to more traditional business processes. The study also covered a methodology for carrying out the risk assessment of the digitalisation process as well as some common definitions of risk.

#### Writing Secure Code

**Information security architecture**
A secure architecture involves creating a system that is able to provide access to data and information to authorized people and systems while preventing any unauthorized access.(Pillai, 2017)

You protect the CIA of the system and its data through security mechanisms such as authetication, authorization and non-reputability

**Secure coding**

Secure coding is the practice of software development that guards programs against security vulnerabilities, and makes it resistant to malicious attacks right from program design to implementation.(Pillai, 2017). It is important to identify assets of value (code/data), then decompose the application into components followed by identifying and categorizing threats to each asset or component and ranking the threats following a risk model. You should then develop strategies to mitigate the identifed threats

**Common security vulnerabilities**

*Overflow errors* such as *buffer overflow*(attackers take control of systems by gaining access to teh systems application stack or heap memory due to code error allowing an application to write past the end of a buffer), and *Integer or arithmetic overflow* (an operation on an integerproduces a result that is too large to be used or stored)

*Lack of validated input* (comon security issue on web application where unvalidated input is injected by an attacker, tricking the system into accepting malicious code or system commands leading to system compromise)
Common examples include Cross-Site-Scripting(XSS), SQL Injections and Shel Execution Exploits.

*Poor Access control* (lack of seperation of super user rights between user groups may be leveraged by an attacker through things like exposed routes (URLs) or workflows)

**Is Python secure?**
°° Reading input
°° Evaluating arbitrary input
°° Overflow errors
°° Serializing objects
°° Security issues with web applications

Unit 1 also provided a lecturecast that provided an introduction to Secure Software Development. 

![Lecturecast 1: Introduction to Secure Software Development](/Modules/4/img/4.png)

- **Figure 4**: Lecturecast 1: Introduction to Secure Software Development (University of Essex Online, 2024)

The lecturecast begun with areminder of the improtance of cyber crime as a problem today.


![Lecturecast 1: Cost of Cybercrime by Vector](/Modules/4/img/5.png)

- **Figure 5**: Lecturecast 1: Cost of Cybercrime by Vector (University of Essex Online, 2024)

I then learnt more about OWASP and the benefits of following OWASP best practices during application design.

![Lecturecast 1: OWASP Top 10 Proactive Controls](/Modules/4/img/6.png)

- **Figure 6**: Lecturecast 1: OWASP Top 10 Proactive Controls (University of Essex Online, 2024)

The lecturecast also helped me to gain an understanding of the differences between the predictive (Waterfall) and adaptive (Agile) approaches to software development


![Lecturecast 1: Software Development Lifecycles](/Modules/4/img/8.png)

- **Figure 7**: Lecturecast 1: Software Development Lifecycles (University of Essex Online, 2024)

This included an appreciation of the challenges of integrating security practices into both the adaptive and predictive approaches to software development

![Lecturecast 1: Challenges with Waterfall](/Modules/4/img/9.png)

- **Figure 8**: Lecturecast 1: Challenges with Waterfall (University of Essex Online, 2024)


![Lecturecast 1: Challenges with Agile](/Modules/4/img/10.png)

- **Figure 9**: Lecturecast 1: Challenges with Agile (University of Essex Online, 2024)


![Lecturecast 1: Design Patterns](/Modules/4/img/12.png)

- **Figure 10**: Lecturecast 1: BDesign Patterns (University of Essex Online, 2024)

![Lecturecast 1: Benefits of design patterns](/Modules/4/img/11.png)

- **Figure 11**: Lecturecast 1: Benefits of design patterns (University of Essex Online, 2024)

Finally, I also learnt about Unified Modelling Language (UML), inlcuding how UML is alligned to SDLC.

![Lecturecast 1: Relating UML Models to SDLC](/Modules/4/img/7.png)

- **Figure 12**: Lecturecast 1: Relating UML Models to SDLC (University of Essex Online, 2024)



### Unit 2

During unit 2 I gained some experiance creating Uniﬁed Modelling Language (UML) flowcharts in order to assist in the design of software. UML, a consolidation of the best practices refined over time, provides a way to present the diverse elements of a software system (e.g., requirements, data structures, data ﬂows, and information ﬂows) within a single framework (Seidl et al., 2015). 

![Module 2 Activity: Collaborative Discussion: UML flowchart](/Modules/4/img/13.png)
- **Figure x**: Collaborative Discussion: UML flowchart (University of Essex Online, 2024)

We got to select a UML model to try. Once done we then uploaded them for peer review and had a collaborative discussion around them.

During the live seminar we learnt mroe on how to align secure coding best practice to the agile development methodology, and familiarised ourselves with ISO 27000 by posting a blog using the ISO terminology.

![Module 2 Activity: Unit 2 Seminar Blog Post](/Modules/4/img/14.png)
- **Figure x**: Unit 2 Seminar Blog Post (University of Essex Online, 2024)

### Unit 3: Introduction to Programming Languages

During unit 3 we spent time investigating programming languages including the history, concepts and design that led to the languages we have today. 

We completed a lecturecast on Programming Languages and Testing. The lecturecast helped me to better describe some key milestones in the development of programming languages, be able to outline some of the key paradigms that define the different types of languages, and describe the different testing strategies and when to apply them.

![Lecturecast 2: Programming Languages and Testing](/Modules/4/img/14.png)

- **Figure 4**: Lecturecast 2: Programming Languages and Testing (University of Essex Online, 2024)



**Strategies for Security – Python**

**Secure coding strategies**





### References
Core Text: Pillai, A.B. (2017) Software Architecture with Python. Birmingham, UK. Packt Publishing Ltd.


*Royce, W. W. (1970) Managing the Development of Large Software Systems.

*OMG (2017) Unified Modelling Language, Version 2.5.1.

*Pohl, C. & Hof, H-J. (2015) Secure Scrum: Development of Secure Software with Scrum, in Proc. of the 9th International Conference on Emerging Security Information, Systems and Technologies.

*ISO/IEC (2018) ISO/IEC Standard 27000 Section 3.








	
## Module 4: Summary Reflection

xxx





## Module 4: Learning Scope & Objectives

*“All human endeavours involve uncertainty and risk.”(Olson, D.L. & Desheng D.W, 2020)*

- Acquire a critical understanding of the concept of abstraction in programming.
- Develop an understanding of the basic principles of secure development methodologies.
- Explore how to undertake analysis, program design, software construction and testing required for software development.
- Demonstrate an understanding of the basic principles of architecture, as well as traditional and contemporary Software Development Life Cycle (SDLC) models, such as TOGAF and Agile.
- The ability to put into practice the techniques learned in a team environment, demonstrating how to deal with conflicts and how to make compromises, and be able to critically evaluate the effectiveness of the approaches.
- Utilise the opportunity to reflect on and evaluate your own personal development.
- Identify and manage security risks as part of a software development project.
- Critically analyse development problems and determine appropriate methodologies, tools and techniques (including program design and development) to solve them.
- Design and develop/adapt computer programs and to produce a solution that meets the design brief and critically evaluate solutions that are produced.
- Systematically develop and implement the skills required to be effective member of a development team in a virtual professional environment, adopting real-life perspectives on team roles and organisation.

## Module 4: Artefacts


| Parameter                                      | Type                        | Description                                                                                                       | References                 |
| :--------                                      | :-------                    | :--------------------------                                                                                       | :------------------------- |
| `Development Team Project: Design Document` | `Report`| Produce an application design for a secure enclave to store lyrics, music scores and musical recordings on behalf of copyright owners and performers.| [View Essay](https://essexuniversity-my.sharepoint.com/:w:/g/personal/cn23070_essex_ac_uk/xxx) |
| `Development Individual Project: Coding Output` | `Code` | Using Python, implement the application designed earlier (see design document artifact). | [View ip](https://essexuniversity-my.sharepoint.com/:w:/g/personal/cn23070_essex_ac_uk/xxx)| 
| `Development Individual Project: README`    | `Read Me` | Using Python, implement the application designed earlier (see design document artifact). | [View README File](https://essexuniversity-my.sharepoint.com/:w:/g/personal/cn23070_essex_ac_uk/xxx)|
| `Individual Reflective Submission`    | `Essay` | Produce a summary report covering the learnings from module 4. | [View Essay](https://cn23070.github.io/module_3/2024/07/12/M3-Security-and-Risk-Management-April-2024.html)|
| `Individual Reflective Submission`    | `Website` | Produce a e-Portfolio covering the learnings from module 4. | [View Website](https://essexuniversity-my.sharepoint.com/:w:/g/personal/cn23070_essex_ac_uk/xxx)|
| `Backup: e-Portfolio Submission Post Raw MD File`    | `MD file` | Backup of the E-Portfolio Post for this module | [View File](https://essexuniversity-my.sharepoint.com/:t:/g/personal/cn23070_essex_ac_uk/xxx)|



## Module 3 Notes 
	
### Unit 1&2: An Introduction to Security and Risk Management, & Users, Assessments and the Risk Management Process


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
- appropriate governance, buy-in and contribution from senior management and involve the senior leaders of all major departments within the company
- all known appropriate standards and certifications that the company is required to be compliant with from both a legal and regulatory perspective
- contiguous improvement following the PDCA model
- be integrated with the companys information security management system


#### Describe various approaches to quantify and qualify risks.

- **1**: Learning about qualitative vs. quantitative

![Qualitative vs. Quantitative During Lecturecast1](/Modules/3/img/3.png)

**Qualitative:**
- Used for lower value assets, or numerical data is missing, or when risk stakeholders do not have qualitative assessment skillsets
- Threats and vulnerabilities are usually assigned a value of high, medium or low

**Quantitative:**
- Well defined mathematical calculation that often uses probability and game theory

Hubbard(2009) argues that quantitative assessments are more useful then qualitative assessments and should be preferred. 

However Busch(n.d.) points out not all risks can be evaluated numerically. This is because risk is subjective, and precluding qualitative assessment may exclude useful input from less numerically oriented staff. 

#### List common security and risk standards and select the appropriate one(s) for a given situation.

The Lecturecast also introduced myself to a number of standards including the OpenFAIR and OCTAVE Framework's.

**OpenFAIR**
Open FAIR is a standard produced by the Open Group  
FAIR is an acronym for "Factor Analysis of Information Risk" (Josey et al, 2014). 
It consists of two documents, the open risk taxonomy (O-RT) which defines the taxonomy for the factors driving information risk; and the open risk analysis (O-RA) which describes the process and procedures associated with performing risk analysis.

**OCTAVE**
OCTAVE stands for Operationally Critical Threat, Asset and Vulnerability Evaluation (OCTAVE) framework standard 
The standard was created at Carnegie Mellon University (CMU) in 1999 (Alberts et al, 1999)
Made up of three phases: 1 Build enterprise wide security requirements, 2 Identify infrastructure vulnerabilities, and 3 determine the security risk management strategy

#### Unit 3,4 & 5: Threat Modelling and Management, and Security and Risk Standards in Industry and the Enterprise

Unit 3 provided an introduction to threat modelling. the lecturecast we learnt the difference between threats and vulnerabilities and reviewed a number of common threat modelling techniques.

![Key Terminology](/Modules/3/img/5.png)

#### Common Threat Models and Features (Shevchenko et al, 2018)

To further support my understanding of the different threat models and their features, I also reviewed a paper by Shevchenko et al (2018) that summarised the most common threat management and modelling methods currently in use which is summarised in the table below.

| Threat Modelling Method                        | Features|
| :--------                                      | :-------|
| STRIDE										 | Helps identify relevant mitigating techniques, Is the most mature, Is easy to use but is time consuming|      
| PASTA 									     | Helps identify relevant mitigating techniques, Directly contributes to risk management, Encourages collaboration among stakeholders, Contains built-in prioritisations of threat mitigation, Is laborious but has rich documentation|
| LINDDUN   									 | Helps identify relevant mitigation techniques, Contains built-in prioritisations of threat mitigation, Can be labor intensive and time consuming |
| CVSS 											 | Contains built-in prioritisations of threat mitigation, Has consistent results when repeated, Automated components, Has score calculations that are not transparent |      
| Attack Trees									 | Helps identify relevant mitigation techniques, Has consistent results when repeated, Is easy to use if you already have a thorough understanding of the system |
| Persona non Grata 							 | Helps identify relevant mitigation techniques, Directly contributes to risk management, Has consistent results when repeated, Tends to detect only some subsets of threats |
| Security Cards 								 | Encourages collaboration among stakeholders, Targets out-of-the-ordinary threats, Leads to many false positives |
| hTMM	                                         | Contains built-in prioritisations of threat mitigation, Encourages collaboration among stakeholders, Has consistent results when repeated |
| Quantitative TMM							     | Contains built-in prioritisations of threat mitigation, Has automated components, Has consistent results when repeated |
| Trike											 | Helps identify relevant mitigation techniques, Directly contributes to risk management , Contains built-in prioritisation of threat mitigation, Encourages collaboration among stakeholders, Has automated components, Has vague, insufficient documentation |
| VAST Modeling 								 | Helps identify relevant mitigation techniques, Directly contributes to risk management, Contains built-in prioritisations of threat mitigation, Encourages collaboration among stakeholders, Has consistent results when repeated, Has automated components, Is explicitly designed to be scalable, Has little publicly available documentation|
| OCTAVE 	                                     | Helps identify relevant mitigation techniques, Directly contributes to risk management, Contains built-in prioritisation of threat mitigation, Encourages collaboration among stakeholders, Has consistent results when repeated, Is explicitly designed to be scalable, Is time consuming and has vague documentation |

####  Initial Threat Modeling with STRIDE, DREAD, and Attack Trees

Unit 4 allowed us to gain experience of the some of the more common threat modelling techniques (STRIDE and DREAD, Attack Trees), by researching them in more detail, attempting to apply them to a scenario, and then discussing them during the uniit 4 group seminar. 

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

#### Units 4,5 & 6: Gaining Experience with Assignment 1

Unit 3 provided an introduction to threat modelling. the lecturecast we learnt the difference between threats and vulnerabilities and reviewed a number of common threat modelling techniques.

Units 4, 5 and 6 equipped with a clear understanding of risk management and the best practice methodologies and frameworks that help you perform it successfully, the module content and activities turned to gaining experience on risk management techniques by applying what we had learnt to date along with delving deeper into some of the topics themselves. 

During Unit 5 we studied several case studies from 2014 – 2018 concerning GDPR related issues and breaches by references content on the Data Protection Commission (2020) Case Studies: Data Protection Commission website. 

I came away with some exerpiance around the different aspects of GDPR that can have issues and how to resolve them.

We concluded unit 6 by submitting  a group assignment where two peers and I carried out a risk assessment and provided a report for the fictional business Pampered Pets; a prominent local pet food shop. 

The business has ambitious plans to expand internationally through digitization, and we were tasked to report on potential risks that could arise and mitigations to eliminate threats; alongside any recommendations. 

![Risk Process Step 1: Establish Context](/Modules/3/img/8.png)

We used ISO 31000 as a risk assessment methodology together with STRIDE and DREAD for assessing the risks before and after digitalization of the Pampered Pets business. 

![Risk Process based on ISO 31000](/Modules/3/img/6.png)

![Risk Register with analysis using STRIDE and DREAD](/Modules/3/img/12.png)

The exercise was fun and resulted in a grade of 80%, giving me confidence for future group exercises including assignments. 

![Group Assignment Results](/Modules/3/img/10.png)

Our group faced challenges including  two thirds of the members being part time students whilst being full time employed. 

I learnt to deal with this by setting expectations up front using a team contract, and establish operating mechanisms for collaboration early was key to our success. 

![Group Assignment Team Contract](/Modules/3/img/11.png)

I liked taking onboard my peers input and found that allowing a platform for candid open collaboration that is grounded by a simple operating framework agreed up front delivers strong results.

#### Units 7 & 8: Delving Deeper Into Quantitative Risk Modelling

Unit 7 and 8 allowed me to tackle my initial concerns around quantitative methods head on by first learning about them in more detail followed by gaining experience around using them.

![Delving Deeper Into Quantitative Risk Modelling](/Modules/3/img/13.png)


Experience was gained carrying out practical exercises that involved applying the most common modelling types: Monte Carlo, Bayes Theorem. We then discussed the results during the live seminars.

I really enjoyed challenging myself to grasp these methods. 


####Unit 9: The Importance of Business Continuity(BC)/Disaster Recovery(DR)

Unit 9 then equipped us with a great understanding of business continuity and disaster recovery. 

![DR and Digitalisation](/Modules/3/img/14.png)

We learnt about the importance of having such a strategy in place, and what the main factors are that make up a BC/DR plan including RTOs and RPOs.

![RTO (Recovery Time Objective) & RPO (Recovery Point Objective)](/Modules/3/img/15.png)

####Units 10 & 11: Putting It All Together - An Executive Summary Assignment, and whats next for Risk

During the final few units we had the opportunity to take the knowledge gained and gain more experience applying it through an executive summary assignment.

This report evaluated Pampered Pets again, but this time focused on the potential product quality and availability risks associated with the digitisation and internationalisation of the Pampered Pets business including the introduction of an international supply chain and automated warehouses worldwide. 

Additionally, it provides a GDPR regulatory analysis and outlines a business continuity / disaster recovery strategy to help ensure a 24/7 digital e-commerce customer service capability.

![Risk Process Step 1: Establish Context](/Modules/3/img/16.png)

Here I had the opportunity to apply Bayeses' Theorem in a risk analysis exercise in order to determine probability of risk occurrence 

![Applying Bayes's Theorem](/Modules/3/img/17.png)

![Risk Process Step 2: Risk Analysis](/Modules/3/img/18.png)

![Risk Process Step 3: Regulatory Impact Analysis](/Modules/3/img/20.png)

I also got to create and submit a BC/DR design proposal for a a critical system requiring an active – active solution that is highly recoverable quickly.

![BC/DR Pampered Pets Proposal](/Modules/3/img/19.png)

####Unit 12: What Next? The Future Trends in SRM

We then concluded the module with a look at the future trends in security and risk management. Learning the current and emerging trends was insightful and something I will take away into my current risk work activities.

![Key Questions](/Modules/3/img/21.png)




