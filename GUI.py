from tkinter import *
from PIL import Image, ImageTk

### Variables 
images_folder_path = "./images/"

### Init
screen_root = Tk()

profile_image_prep = Image.open(images_folder_path+"profile_image_example.jpeg")

width, height = profile_image_prep.size
if width > 150:
    proportion = width / 150
    new_height = int(width / proportion)
    profile_image_prep = profile_image_prep.resize((110, new_height)) 

profile_image = ImageTk.PhotoImage(profile_image_prep)
lbl_profile_image = Label(screen_root, image=profile_image)
lbl_profile_image.image = profile_image
lbl_profile_image.place(relx=200, y=250,  anchor="ne")


screen_root.title("Formulário Interface")

screen_root.configure(background="#f0f")

screen_root.geometry("700x600")

var = StringVar()





screen_root.mainloop()