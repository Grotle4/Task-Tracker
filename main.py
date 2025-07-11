
#Dictionary that will place hold the task implemented, will have placeholder variable for description and ID
task = {
    "task_ID": None,
    "task_name": None, # type: ignore 
    "task_desc": None, # type: ignore
    "task_status": None # type: ignore
    }
 
no_id_terms = ["list", "list todo", "list in progress", ] #Terms that don't need an integer ID
#Iteration to assign ID to the list
iteration = -1
#List that stores the tasks
task_list = [] 


def normalize_string(user_input):
    normalized_string = user_input.replace("-", " ")
    return normalized_string

#Loop match statement with cases for each input user can do 
while True:
    user_prompt = input("Enter a command: " )
    user = normalize_string(user_prompt)
    words = user.split()
    if user not in no_id_terms:
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
            task["task_status"] = "Not Done"
            task_list.append(task.copy())
            print(f"Added Task! Task {task["task_ID"]} has been set to '{task['task_name']}'.")
            print(task_list)
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
                    new_order = 1
                    for item_sort in task_list:
                        item_sort["task_ID"] = new_order
                        new_order += 1
                        print(task_list)
        case "todo":
            for item in task_list:
                if item["task_ID"] == int(list_id):
                    item["task_status"] = "To Do"
                    print(f"Updated Task! Task {item["task_ID"]}: '{item["task_name"]}' has been set to To Do.")
        case "done":
            for item in task_list:
                if item["task_ID"] == int(list_id):
                    item["task_status"] = "Done"
                    print(f"Updated Task! Task {item["task_ID"]}: '{item["task_name"]}' has been set to Done.")
        case _ if "in progress" in user:
            print("THIS WORKS")
            in_prog_id = words[2]
            for item in task_list:
                if item["task_ID"] == int(in_prog_id):
                    item["task_status"] = "In progress"
                    print(f"Updated Task! Task {item["task_ID"]}: '{item["task_name"]}' has been set to In progress.")
        case _ if "list todo" in user:
            if item["task_status"] == "To Do":
                    print(f"{item["task_ID"]}: {item["task_name"]}        Status: {item["task_status"]}")
        case _ if "list in progress" in user:
            print("in prog list")
        case "list":
            for item in task_list:
                print(f"{item["task_ID"]}: {item["task_name"]}        Status: {item["task_status"]}")
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





