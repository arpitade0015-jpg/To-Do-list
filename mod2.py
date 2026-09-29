tasks = ["Eating"]
completed = [False]
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
view_tasks()