import customtkinter as ctk
from tkinter import *
import speech_recognition as sr
import threading
from googletrans import Translator

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("1000x500")
recognizer = sr.Recognizer()
translator = Translator()

def listen():
    global is_listening
    if not is_listening:
        is_listening = True
        mbtn.configure(text="Stop Listening")
        start_listening_thread()
    else:
        is_listening = False
        mbtn.configure(text="Listen")

def start_listening_thread():
    global listen_thread
    listen_thread = threading.Thread(target=listen_continuous)
    listen_thread.start()

def listen_continuous():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        while is_listening:
            audio = recognizer.listen(source)
            try:
                recognized_text = recognizer.recognize_google(audio)
                entry.insert(ctk.END, recognized_text + " ")
                entry.see(ctk.END)
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                entry.insert(ctk.END, "Error occurred. Please try again.\n")
                entry.see(ctk.END)

def translate():
    text = entry.get("1.0", "end-1c").strip()
    result = translator.translate(text, dest='hi')
    output.delete("1.0", "end")
    output.insert("1.0", result.text)

label = ctk.CTkLabel(app, text="LANGUAGE TRANSLATOR")
label.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=40, fill='both', expand=True)

languages = ["English", "Hindi", "Telgu", "Spanish"]
combo1 = ctk.CTkComboBox(master=frame, values=languages)
combo1.pack(padx=15, pady=5)
combo1.place(x=100, y=30)

entry = ctk.CTkTextbox(master=frame, width=300, height=200)
entry.pack(pady=12, padx=10)
entry.place(x=100, y=70)

combo2 = ctk.CTkComboBox(master=frame, values=languages)
combo2.pack(padx=15, pady=5)
combo2.place(x=500, y=30)

output = ctk.CTkTextbox(master=frame, width=300, height=200)
output.pack(pady=12, padx=10)
output.place(x=500, y=70)

is_listening = False
listen_thread = None

label1 = ctk.CTkLabel(master=frame, text="")
label1.pack(pady=20)
label1.place(x=400, y=110)

pic = PhotoImage(file="mic.png")
mic = pic.subsample(20, 20)

mbtn = ctk.CTkButton(master=frame, text="", image=mic, height=40, width=10, corner_radius=100, command=listen)
mbtn.pack(pady=10, padx=10)
mbtn.place(x=400, y=70)

tbtn = ctk.CTkButton(master=frame, text='TRANSLATE', command=translate)
tbtn.pack(pady=10, padx=10)
tbtn.place(x=370, y=300)

app.mainloop()
