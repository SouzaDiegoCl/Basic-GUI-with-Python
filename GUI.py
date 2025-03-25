from tkinter import *
from PIL import Image, ImageTk

### Variables 
images_folder_path = "./"

### Init
screen_root = Tk()


profile_image = ImageTk.PhotoImage(Image.open("./image.png"))
lbl_profile_image = Label(screen_root, image=profile_image)
lbl_profile_image.image = profile_image
lbl_profile_image.place(x=10, y=50)


screen_root.title("Formulário Interface")

screen_root.configure(background="#f0f")

screen_root.geometry("700x600")

var = StringVar()





screen_root.mainloop()