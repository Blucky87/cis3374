#Quality Assurance & Testing Lab1
#Zixuan Liang
#1/23/2018

from datetime import datetime, date
import string




#Open file for student information
Sfile = open("Student", "w")
print (Sfile) 


    
# student's first name
firstName = input("Please enter student's first name: ")
#Check if first name is valid
if len(firstName) >= 0:
  while len(firstName) >= 0:
    if firstName.isalpha():
      print("First name saved!")
      break
    else:
      print ("Sorry, that is not a valid name.")
      firstName=input("Please re-enter student's first name: ")

# student's middle name 
middleName = input("Please enter student's middle name: ")
#Check if middle name is valid
if len(middleName) >= 0:
  while len(middleName) >= 0:
    if middleName.isalpha():
      print("Middle name saved!")
      break
    else:
      print ("Sorry, that is not a valid name.")
      middleName=input("Please re-enter student's middle name: ")

# student's last name
lastName = input("Please enter student's last name: ")
#Check if last name is valid
if len(lastName) >= 0:
  while len(lastName) >= 0:
    if lastName.isalpha():
      print("Last name saved!")
      break
    else:
      print ("Sorry, that is not a valid name.")
      lastName=input("Please re-enter student's last name: ")

#student's birthday
birthDate = input("Please enter student's date of birth in mm/dd/yyyy format: ")
print("Birth date saved!")

#Calculate age
def calculate_age(birthDate):
  today = date.today()
  return   today.year - birthDate.year  - ((today.month, today.day) < (birthDate.month, birthDate.day))
#


# student's phone number 10 digit
phoneNumber = input("Please enter student's 10 digits phone number in ########## format: ")
#Check if student phone number is valid
if len(phoneNumber) != 10:
  while len(phoneNumber) != 10:
    if (phoneNumber.isalpha() or len(phoneNumber) != 10):
      print ("Sorry, that is not a valid phone number with correct formatting.")
      phoneNumber=input("Please re-enter student's 10 digits phone number in ########## format: ")
      if len(phoneNumber) == 10:
        print("Phone number saved!")
else:
  print("Phone number saved!")

# student graduation date
graduationDate = input("Please enter student's expected graduation date in mm/yy format: ")
print("Graduation date saved!")

# TUID
tuID = input("Please enter student's 9-digit TUID number: ")
#Check if TUID# is valid
if len(tuID) != 9:
  while len(tuID) != 9:
    print("Sorry please enter a 9-digit number for your TUID.")
    tuID = input("Please re-enter student's 9-digit TUID number: ")
    if len(tuID) == 9:
      print("TUID saved!")
else:
  print("TUID saved!")


# student's major
major = input("Please enter student's major: ")
#Check if major is valid
if len(major) >= 0:
  while len(major) >= 0:
    if major.isalpha():
      print("Major saved!")
      break
    else:
      print ("Sorry, that is not a valid major.")
      major=input("Please re-enter student's major: ")

# student's email 
email = input("Please enter student's email address: ")
#Check if student email is valid
if len(email) >= 0:
  while True:
    if "@" in email and "." in email:
        print ("Email address saved!")
        break
    else:
      print ("Sorry, that is not a valid email address.")
      email=input("Please re-enter student's email: ")
      continue
else:
  print("Email address saved!")

#undergraduate status
undergradCheck = input("Is this student an undergraduate? Type 'Yes' for yes or 'No' for no: ")
#Check if undergradCheck input is valid
if undergradCheck != 'Yes' or undergradCheck != 'yes' or undergradCheck != 'No' or undergradCheck != 'no':
  while True:
    if (undergradCheck == 'Yes' or undergradCheck == 'yes'):
      undergradCheck = True
      break
    elif (undergradCheck == 'No' or undergradCheck == 'no'):
      undergradCheck = False
      break
    else:
      print("Sorry, that is not a valid entry. Please try again.")
      undergradCheck = input("Is this student an undergraduate? Type 'Yes' for yes or 'No' for no: ")
      continue
else:
    print("Undergraduate status saved.")


#Write student info to file
Sfile.write("Full name: " + firstName + " " + middleName + " " + lastName+ "\n")
Sfile.write("Age: "  +birthDate +  "\n")
Sfile.write("TUID Number: " + tuID + "\n")
Sfile.write("Email Address: " + email + "\n")
Sfile.write("Phone Number: " + phoneNumber + "\n")
Sfile.write("Major: " + major + "\n")
Sfile.write("Expected Graduation Date: " + graduationDate + "\n")
Sfile.write("Undergraduate Status: " + str(undergradCheck) + "\n")

#Close the file 
#Sfile.restart()
#Sfile.close()


