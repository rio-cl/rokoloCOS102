import tkinter as tk
from tkinter import messagebox


def welcomemessage_1(name):
    window = tk.Toplevel(root)
    window.title("Department Information")
    window.geometry("1000x1000")

    label_1 = tk.Label(window, text=f"Welcome {name}\n")
    label_1.pack()
    label_2 = tk.Label(window, text="This is a list of the people in your department")
    label_2.pack()
    for i in logistics:
        label_3 = tk.Label(window, text=f"{i}")
        label_3.pack()

    root.mainloop()

def welcomemessage_2(name):
    window = tk.Toplevel(root)
    window.title("Department Information")
    window.geometry("1000x1000")

    label_1 = tk.Label(window, text=f"Welcome {name}\n")
    label_1.pack()
    label_2 = tk.Label(window, text="This is a list of the people in your department")
    label_2.pack()
    for i in accounting:
        label_3 = tk.Label(window, text=f"{i}")
        label_3.pack()

    root.mainloop()

def welcomemessage_3(name):
    window = tk.Toplevel(root)
    window.title("Department Information")
    window.geometry("1000x1000")

    label_1 = tk.Label(window, text=f"Welcome {name}\n")
    label_1.pack()
    label_2 = tk.Label(window, text="This is a list of the people in your department")
    label_2.pack()
    for i in delivery:
        label_3 = tk.Label(window, text=f"{i}")
        label_3.pack()

    root.mainloop()

def welcomemessage_4(name):
    window = tk.Toplevel(root)
    window.title("Department Information")
    window.geometry("1000x1000")

    label_1 = tk.Label(window, text=f"Welcome {name}\n")
    label_1.pack()
    label_2 = tk.Label(window, text="This is a list of the people in your department")
    label_2.pack()
    for i in administration:
        label_3 = tk.Label(window, text=f"{i}")
        label_3.pack()

    root.mainloop()


logistics = {"Adeniran Oluwatamilore",
             "AGBAKWURU Chiemeziem",
             "ARNIKA Osose",
             "CHUKWUMA Nedi",
             "EZEONYE Makuochukwu",
             "GIWA Moyosore",
             "NWOKOLO Chijindu",
             "NWOTOKUBO Joseph",
             "OKORO Derek",
             "OSSAI Mary-Cynthia",
             "PETER Owoede"}

accounting = {"ADEWUMI Ayomide",
              "AGBAKURU-NWOGU Chukwunonye",
              "AKINDE Oluwatimehin",
              "EBI Stephanie",
              "OBASOGIE Daisy",
              "OBI Samuel",
              "OBIALOR Betha",
              "OLOWOKERE Akorede",
              "OLUBUADE Rasheed",
              "OSEMEKE Daniel",
              "ICHA Ayonete",
              "IKPATI Eche"}

delivery = {"ADOH-AJAGBE Oshim",
            "ATELLY Daniel",
            "AZOGU Onyekachi",
            "BETURE Shalom",
            "EJEDIMU Edward",
            "ILOENYOSI Michael",
            "IYAWE Oluwadamilola",
            "OGBONNA Boluwatife",
            "OIGBOCHIE Mary",
            "QUADRI Oluwafikunmi",
            "UDE-IBE Uchenna"}

administration = {"EGBORO Jason",
                  "ELERI Otu",
                  "EZE Onyinyechi",
                  "OKOCHA-OJEAH Raphael",
                  "OKOLO Victor",
                  "UMEH Ejike"}


def enter():
    name = name_entry.get()
    department = department_entry.get()

    if name in logistics and department == "Logistics":
        welcomemessage_1(name)

    elif name in accounting and department == "Accounting":
        welcomemessage_2(name)

    elif name in delivery and department == "Delivery":
        welcomemessage_3(name)

    elif name in administration and department == "Administration":
        welcomemessage_4(name)

    else:
        messagebox.showerror("Login ", "employee doesn't exist")


root = tk.Tk()
root.title("Login form")
root.geometry("500x200")
name_label = tk.Label(root, text="Name")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

department_label = tk.Label(root, text="Department")
department_label.pack()
department_entry = tk.Entry(root)
department_entry.pack()

enter_button = tk.Button(root, text="Enter", command=enter)
enter_button.pack()
enter_button.config(fg="red")

root.mainloop()
