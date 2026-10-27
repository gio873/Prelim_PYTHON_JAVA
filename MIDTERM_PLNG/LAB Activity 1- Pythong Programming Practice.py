import datetime
import math
import random

print("\n--- Program 1 ---")
print("Hello World")

print("\n--- Program 2 ---")
usertext = input("What is your name? ")
print("Hello", usertext)

print("\n--- Program 3 ---")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
sum_result = float(num1) + float(num2)
print("The sum of {0} and {1} is {2}".format(num1, num2, sum_result))

print("\n--- Program 4 ---")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
average = (int(num1) + int(num2)) / 2
print("average:{0} ".format(average))

print("\n--- Program 5 ---")
visagrade = input("enter your visa grade : ")
finalgrade = input("enter your final grade : ")
average = (float(visagrade) * 0.3) + (float(finalgrade) * 0.7)
print("average :{0} ".format(average))

print("\n--- Program 6 ---")
firstexam = input("your first exam : ")
secondexam = input("your second exam : ")
thirdexam = input("your third exam : ")
average = (float(firstexam) + float(secondexam) + float(thirdexam)) / 3
print("average :{0} ".format(average))

print("\n--- Program 7 ---")
average = input("enter average : ")
if int(average) >= 50:
    print("Passed")
else:
    print("Failed")

print("\n--- Program 8 ---")
num = int(input("Enter a number: "))
if (num % 2) == 0:
    print("{0} is Even".format(num))
else:
    print("{0} is Odd".format(num))

print("\n--- Program 9 ---")
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

print("\n--- Program 10 ---")
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

print("\n--- Program 11 ---")
age = input("enter age : ")
if int(age) < 18:
    print("Your Age Is Not Eligible To Get A Driver's License")
else:
    print("Your Age Is Eligible To Get Your License")

print("\n--- Program 12 ---")
for i in range(1, 101):
    print(i)

print("\n--- Program 13 ---")
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

print("\n--- Program 14 ---")
for i in range(1, 101):
    if i % 2 != 0:
        print(i)

print("\n--- Program 15 ---")
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        print(i)

print("\n--- Program 16 ---")
num = input("enter number : ")
for i in range(1, int(num) + 1):
    print(i)

print("\n--- Program 17 ---")
short = input("Enter short side : ")
tall = input("Enter tall side : ")
area = int(short) * int(tall)
perimeter = 2 * (int(short) + int(tall))
print("area: {0}".format(area))
print("perimeter: {0}".format(perimeter))

print("\n--- Program 18 ---")
word = "mrhuseyin"
for char in word:
    print(char)

print("\n--- Program 19 ---")
sumofnumbers = 0
num1 = input("first number: ")
num2 = input("second number: ")
for i in range(int(num1) + 1, int(num2)):
    sumofnumbers += i
print("Sum of numbers between {0} and {1} : {2}".format(num1, num2, sumofnumbers))

print("\n--- Program 20 ---")
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

print("\n--- Program 21 ---")
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

print("\n--- Program 22 ---")
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

print("\n--- Program 23 ---")
salary = input("enter current salary : ")
raise_rate = input("salary raise rate(%) : ")
newsalary = int(salary) + (int(salary) * int(raise_rate) / 100)
print("increased salary :", newsalary)

print("\n--- Program 24 ---")
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

print("\n--- Program 25 ---")
def areaRectangle(a, b):
    return a * b

def perimeterRectangle(a, b):
    return 2 * (a + b)

a = float(input("Enter width side (a): "))
b = float(input("Enter height side (b): "))
print("Area = ", areaRectangle(a, b))
print("Perimeter = ", perimeterRectangle(a, b))

print("\n--- Program 26 ---")
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))
x = random.randint(lower, upper)
total_chances = round(math.log(upper - lower + 1, 2))
print("\n\tYou've only ", total_chances, " chances to guess the integer!\n")
count = 0
while count < total_chances:
    count += 1
    guess = int(input("Guess a number:- "))
    if x == guess:
        print("Congratulations you did it in ", count, " try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
if count >= total_chances and guess != x:
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next time!")

print("\n--- Program 27 ---")
date = str(input("Enter the date(for example:09 02 2019): "))
day_name = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day = datetime.datetime.strptime(date, "%d %m %Y").weekday()
print(day_name[day])

print("\n--- Program 28 ---")
def find_missing(lst):
    return [x for x in range(lst[0], lst[-1] + 1) if x not in lst]

lst = [1, 2, 4, 6, 7, 9, 10]
print("Original list:", lst)
print("Missing numbers:", find_missing(lst))

print("\n--- Program 29 ---")
char_list = ["a", "b", "c"]
string = "abcd"
matched_list = [characters in char_list for characters in string]
print("Characters processed:", matched_list)
string_contains_chars = all(matched_list)
print("All string characters in list:", string_contains_chars)

print("\n--- Program 30 ---")
total = 0
evenSums = 0
evenCount = 0
oddSums = 0
oddCount = 0
done = False
while not done:
    user_in = input("Give me an integer or type 'done' to be done: ").strip()
    if user_in.lower() == "done":
        done = True
    else:
        val = int(user_in)
        total += val
        if val % 2 == 0:
            evenSums += val
            evenCount += 1
        else:
            oddSums += val
            oddCount += 1
print("Total Sum:", total)
print("Even Average:", (evenSums / evenCount) if evenCount > 0 else 0)
print("Odd Average:", (oddSums / oddCount) if oddCount > 0 else 0)
