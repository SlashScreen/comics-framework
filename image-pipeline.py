from tkinter import filedialog as fd
import os
from PIL import Image

directory = fd.askdirectory()
contents = os.listdir(directory)
num = len(os.listdir("imgs/"))
progress = 1
for filename in contents:
    name = directory+"/"+filename
    try:
        image = Image.open(name)
        image.save("imgs/img"+str(num)+".png")
        print ("Progress: "+ str( ( round ( progress/len( contents ) ,2) ) *100 )+"%")
        progress += 1
        num += 1
    except Exception as e:
        print(e)
print("Done!")
