import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox
import re

# Function to handle adding a new scribble pad and show output in a popup
def add_scribble_pad():
    pad_name = pad_name_entry.get()
    pad_type = pad_type_var.get()
    pad_content = pad_content_text.get("1.0", "end-1c")

    # Prepare the output message
    output_message = f"Scribble Pad Name: {pad_name}\n"
    output_message += f"Scribble Pad Type: {pad_type}\n"
    output_message += "Scribble Pad Content:\n"
    output_message += pad_content

    # Show the output in a popup message box
    messagebox.showinfo("Scribble Pad Details", output_message)

# Function to validate the form inputs
def validate_form():
    # Get values from the input fields
    name = name_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    gender = gender_var.get()
    dob = dob_spinbox.get()

    # Define regular expressions for validation
    name_pattern = r"^[A-Za-z\s]+$"
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$"
    phone_pattern = r"^\d{10}$"
    dob_pattern = r"^(19[0-9][0-9]|20[0-2][0-9]|2030)$"

    # Validate Name
    if not re.match(name_pattern, name):
        result_label.config(text="Invalid Name", foreground="red")
        return

    # Validate Email
    if not re.match(email_pattern, email):
        result_label.config(text="Invalid Email", foreground="red")
        return

    # Validate Phone Number
    if not re.match(phone_pattern, phone):
        result_label.config(text="Invalid Phone Number", foreground="red")
        return

    # Validate Year of Birth
    if not re.match(dob_pattern, dob):
        result_label.config(text="Invalid Year of Birth", foreground="red")
        return

    # If all validations pass, display the result
    result_label.config(text=f"Name: {name}\nEmail: {email}\nPhone: {phone}\nGender: {gender}\nDoB: {dob}", foreground="green")

# Create the main window
root = tk.Tk()
root.title("Scribble Pad Management System and Domain Form")

# Create a notebook to switch between the two forms
notebook = ttk.Notebook(root)
notebook.grid(row=0, column=0)

# Scribble Pad Management System Form
sps_frame = ttk.Frame(notebook, padding=20)
notebook.add(sps_frame, text="Scribble Pad")

# Scribble Pad Name
pad_name_label = ttk.Label(sps_frame, text="Scribble Pad Name:")
pad_name_label.grid(row=0, column=0, sticky="w")
pad_name_entry = ttk.Entry(sps_frame)
pad_name_entry.grid(row=0, column=1)

# Scribble Pad Type
pad_type_label = ttk.Label(sps_frame, text="Scribble Pad Type:")
pad_type_label.grid(row=1, column=0, sticky="w")
pad_type_var = tk.StringVar()
pad_type_var.set("Personal")
personal_radio = ttk.Radiobutton(sps_frame, text="Personal", variable=pad_type_var, value="Personal")
work_radio = ttk.Radiobutton(sps_frame, text="Work", variable=pad_type_var, value="Work")
personal_radio.grid(row=1, column=1)
work_radio.grid(row=1, column=2)

# Scribble Pad Content
pad_content_label = ttk.Label(sps_frame, text="Scribble Pad Content:")
pad_content_label.grid(row=2, column=0, sticky="w")
pad_content_text = tk.Text(sps_frame, height=5, width=30)
pad_content_text.grid(row=2, column=1, columnspan=2)

# Add Scribble Pad Button
add_pad_button = ttk.Button(sps_frame, text="Add Scribble Pad", command=add_scribble_pad)
add_pad_button.grid(row=3, column=0, columnspan=3)

# Domain Form
domain_frame = ttk.Frame(notebook, padding=20)
notebook.add(domain_frame, text="Domain Form")

# Name
name_label = ttk.Label(domain_frame, text="Name:")
name_label.grid(row=0, column=0, sticky="w")
name_entry = ttk.Entry(domain_frame)
name_entry.grid(row=0, column=1)

# Email
email_label = ttk.Label(domain_frame, text="Email:")
email_label.grid(row=1, column=0, sticky="w")
email_entry = ttk.Entry(domain_frame)
email_entry.grid(row=1, column=1)

# Phone Number
phone_label = ttk.Label(domain_frame, text="Phone Number:")
phone_label.grid(row=2, column=0, sticky="w")
phone_entry = ttk.Entry(domain_frame)
phone_entry.grid(row=2, column=1)

# Gender
gender_label = ttk.Label(domain_frame, text="Gender:")
gender_label.grid(row=3, column=0, sticky="w")
gender_var = tk.StringVar()
gender_combobox = ttk.Combobox(domain_frame, textvariable=gender_var, values=["Male", "Female", "Other"])
gender_combobox.grid(row=3, column=1)

# Year of Birth
dob_label = ttk.Label(domain_frame, text="Year of Birth:")
dob_label.grid(row=4, column=0, sticky="w")
dob_spinbox = ttk.Entry(domain_frame)
dob_spinbox.grid(row=4, column=1)

# Submit Button
submit_button = ttk.Button(domain_frame, text="Submit", command=validate_form)
submit_button.grid(row=5, column=0, columnspan=2)

# Result Label
result_label = ttk.Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=1, column=0)

# Menu Bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# File Menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New")
file_menu.add_command(label="Open")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

# Help Menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")

# Run the Tkinter main loop
root.mainloop()
