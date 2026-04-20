tasks = []
while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available")
        else:
            for t in tasks:
                print("-", t)

    elif choice == "3":
        break
    else:
        print("Invalid choice")
