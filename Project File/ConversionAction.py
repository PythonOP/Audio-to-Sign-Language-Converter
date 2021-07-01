from tkinter import *
from PIL import ImageTk, Image

img = list()


def conversionaction(text, signdisplayerframe):
    for Signwidgets in signdisplayerframe.winfo_children():
        Signwidgets.destroy()
    global img
    i = j = z = 0
    # 22 blocks
    words = text.split()
    for x in words:
        if not len(x) <= (22 - i):
            i = 0
            j += 1
        for alphabet in x:
            img.append(alphabet)
            img[z] = Image.open("../Project File/Sign_Pictures/" + alphabet + ".jpg")
            img[z] = img[z].resize((65, 65), Image.ANTIALIAS)
            img[z] = ImageTk.PhotoImage(img[z])
            signalphabet = Label(signdisplayerframe, image=img[z])
            signalphabet.grid(row=j, column=i, pady=10)
            z += 1
            i += 1
        signalphabet = Label(signdisplayerframe, bg='#1c1c1c', fg='#1c1c1c')
        signalphabet.grid(row=j, column=i)
        i += 1
