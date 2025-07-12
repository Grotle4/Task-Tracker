Hello, this Task Tracker programs functions off a simple command line interface. Anything in quotations is meant to be ignored when running commands, ex. add buy groceries

The list of available commands are:
add "Task you want to add here" - adds a task to the list with an id value starting at 1, each new task has a new id number going up from 1
update "task ID number" "Updated task" - will update the task selected with a new task
delete "task ID number" - will remove the task from list and update all id numbers
description "task ID number" "Description of task" - provides a description of the task specified
mark in progress "task ID number" - will mark task as in progress
mark done "task ID number" - will mark task as done
mark todo "task ID number" - will mark task as todo
list - shows all list items, their id numbers and their descriptions
list done - shows all list items that are done
list todo - shows all list items that need to be done
list in progress - show all list items in progress
export - exports all data of tasks to a JSON file
stop - ends the program.
