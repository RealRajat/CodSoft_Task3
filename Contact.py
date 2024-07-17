import tkinter as tk
from tkinter import messagebox

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.contacts = []

        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.pack(padx=10, pady=10)

        self.name_entry = tk.Entry(self.root, width=40)
        self.name_entry.pack(padx=10, pady=10)

        self.phone_label = tk.Label(self.root, text="Phone:")
        self.phone_label.pack(padx=10, pady=10)

        self.phone_entry = tk.Entry(self.root, width=40)
        self.phone_entry.pack(padx=10, pady=10)

        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.pack(padx=10, pady=10)

        self.email_entry = tk.Entry(self.root, width=40)
        self.email_entry.pack(padx=10, pady=10)

        self.address_label = tk.Label(self.root, text="Address:")
        self.address_label.pack(padx=10, pady=10)

        self.address_entry = tk.Entry(self.root, width=40)
        self.address_entry.pack(padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Contact", command=self.add_contact)
        self.add_button.pack(padx=10, pady=10)

        self.search_label = tk.Label(self.root, text="Search:")
        self.search_label.pack(padx=10, pady=10)

        self.search_entry = tk.Entry(self.root, width=40)
        self.search_entry.pack(padx=10, pady=10)

        self.search_button = tk.Button(self.root, text="Search", command=self.search_contact)
        self.search_button.pack(padx=10, pady=10)

        self.contact_listbox = tk.Listbox(self.root, width=40)
        self.contact_listbox.pack(padx=10, pady=10)

        self.update_button = tk.Button(self.root, text="Update Contact", command=self.update_contact)
        self.update_button.pack(padx=10, pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Contact", command=self.delete_contact)
        self.delete_button.pack(padx=10, pady=10)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            contact = Contact(name, phone, email, address)
            self.contacts.append(contact)
            self.contact_listbox.insert(tk.END, f"{name} - {phone}")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Name and phone number are required.")

    def search_contact(self):
        search_term = self.search_entry.get()
        self.contact_listbox.delete(0, tk.END)

        for contact in self.contacts:
            if search_term in contact.name or search_term in contact.phone:
                self.contact_listbox.insert(tk.END, f"{contact.name} - {contact.phone}")

    def update_contact(self):
        try:
            selected_index = self.contact_listbox.curselection()[0]
            contact = self.contacts[selected_index]

            contact.name = self.name_entry.get()
            contact.phone = self.phone_entry.get()
            contact.email = self.email_entry.get()
            contact.address = self.address_entry.get()

            self.contact_listbox.delete(selected_index)
            self.contact_listbox.insert(selected_index, f"{contact.name} - {contact.phone}")
            self.clear_entries()
        except IndexError:
            messagebox.showerror("Error", "Select a contact to update.")

    def delete_contact(self):
        try:
            selected_index = self.contact_listbox.curselection()[0]
            del self.contacts[selected_index]
            self.contact_listbox.delete(selected_index)
        except IndexError:
            messagebox.showerror("Error", "Select a contact to delete.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

def main():
    root = tk.Tk()
    root.title("Contact Information Management System")
    contact_manager = ContactManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()
