def changeme(mylist):
    #This changes a past list
    mylist.append([1,2,3,4])
    print("Values inside the function: ", mylist)
    return

mylist = [5,6,7,8]
changeme(mylist)
print("Values outside the function: ",mylist)

