import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Menu of Available Foods and their Prices")
root.geometry("300x600")
list_of_food = \
    {
    "Jollof rice": 350,"Coconut Fried Rice": 350,"Savoury Beans": 350,"Eba": 100,"Poundo yam": 100,"Semo": 100,
    "Egusi Soup": 450,"Jollof Spaghetti": 350,"Roasted Sweet Potatoes": 150,
    "Boiled yam": 150,"Fried Plantains": 150,"Abala Soup": 450,"Sweet Chili Chicken": 1100,"Grilled Chicken Wings": 400,
    "Fried Beef": 400,"Fried Fish": 100,"Boiled egg": 200,"Sauteed Sausages": 200,"Water": 200,"Glass Drink (35cl)": 150,
    "PET Drink (35cl)": 300,"PET Drink (50cl)": 350,"Canned Malt": 500,"Pineapple juice": 350,"Mango Juice": 350,
    "Zobo Drink": 350,
}


food_var = tk.StringVar(root)

default_item = list(list_of_food.keys())[0]
food_var.set(default_item)

for food_item, price in list_of_food.items():
    label = tk.Label(root, text=f"{food_item}: ₦{price:.2f}")
    label.pack()


def orders():
    order = int(order_entry.get())
    name = name_entry.get()
    quantity = int(q_entry.get())
    price = order * quantity
    discounta = price - (price * 0.10)
    discountb = price - (price * 0.15)
    discountc = price - (price * 0.25)

    if price > 2500 and price < 5000:
        messagebox.showinfo("Total price due", f"{name}\n\n the Total charge for your order is: ₦{discountb}.")
    elif price > 1000 and price < 2500:
        messagebox.showinfo("Total price due", f"{name}\n\n the Total charge for your order is: ₦{discounta}.")
    elif price < 1000:
        messagebox.showinfo("Total price due", f"{name}\n\n the Total charge for your order is: ₦{price}.")
    elif price > 5000:
        messagebox.showinfo("Total price due", f"{name}\n\n the Total charge for your order is: ₦{discountc}.")
    else:
        messagebox.showerror("PRICE NOT AVAILABLE PLEASE CHECK YOUR INPUTS")


root = tk.Tk()
root.title("Menu Form")
root.geometry("600x400")

order_label = tk.Label(root, text="Total Price(₦):")
order_label.pack()

order_entry = tk.Entry(root)
order_entry.pack()

name_label = tk.Label(root, text="Customers Name")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

menu_label = tk.Label(root, text="Menu(Food stuff ordered)")
menu_label.pack()

menu_entry = tk.Entry(root)
menu_entry.pack()

q_label = tk.Label(root, text="Quantity/Portions:")
q_label.pack()

q_entry = tk.Entry(root)
q_entry.pack()

order_button = tk.Button(root, text="Order", command=orders)
order_button.pack()
order_button.config(bg="White",fg="Red")

root.mainloop()

#Algorithm

#1.	 I first made a window for the menu which displays all the food items available with their corresponding prices.
#2.	I then used a for statement to store the name of the food items with their corresponding prices.
#3.	I made another window for the inputting of customer orders in which they will calculate their total price by themselves and input it a long side their choice of food ordered and the quantity with their names.
#4.	I created an enter button which is connected to the enter command function.
#5.	I created a function called enter to give the specifics of how the discount will run.
#6. I made discounts for each of the different discounts that are applicable.
#7.	I used if statement to tell the code how the discounts are to be used
#8.	If the if statement is met, the code will show a message box saying the customers name and his total price and the discounts
#9.	If the if statements aren’t met then it shows an error box saying “PRICE NOT AVAILABLE PLEASE CHECK YOUR INPUTS”






