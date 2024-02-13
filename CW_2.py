import tkinter as tk
from tkinter import messagebox, Menu, filedialog, simpledialog, Scrollbar, Text, Toplevel, Label, Entry, Button
from cryptography.fernet import Fernet
import os

def load_cryptography():
    # In a real application, you would use a persistent key
    key = Fernet.generate_key()
    return Fernet(key)

fernet = None

def authenticate(username, password):
    return True  
def register(username, password):
    return True  


def encryption_key_window():
    def set_encryption_key():
        global fernet
        key = key_entry.get().encode()
        fernet = Fernet(key)
        key_window.destroy()
        messagebox.showinfo("Key Set", "Encryption key is set successfully.")

    key_window = Toplevel(app)
    key_window.title("Set Encryption Key")
    key_window.geometry("400x100")
    
    key_label = Label(key_window, text="Enter your encryption key:")
    key_label.pack(pady=5)
    
    key_entry = Entry(key_window, width=50)
    key_entry.pack(pady=5)
    
    set_key_button = Button(key_window, text="Set Key", command=set_encryption_key)
    set_key_button.pack(pady=5)


def send_message():
    if not fernet:
        messagebox.showerror("Encryption Key Not Set", "Please set the encryption key before sending a message.")
        return
    message = text_area.get("1.0", tk.END)
    encrypted_message = fernet.encrypt(message.encode())
    print(f"Sending encrypted message: {encrypted_message}")
    

def receive_message(encrypted_message):
    if not fernet:
        messagebox.showerror("Encryption Key Not Set", "Please set the encryption key before receiving a message.")
        return
    try:
        decrypted_message = fernet.decrypt(encrypted_message).decode()
        messagebox.showinfo("Received Message", f"You've got a new message: {decrypted_message}")
    except Exception as e:
        messagebox.showerror("Decryption Error", f"An error occurred during decryption: {str(e)}")


app = tk.Tk()
app.title("Advanced Secure Messaging Application")
app.geometry("800x600")


menu_bar = Menu(app)
app.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=lambda: new_file())
file_menu.add_command(label="Open", command=lambda: open_file())
file_menu.add_command(label="Save", command=lambda: save_file())
file_menu.add_command(label="Save As", command=lambda: save_as_file())
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)

# Edit menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo", command=lambda: text_area.edit_undo())
edit_menu.add_command(label="Redo", command=lambda: text_area.edit_redo())
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=lambda: text_area.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: text_area.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: text_area.event_generate("<<Paste>>"))

# Settings menu for encryption
settings_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Settings", menu=settings_menu)
settings_menu.add_command(label="Set Encryption Key", command=encryption_key_window)

# Help menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=lambda: about())

# Status bar
status_bar = tk.Label(app, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Text area with scrollbar
text_scroll = Scrollbar(app)
text_scroll.pack(side=tk.RIGHT, fill=tk.Y)
text_area = Text(app, undo=True, yscrollcommand=text_scroll.set)
text_area.pack(expand=True, fill='both')
text_scroll.config(command=text_area.yview)

# File management functions
def new_file():
    text_area.delete(1.0, tk.END)
    app.title("New File - Advanced Secure Messaging Application")

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        text_area.delete(1.0, tk.END)
        with open(file_path, 'r') as file:
            text_area.insert(1.0, file.read())
        app.title(f"{os.path.basename(file_path)} - Advanced Secure Messaging Application")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get(1.0, tk.END))
        app.title(f"{os.path.basename(file_path)} - Advanced Secure Messaging Application")

