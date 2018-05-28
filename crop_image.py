from PIL import Image
from tkinter import *
from PIL import Image
from PIL import ImageTk
import tkinter.filedialog


#setup for cropping image
def image_crop(save_path):
   
    path = tkinter.filedialog.askopenfilename()
   
    if len(path) > 0:

        img = Image.open(path)
        (img_h,img_w) = img.size
        grid_w = img_h
        grid_h = 100
        range_w = (int)(img_w/grid_w)
        range_h = (int)(img_h/grid_h)
        
        i = 0

        for w in range(range_w):
            for h in range(range_h):
                bbox = (w*grid_w, h*grid_h-(0.6*grid_h), (w+1)*(grid_w), (h+1)*(grid_h))
                #the reason why i code like the above is that the width is fixed
                crop_img = img.crop(bbox)
                fname = "{}.jpg".format(i)
                savename = save_path + fname
                crop_img.save(savename)
                print('save file -> ' + savename + ' ...')
                i += 1

#pick directory for saving crop images
#pick image file for crop
def crop():
    loc = tkinter.filedialog.askdirectory()
    path, dirs, files = next(os.walk(loc))
    image_crop(path+'/')


#initializing toolkit, interface of gui
win = Tk()
win.title("CROP")
win.geometry("200x50")

#buttons for gui
btn = Button(win, text = "Select an image for Crop", command = crop)
btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")

#kick off the gui
win.mainloop()

