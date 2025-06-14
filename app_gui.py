import tkinter as tk
from tkinter import messagebox 
from caesarCipher import caesar_shift # importing from source 


def encrypt():
    msg = entry_message.get()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("invalid input", "shift key must be an integer: ")
        return 
    result = caesar_shift(msg, shift)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result) 

def decrypt():
    msg= entry_message.get()
    try:
        shift = int(entry_shift.get())
    except ValueError:
        messagebox.showerror("invalid input", "shift key must be an integer: ")
        return
    result = caesar_shift(msg, -shift)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, result)

#ui setup

root = tk.Tk()
root.title("caesar cipher gui")

# Message input
tk.Label(root, text="Enter Message:").grid(row=0, column=0, padx=10, pady=10)
entry_message = tk.Entry(root, width=50)
entry_message.grid(row=0, column=1, padx=10, pady=10)

#shift key input

tk.Label(root, text="Enter shift key: ").grid(row=1, column=0, padx=10, pady=10)
entry_shift = tk.Entry(root, width=10)
entry_shift.grid(row=1, column=1, sticky='w', padx=10, pady=10)

#button
encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.grid(row=2, column=1,sticky='w', padx=10, pady=10)

# output 
tk.Label(root, text="Result:").grid(row=3, column=0, padx=10, pady=10)
output_text = tk.Text(root, height=5, width= 50)
output_text.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()