total = 50 #This is the global variable
def sum(arg1,arg2):
    #Add both the parameters
    total = arg1 + arg2;
    print("Inside the function local function total: ", total)
    return total;

#Now you can call sum function
sum(10,20)
print("Outside the function global function total: ",total)

