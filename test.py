import fileinput

with fileinput.FileInput("tasks.txt", inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace("admin", "user1"), end='')

