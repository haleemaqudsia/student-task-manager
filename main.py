from task_manager import TaskManager

manager = TaskManager()

while True:
    print("\n===== STUDENT TASK MANAGER =====")
    print("1. Add Task")
    print("2. Display Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter task title: ")
        manager.add_task(title)
        print("Task added successfully!")

    elif choice == "2":
        tasks = manager.display_tasks()

        if not tasks:
            print("No tasks available.")
        else:
            for task in tasks:
                status = "Completed" if task["completed"] else "Pending"
                print(f'{task["id"]}. {task["title"]} - {status}')

    elif choice == "3":
    try:
        task_id = int(input("Enter task ID: "))

        if manager.complete_task(task_id):
            print("Task completed successfully!")
        else:
            print("Invalid ID, task not found, or task already completed.")

    except ValueError:
        print("Please enter a valid numeric task ID.")

    elif choice == "4":
        task_id = int(input("Enter task ID: "))
        if manager.delete_task(task_id):
            print("Task deleted successfully!")
        else:
            print("Task not found.")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
