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
TextFont = Font(family="Microsoft New Tai Lue", size="30", weight="bold")

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


openningLogo = None


def Main():
    for widgets in root.winfo_children():
        widgets.destroy()
    global bg
    bg = Image.open("../Project File/background.jpg")
    bg = bg.resize((1600, 800), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(bg)
    c = Canvas(root, width=1200, height=700)
    c.pack(fill=BOTH, expand=True)

    c.create_image(0, 0, image=bg, anchor='nw')
    c.create_text(800, 350, text='Audio to Sign Langauge Converter', font=TextFont)

    global openningLogo
    openningLogo = Image.open("../Project File/NielitLogo.jpg")
    openningLogo = openningLogo.resize((300, 180), Image.ANTIALIAS)
    openningLogo = ImageTk.PhotoImage(openningLogo)
    c.create_image(600, 100, image=openningLogo, anchor='nw')

    b1 = Button(root, text='About', font=ButtonFont, padx=40, border=4)
    b2 = Button(root, text='Credits', font=ButtonFont, padx=40, border=4)
    b3 = Button(root, text='Start', font=ButtonFont, command=start, padx=40, border=4)

    c.create_window(180, 600, window=b1, anchor='nw')
    c.create_window(650, 600, window=b2, anchor='nw')
    c.create_window(1200, 600, window=b3, anchor='nw')


Main()
root.mainloop()
