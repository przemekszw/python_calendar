import tkinter as tk
from tkinter import ttk

from downloader import Downloader

dnld = Downloader()
dictionary = dnld.extractor()

def display():
    for termin, godziny in dictionary.items():
        label_termin = ttk.Label(
            frame_daty,
            text=termin,)
        label_termin.pack()
        for godzina in godziny:
            label_godziny = ttk.Label(
                frame_daty,
                text=godzina,
                font=("Helvetica", 16))
            label_godziny.pack()

# window
window = tk.Tk()
window.geometry('600x400')
window.title("Kalendarz")

# Date frames
frame_daty = ttk.Frame(window, width=200, height=200, borderwidth=10, relief=tk.GROOVE)
frame_daty.pack()

# Exit button
b_exit = ttk.Button(window, text="Wyjdz", command=window.destroy)
b_exit.pack()

# Load button
b_load = ttk.Button(window, text="Zapodaj", command=lambda: display())
b_load.pack()





window.mainloop()