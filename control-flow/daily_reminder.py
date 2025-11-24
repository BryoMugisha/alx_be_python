print("=== Daily Reminder ===")

# Loop runs once but allows control flow demonstration
while True:
    task = input("Enter your task: ")
    priority = input("Enter priority level (high/medium/low): ").lower()
    time_sensitive = input("Is this task time-sensitive? (yes/no): ").lower()

    # Use match-case to respond based on priority
    match priority:
        case "high":
            priority_msg = "This is important! Handle it as soon as possible."
        case "medium":
            priority_msg = "This task can be done later today, but don't forget."
        case "low":
            priority_msg = "This is low priority, handle it when you have free time."
        case _:
            priority_msg = "Unknown priority level. Just do your best."

    # Time-sensitive message
    if time_sensitive == "yes":
        time_msg = "Since it's time-sensitive, schedule it immediately!"
    else:
        time_msg = "No rush — but keep it in mind."

    # Final customized reminder
    print("\n--- Your Reminder ---")
    print(f"Task: {task}")
    print(priority_msg)
    print(time_msg)

    # Break after one task to avoid storing multiple tasks
    break

print("\nReminder generated successfully!")
