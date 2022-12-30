from os import linesep
from datetime import datetime

task_list = []
# open tasks.txt file in order to read and store its contents to the user on future operations in another variable (task_list)
with open("tasks.txt", "r+", encoding="utf-8") as file:
    # iterate the file
    for line in file:
        line = line.strip(linesep).split(", ") # first, get each line of the file and then create an individual list for each task's information, excluding the \n escape characters at the end of the word
        task_list.append(line) # append the tasks information list into another variable (task_list)

date = task_list[0][3]
new_date = datetime.strptime(date, "%d %b %Y")

now = datetime.today()

print(date)
print(new_date)
print(now)

if now > new_date:
    print("Cant change")
elif now == new_date:
    print("Cant change")
else:
    print("Can change")
