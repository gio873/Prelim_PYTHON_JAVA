def run_program_2():
    while True:
        first_name = input("Enter first name (e.g., Maria): ").strip()
        if first_name and first_name.isalpha():
            break
        print("Invalid input! First name must contain only letters.")

    while True:
        last_name = input("Enter last name (e.g., Santos): ").strip()
        if last_name and last_name.isalpha():
            break
        print("Invalid input! Last name must contain only letters.")

    print(f"First name: {first_name}")
    print(f"Last name: {last_name}")

    full_name = first_name + " " + last_name
    print(f"Full name: {full_name}")

    print(f"First character: {full_name[0]}")
    print(f"Last character: {full_name[-1]}")

    try:
        first_name[0] = "D"
    except TypeError:
        print("Strings are immutable; individual characters")
        print("cannot be changed directly.")

    new_name = "D" + first_name[1:]
    print(f"New name: {new_name}")
    print(f"Original name: {first_name}")

    print("Characters in the full name:")
    for char in full_name:
        print(char)

    sliced_first = full_name[0:len(first_name)]
    sliced_last = full_name[len(first_name)+1:]
    print(f"Sliced first name: {sliced_first}")
    print(f"Sliced last name: {sliced_last}")

    while True:
        search_char = input("Enter one character to search: ")
        if len(search_char) == 1:
            break
            
    if search_char in full_name:
        index = full_name.find(search_char)
        print(f"Character found at index: {index}")
    else:
        print("Character not found.")

if __name__ == "__main__":
    run_program_2()
