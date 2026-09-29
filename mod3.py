def complete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    number = int(input("Enter task number: "))

    if number >= 1 and number <= len(tasks):
        completed[number - 1] = True
        print("Task completed")
    else:
        print("Invalid task number")
complete_task()