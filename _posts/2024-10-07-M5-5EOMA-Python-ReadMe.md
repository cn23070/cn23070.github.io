---
layout: post
title: Module 5 End of Module Assignment
subtitle: Secure Systems Architecture September 2024 
categories: Module_5
tags: [Module 5]
---

## **Introduction**

Smart homes are quickly gaining popularity as a leading use case of the emerging Internet of Things (IoT) technology. Leveraging the connectivity capabilities available in modern electronic devices like smartphones, tablets, and multimedia systems, Smart homes deliver automated and engaging services to residential users by utilizing distributed and cooperative systems (Lee et al., 2015). 

As these types of networks gain in popularity, it is imperative to ensure an adequate level of protection against cyber-attacks. Existing early-stage smart home solutions have shown significant vulnerabilities (Panwar et al., 2019).

The design document, Development Team Project: Design Document By: Craig Norris, Edward A Bazanye, Fiqki Azizah, Marwa N K A Alkuwari, and Oluwatosin Ibisola, attempts to provide an Attack-Defence Tree that models the security vulnerabilities in an IoT-based Smart Security and Home Automation System as discussed in the paper by (Kodali et al, 2016), as well as provide proposed countermeasures for any vulnerabilities identifed. 

The paper proposed a counter measure, encryption of messages in transit between IoT devices and the central controller, to mitigate a few high priority vulnerabilities including man in the middle (MITM) attacks.

The objective of the application, iot__messages_simulation.py, is to investigate whether encrypting individual messages between IoT devices and a central controller improves security while maintaining an acceptable level of performance in a Smart Home Automation System.



## **Hypothesis**

Does encrypting communication between a simulated IoT device and the central controller at the message level improve security without significantly affecting performance in a Smart Home Automation System?


## **System Model**

A simplified IoT-based Smart Home Automation System was modelled using Python. The model includes:


![System Model](/Modules/5/img/15.png)

- **Figure 1**: System model description


## **Prerequisites**

![Application Prerequisites](/Modules/5/img/16.png)

- **Figure 2**: Application Prerequisites

You can install the required Python packages using pip.

## **Usage Example:**

This section provides guidance on how to simulate plain and encrypted message communication using the provided script.

### **Evidence of testing**

The following video provides evidence of application testing including results of code quality, security and custom configurations.


![Evidence of testing](/Modules/5/Screen Recording 2024-10-21 at 14.04.24.mov)

- **Figure 3**: Evidence of testing



### **Example 1: Default simulation with 10 devices**

The following command will execute the application and in doing so simulate 10 IoT devices sending both plain and encrypted messages to the controller.


![Launching the application](/Modules/5/img/17.png)

- **Figure 4**: Launching the application


## **Expected Output:**


•	It will show messages being sent by each device.
•	Indicate whether each message was intercepted.
•	Display a summary table at the end.


![Example of expected output](/Modules/5/img/18.png)

- **Figure 5**: Example of expected output


### **Example 2: Customisations**

You can adjust parameters to modify the experiment:

Change the number of devices simulated.


![Customising number of devices](/Modules/5/img/19.png)

- **Figure 6**: Customising number of devices


![Example evidence of customised testing with 40 devices](/Modules/5/img/20.png)

- **Figure 7**: Example evidence of customised testing with 40 devices


## **Code Structure and Usage**

![Application code structure](/Modules/5/img/21.png)

- **Figure 8**: Application code structure


## **Experiments**

![Table of experiments](/Modules/5/img/22.png)

- **Figure 9**: Table of experiments


## **Results**

### **Experiment ID 1**

![Experiment 1 results](/Modules/5/img/23.png)

- **Figure 10**: Experiment 1 results

The difference in response time between plain text messages and encrypted messages is negligible, with encryption introducing an overhead of only a few microseconds.


### **Experiment ID 2**


![Evidence of experiment results](/Modules/5/img/24.png)

- **Figure 11**: Evidence of experiment results


![Experiment 2 results](/Modules/5/img/25.png)

- **Figure 12**: Experiment 2 results


Encrypted messages provide a reasonable safeguard against any messages intercepted by an attacker


### **Experiment ID 3**


![Experiment 3 results](/Modules/5/img/26.png)

- **Figure 13**: Experiment 3 results


As the number of devices increased, the response time for both plain text and encrypted messages increased.

Although encryption does consistently introduce a small overhead of additional time, the difference is manageable. 



### **Conclusion**

The hypothesis that encrypting individual messages between IoT devices and the central controller enhances security without significantly affecting performance is supported by the results of our experiments. 


![Conclusion](/Modules/5/img/27.png)

- **Figure 14**: Conclusion



## **References**

### References for Libraries Used

**Time library:**

Python Software Foundation. (n.d.). time — Time access and conversions. Available at: https://docs.python.org/3/library/time.html [Accessed: 21 October 2024].

**Random library:**

Python Software Foundation. (n.d.). random — Generate pseudo-random numbers. Available at: https://docs.python.org/3/library/random.html [Accessed: 21 October 2024].

**String library:**

Python Software Foundation. (n.d.). string — Common string operations. Available at: https://docs.python.org/3/library/string.html [Accessed: 21 October 2024].

**Pandas library (imported as pd):**

The Pandas Development Team. (n.d.). pandas: powerful Python data analysis toolkit. Available at: https://pandas.pydata.org/ [Accessed: 21 October 2024].


### Other References

Lee, I. and Lee, K. (2015). The Internet of Things (IoT): Applications, investments, and challenges for enterprises. Business Horizons, 58(4), pp.431–440. doi:https://doi.org/10.1016/j.bushor.2015.03.008.

Panwar, N., Sharma, S., Mehrotra, S., Krzywiecki, Ł. and Venkatasubramanian, N. (2019). Smart Home Survey on Security and Privacy. [online] arXiv.org. Available at: https://arxiv.org/abs/1904.05476v2 [Accessed 27 Sep. 2024].

Kodali, R.K., Jain, V., Bose, S. and Boppana, L., 2016, April. IoT based smart security and home automation system. In 2016 international conference on computing, communication and automation (ICCCA) (pp. 1286-1289). IEEE.

Richards, D., Abdelgawad, A. and Yelamarthi, K., 2018, December. How does encryption influence timing in IoT?. In 2018 IEEE Global Conference on Internet of Things (GCIoT) (pp. 1-5). IEEE.

Cekerevac, Z., Dvorak, Z., Prigoda, L. and Cekerevac, P., 2017. Internet of things and the man-in-the-middle attacks–security and economic risks. MEST Journal, 5(2), pp.15-25.
