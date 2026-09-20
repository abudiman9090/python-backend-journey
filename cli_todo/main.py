from todo import TodoManager
import storage

def show_menu():
    print("\n1. Add task")
    print("2. List tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Quit")

def main():
    manager = TodoManager()
    manager.tasks = storage.load()

    while True:
        show_menu()
        choice = input("Choose: ")

        if choice == "1":
            title = input("Task title: ")
            manager.add(title)
            storage.save(manager.tasks)
        elif choice == "2":
            for i, t in enumerate(manager.list_all()):
                print(f"{i}. {t}")
        elif choice == "3":
            i = int(input("Task number: "))
            if manager.complete(i):
                storage.save(manager.tasks)
        elif choice == "4":
            i = int(input("Task number: "))
            if manager.delete(i):
                storage.save(manager.tasks)
        elif choice == "5":
            print("Bye")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()