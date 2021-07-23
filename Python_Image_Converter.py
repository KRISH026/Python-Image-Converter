from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image as image

root = Tk()
root.title("Image Converter")
root.iconbitmap("logo.ico")
root.geometry("500x550")
root. configure(bg="#1B1B21")

# create a function to convert png to jpg


def pngTojpg():
    global picture
    for item in frame.winfo_children():
        item.destroy()

    root.filename = filedialog.askopenfilename(title="Choose a Picture", filetypes=(("png files", "*.png"), ("all files", "*.*")))
    if root.filename != '':
        png_pic = image.open(root.filename)
        r_png_pic = png_pic.resize((450, 450), image.ANTIALIAS)
        picture = ImageTk.PhotoImage(r_png_pic)

        lab = Label(frame, image=picture)
        lab.pack()

        if file_name1.get() == '':
            lab.destroy()
            error = Label(root, text="Enter your file name please!!", fg="red", bg="#1b1b21", font="propaganda 12")
            error.grid(row=3, column=0, columnspan=2, pady=(2, 0))
        else:
            with open((root.filename), "rb") as pic:
                b_pic = pic.read()
            with open((file_name1.get()+".jpg"), "wb") as new_pic:
                jpg_pic = new_pic.write(b_pic)
            save = Label(root, text="Your picture is saves successfully!!", fg="green", bg="#1b1b21", font="propaganda 12")
            save.grid(row=3, column=0, columnspan=2, pady=(2, 0))

# create a function to convert jpg to png


def jpgTopng():
    global picture1
    for item in frame.winfo_children():
        item.destroy()

    root.filename = filedialog.askopenfilename(title="choose a picture",
                                               filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
    if root.filename != '':
        jpg_pic = image.open(root.filename)
        r_jpg_pic = jpg_pic.resize((450, 450), image.ANTIALIAS)
        picture1 = ImageTk.PhotoImage(r_jpg_pic)

        lab = Label(frame, image=picture1)
        lab.pack()

        if file_name1.get() == '':
            lab.destroy()
            error = Label(root, text="Enter your file name please!!", fg="red", bg="#1b1b21", font="propaganda 12")
            error.grid(row=3, column=0, columnspan=2, pady=(2, 0))
        else:
            with open((root.filename), "rb") as pic:
                b_pic = pic.read()
            with open((file_name1.get() + ".png"), "wb") as new_pic:
                png_pic = new_pic.write(b_pic)
            save = Label(root, text="Your picture is saves successfully!!", fg="green", bg="#1b1b21",
                         font="propaganda 12")
            save.grid(row=3, column=0, columnspan=2, pady=(2, 0))


def clearAll():
    for item in frame.winfo_children():
        item.destroy()
    file_name1.delete(0, END)


# create a frame"
frame = Frame(root, width=450, height=450)

# create a button
pngTojpg = Button(root, text="PNG_TO_JPG", padx=20, pady=3, font="none 12 bold", command=pngTojpg)
clear = Button(root, text="CLEAR", padx=20, pady=3, font="none 12 bold", command=clearAll)
jpgTopng = Button(root, text="JPG_TO_PNG", padx=20, pady=3, font="none 12 bold", command=jpgTopng)

# create a label for file name
file_name = Label(root, text="File Name", bg="pink", font="propaganda 12 bold")

# create an entry to define name of file
file_name1 = Entry(root, font="none 12 bold")


frame.grid(row=0, column=0, columnspan=3, padx=25, pady=(2, 5))
pngTojpg.grid(row=1, column=0)
clear.grid(row=1, column=1)
jpgTopng.grid(row=1, column=2)
file_name.grid(row=2, column=0, pady=(5, 0))
file_name1.grid(row=2, column=1, pady=(5, 0))
root.mainloop()

