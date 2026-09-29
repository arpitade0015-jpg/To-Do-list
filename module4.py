tasks = ["Eating", "Study Python"]
completed = [False, False]


def view_tasks():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        print("\n----- YOUR TASKS -----")

        for i in range(len(tasks)):
            if completed[i] == True:
                print(i + 1, tasks[i], "- Completed")
            else:
                print(i + 1, tasks[i], "- Pending")


def delete_task():
    view_tasks()

    if len(tasks) == 0:
        return

    number = int(input("Enter task number: "))

    if number >= 1 and number <= len(tasks):
        print("Deleted task:", tasks[number - 1])

        tasks.pop(number - 1)
        completed.pop(number - 1)
    else:
        print("Invalid task number")


delete_task()