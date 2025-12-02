from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    now = datetime.now()
    
    # Save current date
    current_date = now.date()
    
    # Format date and time as a readable string
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current Date: {current_date}")
    print(f"Current Date and Time: {formatted_datetime}")

# Call the function
display_current_datetime()

def calculate_future_date(days: int):
    # Get current date
    today = datetime.now().date()
    
    # Calculate future date
    future_date = today + timedelta(days=days)
    
    # Print future date in YYYY-MM-DD format
    print(f"Future Date after {days} days: {future_date}")

# Prompt user for number of days
try:
    num_days = int(input("Enter the number of days: "))
    calculate_future_date(num_days)
except ValueError:
    print("Invalid input. Please enter an integer.")
