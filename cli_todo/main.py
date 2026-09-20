def show_menu():
    print("\n1. Add task")
    print("2. List tasks")
    print("3. Quit")

def main():
    while True:
        show_menu()
        choice = input("Choose: ")
        if choice == "3":
            print("Bye")
            break
if __name__ == "__main__":
    main()