from datetime import datetime, timedelta

def identify_time_components():
    date_str = input("Enter the date and time in the format 'dd.mm.yyyy hh:mm':\n")
    try:
        date_obj = datetime.strptime(date_str, "%d.%m.%Y %H:%M")
        print(f"You gave year {date_obj.year}")
        print(f"You gave month {date_obj.month}")
        print(f"You gave day {date_obj.day}")
        print(f"You gave hour {date_obj.hour}")
        print(f"You gave minute {date_obj.minute}\n")
    except ValueError:
        print("Incorrect format. Please follow 'dd.mm.yyyy hh:mm' format.")

def calculate_age_in_days():
    dob_str = input("Enter your birthday as dd.mm.yyyy:\n")
    try:
        dob = datetime.strptime(dob_str, "%d.%m.%Y")
        start_of_year = datetime(2024, 1, 1)
        age_in_days = (start_of_year - dob).days
        print(f"On January 1, 2024, you were {age_in_days} days old.\n")
    except ValueError:
        print("Incorrect format. Please use 'dd.mm.yyyy' format.")

def print_days_of_week():
    monday_date = datetime.strptime("01.01.2024", "%d.%m.%Y")  # Assuming any Monday date
    for _ in range(7):
        print(monday_date.strftime("%A"))
        monday_date += timedelta(days=1)
    print("")

def print_months():
    month_date = datetime(2024, 1, 1)
    for _ in range(12):
        print(month_date.strftime("%b"))
        month_date += timedelta(days=31)
        month_date = month_date.replace(day=1)
    print("")

def main():
    print("This program uses the datetime library to deal with time.")
    while True:
        print("What do you want to do:")
        print("1) Identify the components of a time object")
        print("2) Calculate age in days")
        print("3) Print the days of the week")
        print("4) Print the months")
        print("0) Stop")
        choice = input("Your choice:\n")

        if choice == "1":
            identify_time_components()
        elif choice == "2":
            calculate_age_in_days()
        elif choice == "3":
            print_days_of_week()
        elif choice == "4":
            print_months()
        elif choice == "0":
            print("See you again!")
            break
        else:
            print("Unknown choice, please try again.\n")

# Run the main function
main()
