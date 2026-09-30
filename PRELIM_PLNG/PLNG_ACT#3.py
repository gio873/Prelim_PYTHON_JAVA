number = int(input("Enter a multiple of 5 between 1 and 100: "))

if 1 <= number <= 100 and number % 5 == 0:
    print("Valid number! Thank you.")
else:
    print("Invalid number. It must be a multiple of 5 between 1 and 100.")
