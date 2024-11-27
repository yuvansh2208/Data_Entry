from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
import csv
import os

root = Tk()
root.title("Data Entry")
root.geometry("700x400+300+200")
root.resizable(False, False)
root.configure(bg="#326273")

def check_csv_file():
    """Check if the CSV file exists, and create it with headers if it doesn't."""
    if not os.path.isfile("registration_data.csv"):
        with open("registration_data.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Contact", "Age", "Gender", "Address"])

def submit():
    # Ensure CSV file exists
    check_csv_file()
    
    # Retrieve data from the form
    name = namevalue.get()
    contact = contactvalue.get()
    age = agevalue.get()
    gender = gender_combobox.get()
    address = AddressEntry.get("1.0", END).strip()
    
    # Check if all fields are filled
    if not name or not contact or not age or not address:
        messagebox.showwarning("Incomplete Data", "Please fill all the fields.")
        return

    # Save data to CSV
    with open("registration_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, contact, age, gender, address])

    # Show success message
    messagebox.showinfo("Success", "Data submitted successfully!")
    clear()

def clear():
    namevalue.set("")
    contactvalue.set("")
    agevalue.set("")
    AddressEntry.delete(1.0, END)

# Heading
label_heading = Label(root, text="Fill This Registration Form", font=("Arial", 16, "bold"), bg="#326273", fg="#ffffff")
label_heading.place(x=20, y=10)

# Labels
Label(root, text="Name", font=16, bg="#326273", fg="#ffffff").place(x=50, y=80)
Label(root, text="Contact No.", font=16, bg="#326273", fg="#ffffff").place(x=50, y=120)
Label(root, text="Age", font=16, bg="#326273", fg="#ffffff").place(x=50, y=160)
Label(root, text="Gender", font=16, bg="#326273", fg="#ffffff").place(x=370, y=160)
Label(root, text="Address", font=16, bg="#326273", fg="#ffffff").place(x=50, y=200)

# Entries
namevalue = StringVar()
contactvalue = StringVar()
agevalue = StringVar()

nameEntry = Entry(root, textvariable=namevalue, width=45, bd=2, font=("Arial", 12))
nameEntry.place(x=200, y=80)

contactEntry = Entry(root, textvariable=contactvalue, width=45, bd=2, font=("Arial", 12))
contactEntry.place(x=200, y=120)

ageEntry = Entry(root, textvariable=agevalue, width=12, bd=2, font=("Arial", 12))
ageEntry.place(x=200, y=160)

# Gender Combobox
gender_combobox = Combobox(root, values=['Male', 'Female'], font='arial 12', state='readonly', width=10)
gender_combobox.place(x=470, y=160)
gender_combobox.set('Male')

# Address Entry using Text widget
AddressEntry = Text(root, width=45, height=4, bd=2, font=("Arial", 12))
AddressEntry.place(x=200, y=200)

# Buttons
Button(root, text="Submit", bg="#326273", fg="white", width=15, height=2, command=submit).place(x=200, y=300)
Button(root, text="Clear", bg="#326273", fg="white", width=15, height=2, command=clear).place(x=320, y=300)
Button(root, text="Exit", bg="#326273", fg="white", width=15, height=2, command=lambda: root.destroy()).place(x=440, y=300)

root.mainloop()
