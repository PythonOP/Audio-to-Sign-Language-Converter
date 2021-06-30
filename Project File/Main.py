from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
from speechModule import speech

root = Tk()
root.title("Text to Sign Language Converter")
root.state("zoomed")
root.geometry('1200x700')

# All fonts used
ButtonFont = Font(family="Helvetica", size="18", weight="normal")
LabelFont = Font(family="Microsoft New Tai Lue", size="12", weight="normal")
TextFont = Font(family="Helvetica", size="30", weight="normal")


micLabel = None
bg = None
openningLogo = None


def start():
    for widgets in root.winfo_children():
        widgets.destroy()

    # Sign Frame
    signdisplayerframe = LabelFrame(root, text="Sign Language")
    signdisplayerframe.pack(fill=BOTH, expand=1)
    l2 = Label(signdisplayerframe, text="")
    l2.grid(row=0, column=0)

    # Audio Frame
    inputframe = LabelFrame(root, text="Audio")
    inputframe.pack(fill=BOTH)

    global micLabel
    micLabel = Image.open('../Project File/mic.png')
    micLabel = micLabel.resize((50, 80), Image.ANTIALIAS)
    micLabel = ImageTk.PhotoImage(micLabel)
    b = Button(inputframe, image=micLabel, command=lambda: speech(signdisplayerframe), bg='red',
               activebackground='#00ff00',
               height=80, width=60, border=4)
    b.pack()

    Button(root, text="Back", bg='#6dd5ff', activebackground='#6dd5ff', padx=40, font=ButtonFont, border=4, command=main).pack(pady=20)


def main():
    for widgets in root.winfo_children():
        widgets.destroy()
    global bg
    bg = Image.open("../Project File/background.jpg")
    bg = bg.resize((1600, 800), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(bg)
    c = Canvas(root, width=1200, height=700)
    c.pack(fill=BOTH, expand=True)

    c.create_image(0, 0, image=bg, anchor='nw')
    c.create_text(800, 370, text='Audio to Sign Language Converter', font=TextFont)

    global openningLogo
    openningLogo = Image.open("../Project File/NielitLogo.jpg")
    openningLogo = openningLogo.resize((300, 180), Image.ANTIALIAS)
    openningLogo = ImageTk.PhotoImage(openningLogo)
    c.create_image(600, 100, image=openningLogo, anchor='nw')

    b1 = Button(root, text='About', font=ButtonFont, bg='#6dd5ff', activebackground='#6dd5ff', padx=40, border=4)
    b2 = Button(root, text='Start', font=ButtonFont, bg='#6dd5ff', activebackground='#6dd5ff', command=start, padx=40, border=4)
    b3 = Button(root, text='Credits', font=ButtonFont, bg='#6dd5ff', activebackground='#6dd5ff', padx=40, border=4)

    c.create_window(200, 600, window=b1, anchor='nw')
    c.create_window(670, 600, window=b2, anchor='nw')
    c.create_window(1140, 600, window=b3, anchor='nw')


main()
root.mainloop()
