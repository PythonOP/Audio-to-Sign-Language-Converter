from tkinter import messagebox
from ConversionAction import conversionaction
import speech_recognition as sr


def speech(signdisplayerframe):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            conversionaction(text, signdisplayerframe)
        except sr.UnknownValueError:
            messagebox.showerror("Error", "No audio received")
