import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import pygetwindow as gw # type: ignore
import time


active_window = gw.getActiveWindow()
print(active_window.title)
length = 0
def create_popup():
    root = tk.Tk()
    window_width = 300
    window_height = 100
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = screen_width - window_width + 300   
    y = screen_height - window_height - 75
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    root.resizable(False, False)
    root.overrideredirect(True) 

    gameText = tk.Label(
        root,
        text=f"youve been on {active_window.title} for {length} Minutes, you might wanna take a break",
        font = ("Roboto",12),
        wraplength=200,
        justify="left"
        )



    root.columnconfigure(1,weight=1)


    gameText.grid(row=1,column=0,sticky="nw",columnspan=2, padx=10)
    def NotifSlide():
        global x
        x -= 1 
        if x > screen_width - window_width: 
            root.geometry(f"{window_width}x{window_height}+{x}+{y}")
            root.after(2, NotifSlide)
        else:
            root.geometry(f"{window_width}x{window_height}+{screen_width - window_width}+{y}")
            root.after(5000, NotifClose)
    def NotifClose():
        global x
        x += 1 
        if x <= screen_width:
            root.geometry(f"{window_width}x{window_height}+{x}+{y}")
            root.after(2, NotifClose)
        else:
            root.destroy()
            
    while True :
        time.sleep(15*60)
        NotifSlide()

def schedule_popup():
    create_popup()
    root_scheduler.after(15 * 60 * 1000, schedule_popup)  
    length += 15

root_scheduler = tk.Tk()
root_scheduler.withdraw()  
schedule_popup()
root_scheduler.mainloop()

