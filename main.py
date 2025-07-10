
tasks = []
description = []


def check_command():
    iteration = -1
    while True:
        user = input()
        words = user.split()
        sentence = words[1:]
        new_sentence = " ".join(sentence)
        iteration += 1
        command = words[0]
        identifer = ""
        if command != "stop":
            try:
                print("trying")
                new_identifier = check_null(command, words, new_sentence)
                print(new_identifier)
                index_value = new_identifier[0]
                check_type(command, new_identifier, words, iteration, new_sentence, index_value)
            except IndexError:
                print("no 2nd value")
        else:
            break



def list_index(tasks):
    for index, t in enumerate(tasks, start=1):
        print(f"{index}: {t}")



def check_type(user_command, user_identifier, user_words, user_iteration, user_sentence, user_index): 
    match user_command:
                    case "add":
                        if user_identifier != None:
                            tasks.append(user_identifier[0])
                            description.append(user_iteration)
                    case "description":
                        if user_identifier != None:
                            desc_sentence = scrub_index(user_sentence)
                            description[int(user_index) - 1] = desc_sentence
                            print(f"description: {description}")
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


def check_null(user_command, user_words, user_sentence):
    print(f"user command: {user_command}")
    if user_command != "list" and user_command != "description" and len(user_words) > 1:
        print("not working")
        finished_words = user_words[1:]
        finished_task = " ".join(finished_words)
        print(finished_task, user_sentence)
        return finished_task, user_sentence
    elif user_command == "list":
        finished_words = user_words[1:]
        finished_task = " ".join(finished_words)
        print(finished_task, user_sentence)
        return finished_task, user_sentence
    elif user_command == "description":
        print("AHHHH")
        finished_words = user_words[2:]
        finished_task = " ".join(finished_words)
        slot = user_words[1]
        print(description)
        return slot, finished_task
    else:
        return None


def scrub_index(sentence_value):
    split_sentence = sentence_value.split()
    remaining_sentence = split_sentence[1:]
    final_sentence = " ".join(remaining_sentence)
    return final_sentence


check_command()

    
