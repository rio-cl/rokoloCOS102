#Program to check whether a program is positive, negative, or 0

num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
elif num < 0:
    print("Negative number")