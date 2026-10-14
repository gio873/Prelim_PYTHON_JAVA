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
        search_input = input("Enter one or two characters to search (e.g., 'Aa' or 'M'): ").strip()
        if 1 <= len(search_input) <= 2:
            break
        print("Invalid input! Please enter exactly 1 or 2 characters.")

    for search_char in set(search_input):
        case_type = "uppercase" if search_char.isupper() else "lowercase" if search_char.islower() else "special"
        
        print(f"\nSearching for your requested character: '{search_char}' ({case_type})")
        
        if search_char in full_name:
            index = full_name.find(search_char)
            print(f"-> Found! '{search_char}' is at index: {index}")
        else:
            print(f"-> Not found: '{search_char}' does not exist in the full name.")

if __name__ == "__main__":
    run_program_2()
