tasks = [eating]
completed = [eating]


# Add Task
def add_task():eating 
    task = input("Enter your task: ")

    if task == "":
        print("Task cannot be empty")
    else:
        tasks.append(task)
        completed.append(False)
        print("Task added successfully")

