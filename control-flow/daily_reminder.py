
# Prompt for a single task
task = input("Please enter a task description: ")
priority = input(
    "What is the priority of the task (high, medium, low)? ").lower()
time_bound = input("Is the task time-sensitive? (yes or no): ").lower()

# Initialize the reminder message
reminder = f"Reminder: You have a task '{task}' with priority '{priority}'."

# Process the task based on priority
match priority:
    case "high":
        reminder += " This is a high-priority task."
    case "medium":
        reminder += " This is a medium-priority task."
    case "low":
        reminder += " This is a low-priority task."
    case _:
        reminder += " Priority not recognized."

# Modify the reminder if the task is time-sensitive
if time_bound == "yes":
    reminder += " This requires immediate attention today!"
elif time_bound == "no":
    reminder += " This does not require immediate attention."

# Print the customized reminder
print(reminder)
