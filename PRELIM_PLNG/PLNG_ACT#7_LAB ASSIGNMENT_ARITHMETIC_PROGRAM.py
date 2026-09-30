def calculator(x, y, operation):

    print("ARITHMETIC CALCULATOR")
    print("1. Addition  2. Subtraction  3. Multiplication ")
    print("4. Division  5. Modulus 6. Increment")
    print("7. Decrement\n")

    selected_operation = input("Select an operation (1-7): ")
    x = float(input("Enter the value of x: "))
    y = float(input("Enter the value of y: "))

    op_name, result = perform_operation(x, y, selected_operation)

    print(f"Variables Values: x = {x}, y = {y}, operation = {selected_operation}")
    print(f"{op_name}: {x} {get_operator_symbol(selected_operation)} {y} = {result}")

    choice = input("Do you want to continue? (YES/NO): ").strip().upper()
    if choice == 'YES' or choice == 'Y':
        calculator(x, y, selected_operation)
    elif choice == 'NO' or choice == 'N':
        print("Thank you for using the calculator.")

def get_operator_symbol(operation):
    symbols = {
        '1': '+',
        '2': '-',
        '3': '*',
        '4': '/',
        '5': '%',
        '6': '+1',
        '7': '-1'
    }
    return symbols.get(operation, '?')

def perform_operation(x, y, operation):
    if operation == '1':
        return "Addition", x + y
    elif operation == '2':
        return "Subtraction", x - y
    elif operation == '3':
        return "Multiplication", x * y
    elif operation == '4':
        if y != 0:
            return "Division", x / y
        else:
            return "Division", "Error: Division by zero is not allowed."
    elif operation == '5':
        return "Modulus", x % y
    elif operation == '6':
        return "Increment", x + 1
    elif operation == '7':
        return "Decrement", x - 1
    else:
        return "Invalid operation.", "N/A"

calculator(0, 0, None)
