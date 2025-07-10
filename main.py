
def check_command():
    while True:
        user = input()
        words = user.split()
        command = words[0]
        identifer = ""
        if command != "stop":
            try:
                new_identifier = check_null(command, identifer, words)
                check_type(command, new_identifier, words)
                print(type(identifer)) 
            except IndexError:
                print("no 2nd value")
        else:
            break



def list_index(tasks):
    for index, t in enumerate(tasks):
        print(f"{index}: {t}")



def check_type(user_command, user_identifier, user_words):
    match user_command:
                    case "add":
                        print(user_identifier)
                        tasks.append(user_identifier)
                        print("added")
                        print(tasks)
                    case "update":
                        print("updated")
                    case "list":
                        print("listed")
                        try:
                            list_command = user_words[1]
                            if list_command == "done":
                                print("doned")
                            elif list_command == "todo":
                                print("todo'd")
                            elif list_command == "in-progress":
                                print("in progressed")
                        except IndexError:
                            print("no additional list")
                            list_index(tasks)



def check_null(user_command, user_words):
    if user_command != "list" and len(user_words) > 1:
        print("passed")
        return user_words[1]
    return None

tasks = []
check_command()

    
