from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


  password_letters = [choice(letters) for i in range(randint(8, 10))]
  password_numbers = [choice(numbers) for i in range(randint(2, 4))]
  password_symbols = [choice(symbols) for i in range(randint(2, 4))]
  password_list = password_letters + password_numbers + password_symbols

  shuffle(password_list)

  password = "".join(password_list)
  password_entry.delete(0, END)
  password_entry.insert(0, password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def Save():

    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()
    

    if len(website) != 0 and len(password) != 0:
        is_ok = messagebox.askokcancel(title= website, message=f"These are the details entered for {website}:\n Email: {email_username}\n Password: {password}\n Is it ok to save?")
        if is_ok:
            f = open("data.txt" , "a")
            f.write(website + ' | ' + email_username + ' | ' + password + "\n")
            f.close()
            website_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
    else:
        messagebox.showwarning(message= "Please don't leave any fields empty!")


# ---------------------------- UI SETUP ------------------------------- #



window = Tk()
window.title('Password Manager')
window.config(padx=30, pady=30 )


canvas = Canvas(height = 200, width = 200)
logo_image = PhotoImage(file= "logo.png")
canvas.create_image(100,100, image = logo_image)
canvas.grid(column=1 ,row=0)

website_label = Label(text="Website: ", fg="#000000", font= ('Helvetica', 15))
website_label.grid(column=0, row=1)

email_username_label = Label(text = "Email/Username: ", fg="#000000", font= ('Helvetica', 15))
email_username_label.grid(column=0, row=2 )

Password_label = Label(text= "Password: ", fg="#000000", font=("Helvetica", 15))
Password_label.grid(column=0, row=3)


website_entry = Entry(width= 35)
website_entry.grid(column=1, row=1, columnspan= 2)
website_entry.focus()


email_username_entry = Entry(width = 35)
email_username_entry.grid(column=1, row=2, columnspan= 2)
email_username_entry.insert(0, "tomtomi@gmail.com")


password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)


add_button = Button(text="Add", width=35, command=Save)
add_button.grid(column=1, row=4, columnspan=2 )

window.mainloop()