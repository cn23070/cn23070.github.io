---
layout: post
title: Module 1 End of Module Assignment
subtitle: Strong Password Validator Program 
categories: Module_1
tags: [Module 1, Intro, Python]
---

# Strong Password Validator Program and Multifactor Authetication (MFA) Overview

Passwords remain the main security foundation for authenticating humans and machines (Anderson, 2020). 

A lot of the accounts that are compromised today are done so by simply guessing the password, so ensuring a password has sufficient complexity is an important cyber security control. 
 
Although passwords are important, they are also problematic. Humans struggle to remember them, and even then, we struggle to enter them accurately, especially if they are complex (Anderson, 2020).  

This python script firstly helps users determine if their proposed password adheres to current best practices associated with the definition of a strong password. 

It is recommended to use strong passwords as part of a multi factor authentication capability to further strengthen your organisations cyber identify and access management posture. 

With this in mind the script also attempts to provide an overview of how a basic impolementation of MFA works using the python library PyOTP.

MFA requires two or more independent authentication factors, ensuring a more rigorous authentication process. Even if one factor is compromised, the likelihood of a successful breach is still reduced (Fanti, 2023).

### Password Best Practice Criteria:

A strong password can be defined as a password that is sufficiently long and has a mixture of uppercase, lower case, numbers, and special characters (Rawal et al. 2014).

In summary, a strong password should:
 - not be very common or easily guessed
 - be of an optimal length (recommend using a phrase)
 - contain at least one lowercase letter
 - contain at least one uppercase letter
 - contain at least one number

### Password Validation Tests Performed

This program will attempt to validate if a proposed password entered by the user is a strong or not.  
This is accomplished by using python coded functions that perform the following tests:

- **Test 1**: Check if the password is in a deny list of common passwords

![Example Test 1 Failure](/Modules/1/img/Test1.png)

- **Test 2**: Validate that the password is between 12 and 50 characters

![Example Test 2 Failure](/Modules/1/img/Test2.png)

- **Test 3**: Ensure the presence of at least one lowercase character

![Example Test 3 Failure](/Modules/1/img/Test3.png)

- **Test 4**: Ensure the presence of at least one uppercase character

![Example Test 4 Failure](/Modules/1/img/Test4.png)

- **Test 5**: Ensure the presence of at least one number

![Example Test 5 Failure](/Modules/1/img/Test5.png)

If all tests pass successfully, the user will be notified accordingly.

![Example of all tests passing successfully](/Modules/1/img/AllTestsPassed.png)

## Code Usage

The following python functions have been coded:

#### 1. Function: print_with_border(message)
This function prints a given message surrounded by a decorative border.
Used for displaying multi-line messages with a visually appealing format.

#### 2. Function: checkPassword(password)
This function validates a proposed password against a predefined deny list and password policy rules.
Passwords on the deny list (common or easily guessed passwords) are rejected.
Passwords must meet the following criteria:

 - length between 12 and 50 characters.
 - contains at least one lowercase letter.
 - contains at least one uppercase letter.
 - contains at least one number.

#### 3. Function: main()
The main function executes a loop allowing users to enter a proposed password and checks its validity. It allows for a user to try again if their proposed password does not conform or exit the program.

## How To Run The Program
#### Step 1. Execute the script in a Python environment:
 - The script will guide you through the process of entering a proposed password and provide feedback on its adherence to best practices.

 ![Example program execution](/Modules/1/img/GetStarted.png)

#### Step 2. Review Password Best Practice:
 - Follow the outlined steps to ensure your password meets best practices.

 ![Example best practice guidance](/Modules/1/img/StrongPasswordGuideance.png)

#### Step 3. Enter a Proposed Password:
 - Input a proposed password to check if it conforms to best practices.

 ![Example entering proposed password](/Modules/1/img/GetStarted.png)

## Notes

 - Feel free to customise the thresholds for password length and deny list so that it is in accordance with your own organisations password policy.

 ![Test password length code parameters](/Modules/1/img/TestPasswordlength.png)

 ![Code for passwords deny list](/Modules/1/img/PasswordDenyList.png)


## References
- Anderson, T. (2020) Security Engineering: A guide to building dependable distributed systems. 3rd ed. Indianapolis, Indiana: John Wiley & Sons, Inc.
- Rawal, Bharat S, Gunasekaran Manogaran, and Alexender Peter. (2022) Cybersecurity and Identity Access Management. 1st ed. Singapore: Springer.# Sample content Page 1
- Fanti, Marco. (2023) Implementing Multifactor Authentication: Protect Your Applications from Cyberattacks with the Help of MFA. 1st ed. Birmingham, England: Packt Publishing Ltd.

  
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://cn23070.github.io/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/craig-norris-3b787610/)