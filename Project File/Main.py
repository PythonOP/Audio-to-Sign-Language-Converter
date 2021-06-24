from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Text to Sign Language Converter")
root.geometry('1200x700')

img = list()

def conversionAction():
    for widgets in f2.winfo_children():
        widgets.destroy()
    global img
    text = t1.get()
    i = 1
    z = 0
    for x in text:
        if(x.isspace()):
            Label(f2, padx=32).grid(row=0, column=i)
            i += 1
        else:
            img.append(x)
            img[z] = Image.open("../Project File/Sign_Pictures/"+x+".jpg")
            img[z] = img[z].resize((75, 75), Image.ANTIALIAS)
            img[z] = ImageTk.PhotoImage(img[z])
            l = Label(f2, image=img[z])
            l.grid(row=0, column=i)
            i += 1
            z += 1



f1 = LabelFrame(root, text="Text", pady=80)
f1.pack(fill=BOTH)
l1 = Label(f1, text="Enter your text to convert:").pack()
t1 = Entry(f1, width=80)
t1.pack()

b3 = Button(root, text="Convert", padx=40, pady=20, command=conversionAction)
b3.pack(anchor=CENTER)

f2 = LabelFrame(root, text="Sign Language")
f2.pack(fill=BOTH, expand=1)
l2 = Label(f2, text="")
l2.grid(row=0, column=0)

root.mainloop()
