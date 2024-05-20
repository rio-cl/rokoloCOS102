import tkinter as tk
from tkinter import messagebox

departments = {"Retail", "Global", "Commercial"}


class Zenith(object):

    def __init__(self):
        pass

    def unique_services(self):
        pass

    def mutual_services(self):
        pass

    def total_services(self):
        total = self.mutual_services() and self.unique_services()
        return total


class Retail_banking(Zenith):
    def unique_services(self):
        return "Loans and Mortgages", "Checking and Saving"

    def mutual_services(self):
        return "Lines of Credit", "Investment Management and Accounts", "Insurance", "Retirement and Education Accounts"

    def total_services(self):
        total = self.mutual_services() + self.unique_services()
        window = tk.Toplevel(root)
        window.title("Employee Data")
        window.geometry("400x200")

        label_1 = tk.Label(window, text=f"Welcome Esteemed Employee")
        label_1.pack()
        label_2 = tk.Label(window, text=f"Here are the Services in Your Department")
        label_2.pack()
        label_3 = tk.Label(window, text=f"{total}")
        label_3.pack()

        Zenith.__init__(self)


class Global_banking(Zenith):
    def unique_services(self):
        return ["Multi-Currency Management Services and Products",
                "Foreign Currency Accounts",
                "Foreign Currency Credit Cards",
                "Transborder Advisory Services", "Liquidity Management"]

    def mutual_services(self):
        return ["Lines of Credit", "Investment Management and Accounts", "Insurance"]

    def total_services(self):
        total = self.mutual_services() + self.unique_services()
        window = tk.Toplevel(root)
        window.title("Employee Data")
        window.geometry("400x200")

        label_1 = tk.Label(window, text=f"Welcome Esteemed Employee")
        label_1.pack()
        label_2 = tk.Label(window, text=f"Here are the Services in Your Department")
        label_2.pack()
        label_3 = tk.Label(window, text=f"{total}")
        label_3.pack()


class Commercial_banking(Zenith):
    def unique_services(self):
        return ["Advisory Services"]

    def mutual_services(self):
        return ["Lines of Credit", "Investment Management and Accounts", "Insurance"]

    def total_services(self):
        total = self.mutual_services() + self.unique_services()
        window = tk.Toplevel(root)
        window.title("Employee Data")
        window.geometry("400x200")

        label_1 = tk.Label(window, text=f"Welcome Esteemed Employee")
        label_1.pack()
        label_2 = tk.Label(window, text=f"Here are the Services in Your Department")
        label_2.pack()
        label_3 = tk.Label(window, text=f"{total}")
        label_3.pack()


def enter():

    dep = department_entry.get()
    ret = Retail_banking()
    glo = Global_banking()
    com = Commercial_banking()

    if dep in departments:
        ret.total_services()

    elif dep in departments:
        glo.total_services()

    elif dep in departments:
        com.total_services()

    else:
        messagebox.showerror("Error", "Please re-check your input")


root = tk.Tk()
root.title("Login form")
root.geometry("500x200")

name_label = tk.Label(root, text="Full Name")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

department_label = tk.Label(root, text="Department Name")
department_label.pack()
department_entry = tk.Entry(root)
department_entry.pack()

enter_button = tk.Button(root, text="Enter", command=enter)
enter_button.pack()
enter_button.config(fg="red")

root.mainloop()
