
#Dictionary that will place hold the task implemented, will have placeholder variable for description and ID
task = {
    "task_ID": None,
    "task_name": None, # type: ignore 
    "task_desc": None, # type: ignore
    "task_status": None # type: ignore
    }
 
#Terms that don't need an integer ID
no_id_terms = ["list", "list todo", "list in progress", ] 

known_commands = {"add", "update", "delete", "list", "list done", "list todo",
"mark done", "mark todo", "in progress", "stop"}

#Iteration to assign ID to the list
iteration = -1

#List that stores the tasks
task_list = [] 

#takes user input and divides into command and task
def extract_command(user_input: str, known_commands: set):
    words = user_input.lower().split()
    if len(words) >= 2:
        two_word_command = f"{words[0]} {words[1]}"
        if two_word_command in known_commands:
            return two_word_command, words[2:]
    return words[0], words[1:]

#resets iteration value if task other than add is used
def reset_iteration(iteration, tasklist):
 iteration = len(tasklist) - 1
 return iteration


#removes - incase of user input
def normalize_string(user_input):
    normalized_string = user_input.replace("-", " ")
    return normalized_string

#Loop match statement with cases for each input user can do 
while True:
    user_prompt = input("Enter a command: " )
    user = normalize_string(user_prompt)
    user = user.lower()
    words = user.split()
    command, rest_words = extract_command(user, known_commands)
    print(command)
    print(rest_words)                   
    if user not in no_id_terms:
        list_id = words[1]
        listed_task = words[1:]
        no_id = words[2:]
        rejoined_sent = " ".join(listed_task)
        rejoined_no_id = " ".join(no_id)
    iteration += 1 #FIX THIS, iterates weirdly if add isnt run for a few steps

    match command:
        case "add":
            task["task_name"] = rejoined_sent
            task["task_ID"] = iteration + 1 #FIX THIS, iterates weirdly
            task["task_status"] = "Not Done"
            task_list.append(task.copy())
            print(f"Added Task! Task {task["task_ID"]} has been set to '{task['task_name']}'.")
        case "update":
            for item in task_list:
                if item["task_ID"] == int(list_id):
                    item["task_name"] = rejoined_no_id
                    print(f"Updated Task! Task {item["task_ID"]} has been set to '{item['task_name']}'.")
                    iteration = reset_iteration(iteration,task_list)
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
            iteration = reset_iteration(iteration,task_list)
        case "mark todo":
            two_char_id = words[2]
            for item in task_list:
                if item["task_ID"] == int(two_char_id):
                    item["task_status"] = "To Do"
                    print(f"Updated Task! Task {item["task_ID"]}: '{item["task_name"]}' has been set to To Do.")
            iteration = reset_iteration(iteration,task_list)
        case "mark done":
            two_char_id = words[2]
            for item in task_list:
                if item["task_ID"] == int(two_char_id):
                    item["task_status"] = "Done"
                    print(f"Updated Task! Task {item["task_ID"]}: '{item["task_name"]}' has been set to Done.")
            iteration = reset_iteration(iteration,task_list)
        case "list todo":
            print("list todoned")
            for item in task_list:
                if item["task_status"] == "To Do":
                        print(f"{item["task_ID"]}: {item["task_name"]}        Status: {item["task_status"]}") #add exception if empty
            iteration = reset_iteration(iteration,task_list)
        case "list in progress": 
            for item in task_list:
                if item["task_status"] == "In Progress":
                        print(f"{item["task_ID"]}: {item["task_name"]}        Status: {item["task_status"]}") #add exception if empty
            iteration = reset_iteration()
        case "list":
            print("listed")
            for item in task_list:
                print(f"{item["task_ID"]}: {item["task_name"]}        Status: {item["task_status"]}")
            iteration = reset_iteration(iteration,task_list)
        case "in progress":
            print("THIS WORKS")
            two_char_id = words[2]
            for item in task_list:
                if item["task_ID"] == int(two_char_id):
                    item["task_status"] = "In Progress"
                    print(f"Updated Task! Task {item["task_ID"]}: '{item["task_name"]}' has been set to In progress.") 
            iteration = reset_iteration(iteration,task_list)
        case "stop":
            break
        case _:
            print("not valid!")
            iteration = reset_iteration(iteration,task_list)





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





