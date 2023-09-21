import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox

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

# Create the main window
root = tk.Tk()
root.title("Scribble Pad Management System")

# Create a frame for the form
form_frame = ttk.Frame(root, padding=20)
form_frame.grid(row=0, column=0)

# Scribble Pad Name
pad_name_label = ttk.Label(form_frame, text="Scribble Pad Name:")
pad_name_label.grid(row=0, column=0, sticky="w")
pad_name_entry = ttk.Entry(form_frame)
pad_name_entry.grid(row=0, column=1)

# Scribble Pad Type
pad_type_label = ttk.Label(form_frame, text="Scribble Pad Type:")
pad_type_label.grid(row=1, column=0, sticky="w")
pad_type_var = tk.StringVar()
pad_type_var.set("Personal")
personal_radio = ttk.Radiobutton(form_frame, text="Personal", variable=pad_type_var, value="Personal")
work_radio = ttk.Radiobutton(form_frame, text="Work", variable=pad_type_var, value="Work")
personal_radio.grid(row=1, column=1)
work_radio.grid(row=1, column=2)

# Scribble Pad Content
pad_content_label = ttk.Label(form_frame, text="Scribble Pad Content:")
pad_content_label.grid(row=2, column=0, sticky="w")
pad_content_text = tk.Text(form_frame, height=5, width=30)
pad_content_text.grid(row=2, column=1, columnspan=2)

# Add Scribble Pad Button
add_pad_button = ttk.Button(form_frame, text="Add Scribble Pad", command=add_scribble_pad)
add_pad_button.grid(row=3, column=0, columnspan=3)

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
