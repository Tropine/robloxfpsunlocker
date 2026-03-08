import os
import re
import tkinter as tk
from tkinter import messagebox

# Path to Roblox settings file
file_path = os.path.expandvars(r"%localappdata%\Roblox\GlobalBasicSettings_13.xml")

def load_current_value():
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = f.read()

        match = re.search(r'<int name="FramerateCap">(\d+)</int>', data)

        if match:
            value_entry.delete(0, tk.END)
            value_entry.insert(0, match.group(1))
        else:
            messagebox.showerror("Error", "FramerateCap value not found.")

    except FileNotFoundError:
        messagebox.showerror("Error", f"File not found:\n{file_path}")

def save_value():
    try:
        new_value = value_entry.get()

        if not new_value.isdigit():
            messagebox.showerror("Error", "Please enter a valid number.")
            return

        with open(file_path, "r", encoding="utf-8") as f:
            data = f.read()

        updated = re.sub(
            r'<int name="FramerateCap">\d+</int>',
            f'<int name="FramerateCap">{new_value}</int>',
            data
        )

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(updated)

        messagebox.showinfo("Success", "Framerate cap updated!")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("Roblox FPS Cap Editor")
root.geometry("300x150")

tk.Label(root, text="Framerate Cap:").pack(pady=5)

value_entry = tk.Entry(root)
value_entry.pack(pady=5)

tk.Button(root, text="Load Current Value", command=load_current_value).pack(pady=5)
tk.Button(root, text="Save", command=save_value).pack(pady=5)

root.mainloop()