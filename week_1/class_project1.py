#program to solve simpe interest
rate = input("What is the rate? ")
time = input("What is the time interval? ")
principle = input("What is the principle? ")
p = float(principle)
r = float(rate)
t = float(time)
Amount = p * (1 + (( r / 100) * t ))
print("The simple interest is: " + "$" + str(Amount))

