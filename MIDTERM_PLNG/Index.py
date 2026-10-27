from datetime import datetime

def get_name():
    while True:
        val = input("Enter your name: ").strip()
        if val and val.replace(" ", "").isalpha():
            return val
        print("invalid")

def get_positive_int(prompt):
    while True:
        val = input(prompt)
        try:
            num = int(val)
            if num > 0:
                return num
        except ValueError:
            pass
        print("invalid")

def get_pages_read(prompt, total_pages):
    while True:
        val = input(prompt)
        try:
            num = int(val)
            if 0 <= num <= total_pages:
                return num
        except ValueError:
            pass
        print("invalid")

def get_date(prompt):
    while True:
        val = input(prompt)
        try:
            d = datetime.strptime(val, "%Y-%m-%d").date()
            return d
        except ValueError:
            print("invalid")

name = get_name()
print("Welcome", name)

total_pages = get_positive_int("How many pages does the book have? ")
pages_read = get_pages_read("How many pages have you read? ", total_pages)

issue_date = get_date("Enter Issue Date (YYYY-MM-DD): ")
while True:
    due_date = get_date("Enter Due Date (YYYY-MM-DD): ")
    if due_date >= issue_date:
        break
    print("invalid")

today = datetime.now().date()
days_remaining = (due_date - today).days
if days_remaining < 0:
    days_remaining = 0

percentage = (pages_read / total_pages) * 100
remaining_pages = total_pages - pages_read

if days_remaining > 0:
    pages_per_day = round(remaining_pages / days_remaining)
else:
    pages_per_day = remaining_pages

print(f"You have read {percentage:.0f}% of the book.")
print(f"You have {days_remaining} day(s) remaining to return the book.")
print(f"You still have {remaining_pages} page(s) left and you should read {pages_per_day} pages a day")