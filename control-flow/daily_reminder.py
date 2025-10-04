# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process priority using match-case
match priority:
    case "high" | "medium":
        reminder = f"Reminder: '{task}' is a {priority} priority task"
        # Modify reminder based on time-bound
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

# Print a blank line before the reminder to match expected output
print("\n" + reminder)
