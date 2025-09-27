def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # dynamic list to store items

    while True:
        display_menu()  # call display_menu
        try:
            choice = int(input("Enter your choice: "))  # numeric input
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 4.")
            continue

        if choice == 1:  # add item
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print("'" + item + "' has been added to the shopping list.")
        elif choice == 2:  # remove item
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print("'" + item + "' has been removed from the shopping list.")
            else:
                print("'" + item + "' not found in the shopping list.")
        elif choice == 3:  # view list
            if shopping_list:
                print("Current Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(str(idx) + ". " + item)
            else:
                print("Shopping list is empty.")
        elif choice == 4:  # exit
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 4.")

if __name__ == "__main__":
    main()

