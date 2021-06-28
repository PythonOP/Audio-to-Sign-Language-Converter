from tkinter import *
from PIL import ImageTk, Image

img = list()


def conversionaction(text, signdisplayerframe):
    for Signwidgets in signdisplayerframe.winfo_children():
        Signwidgets.destroy()
    global img
    i = 0
    j = 0

    z = 0
    # 21 blocks
    words = text.split()
    for x in words:
        if len(x) <= (21 - i):
            for alphabet in x:
                img.append(alphabet)
                img[z] = Image.open("../Project File/Sign_Pictures/" + alphabet + ".jpg")
                img[z] = img[z].resize((70, 70), Image.ANTIALIAS)
                img[z] = ImageTk.PhotoImage(img[z])
                signalphabet = Label(signdisplayerframe, image=img[z])
                signalphabet.grid(row=j, column=i, pady=10)
                z += 1
                i += 1
            signalphabet = Label(signdisplayerframe)
            signalphabet.grid(row=j, column=i, padx=10)
            i += 1
        else:
            i = 0
            j += 1
            for alphabet in x:
                img.append(alphabet)
                img[z] = Image.open("../Project File/Sign_Pictures/" + alphabet + ".jpg")
                img[z] = img[z].resize((70, 70), Image.ANTIALIAS)
                img[z] = ImageTk.PhotoImage(img[z])
                signalphabet = Label(signdisplayerframe, image=img[z])
                signalphabet.grid(row=j, column=i, pady=10)
                z += 1
                i += 1
            signalphabet = Label(signdisplayerframe)
            signalphabet.grid(row=j, column=i, padx=10)
            i += 1



