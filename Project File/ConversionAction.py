from tkinter import *
from PIL import ImageTk, Image

img = list()


def conversionaction(text,signdisplayerframe):
    for Signwidgets in signdisplayerframe.winfo_children():
        Signwidgets.destroy()
    global img
    i = 1
    z = 0
    # 20 blocks
    for x in text:
        if x.isspace():
            signalphabet = Label(signdisplayerframe, padx=32)
            signalphabet.grid(row=0, column=i)
            i += 1
        else:
            img.append(x)
            img[z] = Image.open("../Project File/Sign_Pictures/" + x + ".jpg")
            img[z] = img[z].resize((75, 75), Image.ANTIALIAS)
            img[z] = ImageTk.PhotoImage(img[z])
            signalphabet = Label(signdisplayerframe, image=img[z])
            signalphabet.grid(row=0, column=i)
            i += 1
            z += 1