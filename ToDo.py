def display_menu():
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Exit")
   # choice = input("Choose an option (1-4):")

def add_task(tasks):
    task = input("Enter a new task:")
    tasks.append({'desc': task, 'completed': False})
    print(f"Task '{task}' added succesfully !")

def view_tasks(tasks):
    print("\n To-Do:")
    for i, task in enumerate(tasks, 1):
        status = "Done" if task['completed'] else "Pending"
        print(f"{i}.{task['desc']} - [{status}]")

def task_done(tasks):
    view_tasks(tasks)
    i = int(input("Enter the number of the completed task:")) - 1
    if 0 <= i < len(tasks):
        tasks[i]['completed'] = True
        print(f"Task '{tasks[i]['desc']}' marked as completed !")
    else:
        print("Invalid task number !")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option from 1 - 4\n")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            task_done(tasks)
        elif choice == '4':
            print("Goodbye !")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
