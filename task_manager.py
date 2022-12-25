# ===== IMPORTING LIBRARIES =====
'''This is the section where I will import libraries'''
import os
import time

# ===== FUNCTION SECTION =====
'''This is the section where I will keep all my functions'''
def divisory_line():
  '''Simple function that print out some lines on the display.'''
  print(f"{'=' * 80}")

def header():
  '''Simple header for the task'''
  divisory_line()
  print(f"{' ' * 25} TASK MANAGEMENT SYSTEM {' ' * 25}")
  divisory_line()



# header of the program
time.sleep(0.7)
header()


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

# while loop that keep asking user to enter its right login and password credentials
# it only stops when user's input is equal to one of the login data inside crendential_list
while is_valid != True:
    # request username and password from user in order to access the system
    # removes all white space before/after user's input and also
    # change all characters into lowercase letter to compare with our database  
    username_input = input("Username: ").lower().strip()
    password_input = input("Password: ").lower().strip()
    
    # for loop that goes through credential_list in order to check if user's input matches with data inside this list
    for username, password in credential_list:
        # check if username and password match with any user login in the list storing this information in a boolean variable; stops the for loopping
        if username_input == username and password_input == password:
            is_valid = True
            break
        # print out a messsage to user if username is correct and password wrong
        elif username_input == username and password_input != password:
            is_password = True
            time.sleep(1)
            divisory_line()
            print("Error: login invalid! \nPlease, enter the correct password.")
            divisory_line()
            time.sleep(0.7)
        # print out a message to user if username is wrong
        elif username_input != username and password_input == password:
            is_username = True
            time.sleep(1)
            divisory_line() 
            print("Error: login invalid! \nPlease, enter the correct username.")
            divisory_line()
            time.sleep(0.7)
    # Here we stop while loop if is_valid variable is true
    if is_valid and (not is_password) and (not is_username):
        break
    # Here we print out another message if both username and password were invalid (not matched with any data inside our database)
    elif not is_valid and not is_password and not is_username:
        time.sleep(1)
        divisory_line()
        print("Error: login invalid! \nPlease, enter correct username and password.")
        divisory_line()
        time.sleep(0.7)


# print out successful login messaged
time.sleep(0.7)
divisory_line()

print("Login successfull!\n")
time.sleep(0.7)

print("Initializing Authentication")
time.sleep(1)

dot = "."
for count in range(1, 6):
    print(dot)
    dot = dot + '.'
    time.sleep(1)
    
# ===== MENU SECTION =====
while True:
    time.sleep(0.7)
    divisory_line()
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r  \t- \tRegistering a user
a  \t- \tAdding a task
va \t- \tView all tasks
vm \t- \tview my task
e  \t- \tExit
: ''').lower().strip()
    
    divisory_line()

    # Check if user wants to register a new user
    if menu == 'r':
        '''
        In this block I will write code to add a new user to the user.txt file
        By doing the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.
        '''
        time.sleep(0.7)
        new_username = input("Enter a new username: \t") # request new username
        new_password = input("Enter a new password: \t") # request new password
        new_password_confirmation = input("Confirm new password: \t") # request confirmation of new password
        # check if the new password and confirmed password are the same
        # then, open user.txt file and add the new username and new password
        # to the end of the file
        if new_password == new_password_confirmation:
            with open("user.txt", "a", encoding="utf-8") as file:
                file.write(f"\n{new_username}, {new_password}")
            time.sleep(1)
            divisory_line()
            print("New user registered!")
        else:
            time.sleep(1)
            divisory_line()
            print("Password does not match! \nPlease, make sure next time that both passwords match!")


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
        print('\nGoodbye!!!')
        exit()

    else:
        print("\nYou have made a wrong choice, Please Try again")