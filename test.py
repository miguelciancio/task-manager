from os import linesep

line_list = []
line_str_list = []

def modify_task(username=None, title=None, choice=None):
    username = "admin"
    title = "Register Users with taskManager.py"
    choice = 1
    # Aqui eu abro um arquivo de texto; pego cada linha separadamente e as coloco como sendo um valor dentro de uma lista - criando assim
    # uma nested list em que cada valor e uma outra lista contendo como valor cada palavra de uma linha
    with open("tasks.txt", "r", encoding="utf-8") as rfile:
        for line in rfile:
            line = line.strip(linesep).split(", ")
            line_list.append(line)
    # Aqui eu faco um loop e pego cada valor da lista line_list para poder selecionar somente a lista o qual o usuario deseja alterar.
    # Para poder selecionar a tarefa especifica que o usuario deseja alterar, eu faco uso do nome do usuario e nome do titulo da tarefa
    # registrado para poder checar se esses dois valores estao dentro da lista line_list.
    # Apos selecionar a tarefa especifica que o usuario deseja alterar, eu checo qual modificacao ele deseja fazer atraves de um outro 
    # if-elif statement.
    # Apos determinar qual alteracao deve ser feita, eu a realizo
    # Apos fazer as devidas alteracoes, eu faco o seguinte:
    #   - converto a list para string
    #   - formato a string para ficar no mesmo formato padrao original do arquivo de texto
    #   - salvo cada string em uma nova lista
    for line_list_value in line_list:
        if (username in line_list_value) and (title in line_list_value):
            if choice == 1:
                line_list_value[5] = "Yes"
        line_list_value = str(line_list_value).replace("[", "").replace("]", "").replace("'", "")
        line_str_list.append(line_list_value)
    # Aqui eu simplesmente abro o arquivo de texto e apago todo o conteudo dele.
    with open("tasks.txt", "w") as wfile:
        wfile.write("")
    # Eu faco um loop dentro da lista line_str_list que contem todas as linhas a serem escritas novamente no arquivo
    # E finalmente, escrevo todas as linhas com as devidas atualizacoes no arquivo e end.
    with open("tasks.txt", "a") as afile:
        for index, line in enumerate(line_str_list):
            if (index + 1) == len(line_str_list):
                afile.write(line)
            else:
                afile.write(f"{line}\n")



modify_task()


'''with open("tasks.txt", "r+") as file:
    lines = file.read()

print(lines)'''

'''task_list = []
# open tasks.txt file in order to read and store its contents to the user on future operations in another variable (task_list)
with open("tasks.txt", "r+", encoding="utf-8") as file:
    # iterate the file
    for line in file:
        line = line.strip(linesep).split(", ") # first, get each line of the file and then create an individual list for each task's information, excluding the \n escape characters at the end of the word
        task_list.append(line) # append the tasks information list into another variable (task_list)
print(task_list)
'''


'''Here we check if the user wants or either change:
            - The completion status of the task to yes, or
            - If wants to edit some information of the task
                - Could change the username of the person to whom the task is assigned, or
                - Could change the due date of the task.

                user_task_choices = int(input("Choose an option \n\n[1] Change Completion status of the task \n[2] Edit others information \n\n:"))
                if user_task_choices == 1:
                    with fileinput.FileInput("tasks.txt", inplace=True, backup='.bak') as file:
                        for index, line in enumerate(file):
                            if index == user_task_choices - 1: # NEED CHECK IF CURRENT DATE IS LOWER THAN DUE DATE
                                print(line.replace("No", "Yes"), end='')
                            else:
                                print(line, end='')
            '''