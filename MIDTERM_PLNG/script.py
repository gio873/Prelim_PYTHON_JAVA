def run_program_1():
    print("\n--- RUNNING PROGRAM #1: Bytes and Bytearray ---")
    
    while True:
        message = input("Enter a message to encode (e.g., Hello Python): ").strip()
        if message and all(char.isalpha() or char.isspace() for char in message):
            break
        print("Invalid input! Please enter text containing only letters and spaces.")

    bytes_obj = message.encode('utf-8')
    print(f"1. Bytes object: {bytes_obj}")

    str_from_bytes = bytes_obj.decode('utf-8')
    print(f"2. Bytes to string: {str_from_bytes}")

    hex_str = bytes_obj.hex()
    print(f"3. Bytes to hex: {hex_str}")

    bytes_from_hex = bytes.fromhex(hex_str)
    print(f"4. Hex to bytes: {bytes_from_hex}")

    bytearray_direct = bytearray(message, 'utf-8')
    print(f"5. New bytearray: {bytearray_direct}")

    bytearray_from_bytes = bytearray(bytes_obj)
    print(f"6. Bytes to bytearray: {bytearray_from_bytes}")

    slice_start = message.find(" ") + 1 if " " in message else len(message) // 2
    sliced_bytes = bytes_obj[slice_start:]
    print(f"7. Sliced bytes: {sliced_bytes}")

    if len(bytearray_from_bytes) > 0:
        first_char = chr(bytearray_from_bytes[0])
        bytearray_from_bytes[0] = ord(first_char.lower())
    
    modified_message = bytearray_from_bytes.decode('utf-8')
    print(f"8. Modified message: {modified_message}")


def run_program_2():
    print("\n--- RUNNING PROGRAM #2: String Operations ---")
    
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
        full_name[0] = "D"
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


def main():
    while True:
        print("      MIDTERM LAB ACTIVITY # 3 MENU     ")
        print("==========================================")
        print("1. Run Program #1 (Bytes & Bytearray)")
        print("2. Run Program #2 (String Operations)")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            run_program_1()
        elif choice == '2':
            run_program_2()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
