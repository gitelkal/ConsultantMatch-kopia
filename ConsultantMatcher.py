import os
import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD
import tkinter as tk
from tkinter import filedialog

def setup_root_window():
    """Setup the main application window."""
    root = TkinterDnD.Tk()
    root.geometry("800x600")
    root.configure(bg='#2e2e2e')
    root.title("Consultant Matcher")
    return root

def setup_ctk():
    """Setup customtkinter appearance and theme."""
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

def handle_file(file_path):
    """Handles the file path and updates the label."""
    file_name = os.path.basename(file_path)
    print(f"Selected file: {file_name}")
    new_label = ctk.CTkLabel(master=frame, text=f"Selected File: {file_name}", font=("Arial", 20))
    new_label.pack(pady=5, padx=20)

def on_drop(event):
    """Handles the file drop event."""
    file_path = event.data.strip()
    handle_file(file_path)

def upload_file():
    """Opens a file dialog to select a file."""
    file_path = filedialog.askopenfilename(filetypes=[("Document files", "*.docx *.pdf")])
    if file_path:
        handle_file(file_path)

def setup_ui(root):
    """Setup the user interface."""
    global frame
    frame = ctk.CTkFrame(master=root)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = ctk.CTkLabel(master=frame, text="Consultant Matcher", font=("Arial", 30))
    label.pack(pady=20, padx=20)

    upload_label = ctk.CTkLabel(master=frame, text="Upload a .docx or .pdf file:", font=("Arial", 16))
    upload_label.pack(pady=6, padx=20)

    upload_button = ctk.CTkButton(master=frame, text="Browse or Drag File", height=60, width=200, font=("Arial", 20), command=upload_file)
    upload_button.pack(pady=15)

if __name__ == "__main__":
    setup_ctk()
    root = setup_root_window()
    setup_ui(root)

    # Register the root window as a drop target and bind the drop event
    root.drop_target_register(DND_FILES)
    root.dnd_bind('<<Drop>>', on_drop)

    root.mainloop()
