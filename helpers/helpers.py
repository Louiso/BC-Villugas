import math
import tkinter as tk
def resize(photo, width, height):
    scaleX = math.floor(photo.width() / width) 
    scaleY = math.floor(photo.height() / height)
    photo = photo.subsample(x = scaleX, y = scaleY)
    return photo