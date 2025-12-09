# Calculates minutes between current date and specified date

# Import necessary Modules
from datetime import date
from re import search
from sys import exit
import inflect
p = inflect.engine()


def validate_date(date_str):
    # Valid Date format YY-MM-DD
    match = search(r"^(?P<year>\d{4})-(?P<month>0[1-9]|1[0-2])-(?P<day>0[1-9]|1[0-9]|2[0-9]|3[0-1])$", date_str)

    if not match:
        print("Invalid Date.")
        exit(1)

    year = int(match.group("year"))
    month = int(match.group("month"))
    day = int(match.group("day"))

    try:
        input_date = date(year, month, day)
        return input_date

    except ValueError:
        print("Invalid Date.")
        exit(1)


def calculate_minutes(valid_date):
    today_date = date.today()

    days_difference = today_date - valid_date

    days = days_difference.days

    minutes = days * 24 * 60

    return round(minutes)


minutes = calculate_minutes(validate_date(input("Enter date (YY-MM-DD): ")))
print(f"{p.number_to_words(minutes, andword="").capitalize()} minutes")
