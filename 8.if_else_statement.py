# Indentation in Python
# Indentation means adding spaces at the beginning of a line to show that the line belongs to a particular block of code.
# if(i<18):
#       print("you can drive")
# this space above is call indentation 

#q1. ask from user input 
# | Marks | Grade |
# |---:|:---|
# | 90–100 | A+ |
# | 80–89 | A |
# | 70–79 | B+ |
# | 60–69 | B |
# | 50–59 | C+ |
# | 40–49 | C |
# | Below 40 | F |

# userinp=int(input("Enter your marks "))
# if(userinp<=100 and userinp>=90):
#     print("A+")
# elif(userinp<=89 and userinp>=80):
#     print("A")
# elif(userinp<=79 and userinp>=70):
#     print("B+")
# elif(userinp<=69 and userinp>=60):
#     print("B")
# elif(userinp<=59 and userinp>=50):
#     print("C+")
# elif(userinp<=49 and userinp>=40):
#     print("C")
# else:
#     print("F")

# nested else if

username="admin"
password="1234"

un=input("enter your username:\t")
pw=input("enter your password:\t")

if(un==username):
    if(pw==password):
        print("Login successful")
    else:
        print("invalid username or password")
else:
    print("you are not admin ")