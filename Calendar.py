# To generate calendar of desired month using calendar module

import calendar


def main():
    year, month = get_year_month()
    print()
    print(calendar.month(year, month))


def get_year_month():
    while True:
        year = get_number("Enter year (e.g 2025): ")
        if not year > 0:
            print("Year should be greater than zero. Try again.")
            continue

        month = get_number("Enter month (1-12): ")
        if not 1 <= month <= 12:
            print("Month should be between 1-12. Try again.")
            continue

        return year, month


def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please input a number.")


if __name__ == "__main__":
    main()
