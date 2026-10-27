from datetime import date
import math


def get_valid_integer(prompt):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Input cannot be empty.")
            continue
        if not user_input.isdigit():
            print("Invalid input! Only numbers are allowed.")
            continue
        return int(user_input)


def get_valid_date(prompt):
    while True:
        user_input = input(prompt).strip()
        parts = user_input.split()
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            print(
                "Invalid format! Please enter as MM DD YYYY (e.g., 08 15 2026)."
            )
            continue
        try:
            month, day, year = map(int, parts)
            return date(year, month, day)
        except ValueError:
            print("Invalid date values! Please try again.")


def main():
    name = input("Enter your name: ").strip()
    while not name or not all(char.isalpha() or char.isspace() for char in name):
        print("Invalid input! Name must contain only letters and spaces.")
        name = input("Enter your name: ").strip()

    print(f"\nWelcome {name}\n")

    total_pages = get_valid_integer("How many pages does the book have? ")

    while True:
        pages_read = get_valid_integer("How many pages have you read? ")
        if pages_read <= total_pages:
            break
        print(f"Pages read cannot exceed total pages ({total_pages}).")

    print("\n--- Enter Dates (Format: MM DD YYYY) ---")
    issue_date = get_valid_date("Issue Date: ")

    while True:
        due_date = get_valid_date("Due Date: ")
        if due_date >= issue_date:
            break
        print("Due date cannot be before the issue date.")

    percentage_read = (pages_read / total_pages) * 100
    
    days_remaining = (due_date - issue_date).days
    pages_left = total_pages - pages_read

    if days_remaining > 0 and pages_left > 0:
        pages_per_day = math.ceil(pages_left / days_remaining)
    else:
        pages_per_day = 0

    print("\n-----------------------------------------")
    print("Message")
    print("-----------------------------------------")
    print(f"You have read {int(percentage_read)}% of the book.")

    if days_remaining >= 0:
        print(f"You have {days_remaining} day(s) remaining to return the book.")
    else:
        print(f"The book is OVERDUE by {abs(days_remaining)} day(s).")

    if pages_left > 0 and days_remaining > 0:
        print(
            f"You still have {pages_left} page(s) left and you should read {pages_per_day} pages a day."
        )
    elif pages_left <= 0:
        print("You have finished the book!")
    print("-----------------------------------------")


if __name__ == "__main__":
    main()
