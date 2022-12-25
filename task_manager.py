# ===== IMPORTING LIBRARIES =====
'''This is the section where you will import libraries'''
import os
import time


# ===== VARIABLES SECTION =====
credential_list = []
is_valid = False
is_invalid = False
is_password = False
is_username = False


# ===== LOGIN SECTION =====
'''Here we have a code that will allow a user to login.
    - The code must read usernames and password from the user.txt file
    - I am using a list of usernames and passwords from the file.
    - I am using a while loop to validate my user name and password.
'''
# open user.txt file in order to check if the user has entered his/her/its correct credentials
with open("user.txt", "r", encoding="utf-8") as file:
    # iterate the file
    for line in file:
        line = line.strip(os.linesep).split(", ") # first, get each line of the file and then create an individual list for each login and password data excluding the \n escape characters at the end of the word
        credential_list.append(line) # append the login and password list into another

# request username and password from user in order to access the system
# removes all white space before/after user's input and also
# change all characters into lowercase letter to compare with our database


# while loop that keep asking user to enter its right login and password credentials
# it only stops when user's input is equal to one of the login data inside crendential_list
while is_valid != True:
    username_input = input("Username: ").lower().strip()
    password_input = input("Password: ").lower().strip()
    for username, password in credential_list:
        if username_input == username and password_input == password:
            is_valid = True
            break
        elif username_input == username and password_input != password:
            is_password = True
            time.sleep(1)
            print("Error: login invalid! \nPlease, enter the correct password.")
            time.sleep(1)
        elif username_input != username and password_input == password:
            is_username = True
            time.sleep(1) 
            print("Error: login invalid! \nPlease, enter the correct username.")
            time.sleep(1)
    if is_valid and (not is_password) and (not is_username):
        break
    elif not is_valid and not is_password and not is_username:
        time.sleep(1)
        print("Error: login invalid! \nPlease, enter correct username and password.")
        time.sleep(1)


# print out successful login messaged
time.sleep(1)
print("Login successfull")
time.sleep(1)
print("Authenticating")
time.sleep(1)
print("...........")
time.sleep(2)


# ===== MENU SECTION =====

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':
        pass
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''

    elif menu == 'a':
        pass
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''

    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''

    elif menu == 'vm':
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")