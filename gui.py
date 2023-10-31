import customtkinter as ctk 
import tkinter.messagebox as tkmb 
from tkinter import *


# Selecting GUI theme - dark, light , system (for system default) 
ctk.set_appearance_mode("dark") 

# Selecting color theme - blue, green, dark-blue 
ctk.set_default_color_theme("blue") 

app = ctk.CTk() 
app.geometry("1000x500") 

label = ctk.CTkLabel(app,text="LANGUAGE TRANSLATOR") 
label.pack(pady=20) 


frame = ctk.CTkFrame(master=app) 
frame.pack(pady=20,padx=40,fill='both',expand=True) 


languages = ["English", "Hindi","Telgu","Spanish"]
combo1 = ctk.CTkComboBox(master=frame, values=languages)
combo1.pack(padx = 15,pady=5)
combo1.place(x=100, y=30)

entry= ctk.CTkTextbox(master=frame,width=300, height=200) 
entry.pack(pady=12,padx=10) 
entry.place(x=100, y=70)

combo2 = ctk.CTkComboBox(master=frame, values=languages)
combo2.pack(padx = 15,pady=5)
combo2.place(x=500, y=30)

output= ctk.CTkTextbox(master=frame,width=300, height=200) 
output.pack(pady=12,padx=10) 
output.place(x=500, y=70)

def listen():
    label1.configure(text = "listening....")
    # label1.configure(text = "")
label1 = ctk.CTkLabel(master=frame,text="")
label1.pack(pady=20)
label1.place(x=400, y= 110)

pic = PhotoImage(file="mic.png")
mic = pic.subsample(20, 20) 

mbtn = ctk.CTkButton(master=frame,text="", image=mic, height=40, width=10, corner_radius=100,command=listen) 
mbtn.pack(pady=10,padx=10) 
mbtn.place(x=400, y=70)

tbtn = ctk.CTkButton(master=frame,text='TRANSLATE') 
tbtn.pack(pady=10,padx=10) 
tbtn.place(x=370, y=300)




app.mainloop()
