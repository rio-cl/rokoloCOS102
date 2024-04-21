import tkinter as tk
from tkinter import messagebox


def pricemessage1(weight,location,price):
    window = tk.Toplevel(root)
    window.title("Price Box")
    window.geometry("700x200")

    label_1 = tk.Label(window, text=f"\nDear User\n")
    label_1.pack()
    label_2 = tk.Label(window, text=f"The size of your package is {weight}kg")
    label_2.pack()
    label_3 = tk.Label(window, text=f"The location your package is being delivered to is {location}")
    label_3.pack()
    label_4 = tk.Label(window, text=f"Due to the fact that the size of your package is {weight}kg "
                                    f"and the location your delivery is {location}\n"
                                    f"\nThe price of your delivery is N{price}")
    label_4.pack()

    root.mainloop()



def enter():
    weight = int(weight_entry.get())
    location = location_entry.get()

    if weight >= 10 and location.lower() == "Ibeju-Lekki":
        price = 5000
        pricemessage1(weight,location,price)
    elif weight < 10 and location == "Ibeju-Lekki":
        price = 3500
        pricemessage1(weight,location,price)
    elif weight >= 10 and location == "Epe":
        price = 10000
        pricemessage1(weight,location,price)
    elif weight < 10 and location == "Epe":
        price = 5000
        pricemessage1(weight,location,price)
    else:
        messagebox.showerror("Location ", "We do not deliver to your location")


root = tk.Tk()
root.title("Login form")
root.geometry("500x200")

weight_label = tk.Label(root, text ="weight")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

location_label = tk.Label(root, text ="location")
location_label.pack()
location_entry = tk.Entry(root)
location_entry.pack()

submit_button = tk.Button(root, text="ENTER", command=enter)
submit_button.pack()
submit_button.config(fg="red")

root.mainloop()
