# ===== IMPORTING LIBRARIES =====
'''This is the section where I will import libraries'''
from os import linesep
from datetime import datetime

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

def user_file():
    user_list = []

    with open("user.txt", "r", encoding="utf-8") as file:
        for line in map(str.strip, file):
            if not line:
                continue
            username, password = [
                l.strip() for l in line.split(",")
            ]
            user_list.append(
                {
                    "user": username,
                    "password": password,
                }
            )
    return user_list

def task_file():
    '''Function that will read tasks.txt file and then return a list which contains each line of the file.'''
    task_list = []
    # open tasks.txt file in order to read and store its contents to the user on future operations in another variable (task_list)
    with open("tasks.txt", "r+", encoding="utf-8") as file:
        # iterate the file
        for line in map(str.strip, file):
            # if statement to ignore any blank line inside tasks.txt
            if not line:
                continue
            username, title, description, issued_date, due_date, status = [
                l.strip() for l in line.split(",")
            ]
            task_list.append(
                {
                    "username": username,
                    "title": title,
                    "desc": description,
                    "issued": issued_date,
                    "due": datetime.strptime(due_date, "%d %b %Y"),
                    "status": status,
                }
            )
    return task_list

def modify_task(username=None, title=None, due_date=None, choice=None):
    """This function modifies specific part of the "tasks.txt" file and return a message to the user that will be print out on screen.

    keyword arguments:
    username -- the username of the task that the user wants to change (default None)
    title -- the title of the task that the user wants to change (default None)
    due date -- The currently due date of the task that the user wants to change (default None)
    choice -- what change the user wants to do (default None)
    """
    line_list = []
    line_str_list = []
    message = ""
    now = datetime.today()
    with open("tasks.txt", "r", encoding="utf-8") as rfile:
        for line in rfile:
            line = line.strip(linesep).split(", ")
            line_list.append(line)
    # Get the specific task that the user wants to make the changes
    for line_list_value in line_list:
        if (username in line_list_value) and (title in line_list_value):
            # Change tasks' completion to "Yes"; Print out error message if it is already "Yes"
            if choice == 1:
                if line_list_value[5] == "Yes":
                    message = f"\n[ERROR] Task \"{title}\" has already been marked as \"Yes\"."
                else:
                    line_list_value[5] = "Yes"
                    message = f"\nTask \"{title}\" successfully changed to \"Yes\"!"
            # Change tasks' username if currently day is lower than task due date; Otherqise print out error message
            elif choice == 2:
                divisory_line()
                if now < due_date:
                    new_username = input(f"\nEnter the new username for the task \"{title}\": ").lower().strip()
                    line_list_value[0] = new_username
                    message = "\nNew username successfully updated!\n"
                else:
                    message = f"\n[ERROR] Task \"{title}\" due date has already passed! \nTherefore, you cannot change this information anymore.\n"
            # Change tasks' due date if currently date is lower than task due date; Otherwise print out error message
            elif choice == 3:
                divisory_line()
                if now < due_date:
                    new_due_date = input("\nEnter a new due date of the task (dd Mmm yyyy):\t")
                    line_list_value[4] = new_due_date
                    message = "\nNew due date successfully updated!\n"
                else:
                    message = f"\n[ERROR] Task \"{title}\" due date has already passed! \nTherefore, you cannot change this information anymore.\n"
        # Create a new list which each line inside it with the new values
        line_list_value = str(line_list_value).replace("[", "").replace("]", "").replace("'", "")
        line_str_list.append(line_list_value)
    # rewrite "tasks.txt" file but now with the new lines after the modification has been maden.
    with open("tasks.txt", "w") as wfile:
        for index, line in enumerate(line_str_list):
            if (index + 1) == len(line_str_list):
                wfile.write(line)
            else:
                wfile.write(f"{line}\n")
    # Just return a message to the user in order to inform if the changes were made or not
    return message

    #usernames = username_list()

def password_check(file_name, username, password, password_confirmation):
    """This function checks if the user admin entered the same password during the register procedure.
    If yes, the application add the new user in the system.
    Otherwise, print out a message saying passwords doesn't match.
    
    keyword arguments:
    file_name -- the file that will be opened in order to store the fresh new registered user.
    username -- the username that the admin user wants to add in the system.
    password -- the password that the admin enter for the user that he/she/it wants to register in the system.
    password_confirmation -- the second input password in order to confirm the password entered by the admin user.
    """
    if password == password_confirmation:
        with open(file_name, "a", encoding="utf-8") as file:
            file.write(f"\n{username}, {password}")
        divisory_line()
        print("New user registered!")
    else:
        divisory_line()
        print("Password does not match! \nPlease, make sure next time that both passwords match!")

def reg_user(username):
    '''In this block I will write code to add a new user to the user.txt file
    By doing the following on these steps:
        - Request input of a new username
        - Check if the new username already existed in our database
        - If it doesn't exist, add it to the user.txt file
        - Otherwise it present a relevant message
        - Request input of a new password
        - Request input of password confirmation.
        - Check if the new password and confirmed password are the same calling password_check() function.
    '''
    user_data = user_file() 

    usernames = []
    for data in user_data:
        usernames.append(data["user"])

    if username == "admin":
        new_username = input("Enter a new username: \t") # request new username
        # While loop that will keep asking user to enter a new username,
        # if that username already exists in our database
        # Otherwise, ask user to enter a password and to confirm the password
        while True:
            if new_username in usernames:
                print(f"\n[ERROR] - {new_username} already exist. Please choose another one.")
                divisory_line()
                new_username = input("Enter a new username: \t") # request new username
            else:
                break
        new_password = input("Enter a new password: \t") # request new password
        new_password_confirmation = input("Confirm new password: \t") # request confirmation of new password
        password_check("user.txt", new_username, new_password, new_password_confirmation) # Check if both passwords match or not

    # print out Access Denied Message to User.
    else:
        print("Access Denied! \nYou need to have Admin Access Level \nIn order to register a new user!")

def add_task():
    '''In this function I will put code that will allow a user to add a new task to task.txt file
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
    username_task_assignment = input("Enter username task is assign to:\t\t") # request username of the person that the task was assigned to
    task_title = input("Enter task title: \t\t\t\t") # request task's title
    task_due_date = input("Enter due date of the task (dd Mmm yyyy):\t") # request task's due date
    task_description = input("Enter task description: \n") # request task's description
    

    # get the current date time of the system and store into a variable
    now = datetime.now()
    # convert the current date into a string variable
    task_date_assignment = now.strftime(f"%d %b %Y")
    task_completion = "No"

    # open tasks.txt file and append the new task registered
    # at the end of it.
    with open("tasks.txt", "a", encoding="utf-8") as file:
        file.write(f"\n{username_task_assignment}, {task_title}, {task_description}, {task_due_date}, {task_date_assignment}, {task_completion}")
    
    # print out that the task was successfully registered
    divisory_line()
    print("New task successfully registered!")

def view_all():
    '''In this function I will put code so that the program will read the task from task_file() function and
    print to the console (include spacing and labelling)
    I will do it in this way:
        - Call the function task_file(), storing it in a variable.
        - iterate through this variable to get all value individually and
        - Then print out the results
    '''
    task_list = task_file()
    # for loop that iterates through task_list in order to
    # extract each value and print out to the user
    for task_value in task_list:
        task_due = task_value["due"]
        print(f"""\nTask: \t\t\t{task_value["title"]} \nAssigned to: \t\t{task_value["username"]} \
        \nDate assigned: \t\t{task_value["issued"]} \nDue date: \t\t{task_due.strftime("%d %b %Y")}\
        \nTask complete? \t\t{task_value["status"]} \nTask description: \n  {task_value["desc"]}\n""")

def view_mine():
    '''In this block I will put code the that will read the task from task.txt file and
    print to the console (include spacing and labelling)
    I will do it in this way:
        - Call the function task_file() storing it in a variable.
        - Check if the username of the person logged in is the same as the username I have
        read from the file.
        - If they are the same print it out in a user-friendly way the task
        - Otherwise, print out that the user does not have any task
    '''
    menu = 0
    while menu != int(-1):
        count = 0
        assigned_tasks_list = []
        username_assigned_task = False 
        task_list = task_file() # call task_file() function and store in a variable
        divisory_line()
        # for loop that iterates through task_list in order to
        # extract each value and append to username_assigned_task
        for task_value in task_list:
            if username_input == task_value["username"]:
                count += 1
                task_due = task_value["due"]
                print(f"""\nTask: \t\t\t{task_value["title"]} \nAssigned to: \t\t{task_value["username"]} \
                \nDate assigned: \t\t{task_value["issued"]} \nDue date: \t\t{task_due.strftime("%d %b %Y")}\
                \nTask complete? \t\t{task_value["status"]} \nTask description: \n  {task_value["desc"]}\n""")
                username_assigned_task = True
                assigned_tasks_list.append(task_value)
        if username_input != task_value["username"] and username_assigned_task == False:
            print(f"\nThe {username_input} does not have any task assigned yet.\n")
            break
        
        divisory_line()
        
        # Get which task user wants to change; or break the loop if enter -1.
        menu = int(input("""Enter the number of the task which you would like to access
Or enter -1 to return to the main menu
: """))
        if menu == -1:
            break
        # get the name and the title's name of the task that the user wants to change
        for index, value in enumerate(assigned_tasks_list):
            if menu == (index + 1):
                task_username = value["username"]
                task_title = value["title"]
                task_due_date = value["due"]
        # get what change the user wants to make
        divisory_line()
        menu2 = int(input(f"""***** Task \"{task_title}\" Selected ***** \n\n
Choose one of the option below in order to modify its contents:
[1] Mark the task as completed
[2] Change the username of the task
[3] Change the due date of the task
:"""))
        # call modify_task and print out its result
        print(modify_task(task_username, task_title, task_due_date, menu2))

def generate_reports():
    """Function that creates a text file called task_overview.txt which contains the following:
    """
    task_list = task_file()
    user_list = user_file()
    now =  datetime.today()

    usernames = []
    titles = []
    users_tasks = {}
    tasks_status = {}
    tasks_uncompleted_overdue = {}
    total_tasks_uncompleted_overdue = 0
    total_tasks_completed = 0
    tasks_completed = 0
    total_tasks_uncompleted = 0
    tasks_uncompleted = 0
    

    # ===== USER REPORTS =====

    for user_data in user_list:
        usernames.append(user_data["user"])

    usernames_registered = set(usernames)
    total_usernames_registered = len(usernames_registered)

    for data in task_list:
        titles.append(data["title"])
        users_tasks.setdefault(data["username"], []).append(data["title"])
        tasks_status.setdefault(data["username"], []).append(data["status"])
        if data["status"] == "No" and (now > data["due"]):
            tasks_uncompleted_overdue.setdefault(data["username"], []).append(data["due"])
            total_tasks_uncompleted_overdue += 1
    
    tasks_registered = set(titles)
    total_tasks_registered = len(tasks_registered)

    with open("user_overview.txt", "w") as wfile:
        wfile.write("********** ADMIN USERS OVERVIEW REPORT **********\n")
        wfile.write("\n")
        wfile.write(f"Total number of registered users: {str(total_usernames_registered)}.\n")
        wfile.write(f"Total number of tasks: {total_tasks_registered}.\n")
        wfile.write(f"\nTotal Number of Tasks assigned to each user and its percentage of the total number of tasks registered:\n")
        for user in users_tasks:
            wfile.write(f"User: {user} \t\t No: {len(users_tasks[user])} \t\t Percentage(%): {(len(users_tasks[user]) / len(titles)) * 100:.2f}%.\n")
        wfile.write(f"\nPercentage of the total number of tasks assigned to each user that either have been completed or must still be completed:\n")
        for user in tasks_status:
            for status in tasks_status[user]:
                if status == "Yes":
                    tasks_completed += 1
                    total_tasks_completed += 1
                elif status == "No":
                    tasks_uncompleted += 1
                    total_tasks_uncompleted += 1
            wfile.write(f"User: {user:5} \t\t Percentage Completed Tasks(%): {(tasks_completed / len(tasks_status[user])) * 100:5.2f}% \t\t Percentage Incomplete Tasks(%): {(tasks_uncompleted / len(tasks_status[user])) * 100:6.2f}%.\n")
            tasks_completed = 0
            tasks_uncompleted = 0
        wfile.write(f"\nPercentage of the total number of tasks assigned to each user that have not yet been completed and are overdue:\n")
        if len(tasks_uncompleted_overdue) == 0:
            wfile.write(f"0% - All users have completed all their tasks so far!\n")
        else:
            for user in tasks_uncompleted_overdue:
                wfile.write(f"User: {user} \t\t Percentage(%): {(len(tasks_uncompleted_overdue[user]) / len(users_tasks[user])) * 100:5.2f}%.\n")
        wfile.write("\n")
        wfile.write("******************* END *************************")

    # ===== TASKS REPORTS =====

    with open("task_overview.txt", "w", encoding="utf-8") as wfile:
        wfile.write("********** ADMIN TASK OVERVIEW REPORT **********\n")
        wfile.write("\n")
        wfile.write(f"Total Number of Tasks {'.' * 39} {total_tasks_registered}.\n")
        wfile.write(f"Total Number of Completed Tasks {'.' * 29} {total_tasks_completed}.\n")
        wfile.write(f"Total Number of Uncompleted Tasks {'.' * 27} {total_tasks_uncompleted}.\n")
        wfile.write(f"Total Number of Uncompleted and Overdue Tasks {'.' * 15} {total_tasks_uncompleted_overdue}.\n")
        wfile.write(f"Percentage of Uncompleted Tasks {'.' * 29} {(total_tasks_uncompleted / total_tasks_registered) * 100:.2f}%.\n")
        wfile.write(f"Percentage of Overdue Tasks {'.' * 33} {(total_tasks_uncompleted_overdue / total_tasks_registered) * 100:.2f}%.\n")
        wfile.write("\n")
        wfile.write("******************* END *************************")

def display_stats():
    generate_reports()

    with open("user_overview.txt", "r", encoding="utf-8") as rfile:
        for line in rfile:
            print(line, end="")
    print("")
    divisory_line()
    with open("task_overview.txt", "r", encoding="utf-8") as rfile:
        for line in rfile:
            print(line, end="")
    print("")

def main_menu(username):
    """This function simple returns a menu option according to the user.
    If user is admin then more options will be displayed.

    Keyword arguments:
    username -- The username that has logged in the app.
    """
    if username == "admin":
        user_menu = input('''Select one of the following Options below:
r  \t- \tRegistering a user
a  \t- \tAdding a task
va \t- \tView all tasks
vm \t- \tView my task
gr \t- \tGenerate Reports
ds \t- \tStatistics
e  \t- \tExit
: ''').lower().strip()
    else:
        user_menu = input('''Select one of the following Options below:
r  \t- \tRegistering a user
a  \t- \tAdding a task
va \t- \tView all tasks
vm \t- \tView my task
e  \t- \tExit
: ''').lower().strip()

    return user_menu

# header of the program
header()

# ===== VARIABLES SECTION =====
username_input = ""
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
credentials = user_file()

# while loop that keep asking user to enter its right login and password credentials
# it only stops when user's input is equal to one of the login data inside crendential_list
while is_valid != True:
    # request username and password from user in order to access the system
    # removes all white space before/after user's input and also
    # change all characters into lowercase letter to compare with our database  
    username_input = input("Username: ").lower().strip()
    password_input = input("Password: ").lower().strip()
    
    # for loop that goes through credential_list in order to check if user's input matches with data inside this list
    for credential_data in credentials:
        # check if username and password match with any user login in the list storing this information in a boolean variable; stops the for loopping
        if username_input == credential_data["user"] and password_input == credential_data["password"]:
            is_valid = True
            break
        # print out a messsage to user if username is correct and password wrong
        elif username_input == credential_data["user"] and password_input != credential_data["password"]:
            is_password = True
            print("Error: login invalid! \nPlease, enter the correct password.")
            divisory_line()
        # print out a message to user if username is wrong
        elif username_input != credential_data["user"] and password_input == credential_data["password"]:
            is_username = True
            divisory_line() 
            print("Error: login invalid! \nPlease, enter the correct username.")
            divisory_line()
    # Here we stop while loop if is_valid variable is true
    if is_valid and (not is_password) and (not is_username):
        break
    # Here we print out another message if both username and password were invalid (not matched with any data inside our database)
    elif not is_valid and not is_password and not is_username:
        divisory_line()
        print("Error: login invalid! \nPlease, enter correct username and password.")
        divisory_line()
        


# print out successful login messaged
divisory_line()
print("Login successfull!")
print("Initializing Authentication")
    
# ===== MENU SECTION =====
while True:
    divisory_line()
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = main_menu(username_input)
    # Check if user wants to register a new user
    if menu == 'r':
        # call reg_user() function
        reg_user(username_input)
    
    # Check if user wants to add a new task
    elif menu == 'a':
        # call add_task() function
        add_task()
        
    # Check if user wants to view all tasks registered
    elif menu == 'va':
        # call view_all() function
        view_all()

    # check if user wants to view all his/hers/its tasks registered
    elif menu == 'vm':
        # call view_mine() function
        view_mine()

    elif username_input == "admin" and menu == "gr":
        generate_reports()

    # Statistics Option that only admin has access to
    # When this option is selected, it will display the 
    # total number of tasks and the total number of users
    elif username_input == "admin" and menu == "ds":
        divisory_line()
        display_stats()

    # condition to exit the program            
    elif menu == 'e':
        divisory_line()
        print('\nGoodbye!!!')
        exit()
    # return error message if user enter wrong input
    else:
        divisory_line()
        print("\nYou have made a wrong choice \nPlease Try again!\n")