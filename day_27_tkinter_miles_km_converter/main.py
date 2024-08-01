from tkinter import *


def calculate():
    miles = float(miles_input.get())
    km = round(miles * 1.60934, 2)
    km_convert.config(text=km)


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

equal_label = Label(text="is equal to")
equal_label.grid(row=1, column=0)

km_label = Label(text="Km")
km_label.grid(row=1, column=2)

km_convert = Label(text=0)
km_convert.grid(row=1, column=1)

button = Button(text="Calculate", command=calculate)
button.grid(row=2, column=1)

window.mainloop()
