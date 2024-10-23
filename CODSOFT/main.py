import tkinter as tk
from tkinter import messagebox

contacts = {}

def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    
    if name and phone and email:
        contacts[name] = {"Phone": phone, "Email": email}
        messagebox.showinfo("Success", f"Contact {name} added successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Error", "All fields are required!")

def search_contact():
    name = entry_name.get()
    
    if name in contacts:
        contact = contacts[name]
        entry_phone.delete(0, tk.END)
        entry_phone.insert(0, contact["Phone"])
        entry_email.delete(0, tk.END)
        entry_email.insert(0, contact["Email"])
    else:
        messagebox.showwarning("Not found", f"Contact {name} not found.")

def update_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()

    if name in contacts:
        contacts[name] = {"Phone": phone, "Email": email}
        messagebox.showinfo("Success", f"Contact {name} updated successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Not found", f"Contact {name} does not exist.")

# Function to delete a contact
def delete_contact():
    name = entry_name.get()
    
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", f"Contact {name} deleted successfully!")
        clear_entries()
    else:
        messagebox.showwarning("Not found", f"Contact {name} does not exist.")

# Function to clear text fields
def clear_entries():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)

# Function to display all contacts
def display_contacts():
    if contacts:
        contact_list = ""
        for name, info in contacts.items():
            contact_list += f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}\n"
        messagebox.showinfo("Contacts", contact_list)
    else:
        messagebox.showinfo("Contacts", "No contacts available.")

root = tk.Tk()
root.title("Contact Book")
root.geometry("300x400")
root.configure(bg="pink")

# Create labels and entry widgets
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_phone = tk.Label(root, text="Phone:")
label_phone.grid(row=1, column=0, padx=10, pady=5)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1, padx=10, pady=5)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=2, column=0, padx=10, pady=5)
entry_email = tk.Entry(root)
entry_email.grid(row=2, column=1, padx=10, pady=5)

# Create buttons
btn_add = tk.Button(root, text="Add Contact", command=add_contact)
btn_add.grid(row=3, column=0, padx=10, pady=10)

btn_search = tk.Button(root, text="Search Contact", command=search_contact)
btn_search.grid(row=3, column=1, padx=10, pady=10)

btn_update = tk.Button(root, text="Update Contact", command=update_contact)
btn_update.grid(row=4, column=0, padx=10, pady=10)

btn_delete = tk.Button(root, text="Delete Contact", command=delete_contact)
btn_delete.grid(row=4, column=1, padx=10, pady=10)

btn_display = tk.Button(root, text="Display All Contacts", command=display_contacts)
btn_display.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

btn_clear = tk.Button(root, text="Clear", command=clear_entries)
btn_clear.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter main loop
root.mainloop()
