from tkinter import *
from tkinter import messagebox
import random
import pyperclip


def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_symbols + password_letters + password_numbers

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    password_entry.insert(0, password)
    pyperclip.copy(password)


def save_password():
    website_entry_string = website_entry.get()
    email_entry_string = email_entry.get()
    password_entry_string = password_entry.get()

    if len(website_entry_string) == 0 or len(password_entry_string) == 0:
        message_empty = messagebox.showinfo(title="Empty", message="Please fill all the entry")

    else:
        is_ok = message = messagebox.askokcancel(title=website_entry_string,
                                                 message=f"These are the details entered: \n\n"
                                                         f"Email: {email_entry_string} "
                                                         f"\nPassword: {password_entry_string} \n"
                                                         f"Is it ok to save?")

        if is_ok:
            with open("data.txt", "a", encoding="utf-8") as file:
                file.write(f"{website_entry_string} | {email_entry_string} | {password_entry_string}\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.minsize(width=550, height=450)
window.resizable(0, 0)

canvas = Canvas(width=200, height=200)
image = PhotoImage(file="logo.png")
canvas_image = canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", font=("Antonio", 10, "bold"))
website_label.grid(row=1, column=0)
website_entry = Entry(width=55)
website_entry.grid(row=1, column=1, columnspan=2)


email = Label(text="Email/Username:", font=("Antonio", 10, "bold"))
email.grid(row=2, column=0)
email_entry = Entry(width=55)
email_entry.insert(0, "passwordmanager@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)


password_label = Label(text="Password:", font=("Antonio", 10, "bold"))
password_label.grid(row=3, column=0)
password_entry = Entry(width=34)
password_entry.grid(row=3, column=1)


generate_button = Button(text="Generate Password", font=("Antonio", 8, "bold"), command=generate_password)
generate_button.grid(row=3, column=2)
add_button = Button(text="Add", font=("Antonio", 8, "bold"), width=47, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()