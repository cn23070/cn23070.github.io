---
layout: post
title: Module 1 End of Module Assignment
subtitle: Strong Password Validator Program 
categories: Module_1
tags: [Module 1, Intro, Python]
---

# Strong Password Validator Program and Multifactor Authentication (MFA) Overview

Passwords remain the main security foundation for authenticating humans and machines (Anderson, 2020). 

A lot of the accounts that are compromised today are done so by simply guessing the password, so ensuring a password has sufficient complexity is an important cyber security control. 
 
Although passwords are important, they are also problematic. Humans struggle to remember them, and even then, we struggle to enter them accurately, especially if they are complex (Anderson, 2020).  

This python script firstly helps users determine if their proposed password adheres to current best practices associated with the definition of a strong password. 

The script then attempts to provide an overview of how a basic implementation of MFA works using the python library PyOTP.

It is recommended to use strong passwords as part of a multi factor authentication capability to further strengthen your organisations cyber identify and access management posture. 

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

- **1**: Check against deny list of common passwords

![Example Test 1 Failure](/Modules/1/img/Test1.png)

- **2**: Validate password is between 12 and 50 characters

![Example Test 2 Failure](/Modules/1/img/Test2.png)

- **3**: Confirm at least one lowercase character

![Example Test 3 Failure](/Modules/1/img/Test3.png)

- **4**: Confirm at least one uppercase character

![Example Test 4 Failure](/Modules/1/img/Test4.png)

- **5**: Confirm at least one number

![Example Test 5 Failure](/Modules/1/img/Test5.png)

If all tests pass successfully, the user will be notified accordingly.

![Example of all tests passing successfully](/Modules/1/img/AllTestsPassed.png)

## Code Usage

The following python functions have been coded:

#### 1. print_with_border(message)
Print a given message surrounded by a decorative border.
Used for displaying multi-line messages with a visually appealing format.

#### 2. checkPassword(password)
Validates a proposed password against a predefined deny list and password policy rules.

#### 3. main()
The main function executes a loop allowing users to enter a proposed password and checks its validity. It allows for a user to try again if their proposed password does not conform or exit the program.

## How To Run The Program

### Run the Strong Password Validation script

#### 1. Execute the script in a Python environment:
 - The script will guide you through the process of entering a proposed password and provide feedback on its adherence to best practices.

 ![Example program execution](/Modules/1/img/GetStarted.png)

#### 2. Review Password Best Practice:
 - Follow the outlined steps to ensure your password meets best practices.

 ![Example best practice guidance](/Modules/1/img/StrongPasswordGuideance.png)

#### 3. Enter a Proposed Password:
 - Input a proposed password to check if it conforms to best practices.

 ![Example entering proposed password](/Modules/1/img/GetStarted.png)

 ### Run the MFA walk through script
 Once you have exited the Strong Password Validation exercise, walk through the MFA example using PyOTP

#### 1. install the python library PyOTP:
Install the python library PyOTP:
 - `pip install pyotp`
 - `Successfully installed pyotp-2.9.0`

#### 2. import the necessary module into our Python script
Import the necessary module into our Python script:
 - `import pyotp`

#### 3. Generate a time based secret key
Create the secret key used to generate TOTPs.
- `totp_secret = pyotp.random_base32()`

#### 4. Generrate object and determine expiration interval
Ensure new OTP is generated every 20 seconds:
- `custom_interval = 20
  totp = pyotp.TOTP(totp_secret, interval=custom_interval)`

#### 5. Validate OTP generation
Confirm the script is now able to generate a OTP:
- `print("Your one time Code is:",totp.now())`

#### 6. Verify current OTP system use 
Verify TOTP use using the 'verify() method:
- `enduser_input = input("Please enter the one time code (TOTP):  ")
is_valid = totp.verify(enduser_input)
if is_valid:
    print("your Code is valid :-).")
else:
    print ("Sorry, your Code is invalid :-()")`

#### 7. Verify the system is using the defined timeout interval
- Verify TOTP is changing according to custom interval defined:
- `import time`
- `for i in range(5):
    totp_code = totp.now()
    print("Generated TOTP code at t =", i * custom_interval, "seconds:", totp_code)
    time.sleep(custom_interval)`


## References
- Anderson, T. (2020) Security Engineering: A guide to building dependable distributed systems. 3rd ed. Indianapolis, Indiana: John Wiley & Sons, Inc.
- Rawal, Bharat S, Gunasekaran Manogaran, and Alexender Peter. (2022) Cybersecurity and Identity Access Management. 1st ed. Singapore: Springer.# Sample content Page 1
- Fanti, Marco. (2023) Implementing Multifactor Authentication: Protect Your Applications from Cyberattacks with the Help of MFA. 1st ed. Birmingham, England: Packt Publishing Ltd.

  
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://cn23070.github.io/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/craig-norris-3b787610/)
