from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
from speechModule import speech

root = Tk()
root.title("Text to Sign Language Converter")
# root.attributes('-fullscreen', True)
root.state("zoomed")
root.geometry('1200x700')

# All fonts used
ButtonFont = Font(family="Helvetica", size="18", weight="normal")
LabelFont = Font(family="Microsoft New Tai Lue", size="12", weight="normal")
TextFont = Font(family="Helvetica", size="31", weight="bold")
TextFont2 = Font(family="Helvetica", size="16", weight="normal")
TextFont3 = Font(family="Helvetica", size="23", weight="normal")

micLabel = None
bg = None
Logo = None
heartLogo = None


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
    bg = Image.open("background.jpg")
    bg = bg.resize((1150, 800), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(bg)
    c = Canvas(root, width=1600, height=800)
    c.pack(fill=BOTH, expand=True)

    c.create_image(0, 0, image=bg, anchor='nw')
    c.create_text(450, 200, text='Audio to Sign Language Translator', font=TextFont, fill='white')
    c.create_rectangle(170, 230, 500, 235, outline='white', fill='white')
    c.create_text(110, 300, text='Indian Sign Language(ISL) is used in the deaf community all over India. '
                                 '\nBut ISL is not used in deaf schools to teach deaf children. Teacher training '
                                 '\nprograms do not orient teachers towards teaching methods that use ISL. '
                                 '\nThere is no teaching material that incorporates sign language.', font=TextFont2, fill='white', anchor='nw')
    c.create_text(110, 450, text='This translator is based on Indian Sign Language(ISL) which can be used for '
                                 '\ntraining the people learning the sign language. The system is currently designed '
                                 '\nfor one to one communication of people who understands sign to people who don\'t.', anchor='nw', font=TextFont2, fill='white')
    c.create_rectangle(1100, 0, 1800, 800, outline='#1c1c1c', fill='#1c1c1c')

    global Logo
    Logo = Image.open("NielitLogo.png")
    Logo = Logo.resize((230, 150), Image.ANTIALIAS)
    Logo = ImageTk.PhotoImage(Logo)
    c.create_image(1210, 100, image=Logo, anchor='nw')

    c.create_text(1240, 350, text='Made with', font=TextFont3, anchor='nw', fill='white')
    global heartLogo
    heartLogo = Image.open("../Project File/heartLogo.png")
    heartLogo = heartLogo.resize((70, 70), Image.ANTIALIAS)
    heartLogo = ImageTk.PhotoImage(heartLogo)
    c.create_image(1380, 330, image=heartLogo, anchor='nw')
    c.create_text(1240, 385, text='by the students of\nNIELIT Agartala Centre', font=TextFont2, anchor='nw', fill='white')

    b = Button(root, text='Start', font=ButtonFont, bg='#34c9eb', activebackground='#34c9eb', command=start, padx=20, border=5)
    c.create_window(1275, 600, window=b, anchor='nw')


main()
root.mainloop()
