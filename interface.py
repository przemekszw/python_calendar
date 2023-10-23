from tkinter import *
from tkinter import ttk

from downloader import Downloader

dnld = Downloader()
dictionary = dnld.extractor()
root = Tk()


def display():
    i = ""
    x = 1
    for termin, godziny in dictionary.items():
        i += f"{termin}\n "
        print("+")
        for godzina in godziny:
            i += f"({godzina}) "
            print("-")
        label_disp.config(text=i)
        i += f" \n"


    label_disp.grid(column=x, row=x)



root.title("Kalendarz")

b_exit = ttk.Button(root, text="Wyjdz",command=root.destroy)
b_load = ttk.Button(root, text="Zapodaj",command=lambda: display())
label_disp = ttk.Label(root, text="Tutaj wyświetlą się terminy")
frame = ttk.Frame(root,padding=10)

b_exit.grid(column=0,row=0)

b_load.grid(column=10,row=2)

show_frame = ttk.Label(frame, text="Siema Byq")
frame.grid()



root.mainloop()