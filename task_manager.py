# ===== IMPORTING LIBRARIES =====
'''This is the section where I will import libraries'''
from os import linesep
import time
import datetime

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

def user_file(file_name, mode, username, password, password_confirmation):
    if mode == "a" and password == password_confirmation:
        with open(file_name, mode, encoding="utf-8") as file:
            file.write(f"\n{username}, {password}")
        time.sleep(1)
        divisory_line()
        print("New user registered!")
    elif mode == "a" and password != password_confirmation:
        time.sleep(1)
        divisory_line()
        print("Password does not match! \nPlease, make sure next time that both passwords match!")

def username_list():
    '''Function that returns a list with all usernames in user.txt file.'''
    line_list = [] # List that will receive all lines from user.txt file
    username_list = [] # list that will receive only the usernames from user.txt file
    # open user.txt file
    with open("user.txt", "r", encoding="utf-8") as file:
        # iterate the file
        for line in file:
            line = line.strip(linesep).split(", ") # strip the special escape character \n and split the lines
            line_list.append(line) # append each line to line_list
    # iterate through line_list
    for index, value in enumerate(line_list):
        username_list.append(value[0]) # append only the usernames to username_list

    return username_list # return a list that contains only the usernames

def password_list():
    '''Function that returns a list with all passwords in user.txt file.'''
    line_list = [] # List that will receive all lines from user.txt file
    password_list = [] # list that will receive only the usernames from user.txt
    # Open user.txt file
    with open("user.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip(linesep).split(", ") # strip the special escape character \n an split the lines
            line_list.append(line) # append each line to line_list
    # iterate through line_list
    for index, value in enumerate(line_list):
        password_list.append(value[1]) # append only the passwords to password_list
    
    return password_list # return a list that contains onle the passwords

def reg_user(username, username_list):
    '''
    In this block I will write code to add a new user to the user.txt file
    By doing the following on these steps:
        - Request input of a new username
        - Check if the new username already existed in our database
        - If it doesn't exist, add it to the user.txt file
        - Otherwise it present a relevant message
        - Request input of a new password
        - Request input of password confirmation.
        - Check if the new password and confirmed password are the same.
        - If they are the same, add them to the user.txt file,
        - Otherwise it present a relevant message.
    '''
    if username == "admin":
        time.sleep(0.7)
        new_username = input("Enter a new username: \t") # request new username
        while True:
            time.sleep(0.7)
            if new_username in username_list:
                print(f"\n[ERROR] - {new_username} already exist. Please choose another one.")
                divisory_line()
                new_username = input("Enter a new username: \t") # request new username
            else:
                new_password = input("Enter a new password: \t") # request new password
                new_password_confirmation = input("Confirm new password: \t") # request confirmation of new password
                user_file("user.txt", "a", new_username, new_password, new_password_confirmation)
                break
    else:
            print("Access Denied! \nYou need to have Admin Access Level \nIn order to register a new user!")

def add_task():
    pass

def view_all():
    pass

def view_mine():
    pass



# header of the program
time.sleep(0.7)
header()


# ===== VARIABLES SECTION =====
usernames = username_list()
passwords = password_list()
username_input = ""
credential_list = []
task_list = []
is_valid = False
is_invalid = False
is_password = False
is_username = False

# open tasks.txt file in order to read and store its contents to the user on future operations in another variable (task_list)
with open("tasks.txt", "r", encoding="utf-8") as file:
    # iterate the file
    for line in file:
        line = line.strip(linesep).split(", ") # first, get each line of the file and then create an individual list for each task's information, excluding the \n escape characters at the end of the word
        task_list.append(line) # append the tasks information list into another variable (task_list)


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
        line = line.strip(linesep).split(", ") # first, get each line of the file and then create an individual list for each login and password data excluding the \n escape characters at the end of the word
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
print("Login successfull!")
time.sleep(0.7)
print("Initializing Authentication")
time.sleep(1)
dot = "."
for count in range(1, 4):
    print(dot)
    time.sleep(1)
    
# ===== MENU SECTION =====
while True:
    time.sleep(0.7)
    divisory_line()
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    if username_input != "admin":
        menu = input('''Select one of the following Options below:
r  \t- \tRegistering a user
a  \t- \tAdding a task
va \t- \tView all tasks
vm \t- \tview my task
e  \t- \tExit
: ''').lower().strip()
    else:
        menu = input('''Select one of the following Options below:
r  \t- \tRegistering a user
a  \t- \tAdding a task
va \t- \tView all tasks
vm \t- \tView my task
s  \t- \tStatistics
e  \t- \tExit
: ''').lower().strip()
    
    divisory_line()

    # Check if user wants to register a new user
    if menu == 'r':
        reg_user(username_input, usernames)

    elif menu == 'a':
        '''
        In this block I will put code that will allow a user to add a new task to task.txt file
        By doing the following on these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - Include the 'No' as initial value to indicate if the task is complete.
        '''
        time.sleep(0.7)
        username_task_assignment = input("Enter username task is assign to:\t\t") # request username of the person that the task was assigned to
        task_title = input("Enter task title: \t\t\t\t") # request task's title
        task_due_date = input("Enter due date of the task (dd Mmm yyyy):\t") # request task's due date
        task_description = input("Enter task description: \n") # request task's description
        

        # get the current date time of the system and store into a variable
        now = datetime.datetime.now()
        # convert the current date into a string variable
        task_date_assignment = now.strftime(f"%d %b %Y")
        task_completion = "No"

        # open tasks.txt file and append the new task registered
        # at the end of it.
        with open("tasks.txt", "a", encoding="utf-8") as file:
            file.write(f"\n{username_task_assignment}, {task_title}, {task_description}, {task_due_date}, {task_date_assignment}, {task_completion}")
        
        # print out that the task was successfully registered
        time.sleep(1)
        divisory_line()
        print("New task successfully registered!")

    elif menu == 'va':
        '''
        In this block I will put code so that the program will read the task from task.txt file and
        print to the console (include spacing and labelling)
        I will do it in this way:
            - Read a line from the file.
            - Split the line where there is comma and space.
            - Then print the results
        '''
        time.sleep(0.7)
        # for loop that iterates through task_list in order to
        # extract each value and print out to the user
        for values in task_list:
            print(f"""\nTask: \t\t\t{values[0]} \nAssigned to: \t\t{values[1]} \nDate assigned: \t\t{values[3]} \nDue date: \t\t{values[4]} \nTask complete? \t\t{values[5]} \nTask description: \n  {values[2]}\n""")
            time.sleep(0.7)


    elif menu == 'vm':
        '''
        In this block I will put code the that will read the task from task.txt file and
        print to the console (include spacing and labelling)
        I will do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username I have
            read from the file.
            - If they are the same print it out
        '''
        time.sleep(0.7)
        # for loop that iterates through task_list in order to
        # extract each value and print out to the user
        for values in task_list:
            if username_input == values[0]:
                print(f"""\nTask: \t\t\t{values[0]} \nAssigned to: \t\t{values[1]} \nDate assigned: \t\t{values[3]} \nDue date: \t\t{values[4]} \nTask complete? \t\t{values[5]} \nTask description: \n  {values[2]}\n""")
                time.sleep(0.7)

    # Statistics Option that only admin has access to
    # When this option is selected, it will display the 
    # total number of tasks and the total number of users
    elif username_input == "admin" and menu == "s":
        print(f"""***** STATISTICS *****
{task_list}
{credential_list}
Number of tasks: \t{len(task_list)}   
Number of users: \t{len(credential_list) - 1} 
        """) # we do credential_list - 1 to exclude the admin from the count.
    
    # condition to exit the program            
    elif menu == 'e':
        print('\nGoodbye!!!')
        exit()
    # return error message if user enter wrong input
    else:
        print("\nYou have made a wrong choice, Please Try again")