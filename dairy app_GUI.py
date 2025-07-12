import tkinter as tk
from tkinter import messagebox
import datetime
import os

PASSWORD = "ananya123"

def check_password():
    entered_password = password_entry.get()
    if entered_password == PASSWORD:
        login_window.destroy()
        open_main_app()
    else:
        messagebox.showerror("Wrong Password", "Incorrect password! Try again.")

def open_main_app():
    root.deiconify()
    root.title("Diary APP")
    root.geometry("800x600")
    root.configure(bg="#FFFBDE")

    label = tk.Label(root, text="DEAR DIARY", bg="#91C8E4", font=("Arial", 22, "bold"))
    label.pack(pady=40)

    text_area = tk.Text(root, height=20, width=80, font=("Arial", 14), wrap="word", bd=2, relief="ridge")
    text_area.pack(pady=20)

    def save_entry():
        entry_text = text_area.get("1.0", tk.END).strip()
        if entry_text == "":
            messagebox.showwarning("Empty Entry", "Please write something before saving!")
            return
        current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"Diary_{current_time}.txt"
        with open(filename, "w") as file:
            file.write(entry_text)
        messagebox.showinfo("Saved!", f"Your entry has been saved as {filename}")
        text_area.delete("1.0", tk.END)

    savebutton = tk.Button(root, text="Save Entry", command=save_entry, font=("Arial", 14), bg="#FF9587", fg="black", padx=10, pady=5)
    savebutton.pack(pady=20)

    def view_entries():
        files = [f for f in os.listdir() if f.startswith("Diary_") and f.endswith(".txt")]

        if not files:
            messagebox.showinfo("No Entries", "No diary entries found.")
            return

        view_window = tk.Toplevel(root)
        view_window.title("View Diary Entries")
        view_window.geometry("700x500")
        view_window.configure(bg="#91C8E4")

        label = tk.Label(view_window, text="Saved Entries", font=("Arial", 18, "bold"), bg="#91C8E4")
        label.pack(pady=10)

        scrollbar = tk.Scrollbar(view_window)
        scrollbar.pack(side="right", fill="y")

        listbox = tk.Listbox(view_window, font=("Arial", 14), fg='black', height=15, width=50, bg="#FFD8D8", selectbackground="#FFFCFB", selectforeground="black", yscrollcommand=scrollbar.set)
        listbox.pack(pady=10)
        scrollbar.config(command=listbox.yview)

        for f in files:
            listbox.insert(tk.END, f)

        def show_content():
            selected = listbox.curselection()
            if not selected:
                messagebox.showwarning("No Selection", "Select a file to view its content.")
                return
            filename = listbox.get(selected[0])
            with open(filename, "r") as file:
                content = file.read()

            content_window = tk.Toplevel(view_window)
            content_window.title(filename)
            content_window.geometry("600x400")
            content_window.configure(bg="#555879")

            text = tk.Text(content_window, wrap="word", font=("Arial", 13), bg="#FEEBF6")
            text.pack(expand=True, fill="both", padx=10, pady=10)
            text.insert(tk.END, content)
            text.config(state="disabled")

        open_button = tk.Button(view_window, text="Open Entry", command=show_content, font=("Arial", 14), bg="#FF9587", fg="black", padx=10, pady=5)
        open_button.pack(pady=10)

    viewbutton = tk.Button(root, text="View Entries", command=view_entries, font=("Arial", 14), bg="#FF9587", fg="black", padx=10, pady=5)
    viewbutton.pack(pady=10)

root = tk.Tk()
root.withdraw() 
login_window = tk.Toplevel()
login_window.title("Login")
login_window.geometry("400x200")
login_window.configure(bg="#91C8E4")

label = tk.Label(login_window, text="Enter Password to Access Diary", font=("Arial", 14, "bold"), bg="#FFECCC")
label.pack(pady=20)

password_entry = tk.Entry(login_window, show="*", font=("Arial", 14), width=20)
password_entry.pack(pady=10)

login_button = tk.Button(login_window, text="Login", command=check_password, font=("Arial", 12), bg="#FF9587", fg="white")
login_button.pack(pady=10)

root.mainloop()







