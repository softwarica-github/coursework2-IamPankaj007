import tkinter as tk
from tkinter import messagebox, Menu, filedialog, simpledialog, Scrollbar, Text, Button
from cryptography.fernet import Fernet

# Static key for encryption/decryption
static_key = b'VQM57HBEeRWBw_5ewGxHrp_Hm4c0jnqtw9h5VVsZRzE='
fernet = Fernet(static_key)

# Placeholder functions for future implementation
contacts = {}  # Simulate a contacts database

def authenticate(username, password):
    # This is a placeholder for real authentication logic
    return True

def send_message():
    # Encrypt and display the message
    message = text_area.get("1.0", tk.END).strip()
    if message:
        encrypted_message = fernet.encrypt(message.encode())
        messagebox.showinfo("Encrypted Message", f"Encrypted message: {encrypted_message.decode()}")
        text_area.delete('1.0', tk.END)
    else:
        messagebox.showinfo("Info", "Please enter a message.")

def show_encrypted_message():
    # Ask for an encrypted message, decrypt it, and show the decrypted message
    encrypted_message = simpledialog.askstring("Decrypt Message", "Enter the encrypted message:")
    if encrypted_message:
        try:
            decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
            messagebox.showinfo("Decrypted Message", f"Decrypted message: {decrypted_message}")
        except Exception as e:
            messagebox.showerror("Error", "Invalid encryption message.")

def add_contact():
    # Future feature for adding a contact
    contact_name = simpledialog.askstring("Add Contact", "Enter the contact name:")
    if contact_name:
        contacts[contact_name] = contact_name  # Simulate saving the contact

def settings():
    # Future feature for settings
    messagebox.showinfo("Settings", "Settings feature coming soon.")

# GUI related functions for file management
def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete(1.0, tk.END)
            text_area.insert(1.0, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))

# Additional function for the "About" dialog
def about():
    messagebox.showinfo("About", "Secure Messaging Application\nVersion 1.0\nUsing Fernet for encryption.")

# Function to show the login dialog at startup
def show_login_dialog():
    # Login dialog to authenticate user
    username = simpledialog.askstring("Username", "Enter your username:")
    password = simpledialog.askstring("Password", "Enter your password:", show="*")
    if not authenticate(username, password):
        messagebox.showerror("Login failed", "Incorrect username or password")
        app.quit()
    else:
        messagebox.showinfo("Login successful", "You are logged in.")

# Set up the main application window
app = tk.Tk()
app.title("Secure Messaging Application")
app.geometry("500x400")

# Menu setup
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

# Text area and scrollbar
text_scroll = Scrollbar(app)
text_scroll.pack(side=tk.RIGHT, fill=tk.Y)

text_area = Text(app, undo=True, yscrollcommand=text_scroll.set)
text_area.pack(expand=True, fill='both')

text_scroll.config(command=text_area.yview)

# Buttons for sending and showing encrypted messages
send_button = Button(app, text="Send Message", command=send_message)
send_button.pack(side=tk.BOTTOM, fill=tk.X, pady=5)

decrypt_button = Button(app, text="Decrypt Message", command=show_encrypted_message)
decrypt_button.pack(side=tk.BOTTOM, fill=tk.X)

# Status bar to show application status messages
status_bar = tk.Label(app, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

def update_status(message):
    status_bar.config(text=message)

# Enhance the send_message function to update the status bar
def send_message():
    message = text_area.get("1.0", tk.END)
    # Strip the message of leading/trailing whitespace
    if message.strip() == "":
        messagebox.showinfo("Empty Message", "Please enter a message to send.")
        return
    # Encrypt the message
    encrypted_message = fernet.encrypt(message.encode())
    # The encrypted message is in bytes, convert it to a base64 encoded string for display
    encrypted_message_str = encrypted_message.decode('utf-8')
    # Show the encrypted message in a messagebox
    messagebox.showinfo("Encrypted Message", f"Encrypted message:\n\n{encrypted_message_str}")
    # Clear the text area after showing the encrypted message
    text_area.delete('1.0', tk.END)
    # Update the status bar
    update_status("Message sent successfully.")

# Additional menu options for future features
contact_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Contacts", menu=contact_menu)
contact_menu.add_command(label="Add Contact", command=add_contact)

settings_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Settings", menu=settings_menu)
settings_menu.add_command(label="Settings", command=settings)

# Run the application
if __name__ == "__main__":
    show_login_dialog()
    app.mainloop()
