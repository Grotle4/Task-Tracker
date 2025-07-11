
#Dictionary that will place hold the task implemented, will have placeholder variable for description and ID
task = {
    "task_ID": None,
    "task name": None, # type: ignore 
    "task_desc": None, # type: ignore
    }
 
#Iteration to assign ID to the list
iteration = -1
#List that stores the tasks
task_list = [] 


#Loop match statement with cases for each input user can do 
while True:
    user = input("Enter a command: " )
    words = user.split()
    print(words)
    listed_task = words[1:]
    rejoined_sent = " ".join(listed_task)
    iteration += 1
    match words[0]:
        case "add":
            print(rejoined_sent)
            task["task name"] = rejoined_sent
            task["task_ID"] = iteration + 1
            task_list.append(task)
            print("Added Task!")
            print(task_list)
        case "update":
            print("update")
        case "delete":
            print("delete")
        case "todo":
            print("todo")
        case "done":
            print("done")
        case _ if "list todo" in user:
            print("todo list")
        case _ if "list in-progress" in user:
            print("in prog list")
        case "list":
            print("list")
        case "stop":
            break
        case _:
            print("not valid!")



#add
#update
#delete
#mark task in progress
#mark tasks that are done
#list all tasks
#list all tasks that are not done
#list all tasks that are in progress
#stop program

#have a exception if the input conditions are not correct





