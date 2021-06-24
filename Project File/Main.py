from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.title("Text to Sign Language Converter")
root.geometry('1200x700')


def p2():
    for widgets in root.winfo_children():
        widgets.destroy()
    img = list()

    def conversionaction():
        for widgets in signDisplayerFrame.winfo_children():
            widgets.destroy()
        global img
        text = t1.get()
        i = 1
        z = 0
        for x in text:
            if x.isspace():
                signAlphabet = Label(signDisplayerFrame, padx=32)
                signAlphabet.grid(row=0, column=i)
                i += 1
            else:
                img.append(x)
                img[z] = Image.open("../Project File/Sign_Pictures/" + x + ".jpg")
                img[z] = img[z].resize((75, 75), Image.ANTIALIAS)
                img[z] = ImageTk.PhotoImage(img[z])
                signAlphabet = Label(signDisplayerFrame, image=img[z])
                signAlphabet.grid(row=0, column=i)
                i += 1
                z += 1

    # Text Frame
    inputFrame = LabelFrame(root, text="Text", pady=80)
    inputFrame.pack(fill=BOTH)
    l1 = Label(inputFrame, text="Enter your text to convert:").pack()
    t1 = Entry(inputFrame, width=80)
    t1.pack()

    midButton = Button(root, text="Convert", padx=40, pady=20, command=conversionaction)
    midButton.pack(anchor=CENTER)

    # Sign Frame
    signDisplayerFrame = LabelFrame(root, text="Sign Language")
    signDisplayerFrame.pack(fill=BOTH, expand=1)
    l2 = Label(signDisplayerFrame, text="")
    l2.grid(row=0, column=0)


Button(root, text='Start', command=p2).pack()


root.mainloop()
