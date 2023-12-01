from gtts import gTTS
import os
import tkinter as tk
from tkinter import ttk

def text_to_speech(text, language='en', slow_speed=False):
    
    tts = gTTS(text=text, lang=language, slow=slow_speed)

    
    tts.save("output.wav")

   
    os.system("vlc output.wav")

def on_submit():
    input_text = text_entry.get()
    language = language_var.get()
    slow_speed = slow_speed_var.get()
    
    text_to_speech(input_text, language, slow_speed)


window = tk.Tk()
window.title("Text-to-Speech Converter")

label = ttk.Label(window, text="Enter the text:")
label.grid(row=0, column=0, padx=10, pady=10)

text_entry = ttk.Entry(window, width=40)
text_entry.grid(row=0, column=1, padx=10, pady=10)

language_label = ttk.Label(window, text="Select language:")
language_label.grid(row=1, column=0, padx=10, pady=10)

language_var = tk.StringVar()
language_combobox = ttk.Combobox(window, textvariable=language_var, values=['en', 'es', 'fr', 'de'])
language_combobox.grid(row=1, column=1, padx=10, pady=10)
language_combobox.set('en')

slow_speed_var = tk.BooleanVar()
slow_speed_checkbox = ttk.Checkbutton(window, text="Use slow speed", variable=slow_speed_var)
slow_speed_checkbox.grid(row=2, column=0, columnspan=2, pady=10)

submit_button = ttk.Button(window, text="Convert and Play", command=on_submit)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)


window.mainloop()
