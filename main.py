
#Dictionary that will place hold the task implemented, will have placeholder variable for description and ID
task = {}
#List that stores the tasks
tasks = [] 

#Loop match statement with cases for each input user can do 

while True:
    user = input("Enter a command: " )
    words = user.split()
    match words[0]:
        case "add":
            print("add")
        case "update":
            print("update")
        case "delete":
            print("delete")
        case "todo":
            print("todo")
        case "done":
            print("done")
        case "list":
            print("list")
        case "list" if "todo" in words[1:]:
            print("todo list")
        case "list" if "in-progress" in words[1:]:
            print("in prog list")




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





