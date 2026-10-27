def run_program_one(task):
    msg = "Hello Python"
    if task == "1":
        b_obj = msg.encode("utf-8")
        print(b_obj)
    elif task == "2":
        b_obj = msg.encode("utf-8")
        print(b_obj.decode("utf-8"))
    elif task == "3":
        b_obj = msg.encode("utf-8")
        print(b_obj.hex())
    elif task == "4":
        hex_str = "48656c6c6f20507974686f6e"
        print(bytes.fromhex(hex_str))
    elif task == "5":
        print(bytearray("Hello Python", "utf-8"))
    elif task == "6":
        b_obj = msg.encode("utf-8")
        print(bytearray(b_obj))
    elif task == "7":
        b_obj = msg.encode("utf-8")
        print(b_obj[6:])
    elif task == "8":
        b_obj = msg.encode("utf-8")
        ba = bytearray(b_obj)
        ba[0] = ord('h')
        print(ba.decode("utf-8"))
    else:
        print("Invalid")

def run_program_two(task):
    first_name = "Maria"
    last_name = "Santos"
    full_name = first_name + " " + last_name
    if task == "1":
        print("First name:", first_name)
        print("Last name:", last_name)
    elif task == "2":
        print("Full name:", full_name)
    elif task == "3":
        print("First character:", first_name[0])
        print("Last character:", last_name[-1])
    elif task == "4":
        try:
            first_name[0] = "D"
        except TypeError:
            print("Strings are immutable; individual characters cannot be changed directly.")
    elif task == "5":
        new_name = "D" + first_name[1:]
        print("New name:", new_name)
        print("Original name:", first_name)
    elif task == "6":
        print("Characters in the full name:")
        for char in full_name:
            print(char)
    elif task == "7":
        print("Sliced first name:", full_name[0:5])
        print("Sliced last name:", full_name[6:])
    elif task == "8":
        while True:
            char_input = input("Enter one character to search: ")
            if len(char_input) == 1:
                if char_input in full_name:
                    print("Character found at index:", full_name.find(char_input))
                else:
                    print("Character not found.")
                break
            else:
                print("Invalid")
    else:
        print("Invalid")

while True:
    prog = input("Enter program number (1 for Bytes/Bytearray, 2 for Strings, or 'q' to quit): ")
    if prog == 'q':
        break
    if prog not in ["1", "2"]:
        print("Invalid")
        continue
    
    task = input("Enter task number (1 to 8): ")
    if task not in [str(i) for i in range(1, 9)]:
        print("Invalid")
        continue
    
    if prog == "1":
        run_program_one(task)
    elif prog == "2":
        run_program_two(task)