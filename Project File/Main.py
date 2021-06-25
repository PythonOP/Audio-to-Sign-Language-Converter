from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
root = Tk()
root.title("Text to Sign Language Converter")
root.state("zoomed")
root.geometry('1200x700')

# All fonts used
ButtonFont = Font(family="Helvetica", size="18", weight="normal")
LabelFont = Font(family="Microsoft New Tai Lue", size="12", weight="normal")

img = list()


def start():
    for widgets in root.winfo_children():
        widgets.destroy()

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
    l1 = Label(inputFrame, text="Enter your text to convert:", font=LabelFont)
    l1.pack()
    t1 = Entry(inputFrame, width=60, font=ButtonFont)
    t1.pack()

    midButton = Button(root, text="Convert", font=ButtonFont, border=4, padx=40, command=conversionaction)
    midButton.pack(anchor='center')

    # Sign Frame
    signDisplayerFrame = LabelFrame(root, text="Sign Language")
    signDisplayerFrame.pack(fill=BOTH, expand=1)
    l2 = Label(signDisplayerFrame, text="")
    l2.grid(row=0, column=0)

    Button(root, text="Back", font=ButtonFont, padx=40, border=4, command=Main).pack()



def Main():
    for widgets in root.winfo_children():
        widgets.destroy()
    global openningLogo
    openningLogo = Image.open("../Project File/NielitLogo.jpg")
    openningLogo = openningLogo.resize((300, 180), Image.ANTIALIAS)
    openningLogo = ImageTk.PhotoImage(openningLogo)
    Label(root, image=openningLogo).place(x=580, y=80)
    Button(root, text='About', font=ButtonFont, padx=40, border=4).place(x=80, y=700)
    Button(root, text='Credits', font=ButtonFont, padx=40, border=4).place(x=670, y=700)
    Button(root, text='Start', font=ButtonFont, command=start, padx=40, border=4).place(x=1200, y=700)


Main()
root.mainloop()
