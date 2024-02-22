import tkinter as tk
from tkinter import messagebox, Menu, filedialog, simpledialog, Scrollbar, Text, Button, Listbox, END
from cryptography.fernet import Fernet

# Static key for encryption/decryption, replace with your own secure key for a real application
static_key = b'VQM57HBEeRWBw_5ewGxHrp_Hm4c0jnqtw9h5VVsZRzE='
fernet = Fernet(static_key)

# Placeholder for a contacts database
contacts = {}

def authenticate(username, password):
    # Placeholder for authentication logic
    return True

def encrypt_message():
    # Encrypts the message in the text area
    message = text_area.get("1.0", tk.END).strip()
    if message:
        encrypted_message = fernet.encrypt(message.encode())
        text_area.delete('1.0', tk.END)
        text_area.insert('1.0', encrypted_message.decode())
        update_status("Message encrypted.")
    else:
        messagebox.showinfo("Empty Message", "Please enter a message to encrypt.")

def decrypt_message():
    # Decrypts the message in the text area
    encrypted_message = text_area.get("1.0", tk.END).strip()
    if encrypted_message:
        try:
            decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
            text_area.delete('1.0', tk.END)
            text_area.insert('1.0', decrypted_message)
            update_status("Message decrypted.")
        except Exception as e:
            messagebox.showerror("Decryption Error", "Invalid encrypted message.")
    else:
        messagebox.showinfo("Empty Message", "Please enter an encrypted message to decrypt.")

def send_message():
    # Simulates sending the encrypted message
    message = text_area.get("1.0", tk.END).strip()
    if message:
        # In a real application, integrate actual send logic here
        messagebox.showinfo("Send Message", "Encrypted message sent.")
        text_area.delete('1.0', tk.END)
        update_status("Message sent.")
    else:
        messagebox.showinfo("Empty Message", "Please enter a message to send.")

def add_contact():
    # Adds a new contact
    contact_name = simpledialog.askstring("Add Contact", "Enter the contact name:")
    if contact_name:
        contacts[contact_name] = contact_name
        contacts_listbox.insert(END, contact_name)
        update_status(f"Contact '{contact_name}' added.")

def view_contacts():
    # Displays the contacts window
    contacts_window = tk.Toplevel(app)
    contacts_window.title("Contacts")
    contacts_window.geometry("200x300")
    for contact in contacts:
        tk.Label(contacts_window, text=contact).pack()

def settings():
    # Placeholder for settings window
    messagebox.showinfo("Settings", "Settings feature coming soon.")

def new_file():
    text_area.delete('1.0', tk.END)
    update_status("New file opened.")

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete('1.0', tk.END)
            text_area.insert('1.0', file.read())
            update_status(f"Opened {file_path}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get('1.0', tk.END))
            update_status(f"Saved to {file_path}")

def about():
    messagebox.showinfo("About", "Secure Messaging Application\nVersion 1.0\nUsing Fernet for encryption.")

def show_login_dialog():
    username = simpledialog.askstring("Username", "Enter your username:")
    password = simpledialog.askstring("Password", "Enter your password:", show="*")
    if authenticate(username, password):
        messagebox.showinfo("Login Successful", "You are now logged in.")
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")
        app.quit()

app = tk.Tk()
app.title("Secure Messaging Application")
app.geometry("600x400")

menu_bar = Menu(app)
app.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

contacts_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Contacts", menu=contacts_menu)
contacts_menu.add_command(label="View Contacts", command=view_contacts)
contacts_menu.add_command(label="Add Contact", command=add_contact)

settings_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Settings", menu=settings_menu)
settings_menu.add_command(label="Settings", command=settings)

text_scroll = Scrollbar(app)
text_scroll.pack(side=tk.RIGHT, fill=tk.Y)

text_area = Text(app, undo=True, yscrollcommand=text_scroll.set)
text_area.pack(expand=True, fill='both')

text_scroll.config(command=text_area.yview)

encrypt_button = Button(app, text="Encrypt Message", command=encrypt_message)
encrypt_button.pack(side=tk.BOTTOM, fill=tk.X, pady=2)

decrypt_button = Button(app, text="Decrypt Message", command=decrypt_message)
decrypt_button.pack(side=tk.BOTTOM, fill=tk.X, pady=2)

send_button = Button(app, text="Send Message", command=send_message)
send_button.pack(side=tk.BOTTOM, fill=tk.X, pady=2)

contacts_listbox = Listbox(app)
# Positioning the contacts list box on the right side might require additional layout configuration.

status_bar = tk.Label(app, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

def update_status(message):
    status_bar.config(text=message)

if __name__ == "__main__":
    show_login_dialog()
    app.mainloop()
