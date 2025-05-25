import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import time

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
    text="xxxxxxxxx for 45 Minutes",
    font = ("Roboto",12),
    wraplength=100,
    justify="left"
    )


preSize = Image.open("logo/terraria.png")
resized = preSize.resize((50, 50), Image.Resampling.LANCZOS)
photo = ImageTk.PhotoImage(resized)
logo = tk.Label(root, image=photo)
logo.image = photo 


root.columnconfigure((0,1,2),weight=1)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)


gameText.grid(row=1,column=0,sticky="w",columnspan=2, padx=10)
logo.grid(row=0,column=0, sticky="ns")

def NotifSlide():
    global x
    x -= 1 
    if x > screen_width - window_width: 
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        root.after(2, NotifSlide)
    else:
        root.geometry(f"{window_width}x{window_height}+{screen_width - window_width}+{y}")
        root.after(5000, notifclose)
def notifclose():
    global x
    x += 1 
    if x < screen_width - window_width:
        root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        root.after(2, notifclose)
    else:
        root.destroy()
        

NotifSlide()
root.mainloop()


