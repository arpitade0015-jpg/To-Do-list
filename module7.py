# Main Menu

def add_task():
    print("Add Task selected")


def view_tasks():
    print("View Tasks selected")


def complete_task():
    print("Complete Task selected")


def delete_task():
    print("Delete Task selected")


def search_task():
    print("Search Task selected")


def exit_program():
    print("Thank you for using To-Do List")


while True:

    print("\n----- TO-DO LIST -----")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Task")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        complete_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        search_task()

    elif choice == "6":
        exit_program()
        break

    else:
        print("Invalid choice")