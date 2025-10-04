# Prompt user for input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Use match case to react based on priority
match priority:
    case "high" | "medium":
        reminder = f"Reminder: '{task}' is a {priority} priority task"
        # Use if statement to handle time-bound tasks
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += "."
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
        if time_bound == "no":
            reminder += ". Consider completing it when you have free time."
        else:
            reminder += "."
    case _:
        reminder = f"Note: '{task}' has an undefined priority."

# Print the customized reminder
print(reminder)
