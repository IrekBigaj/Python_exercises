# #100days of code - Day 27 - Miles to km converter

import tkinter
window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=200)
window.config(padx=50, pady=50)


def button_clicked():
    distance = float(miles_data.get())
    distance_km = float(distance * 1.609)
    distance_label["text"] = f"{distance_km}"
    pass


miles_data = tkinter.Entry(width=10)
miles_data.grid(column=1, row=0)
# miles_data.config(padx=10, pady=10)

miles_label = tkinter.Label(text="Miles", font=("Arial", 10))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10, pady=10)

equal_label = tkinter.Label(text="is equal to", font=("Arial", 10))
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

km_label = tkinter.Label(text="Km", font=("Arial", 10))
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

distance_label = tkinter.Label(text="0", font=("Arial", 10))
distance_label.grid(column=1, row=1)
distance_label.config(padx=10, pady=10)

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)
button.config(padx=10, pady=10)




window.mainloop()  # na koniec programu
