print("Welcome to my quadratic and cubic equations calculator")
purpose = input("What do you want to calculate the roots for quadratic(q) or cubic(c): ")
if purpose.lower() == "q":
    a = int(input("What is the coefficient of x^2: "))
    b = int(input("What is the coefficient of x: "))
    c = int(input("What is the single digit or the intercept: "))
    import math as m
    formula1 = ((-b + (m.sqrt(((b ** 2) - (4 * a *c)))))/ (2 * a))
    formula2 = ((-b - (m.sqrt(((b ** 2) - (4 * a *c)))))/ (2 * a))
    print(formula1)
    print(formula2)

elif purpose.lower() == "c":
   a = print("")