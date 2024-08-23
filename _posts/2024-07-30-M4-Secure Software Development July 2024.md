---
layout: post
title: Module4: Secure Software Development July 2024
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







