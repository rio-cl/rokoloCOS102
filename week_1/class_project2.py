#Formula to solve compound interest
principle = input("What is the original principle? ")
rate = input("What is the interest rate? ")
time = input("What is the time period elasped? ")
number = input("What is the number of times interest applied per time period? ")

p = float(principle)
r = float(rate)
t = float(time)
n = float(number)

amount = p * (( 1 + ( r / n )) ** ( n * t ))
print("The simple interest is: $" + str(amount))
