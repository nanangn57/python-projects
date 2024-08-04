from tkinter import *
from tkinter import messagebox
import random
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pw():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    ran_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    ran_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    ran_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = ran_letters + ran_symbols + ran_numbers
    random.shuffle(password_list)

    password = "".join(password_list)

    current_pw = pw_entry.get()
    if len(current_pw) > 0:
        pw_entry.delete(0, END)

    pw_entry.insert(0, string=password)

    window.clipboard_clear()
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pw():
    web = web_entry.get()
    user = user_entry.get()
    pw = pw_entry.get()
    new_data = {
        web: {
            "email": user,
            "password": pw
        }
    }

    if len(web) == 0 or len(pw) == 0 or len(user) == 0:
        messagebox.showwarning(title="Missing value to save",
                               message="Please fill in missing fields before saving")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered: "
                                                          f"\nEmail:{user} \nPassword: {pw} \n Is it ok to save?")
        if is_ok:
            try:
                with open("pw.json", "r") as file:
                    pw_data = json.load(file)
                    pw_data.update(new_data)
            except FileNotFoundError:
                with open("pw.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("pw.json", "w") as file:
                    json.dump(pw_data, file, indent=4)
            finally:
                web_entry.delete(0, END)
                pw_entry.delete(0, END)


def search_pw():
    web = web_entry.get()

    with open("pw.json", "r") as file:
        pw_data = json.load(file)
        try:
            email = pw_data[web]['email']
            pw = pw_data[web]['password']
        except KeyError:
            messagebox.showwarning(title="Error", message="No website information available")
        else:
            messagebox.showinfo(title=f"{web}", message=f"Email: {email} \nPassword: {pw}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=1, column=2)

# ----- Label -----
web_label = Label(text="Website:")
web_label.grid(row=2, column=1, sticky=E)

user_label = Label(text="Email/Username:")
user_label.grid(row=3, column=1, sticky=E)

pw_label = Label(text="Password:")
pw_label.grid(row=4, column=1, sticky=E)

# ----- Entry/ Button -----
web_entry = Entry(width=32)
web_entry.grid(row=2, column=2, sticky=W)
web_entry.focus()

user_entry = Entry(width=51)
user_entry.grid(row=3, column=2, columnspan=2, sticky=W)
user_entry.insert(0, "anhnguyen.workmail@gmail.com")

pw_entry = Entry(width=32)
pw_entry.grid(row=4, column=2, sticky=W)

search_button = Button(text="Search", command=search_pw, width=14)
search_button.grid(row=2, column=3, sticky=E)

gen_button = Button(text="Generate Password", command=gen_pw, width=14)
gen_button.grid(row=4, column=3, sticky=E)

add_button = Button(text="Add", command=save_pw, width=43)
add_button.grid(row=5, column=2, columnspan=2, sticky=W)

# ----- Pop-up -----

window.mainloop()
