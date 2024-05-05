import tkinter as tk
from tkinter import messagebox

rice = {"1.Jollof rice\t2.Coconut fried rice\t3.Jollof spaghetti"}
side_dishes = {"1.Savoury Beans\t2.Roasted Sweet Potatoes\t3.Fried Plantains\t4.Mixed Vegetable Salad\t5.Boiled Yarn"}
soups = {"1.Eba\t2.Poundo Yam\t3.Semo\t4.Atama Soup\t5.Egusi Soup"}
protein = {"1.Sweet Chilli Chicken\t2.Grilled Chicken Wings\t3.Fried Beef\t4.Fried Fish\t5.Boiled Egg\t6.Sauteed Sausages"}
beverages = {"1.Water\t2.Class Drink (35cl)\t3.Pet Drink (35cl)\t4.Pet Drink (50c)\t5.Glass/Canned Malt\t6.Fresh Yo\t7.Pineapple Juice\t8.Mango Juice\t9.Zobo drink"}

rice1 = {"Jollof rice": 350,"Coconut fried rice": 350,"Jollof spaghetti": 350}
side_dishes1 = {"Savoury Beans": 350,"Roasted Sweet Potatoes": 300,"Fried Plantains": 150,"Mixed Vegetable Salad": 150,"Boiled Yarn": 150}
soups1 = {"Eba": 100,"Poundo Yam": 100,"Semo": 100,"Atama Soup": 450,"Egusi Soup": 450}
protein1 = {"Sweet Chilli Chicken": 1100,"Grilled Chicken Wings": 400,"Fried Beef": 400,"Fried Fish": 500,"Boiled Egg": 200,"Sauteed Sausages": 200}
beverages1 = {"Water": 200,"Class Drink (35cl)": 150,"Pet Drink (35cl)": 300,"Pet Drink (50c)": 350,"Glass/Canned Malt": 500,"Fresh Yo": 600,"Pineapple Juice": 350,"Mango Juice": 350,"Zobo drink": 350}




def enter():
    window1 = tk.Toplevel(root)
    window1.title("Price Box")
    window1.geometry("700x700")


    name_label = tk.Label(window1, text="Input name ")
    name_label.pack()
    name_entry = tk.Entry(window1)
    name_entry.pack()

    rices_label = tk.Label(window1, text="Input Rice Order")
    rices_label.pack()
    rices_entry = tk.Entry(window1)
    rices_entry.pack()

    rquantity_label = tk.Label(window1, text="Quantity/Portions of rice")
    rquantity_label.pack()
    rquantity_entry = tk.Entry(window1)
    rquantity_entry.pack()

    si_label = tk.Label(window1, text="Input Side Dishes order")
    si_label.pack()
    si_entry = tk.Entry(window1)
    si_entry.pack()

    si_quantity_label = tk.Label(window1, text="Quantity/Portions of side dish")
    si_quantity_label.pack()
    si_quantity_entry = tk.Entry(window1)
    si_quantity_entry.pack()

    so_label = tk.Label(window1, text="Input Soup order")
    so_label.pack()
    so_entry = tk.Entry(window1)
    so_entry.pack()

    so_quantity_label = tk.Label(window1, text="Quantity/Portions of Soup")
    so_quantity_label.pack()
    so_quantity_entry = tk.Entry(window1)
    so_quantity_entry.pack()

    pr_label = tk.Label(window1, text="Input Protien order")
    pr_label.pack()
    pr_entry = tk.Entry(window1)
    pr_entry.pack()

    pr_quantity_label = tk.Label(window1, text="Protien Quantity")
    pr_quantity_label.pack()
    pr_quantity_entry = tk.Entry(window1)
    pr_quantity_entry.pack()

    be_label = tk.Label(window1, text="Input Beverage order")
    be_label.pack()
    be_entry = tk.Entry(window1)
    be_entry.pack()

    be_quantity_label = tk.Label(window1, text="Quantity of Beverages")
    be_quantity_label.pack()
    be_quantity_entry = tk.Entry(window1)
    be_quantity_entry.pack()

    name = name_entry.get()
    rices = rices_entry.get()
    rquantity = int(rquantity_entry.get())
    si = si_entry.get()
    si_quantity = int(si_quantity_entry.get())
    so = so_entry.get()
    so_quantity = int(so_quantity_entry.get())
    pr = pr_entry.get()
    pr_quantity = int(pr_quantity_entry.get())
    be = be_entry.get()
    be_quantity = int(be_quantity_entry.get())

    total_price = (be*be_quantity) + (pr*pr_quantity) + (so*so_quantity) + (si*si_quantity) + (rices * rquantity)

    root.mainloop()


root = tk.Tk()
root.title("MENU")
root.geometry("1106x500")

title1_label = tk.Label(root, text="WELCOME TO PAU MENU\nHere are a list of things we have")
title1_label.pack()

rice_title_label = tk.Label(root, text="\nRICE/PASTA")
rice_title_label.pack()
for i in rice:
    rice_menu_label = tk.Label(root, text=f"{i}")
    rice_menu_label.pack()

sidedishes_title_label = tk.Label(root, text="\nSIDE DISHES")
sidedishes_title_label.pack()
for j in side_dishes:
    side_menu_label = tk.Label(root, text=f"{j}")
    side_menu_label.pack()

soups_title_label = tk.Label(root, text="\nSOUPS & SWALLOWS")
soups_title_label.pack()
for i in soups:
    soups_menu_label = tk.Label(root, text=f"{i}")
    soups_menu_label.pack()

protein_title_label = tk.Label(root, text="\nPROTIENS")
protein_title_label.pack()
for i in protein:
    protein_menu_label = tk.Label(root, text=f"{i}")
    protein_menu_label.pack()

beverages_title_label = tk.Label(root, text="\nBEVERAGES")
beverages_title_label.pack()
for i in beverages:
    beverages_menu_label = tk.Label(root, text=f"{i}\n\n")
    beverages_menu_label.pack()

root.mainloop()




