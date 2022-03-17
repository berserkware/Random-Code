import tkinter as tk
from tkinter.ttk import *
import requests
import json

window = tk.Tk(root)
window.title('Weather App')

p1 = tk.PhotoImage('B:/Code/Python/WeatherApp/Images/Sun.png')
window.iconphoto(True, p1)

label = tk.Label(
    text="\nAuckland, New Zealand",
    foreground="white",
    background="black",
    font=("arial", 15, "bold")
)

window.configure(bg='black')

label.pack()

window.mainloop()