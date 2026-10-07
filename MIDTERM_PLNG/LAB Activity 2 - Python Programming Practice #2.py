import datetime
import math
import random

print("--- Python Practice Programs 1 to 30 ---")
choice = input("Enter the program number you want to run (1-30): ")

if choice == "1":
    print("\n[Program 1] This program prints a basic 'Hello World!' greeting.")
    print("Hello World!")

elif choice == "2":
    print(
        "\n[Program 2] This program asks for your name and greets you personally."
    )
    usertext = input("What is your name? ")
    print("Hello", usertext)

elif choice == "3":
    print(
        "\n[Program 3] This program takes two numbers and calculates their sum."
    )
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    sum_result = float(num1) + float(num2)
    print("The sum of {0} and {1} is {2}".format(num1, num2, sum_result))

elif choice == "4":
    print(
        "\n[Program 4] This program takes two integers and calculates their average."
    )
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")
    average = (int(num1) + int(num2)) / 2
    print("average: {0}".format(average))

elif choice == "5":
    print(
        "\n[Program 5] This program calculates a weighted academic average using a visa grade (30%) and a final grade (70%)."
    )
    visagrade = input("enter your visa grade : ")
    finalgrade = input("enter your final grade : ")
    average = (float(visagrade) * 0.3) + (float(finalgrade) * 0.7)
    print("average :{0} ".format(average))

elif choice == "6":
    print(
        "\n[Program 6] This program calculates the average score of three exam inputs."
    )
    firstexam = input("your first exam : ")
    secondexam = input("your second exam : ")
    thirdexam = input("your third exam : ")
    average = (float(firstexam) + float(secondexam) + float(thirdexam)) / 3
    print("average :{0} ".format(average))

elif choice == "7":
    print(
        "\n[Program 7] This program determines if a student passed or failed based on an average threshold of 50."
    )
    average = input("enter average : ")
    if int(average) >= 50:
        print("Passed")
    else:
        print("Failed")

elif choice == "8":
    print(
        "\n[Program 8] This program checks whether an entered integer is odd or even."
    )
    num = int(input("Enter a number: "))
    if (num % 2) == 0:
        print("{0} is Even".format(num))
    else:
        print("{0} is Odd".format(num))

elif choice == "9":
    print(
        "\n[Program 9] This program checks whether a given number is positive, negative, or zero."
    )
    num = float(input("Enter a number: "))
    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")

elif choice == "10":
    print(
        "\n[Program 10] This program calculates Body Mass Index (BMI) and classifies your weight category status."
    )
    print("body mass index calculation program")
    height = float(input("enter height (m): "))
    weight = int(input("enter weight (kg): "))
    index = weight / (height * height)
    if index <= 18:
        print("\n underweight BMI:{}".format(index))
    elif index > 18 and index <= 25:
        print("\n normal weight BMI:{}".format(index))
    elif index > 25 and index <= 30:
        print("\n obese BMI:{}".format(index))
    elif index > 30:
        print("\n severely obese BMI:{}".format(index))

elif choice == "11":
    print(
        "\n[Program 11] This program checks if a person is old enough (18+) to be eligible for a driver's license."
    )
    age = input("enter age : ")
    if int(age) < 18:
        print("Your Age Is Not Eligible To Get A Driver's License")
    else:
        print("Your Age Is Eligible To Get Your License")

elif choice == "12":
    print(
        "\n[Program 12] This program uses a loop to display numbers sequentially from 1 to 100."
    )
    for i in range(1, 101):
        print(i)

elif choice == "13":
    print(
        "\n[Program 13] This program loops from 1 to 100 and prints only the even numbers."
    )
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)

elif choice == "14":
    print(
        "\n[Program 14] This program loops from 1 to 100 and prints only the odd numbers."
    )
    for i in range(1, 101):
        if i % 2 != 0:
            print(i)

elif choice == "15":
    print(
        "\n[Program 15] This program filters and prints numbers from 1 to 100 that are divisible by either 3 or 5."
    )
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0:
            print(i)

elif choice == "16":
    print(
        "\n[Program 16] This program requests an integer limit and prints all numbers from 1 up to that value."
    )
    num = input("enter number : ")
    for i in range(1, int(num) + 1):
        print(i)

elif choice == "17":
    print(
        "\n[Program 17] This program computes both the area and geometric perimeter of a rectangle."
    )
    short = input("Enter short side : ")
    tall = input("Enter tall side : ")
    area = int(short) * int(tall)
    perimeter = 2 * (int(short) + int(tall))
    print("area: {0}".format(area))
    print("perimeter: {0}".format(perimeter))

elif choice == "18":
    print(
        "\n[Program 18] This program loops through a predefined word and prints each of its characters line-by-line."
    )
    word = "mrhuseyin"
    for char in word:
        print(char)

elif choice == "19":
    print(
        "\n[Program 19] This program sums all the integer elements located between two user-defined number boundaries."
    )
    sumofnumbers = 0
    num1 = input("first number: ")
    num2 = input("second number: ")
    for i in range(int(num1) + 1, int(num2)):
        sumofnumbers += i
    print(
        "Sum of numbers between {0} and {1} : {2}".format(
            num1, num2, sumofnumbers
        )
    )

elif choice == "20":
    print(
        "\n[Program 20] This program calculates the entry fee for an activity and applies a 50% discount if you are a student."
    )
    selection = input("Press (1) for Cinema, (2) for Theater : ")
    student = input("Are you student(Y/N) : ")
    price = 0
    if selection == "1":
        price = 10
    elif selection == "2":
        price = 5
    if student == "Y" or student == "y":
        price = price / 2
    print(" The fee you have to pay :{}".format(price))

elif choice == "21":
    print(
        "\n[Program 21] This program verifies if a given integer qualifies as a prime number."
    )
    num = int(input("Enter a number: "))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                print(i, "times", num // i, "is", num)
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

elif choice == "22":
    print(
        "\n[Program 22] This program takes a list of integers and separately accumulates the sums of all even and odd values."
    )
    NumList = []
    Even_Sum = 0
    Odd_Sum = 0
    Number = int(input("Please enter the Total Number of List Elements: "))
    for i in range(1, Number + 1):
        value = int(input("Please enter the Value of %d Element : " % i))
        NumList.append(value)
    for j in range(Number):
        if NumList[j] % 2 == 0:
            Even_Sum = Even_Sum + NumList[j]
        else:
            Odd_Sum = Odd_Sum + NumList[j]
    print("\nThe Sum of Even Numbers in this List = ", Even_Sum)
    print("The Sum of Odd Numbers in this List = ", Odd_Sum)

elif choice == "23":
    print(
        "\n[Program 23] This program computes an updated salary based on a base payment rate and percentage raise value."
    )
    salary = input("enter current salary : ")
    raise_rate = input("salary raise rate(%) : ")
    newsalary = int(salary) + (int(salary) * int(raise_rate) / 100)
    print("increased salary :", newsalary)

elif choice == "24":
    print(
        "\n[Program 24] This program utilizes dedicated geometry formulas to calculate circle diameter, circumference, and area."
    )

    def find_Diameter(radius):
        return 2 * radius

    def find_Circumference(radius):
        return 2 * math.pi * radius

    def find_Area(radius):
        return math.pi * radius * radius

    r = float(input(" Please Enter the radius of a circle: "))
    print("\n Diameter Of a Circle = %.2f" % find_Diameter(r))
    print(" Circumference Of a Circle = %.2f" % find_Circumference(r))
    print(" Area Of a Circle = %.2f" % find_Area(r))

elif choice == "25":
    print(
        "\n[Program 25] This program tests function structures by calculating the area and perimeter of a static rectangle dimensions."
    )

    def areaRectangle(a, b):
        return a * b

    def perimeterRectangle(a, b):
        return 2 * (a + b)

    a = 5
    b = 6
    print("Area = ", areaRectangle(a, b))
    print("Perimeter = ", perimeterRectangle(a, b))

elif choice == "26":
    print(
        "\n[Program 26] This program runs a dynamic number guessing game using algorithmic probability logs to determine turn counts."
    )
    lower = int(input("Enter Lower bound:- "))
    upper = int(input("Enter Upper bound:- "))
    x = random.randint(lower, upper)
    max_guesses = math.log(upper - lower + 1, 2)
    print(
        "\n\tYou've only ",
        round(max_guesses),
        " chances to guess the integer!\n",
    )
    count = 0
    while count < max_guesses:
        count += 1
        guess = int(input("Guess a number:- "))
        if x == guess:
            print("Congratulations you did it in ", count, " try")
            break
        elif x > guess:
            print("You guessed too small!")
        elif x < guess:
            print("You Guessed too high!")
    if count >= max_guesses and x != guess:
        print("\nThe number is %d" % x)
        print("\tBetter Luck Next time!")

    elif choice == "27":
        print(
            "\n[Program 27] This program parses an arbitrary string date and extracts the matching calendar name of that week day."
        )
        date = str(input("Enter the date(for example:09 02 2019): "))
        day_name = [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        day = datetime.datetime.strptime(date, "%d %m %Y").weekday()
        print(day_name[day])

    elif choice == "28":
        print(
            "\n[Program 28] This program scans a sorted sequence list and outputs an array pinpointing all missing numeric elements."
        )

        def find_missing(lst):
            return [x for x in range(lst[0], lst[-1] + 1) if x not in lst]

        lst = [1, 2, 4, 6, 7, 9, 10]
        print(find_missing(lst))

    elif choice == "29":
        print(
            "\n[Program 29] This program validates string composition match sets against targeted lookup elements."
        )
        char_list = ["a", "b", "c"]
        string = "abcd"
        matched_list = [characters in char_list for characters in string]
        print(matched_list)
        print(all(matched_list))

    elif choice == "30":
        print(
            "\n[Program 30] This continuous loop program calculates sums and averages for custom streams of odd and even numbers until 'done' is entered."
        )
        total = 0
        evenSums = 0
        oddSums = 0
        evenCount = 0
        oddCount = 0
        done = False
        while not done:
            user_in = input("Give me an integer or type 'done' to be done: ")
            if user_in.lower() == "done":
                done = True
            else:
                num = int(user_in)
                total += num
                if num % 2 == 0:
                    evenSums += num
                    evenCount += 1
                else:
                    oddSums += num
                    oddCount += 1
        evenAverage = evenSums / evenCount if evenCount > 0 else 0
        oddAverage = oddSums / oddCount if oddCount > 0 else 0
        print("Total sum:", total)
        print("Even Average: " + str(evenAverage))
        print("Odd Average: " + str(oddAverage))

    else:
        print("\nInvalid choice! Please select a valid number from 1 to 30.")
