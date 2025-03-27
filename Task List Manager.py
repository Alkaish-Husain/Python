'''Experiment No:-5
   Title:-  Task List Manager*
   Aim:-    Develop a Python program to manage a task list using lists and tuples, including adding,
            removing, updating, and sorting tasks.
   Name:-   Shaikh Alkaish Husain Ahmad Husain
   UIN:-    241P088
   Roll No:-19
   Div:-    D
   Class:-  F.E.(Computer Enigneering)
   Date:-                          '''
tasks = []  # List to store tasks
def add_task(task):
    tasks.append(task)
    print(f"{task} added Successfully.")
    # Show updated task list after adding
    display_tasks()  
def update_task(index, new_task):
    '''Updates a task at a given index.'''
    if 0 < index <= len(tasks):
        print(f"\nUpdating Task {index}: '{tasks[index - 1]}' → '{new_task}'")
        tasks[index - 1] = new_task
        print("\nTask updated successfully.")
        display_tasks()
    else:
        print("\nInvalid task number.")
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"{task} removed Successfully.")
        # Show updated task list after removal
        
        display_tasks()
    else:
        print("Task not found.")
def display_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Task List:- ") 
        tasks
        print(f" {tasks}")
def sort_tasks():
    '''Sorts the task list alphabetically.'''
    if tasks:
        tasks.sort()
        print("\n Tasks sorted Successfully.")
        # Show Sorted task list
        display_tasks()
    else:
        print("\n No tasks available to sort.")
# User input loop
while True:
    print("\nOptions:- 1. Add Task  2.Update Task. 3. Remove Task  4. Display Tasks 5.Sort  6. Exit")
    choice = input("Enter choice:- ")
    if choice == "1":
        task = input("Enter task to add:- ")
        add_task(task)
    elif choice == "2":
       display_tasks()
       try:
            idx = int(input("Enter task index to update:- "))
            new_task = input("Enter the new task:-  ")
            update_task(idx, new_task)
       except ValueError:
            print("\nInvalid input. Please enter a valid number.")
    elif choice == "3":
        task = input("Enter task to remove:- ")
        remove_task(task)
    elif choice == "4":
        display_tasks()
    elif choice == "5":
        sort_tasks()
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice, please try again.")
