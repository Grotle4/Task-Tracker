import json
from datetime import datetime

def check_time():
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime("%b-%d-%Y-%H:%M:%S")
    return formatted_datetime


#Dictionary that will place hold the task implemented, will have placeholder variable for description and ID
task = {
    "id": None,
    "name": None, # type: ignore 
    "description": None, # type: ignore
    "status": None, # type: ignore
    "createdAt": None, #type: ignore
    "updatedAt": None #type: ignore
    }
 
#Terms that don't need an integer ID
no_id_terms = ["list", "list todo", "list in progress", "export", "stop" ] 

known_commands = {"add", "update", "delete", "list", "list done", "list todo", "list in progress",
"mark done", "mark todo", "mark in progress", "stop"}

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
    if len(words) >= 3:
        print("AHHHHHH")
        three_word_command = f"{words[0]} {words[1]} {words[2]}"
        if three_word_command in known_commands:
            return three_word_command, words[3:]
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
    if user not in no_id_terms:
        list_id = words[1]
        listed_task = words[1:]
        no_id = words[2:]
        rejoined_sent = " ".join(listed_task)
        rejoined_no_id = " ".join(no_id)
    iteration += 1 #FIX THIS, iterates weirdly if add isnt run for a few steps

    match command:
        case "add":
            task_time = check_time()
            task["name"] = rejoined_sent
            task["id"] = iteration + 1 #FIX THIS, iterates weirdly
            task["status"] = "Not Done"
            task["createdAt"] = task_time
            task_list.append(task.copy())
            print(f"Added Task! Task {task["id"]} has been set to '{task['name']}'.")
            print(task)
        case "update":
            task_time = check_time()
            for item in task_list:
                if item["id"] == int(list_id):
                    item["name"] = rejoined_no_id
                    task["updatedAt"] = task_time
                    print(f"Updated Task! Task {item["id"]} has been set to '{item['name']}'.")
                    iteration = reset_iteration(iteration,task_list)
                    print(task)
                    break
        case "delete":
            for item in task_list:
                if item["id"] == int(list_id):
                    task_list.remove(item)
                    print(f"Deleted Task! Task {item["id"]}: '{item["name"]}' has been removed.")
                    new_order = 1
                    for item_sort in task_list:
                        item_sort["id"] = new_order
                        new_order += 1
            iteration = reset_iteration(iteration,task_list)
        case "mark todo":
            two_char_id = words[2]
            for item in task_list:
                if item["id"] == int(two_char_id):
                    item["status"] = "To Do"
                    print(f"Updated Task! Task {item["id"]}: '{item["name"]}' has been set to To Do.")
            iteration = reset_iteration(iteration,task_list)
        case "mark done":
            two_char_id = words[2]
            for item in task_list:
                if item["id"] == int(two_char_id):
                    item["status"] = "Done"
                    print(f"Updated Task! Task {item["id"]}: '{item["name"]}' has been set to Done.")
            iteration = reset_iteration(iteration,task_list)
        case "list todo":
            print("list todoned")
            is_occupied = False
            for item in task_list:
                if item["status"] == "To Do":
                        print(f"{item["id"]}: {item["name"]}        Status: {item["status"]}")
            if is_occupied == False:
                print("No Tasks set to To Do.")
            iteration = reset_iteration(iteration,task_list)
        case "list in progress": 
            is_occupied = False
            for item in task_list:
                if item["status"] == "In Progress":
                        print(f"{item["id"]}: {item["name"]}        Status: {item["status"]}") 
                        is_occupied = True
            if is_occupied == False:
                print("No Tasks set to In Progress.")
            iteration = reset_iteration(iteration, task_list)
        case "list done": 
            is_occupied = False
            for item in task_list:
                if item["status"] == "Done":
                        print(f"{item["id"]}: {item["name"]}        Status: {item["status"]}") 
                        is_occupied = True
            if is_occupied == False:
                print("No Tasks set to Done.")
            iteration = reset_iteration(iteration, task_list)
        case "list":
            print("listed")
            is_occupied = False
            for item in task_list:
                print(f"{item["id"]}: {item["name"]}        Status: {item["status"]}")
                is_occupied = True
            if is_occupied == False:
                print("No Tasks set.")
            iteration = reset_iteration(iteration,task_list)
        case "mark in progress":
            is_occupied = False
            three_char_id = words[3]
            for item in task_list:
                if item["id"] == int(three_char_id):
                    item["status"] = "In Progress"
                    is_occupied = True
                    print(f"Updated Task! Task {item["id"]}: '{item["name"]}' has been set to In progress.") 
            iteration = reset_iteration(iteration,task_list)
        case "stop":
            break
        case "export":
            filename = "export.json"
            try:
                with open(filename, "w") as f:
                    json.dump(task_list, f, indent=4)
                print(f"JSON data succesfully written to {filename}")
            except IOError as e:
                print(f"There was an error exporting to file: {e}")
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





