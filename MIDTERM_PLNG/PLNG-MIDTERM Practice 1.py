def main():
    while True:
        print("\nChoose the program you want to run")
        print("Program #1")
        print("Program #2")
        print("Program #3")
        print("Program #4")
        print("Program #5")
        print("Program #6")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            print("\n--- Running Program #1 ---")
            arr = []
            print("Enter 10 real numbers (negative and positive):")
            for i in range(10):
                while True:
                    try:
                        num = float(input(f"Element {i+1}: "))
                        arr.append(num)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a real number.")
            
            pos_sum = 0
            pos_count = 0
            for num in arr:
                if num > 0:
                    pos_sum += num
                    pos_count += 1
            
            if pos_count > 0:
                pos_avg = pos_sum / pos_count
                print(f"Sum of positive numbers: {pos_sum}")
                print(f"Average of positive numbers: {pos_avg}")
            else:
                print("No positive numbers entered, so sum and average cannot be calculated.")
            
            neg_count = 0
            for num in arr:
                if num < 0:
                    neg_count += 1
            print(f"Count of negative numbers: {neg_count}")
            
            if len(arr) > 0:
                min_val = arr[0]
                for num in arr:
                    if num < min_val:
                        min_val = num
                print(f"Minimum value of the array: {min_val}")

        elif choice == '2':
            print("\n--- Running Program #2 ---")
            arr = []
            print("Enter 8 integer numbers:")
            for i in range(8):
                while True:
                    try:
                        num = int(input(f"Element {i+1}: "))
                        arr.append(num)
                        break
                    except ValueError:
                        print("Invalid input. Please enter an integer.")
            
            unique_arr = []
            for num in arr:
                if num not in unique_arr:
                    unique_arr.append(num)
            print(f"Array after removing duplicates: {unique_arr}")
            
            sorted_unique = sorted(unique_arr)
            
            if len(sorted_unique) >= 2:
                print(f"Second largest element: {sorted_unique[-2]}")
            else:
                print("Second largest element does not exist (not enough unique values).")
                
            if len(sorted_unique) >= 2:
                print(f"Second smallest element: {sorted_unique[1]}")
            else:
                print("Second smallest element does not exist (not enough unique values).")

        elif choice == '3':
            print("\nOUTPUT")
            raw_input = input("Enter Data in Array: ")
            arr = [int(x) for x in raw_input.split()]
            
            print("Stored Data in Array:", " ".join(map(str, arr)))
            
            try:
                pos = int(input("Enter poss. of Element to Delete: "))
                if 0 <= pos < len(arr):
                    del arr[pos]
                    print("New data in Array:", " ".join(map(str, arr)))
                else:
                    print(f"Position {pos} is out of bounds for the current array.")
            except ValueError:
                print("Invalid input for position.")

        elif choice == '4':
            print("\nOUTPUT:")
            try:
                size = int(input("Enter Size of Array : "))
                raw_input = input(f"Enter any {size} elements in Array: ")
                arr = [int(x) for x in raw_input.split()][:size]
                
                evens = [str(x) for x in arr if x % 2 == 0]
                odds = [str(x) for x in arr if x % 2 != 0]
                
                print("Even Elements:", " ".join(evens))
                print("Odd Elements:", " ".join(odds))
            except ValueError:
                print("Please enter numeric inputs.")

        elif choice == '5':
            print("\nOUTPUT :")
            print("*")
            print("*A*")
            print("*A*A*")
            print("*A*A*A*")

        elif choice == '6':
            print("\n--- Running Program #6 ---")
            basic_salary = 12000
            da = 0.12 * basic_salary
            hra = 150
            ta = 120
            others = 450
            pf = 0.14 * basic_salary
            it = 0.15 * basic_salary
            
            net_salary = (basic_salary + da + hra + ta + others) - (pf + it)
            
            print(f"Basic Salary : ${basic_salary}")
            print(f"DA           : ${da:.2f}")
            print(f"HRA          : ${hra}")
            print(f"TA           : ${ta}")
            print(f"Others       : ${others}")
            print(f"PF Tax Cut   : ${pf:.2f}")
            print(f"IT Tax Cut   : ${it:.2f}")
            print(f"------------------------")
            print(f"Net Salary   : ${net_salary:.2f}")

        else:
            print("Invalid choice! Please select a valid number from 1 to 6.")
            continue

        cont = input("\nDo you want to continue ? Y/N: ").strip().upper()
        if cont != 'Y':
            print("Exiting Menu. Goodbye!")
            break

if __name__ == "__main__":
    main()
