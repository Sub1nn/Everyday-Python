from datetime import datetime

def check_date():
    date_str = input("Enter a date in YYYY-MM-DD format:\n")
    try:
        # Attempt to create a datetime object with the provided date
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        print(f"{date_str} is a valid date.")
    except ValueError:
        # Handle invalid date format or non-existent dates
        print(f"{date_str} is not a valid date.")

# Run the function
check_date()
