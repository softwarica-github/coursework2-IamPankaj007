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
