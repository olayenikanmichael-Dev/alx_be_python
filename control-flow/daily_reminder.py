task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case for priority
match priority:
    case "high":
        message = f"'{task}' is a high priority task"
    case "medium":
        message = f"'{task}' is a medium priority task"
    case "low":
        message = f"'{task}' is a low priority task"
    case _:
        message = f"'{task}' has an unknown priority"

# Time-bound condition
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."

# REQUIRED print line
print(f"Reminder: {message}")
