import tkinter as tk
from tkinter import messagebox


def admission_message(name, course, jamb_score, credit, interview_status):
    window = tk.Toplevel(roots)
    window.title("Price Box")
    window.geometry("700x200")

    label_1 = tk.Label(window, text="CONGRATULATIONS YOU HAVE REACH THE REQUIREMENT TO BE GRANTED ADMISSION\n"
                                    "\nBelow are your details\n")
    label_1.pack()
    label_2 = tk.Label(window, text=f"Name: {name}")
    label_2.pack()
    label_3 = tk.Label(window, text=f"Choice of course:  {course}")
    label_3.pack()
    label_4 = tk.Label(window, text=f"Jamb score:  {jamb_score}")
    label_4.pack()
    label_5 = tk.Label(window, text=f"Number of credits in your core subject:  {credit}")
    label_5.pack()
    label_6 = tk.Label(window, text=f"Interview status:  {interview_status}")
    label_6.pack()

    roots.mainloop()


def enter():
    name = name_entry.get()
    course = course_entry.get()
    jamb_score = int(jamb_score_entry.get())
    credit = int(credits_entry.get())
    interview_status = interview_status_entry.get()

    if course == "Computer Science" and (jamb_score >= 250) and (jamb_score <= 400) and (credit >= 5) and (interview_status == "Passed"):
        name = name
        admission_message(name, course, jamb_score, credit, interview_status)
    elif course == "Mass Communication" and (jamb_score >= 230) and (jamb_score <= 400) and (credit >= 5) and interview_status == "Passed":
        name = name
        admission_message(name, course, jamb_score, credit, interview_status)

    else:
        messagebox.showerror("No admission", "Sorry you didn't meet the requirements to gain "
                                             "admission to Pan Atlantic University OR you have made and error in your inputs")


roots = tk.Tk()
roots.title("Admission Form")
roots.geometry("500x500")

name_label = tk.Label(roots, text="Name")
name_label.pack()
name_entry = tk.Entry(roots)
name_entry.pack()

course_label = tk.Label(roots, text="Choice of course")
course_label.pack()
course_entry = tk.Entry(roots)
course_entry.pack()

jamb_score_label = tk.Label(roots, text="Jamb Score")
jamb_score_label.pack()
jamb_score_entry = tk.Entry(roots)
jamb_score_entry.pack()

credits_label = tk.Label(roots, text="Number of credits (or above)  in core subjects")
credits_label.pack()
credits_entry = tk.Entry(roots)
credits_entry.pack()

interview_status_label = tk.Label(roots, text="Interview Status")
interview_status_label.pack()
interview_status_entry = tk.Entry(roots)
interview_status_entry.pack()

submit_button = tk.Button(roots, text="Submit", command=enter)
submit_button.pack()
submit_button.config(fg="Red", bg="Black")
roots.mainloop()
