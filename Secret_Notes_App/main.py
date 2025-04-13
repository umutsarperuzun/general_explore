from tkinter import *
from cryptography.fernet import Fernet
import base64
import hashlib

# === Generate Fernet key from user-provided master key ===
def get_fernet_key(master_key):
    hashed = hashlib.sha256(master_key.encode()).digest()
    return base64.urlsafe_b64encode(hashed)

# === Encrypt and save the note to file ===
def encrypt():
    title = entry1.get()
    message = text.get("1.0", END).strip()
    master_key = entry2.get()

    if not (title and message and master_key):
        label4.config(text="Please fill in all fields.")
        return

    try:
        key = get_fernet_key(master_key)
        cipher = Fernet(key)
        encrypted_message = cipher.encrypt(message.encode())

        # Append encrypted note
        with open("notes.txt", "ab") as file:
            file.write(f"[TITLE:{title}]\n".encode())
            file.write(encrypted_message + b"\n")

        # Clear inputs after saving
        entry1.delete(0, END)
        text.delete("1.0", END)
        entry2.delete(0, END)

        label4.config(text="Note encrypted and saved.")

    except Exception:
        label4.config(text="Encryption failed.")

# === Decrypt and display the note based on title and master key ===
def decrypt():
    title = entry1.get()
    master_key = entry2.get()

    if not (title and master_key):
        label4.config(text="Please enter title and master key.")
        return

    try:
        key = get_fernet_key(master_key)
        cipher = Fernet(key)

        with open("notes.txt", "rb") as file:
            lines = file.readlines()

        found = False
        for i in range(len(lines)):
            if lines[i].strip() == f"[TITLE:{title}]".encode():
                encrypted_message = lines[i + 1].strip()
                decrypted_message = cipher.decrypt(encrypted_message).decode()

                text.delete("1.0", END)
                text.insert("1.0", decrypted_message)

                label4.config(text="Message decrypted successfully.")
                found = True
                break

        if not found:
            label4.config(text="Title not found.")

    except Exception:
        label4.config(text="Decryption failed. Wrong key or corrupted data.")

# === UI Setup ===
window = Tk()
window.title("Secret Notes")
window.config(padx=30, pady=30)

# === Logo Image ===
img = PhotoImage(file="Secret_Notes_App/istockphoto-1477970031-612x612.png")
img = img.subsample(3, 3)
label = Label(window, image=img)
label.pack()

# === Title Entry ===
label1 = Label(text="Enter your title", pady=10)
label1.pack()

entry1 = Entry()
entry1.pack()

# === Secret Text ===
label2 = Label(text="Enter your secret", pady=10)
label2.pack()

text = Text(width=30, height=10)
text.pack()

# === Master Key Entry ===
label3 = Label(text="Enter master key", pady=10)
label3.pack()

entry2 = Entry(show="*")  # Hide characters for master key
entry2.pack()

# === Status Label ===
label4 = Label(text="", pady=10)
label4.pack()

# === Buttons ===
button1 = Button(text="Save and Encrypt", command=encrypt, padx=10, pady=10)
button1.pack()

button2 = Button(text="Decrypt", command=decrypt, padx=10, pady=10)
button2.pack()


window.mainloop()
