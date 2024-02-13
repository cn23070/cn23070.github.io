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

The script then attempts to provide an overview of how a basic impolementation of MFA works using the python library PyOTP.

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

### Run the Strong Password Validation script

#### Step 1. Execute the script in a Python environment:
 - The script will guide you through the process of entering a proposed password and provide feedback on its adherence to best practices.

 ![Example program execution](/Modules/1/img/GetStarted.png)

#### Step 2. Review Password Best Practice:
 - Follow the outlined steps to ensure your password meets best practices.

 ![Example best practice guidance](/Modules/1/img/StrongPasswordGuideance.png)

#### Step 3. Enter a Proposed Password:
 - Input a proposed password to check if it conforms to best practices.

 ![Example entering proposed password](/Modules/1/img/GetStarted.png)

 ### Run the MFA walk through script
 Once you have exited the Strong Password Validation exercise, walk through the MFA example using PyOTP

#### Step 1. install the python library PyOTP:
 - install the python library PyOTP:
 - pip install pyotp

you should see a similar message to the following:
Collecting pyotp
  Downloading pyotp-2.9.0-py3-none-any.whl (13 kB)
Installing collected packages: pyotp
Successfully installed pyotp-2.9.0


#### Step 2. import the necessary module into our Python script
 - import the necessary module into our Python script
 - import pyotp

#### Step 3. Generate a time based secret key
- Next generate a secret key that will be used to generate time based one time password codes. We will do this by creating an instance of the TOTP class and calling its generate secret() method
- totp_secret = pyotp.random_base32()

#### Step 4. Generrate object and determine expiration interval
- Its important to ensure the one time password we generate will expire after an applicable internal. We will use 20 seconds for this demonstration:
- custom_interval = 20
- totp = pyotp.TOTP(totp_secret, interval=custom_interval)

#### Step 5. Validate OTP generation
- confirm the script is now able to generate a OTP:
- print("Your one time Code is:",totp.now())

#### Step 6. Verify current OTP system use 
- we then verify a TOTP code using the 'verify() method
- enduser_input = input("Please enter the one time code (TOTP):  ")
is_valid = totp.verify(enduser_input)
if is_valid:
    print("your Code is valid :-).")
else:
    print ("Sorry, your Code is invalid :-()")

#### Step 7. Verify the system is using the defined timeout interval
- we then verify a TOTP code is changing in accordance with the customer interval we defined in  'verify() method
for i in range(5):
    totp_code = totp.now()
    print("Generated TOTP code at t =", i * custom_interval, "seconds:", totp_code)
    time.sleep(custom_interval)




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
