from tkinter import *
from tkinter import ttk

from downloader import Downloader

dnld = Downloader()
dictionary = dnld.extractor()
root = Tk()


def display():
    for termin, godziny in dictionary.items():
        label_termin = ttk.Label(frame_daty, text=termin, width=12, anchor='w')
        label_termin.grid(sticky='w')
        #(sticky='w', padx=(0, 10)))
        #i += f"{termin}\n "
        for godzina in godziny:
            label_godziny = ttk.Label(frame_daty, text=godzina, width=12, anchor='w')
            label_godziny.grid(sticky='w')
        #i += f" \n"




root.title("Kalendarz")
frame_daty = ttk.Frame(root)
b_exit = ttk.Button(root, text="Wyjdz",command=root.destroy)
b_load = ttk.Button(root, text="Zapodaj",command=lambda: display())
label_disp = ttk.Label(root, text="Tutaj wyświetlą się terminy")

b_exit.grid(column=0,row=0)
b_load.grid(column=1,row=1)
frame_daty.grid()


root.mainloop()