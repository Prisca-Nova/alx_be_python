#!/usr/bin/env python3
"""
Personal Daily Reminder
A simplified Python script that uses conditional statements, Match Case, and loops
to remind the user about a single, priority task for the day based on time sensitivity.
"""

def main():
    # Prompt for a Single Task
    task = input("Enter your task: ")
    
    # Prompt for priority with validation loop
    while True:
        priority = input("Priority (high/medium/low): ").lower()
        if priority in ['high', 'medium', 'low']:
            break
        print("Please enter 'high', 'medium', or 'low'")
    
    # Prompt for time-bound with validation loop
    while True:
        time_bound = input("Is it time-bound? (yes/no): ").lower()
        if time_bound in ['yes', 'no']:
            break
        print("Please enter 'yes' or 'no'")
    
    # Process the Task Based on Priority and Time Sensitivity
    print()  # Empty line for better output formatting
    
    # Use Match Case statement to react differently based on priority
    match priority:
        case 'high':
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{task}' is a high priority task. Focus on this when possible.")
        
        case 'medium':
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a medium priority task that should be completed today!")
            else:
                print(f"Reminder: '{task}' is a medium priority task. Schedule time for this soon.")
        
        case 'low':
            if time_bound == 'yes':
                print(f"Reminder: '{task}' is a low priority task that needs completion today.")
            else:
                print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")

if __name__ == "__main__":
    main()