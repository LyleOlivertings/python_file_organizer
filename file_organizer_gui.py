import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil

def organize_files():
    path = folder_path.get()
    if not path:
        messagebox.showerror("Error", "Please select a folder first!")
        return

    try:
        categories = {
            "Images": [".jpg", ".jpeg", ".png", ".gif"],
            "Documents": [".pdf", ".docx", ".txt"],
            "Spreadsheets": [".xlsx", ".csv"],
            "Others": []
        }

        for category in categories:
            os.makedirs(os.path.join(path, category), exist_ok=True)

        moved_files = 0
        for filename in os.listdir(path):
            if filename == "desktop.ini":
                continue
            
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(filename)[1].lower()
                
                destination = "Others"
                for category, extensions in categories.items():
                    if file_extension in extensions:
                        destination = category
                        break
                
                dest_path = os.path.join(path, destination, filename)
                shutil.move(file_path, dest_path)
                moved_files += 1

        status_label.config(text=f"Success! Organized {moved_files} files!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Create main window
root = tk.Tk()
root.title("File Organizer")
root.geometry("400x200")

# GUI Elements
label = tk.Label(root, text="Select a folder to organize:")
label.pack(pady=10)

folder_path = tk.StringVar()

def select_folder():
    path = filedialog.askdirectory()
    if path:
        folder_path.set(path)

select_button = tk.Button(root, text="Browse Folder", command=select_folder)
select_button.pack()

status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=10)

organize_button = tk.Button(root, text="Organize Files!", command=organize_files)
organize_button.pack()

root.mainloop()