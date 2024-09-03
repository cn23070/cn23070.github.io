# Secure Media Application

For several years, the music industry has been facing significant challenges related to copyright infringement and the protection of intellectual property. According to the Institute for Policy Innovation (2007), because of global and U.S.-based piracy of sound recordings, the U.S. economy loses $12.5 billion in total output and 71,060 jobs annually. To address these challenges, the following secure digital application has been developed to store and manage copyright materials, ensuring that the rights of writers, performers, and other stakeholders are protected (University of Essex Online, 2024).

The following secure media application has been developed in accordance with the design document: Development Team Project: Design Document by Ming Lee, Bing Hung Lui and Craig Norris. 

The key use cases addressed by this application is secure storage, integrity validation, and role-based access control for music-related artefacts including lyrics, music scores, and recordings.

Any deviations from the original design are explicitly called out along with a correspponding justification as to why.

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

![Example Test 1 Failure](.guides/img/Test1Failed.png)

- **Test 2**: Validate that the password is between 12 and 50 characters

![Example Test 2 Failure](.guides/img/Test2failed.png)

- **Test 3**: Ensure the presence of at least one lowercase character

![Example Test 3 Failure](.guides/img/Test3failed.png)

- **Test 4**: Ensure the presence of at least one uppercase character

![Example Test 4 Failure](.guides/img/Test4Failed.png)

- **Test 5**: Ensure the presence of at least one number

![Example Test 5 Failure](.guides/img/Test5Failed.png)

If all tests pass successfully, the user will be notified accordingly.

![Example of all tests passing successfully](.guides/img/StrongPasswordSuccess.png)

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

 ![Example program execution](.guides/img/GetStarted.png)

#### Step 2. Review Password Best Practice:
 - Follow the outlined steps to ensure your password meets best practices.

 ![Example best practice guidance](.guides/img/StrongPasswordGuideance.png)

#### Step 3. Enter a Proposed Password:
 - Input a proposed password to check if it conforms to best practices.

 ![Example entering proposed password](.guides/img/StartEnteringPassword.png)

## Notes

 - Feel free to customise the thresholds for password length and deny list so that it is in accordance with your own organisations password policy.

 ![Test password length code parameters](.guides/img/TestPasswordlengthCode.png)

 ![Code for passwords deny list](.guides/img/DenyListCode.png)

 - Final note please. It is recommended to use strong passwords as part of a multi factor authentication capability to further strengthen your organisations cyber identify and access management posture.

## References
- Anderson, T. (2020) Security Engineering: A guide to building dependable distributed systems. 3rd ed. Indianapolis, Indiana: John Wiley & Sons, Inc.
- Rawal, Bharat S, Gunasekaran Manogaran, and Alexender Peter. (2022) Cybersecurity and Identity Access Management. 1st ed. Singapore: Springer.# Sample content Page 1
