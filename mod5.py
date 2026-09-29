tasks = ["Eating", "Study Python"]
completed = [False, False]


# Search Task
def search_task():
    search = input("Enter task to search: ")

    found = False

    for i in range(len(tasks)):
        if search in tasks[i]:
            print("Task found:", tasks[i])
            found = True

    if found == False:
        print("Task not found")


search_task()