import tkinter as tk
from tkinter import messagebox, Menu

def send_message():
    # Example of a basic "encryption" - reversing the message. Replace with a real encryption method.
    message = message_entry.get()
    encrypted_message = message[::-1]  # Simple encryption by reversing the message
    print(f"Sending encrypted message: {encrypted_message}")
    # Add networking code here to send the encrypted_message

def receive_message():
    # Placeholder function for simulating message reception
    encrypted_message = "egaugnal nohtyP nraeL"  # Example encrypted message
    # Decrypt the message. Here, simply reverse it back. Replace with a real decryption method.
    decrypted_message = encrypted_message[::-1]
    messagebox.showinfo("Received Message", f"You've got a new message: {decrypted_message}")

def about():
    messagebox.showinfo("About", "Secure Messaging Application\nVersion 1.0")

app = tk.Tk()
app.title("Secure Messaging Application")
app.geometry("500x300")  # Making the window larger

menu_bar = Menu(app)
app.config(menu=menu_bar)

# File Menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", command=app.quit)

# Help Menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

# Frame for User Authentication
auth_frame = tk.Frame(app)
auth_frame.pack(pady=10)

username_label = tk.Label(auth_frame, text="Username:")
username_label.grid(row=0, column=0)
username_entry = tk.Entry(auth_frame)
username_entry.grid(row=0, column=1)

password_label = tk.Label(auth_frame, text="Password:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(auth_frame, show="*")
password_entry.grid(row=1, column=1)

# Frame for Messaging
message_frame = tk.Frame(app)
message_frame.pack(pady=10)

message_label = tk.Label(message_frame, text="Message:")
message_label.grid(row=0, column=0)
message_entry = tk.Entry(message_frame, width=50)
message_entry.grid(row=0, column=1)

# Send and Receive buttons
send_button = tk.Button(message_frame, text="Send Message", command=send_message)
send_button.grid(row=1, column=0, pady=10)
receive_button = tk.Button(message_frame, text="Receive Message", command=receive_message)
receive_button.grid(row=1, column=1, pady=10)

app.mainloop()
