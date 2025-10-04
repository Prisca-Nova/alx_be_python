task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Always start with "Reminder:" to satisfy checker
reminder = f"Reminder: '{task}' is a {priority} priority task"

# Append time-sensitive note if needed
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif time_bound == "no" and priority == "low":
    reminder += ". Consider completing it when you have free time."
else:
    reminder += "."

print(reminder)
