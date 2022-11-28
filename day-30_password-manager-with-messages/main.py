from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

FONT_BOLD = ("Arial", 10, "bold")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_pass_func():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_choices = [choice(letters) for i in range(randint(8, 10))]
    number_choices = [choice(numbers) for i in range(randint(2, 4))]
    symbol_choices = [choice(symbols) for i in range(randint(2, 4))]

    password_list = letter_choices + number_choices + symbol_choices

    shuffle(password_list)

    generated_password = "".join(password_list)
    entry_password.insert(0, generated_password)
    pyperclip.copy(generated_password)

    password_list.clear()

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = entry_web.get()

    mail = entry_mail.get()

    password = entry_password.get()

    new_data = {
        web: {
            "email": mail,
            "password": password
        }
    }
    if len(web) == 0 or len(mail) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning!", message="Please make sure you don't leave any fields empty ")
    else:
        is_ok = messagebox.askokcancel(title="Check your info", message=f"Website: {web}\nEmail: {mail}\n"
                                                                        f"Password: {password}"f"\nDo you confirm? ")
        if is_ok:
            try:
                with open("json_file.txt", mode="r") as file:
                    data = json.load(file)
                    data.update(new_data)
                with open("json_file.txt", mode="w") as file:
                    json.dump(data, file, indent=4)
            except FileNotFoundError:
                with open("json_file.txt", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            entry_web.delete(0, END)
            entry_password.delete(0, END)


def search_website():
    web = entry_web.get()
    try:
        with open("json_file.txt", mode="r") as file:
            data = json.load(file)
            messagebox.showinfo(title=f"{web}", message=f'Email: {data[web]["email"]}\n'
                                                        f'Password: {data[web]["password"]}')
    except KeyError:
        messagebox.showerror(title="Warning!", message=f'No "{web}" Data Was Found!\nPlease Check Your Input.')
    except FileNotFoundError:
        messagebox.showerror(title="Warning!", message="No Data File Found")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas()

image = PhotoImage(file="logo.png")
canvas.config(width=200, height=200)
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

web_label = Label(text="Website: ", font=FONT_BOLD)
web_label.grid(column=0, row=1)

mail_label = Label(text="Email/Username: ", font=FONT_BOLD)
mail_label.grid(column=0, row=2)

password_label = Label(text="Password: ", font=FONT_BOLD)
password_label.grid(column=0, row=3)

entry_web = Entry(width=36)
entry_web.grid(column=1, row=1)
entry_web.focus()


entry_mail = Entry(width=55)
entry_mail.grid(column=1, row=2, columnspan=2)
entry_mail.insert(0, "elif@gmail.com")


entry_password = Entry(width=36)
entry_password.grid(column=1, row=3)


generate_password = Button(text="Generate Password", command=generate_pass_func)
generate_password.grid(column=2, row=3)

add = Button(text="Add", width=47, command=save)
add.grid(column=1, row=4, columnspan=2)

search = Button(text="Search", width=15, command=search_website)
search.grid(column=2, row=1)


window.mainloop()
