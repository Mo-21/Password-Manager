from tkinter import *
from tkinter import messagebox
# Save Passwords ----------------


def add_password():
    web = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(web) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo("Some of the fields is empty")
    else:
        is_ok = messagebox.askokcancel(title=web, message="Are you sure you want to save?")
        if is_ok:
            with open(file="passwords.txt", mode="a") as file:
                file.write(f"\n{web} | {email} | {password}")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)


# UI Related ----------------
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=0)

# Labels
website_label = Label(text="Website", width=35)
website_label.grid(row=1, column=0)

email_label = Label(text="Email", width=35)
email_label.grid(row=2, column=0)

password_label = Label(text="Password", width=35)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_btn = Button(text="Generate Password", width=14)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add Password", command=add_password)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
