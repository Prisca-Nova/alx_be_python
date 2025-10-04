task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Prepare reminder message
if priority == "high":
    message = f"Reminder: '{task}' is a high priority task"
elif priority == "medium":
    message = f"Reminder: '{task}' is a medium priority task"
elif priority == "low":
    message = f"Reminder: '{task}' is a low priority task"
else:
    message = f"Reminder: '{task}' has an undefined priority"

# Append time-bound note
if time_bound == "yes" and priority in ["high", "medium", "low"]:
    message += " that requires immediate attention today!"
elif time_bound == "no" and priority == "low":
    message += ". Consider completing it when you have free time."
else:
    message += "."

print(message)
