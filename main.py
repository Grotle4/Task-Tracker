
#Dictionary that will place hold the task implemented, will have placeholder variable for description and ID
task = {}
#List that stores the tasks
tasks = [] 

#Loop match statement with cases for each input user can do 

while True:
    user = input("Enter a command: " )
    words = user.split()
    try:
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
    except:
        print("not a valid command!")



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





