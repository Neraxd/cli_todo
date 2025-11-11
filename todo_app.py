todo_data = {}

print("Welcome to your todo app! ")


# adding a new item to the todo list


def add_task():
    """Adding item to the todo_data variable.

    handling already existing items.
    """
    name = input("Please enter the name of the task: ")
    for item in todo_data:
        if name in item:
            print(f"item {name} already exists")
            return

    status = input(
        "Please enter the sattus of the task: Unchecked(U)/Checked(C)/In Progress(I) "
    ).lower()

    if status in ["u", "unchecked"]:
        status = "Unchecked"
    elif status in ["c", "checked"]:
        status = "Checked"
    elif status in ["i", "in progress"]:
        status = "In progress"
    else:
        print("Invalid input! Defaulting to 'Unchecked'.")
        status = "Unchecked"
    todo_data[name] = status


# Removing item from the todo list


def remove_task():
    """Removing item from the todo_data variable.

    handling underfllow, assertion error.
    """
    if not todo_data:
        print("Cannot remove! the list is empty!")
        return

    print("\nWhich task do you want to change? 1 through n : ")
    display_list()
    item = input("Enter the number : ")
    current_choice = display_list(choice=int(item))

    if current_choice in todo_data:
        todo_data.pop(current_choice, None)
        display_list()
    else:
        print("Could not find the item you want! ")


# Edit a task from the todo list
def edit_task():
    """Edit a task from the todo_data variable.

    handling thhe edition of tasks
    """
    if not todo_data:
        print("Cannot edit! the list is empty!")

    print("Which task do you want to delete? 1 through n : ")
    display_list()
    number = input("Enter the number : ")
    current_choice = display_list(choice=int(number))

    if current_choice in todo_data:
        status = input(
            f"you are editing {current_choice}: Unchecked(U)/Checked(C)/In Progress(I)"
        ).lower()

        if status in ["u", "unchecked"]:
            status = "Unchecked"
        elif status in ["c", "checked"]:
            status = "Checked"
        elif status in ["i", "in progress"]:
            status = "In progress"
        else:
            print("Invalid input! Defaulting to 'Unchecked'.")
            status = "Unchecked"
        todo_data[current_choice] = status


# Display current items


def display_list(choice=0):
    """Display the todo list.

    returns a value if the optional keyword arg is provided
    """
    print("====== todo list =======")
    if todo_data:
        for i, (todo_key, todo_value) in enumerate(todo_data.items(), 1):
            if int(choice) == i and choice != 0:
                return todo_key.lower()
            print(f"{i}. {todo_key.title()} : {todo_value.title()}")
    else:
        print("\nThe list is empty! ")


# Main entry of the program

while True:
    choice = int(
        input(
            "\nwhat do you want to do now?\n1.Add a new task\n2.Remove a task\n3.Edit a task\n4.View list\n5.Exit\n>>> "
        )
    )
    match choice:
        case 1:
            add_task()

        case 2:
            remove_task()
        case 3:
            edit_task()
        case 4:
            display_list()
        case 5:
            exit_confirmation = input("Are you sure you want to exit? (Y/N): ").lower()
            if exit_confirmation == "y":
                print("Exiting the todo app. Goodbye!")
                break
            else:
                print("Continuing...")
        case _:
            print("your choice is invalid! ")
