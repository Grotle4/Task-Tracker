
#Dictionary that will place hold the task implemented, will have placeholder variable for description and ID
task = {
    "task_ID": None,
    "task_name": None, # type: ignore 
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
    list_id = words[1]
    listed_task = words[1:]
    no_id = words[2:]
    rejoined_sent = " ".join(listed_task)
    rejoined_no_id = " ".join(no_id)
    iteration += 1
    match words[0]:
        case "add":
            task["task_name"] = rejoined_sent
            task["task_ID"] = iteration + 1
            task_list.append(task)
            print(f"Added Task! Task {task["task_ID"]} has been set to '{task['task_name']}'.")
        case "update":
            for item in task_list:
                if item["task_ID"] == int(list_id):
                    item["task_name"] = rejoined_no_id
                    print(f"Updated Task! Task {item["task_ID"]} has been set to '{item['task_name']}'.")
                    break
        case "delete":
            for item in task_list:
                if item["task_ID"] == int(list_id):
                    task_list.remove(item)
                    print(f"Deleted Task! Task {item["task_ID"]}: '{item["task_name"]}' has been removed.")
                    print(task_list)
                    break
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





