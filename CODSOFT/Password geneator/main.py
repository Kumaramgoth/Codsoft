import random
import string
from tkinter import *
from ttkthemes import ThemedTk 
from tkinter import ttk

# Function to generate password
def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(var.get()))
    output.config(text=password, font=("Ubuntu", 20), justify='center')

# Function to copy the generated password to the clipboard
def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(output['text'])


window = ThemedTk(theme="white")
window.title("Password Generator")
window.geometry("300x200")
window.config(bg="green") 

#password length 
var = IntVar()
var.set(8)

# Dropdown menu 
dropdown = ttk.Combobox(window, textvariable=var, values=[8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
dropdown.pack(pady=5, anchor='center')

# Generate button
generate_button = ttk.Button(window, text="Generate", command=generate_password)
generate_button.pack(pady=5, anchor='center')

# Copy button
copy_button = ttk.Button(window, text="Copy",
                         command=copy_to_clipboard)
copy_button.pack(pady=5, anchor='center')

# Output label to display the generated password, center-aligned
output = ttk.Label(window, justify='center')
output.pack(pady=20, anchor='center', expand=True)

window.mainloop()
