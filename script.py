print("Hello Wordl")


txt = "Hello World"


print(txt[5:7])
print(txt.upper)
name = "Python"
print(f"I love {name}")


print(10 > 9)
print(10 == 9)
print(10 < 9)


print(10 > 9)
print(10 == 9)
print(bool("Hello"))
print(bool(0))


a = 15 
b = 4
print(a % b)
print(a // b)
print(a ** b)
a += 10


print("")
thislist = ['apple', 'banana', 'cheery']
print(thislist)


thislis = ['apple', 'banana', 'cheery']
thislis.insert(3, 'maksuda')
print(thislis)


thislis = ['apple', 'banana', 'cheery']
thislis.insert(3, 'maksuda')
thislis.remove('maksuda')
print(thislis)


thislis = ['apple', 'banana', 'cheery']
del thislis[0]
print(thislis)


thisliss = ['red', 'green', 'blue']
print(thisliss)
thisliss[thisliss.index('green')] = 'yellow'
thisliss.append('purple')
thisliss.remove('red')
print(thisliss)




thistuple = ['apple', 'banana', 'cherry']
print(thistuple[-1])


thistuple = ['apple', 'banana', 'cherry', 'kiwi', 'melon', 'mango',]
print(thistuple[2:5])


a=200
b=30
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b is equal")
else:
    print("a is greater than b")


age=20
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")