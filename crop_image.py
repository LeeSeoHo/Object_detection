##################################
#This code is for cropping images#
##################################

import tkinter.filedialog
import os

from PIL import Image
from tkinter import *
from PIL import Image
from PIL import ImageTk

def image_crop(save_path):
    
    global origin_image
   
    path = tkinter.filedialog.askopenfilename()
    
    origin_image = path
   
    if len(path) > 0:

        h_get = int(score.get())
        
        img = Image.open(path)
        (img_w,img_h) = img.size
        grid_w = img_w #width are fixed
        grid_h = h_get #put numbers for cropping image's height
        range_w = (int)(img_w/grid_w)
        range_h = (int)(img_h/grid_h)
        
        
        i = 0

        for w in range(range_w):
            for h in range(range_h):
                bbox = (w*grid_w, h*grid_h-(0.6*grid_h), (w+1)*(grid_w), (h+1)*(grid_h))
                crop_img = img.crop(bbox)
                fname = "{}.jpg".format(i)
                savename = save_path + fname
                crop_img.save(savename)
                print('save file -> ' + savename + ' ...')
                i += 1              
def crop():
    loc = tkinter.filedialog.askdirectory()
    path, dirs, files = next(os.walk(loc))
    image_crop(path+'/')
    score.delete(0,END)

#interface in gui
win = Tk()
win.title("CROP")
win.geometry("200x120")

# button the GUI
btn = Button(win, text = "Select an image for Crop", command = crop)
btn.pack(side="bottom", fill="none", expand="yes", padx="10", pady="10")
score = Entry(win)
score.pack(side="bottom", fill="none", expand="yes", padx="10", pady="10")
Label(win,text = "* Input height for Crop Images *").pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")


#kick off the GUI
win.mainloop()

