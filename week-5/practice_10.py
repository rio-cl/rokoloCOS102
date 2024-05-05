import tkinter as tk
import tkinter.messagebox as msgbox


#Handling button click event

def button_click():
    #print("Button clicked!")
    #Show an information message box
    msgbox.showinfo("Info", "Welcome to COS 102 GUI APP! \n")
    #Ask for user confirmation
    result = msgbox.askyesno("Confirmation","Do you want to continue?")

#Create the main window
root = tk.Tk()
root.title("Home page")
root.geometry("300x100")

#Add label widget
label = tk.Label(root, text = "Hello friend \n")
label.pack()

#Add a button widget
button = tk.Button(root, text = "Click me!", command = button_click)
button.pack()

#Styling the button widget
button.config(fg = "green", bg = "black")

#Start the event loop
root.mainloop()