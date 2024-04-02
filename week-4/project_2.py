print("Welcome to Izifin Technology Annual Tax Revenue (ATR) calculator \n")

experience = int(input("How many years of experience do you have: "))
age = int(input("How old are you: "))

if (experience > 25) & (age >= 55):
    print("Your Annual Staff Revenue is: N5,600,000")
elif (experience > 20) & (age >= 45):
    print("Your Annual Staff Revenue is: N4,480,000")
elif (experience > 10) & (age >= 35):
    print("Your Annual Staff Revenue is: N1,500,000")
elif (experience < 10) & (age < 35):
    print("Your Annual Staff Revenue is: N550,000")
else:
    print("You are not in any of these categories")