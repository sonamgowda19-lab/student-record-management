def show_menu():
    print("\nStudent Record Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Add Student feature coming soon...")
        elif choice == "2":
            print("View Students feature coming soon...")
        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
