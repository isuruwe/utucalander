import json
from datetime import datetime, timedelta

calendar_file = 'calendar.json'

def load_calendar():
    try:
        with open(calendar_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_calendar(calendar):
    with open(calendar_file, 'w') as file:
        json.dump(calendar, file)

def display_calendar(year, month):
    print(f"Calendar for {year}-{month:02}")
    for day in range(1, 32):
        try:
            date = datetime(year, month, day)
            print(f"{day:02}: {calendar.get(date.strftime('%Y-%m-%d'), '')}")
        except ValueError:
            break

def add_reminder(year, month, day, reminder):
    date_str = f"{year}-{month:02}-{day:02}"
    if date_str not in calendar:
        calendar[date_str] = []
    calendar[date_str].append(reminder)
    save_calendar(calendar)
    print(f"Reminder added for {date_str}")

def show_daily_reminders():
    today = datetime.now().strftime('%Y-%m-%d')
    reminders = calendar.get(today, [])
    print(f"Reminders for today ({today}):")
    for reminder in reminders:
        print(f"- {reminder}")

if __name__ == '__main__':
    calendar = load_calendar()
    while True:
        print("1. Display calendar")
        print("2. Add reminder")
        print("3. Show daily reminders")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            year = int(input("Enter year: "))
            month = int(input("Enter month: "))
            display_calendar(year, month)
        elif choice == '2':
            year = int(input("Enter year: "))
            month = int(input("Enter month: "))
            day = int(input("Enter day: "))
            reminder = input("Enter reminder: ")
            add_reminder(year, month, day, reminder)
        elif choice == '3':
            show_daily_reminders()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")
