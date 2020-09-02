from tkinter import *
import random
import numpy as np
import cmath
import os

#! TO DRAW

HEIGHT, WIDTH = 400, 400
root = Tk()
root.geometry("{}x{}".format(WIDTH, HEIGHT))

canvas = Canvas(root, height = HEIGHT, width = WIDTH, bg = "black" )
canvas.pack()

def paintPoint(x, y, color): #To paint a point in canvas
    canvas.create_oval(x,y,x+1,y+1, width = 0, fill = color)
############################################################################
#! MATH AND STUFF

def funcion(x, y, real, imag, complexC, maxIterating):
    z = complex(real,imag)
    n=0
    while n < maxIterating:
        z = cmath.exp(z**3) + complexC #TODO The Principal Function
        if z.__abs__() > 2:
            break
        n +=1

    #? Painting
    if n >= 25:
        paintPoint(x,y, "gray{}".format(n))
    elif 4<=n<25:
        paintPoint(x,y, "green{}".format(n%3 + 2))
    else:
        paintPoint(x,y, "RoyalBlue{}".format(n+1))

            


reMapX = np.linspace(-2,2, WIDTH )
reMapY = np.linspace(-2,2, HEIGHT ) #? Mapping pixels into numbers between -2,2

for indexX, x in enumerate(reMapX):
    for indexY, y in enumerate(reMapY):
        funcion(indexX, indexY, x,y, complex(-0.59) ,100) #? Painting every point in the pixel




root.mainloop()