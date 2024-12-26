from PIL import Image
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def select_source_folder():
    folder_selected = filedialog.askdirectory()
    source_folder.set(folder_selected)

def select_destination_folder():
    folder_selected = filedialog.askdirectory()
    destination_folder.set(folder_selected)

def start_renaming():
    src_folder = source_folder.get()
    dest_folder = destination_folder.get()
    img_format = format_var.get()

    if not src_folder or not dest_folder or not img_format:
        messagebox.showerror("Error", "All fields are required")
        return

    files = os.listdir(src_folder)
    extensions = ['jpg', 'jpeg', 'png', 'gif']
    counter = 1

    for file in files:
        ext = file.split(".")[-1]
        if ext.lower() in extensions:
            im = Image.open(os.path.join(src_folder, file))
            filepath = os.path.join(dest_folder, f"{counter}.{img_format}")
            im.save(filepath)
            counter += 1

    messagebox.showinfo("Success", "Images renamed successfully")

root = tk.Tk()
root.title("Image Renamer")

source_folder = tk.StringVar()
destination_folder = tk.StringVar()
format_var = tk.StringVar(value="png")

tk.Label(root, text="Source Folder:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=source_folder, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_source_folder).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Destination Folder:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=destination_folder, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_destination_folder).grid(row=1, column=2, padx=10, pady=10)

tk.Label(root, text="Format:").grid(row=2, column=0, padx=10, pady=10)
format_options = ["jpg", "jpeg", "png", "gif"]
tk.OptionMenu(root, format_var, *format_options).grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Start Renaming", command=start_renaming).grid(row=3, column=0, columnspan=3, pady=20)

root.mainloop()