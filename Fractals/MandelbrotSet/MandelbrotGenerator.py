from tkinter import *
import random
import numpy as np
import cmath
import os

exponent = int(input("Entry the exponent bigger than 0\n"))
#TO DRAW

HEIGHT, WIDTH = 650, 650
root = Tk()
root.geometry("{}x{}".format(WIDTH, HEIGHT))

canvas = Canvas(root, height = HEIGHT, width = WIDTH, bg = "black" )
canvas.pack()

def paintPoint(x, y, color): #To paint a point in canvas
    canvas.create_oval(x,y,x+1,y+1, width = 0, fill = color)

########################################################################
#Numbers and stuff

#?Mapping
reMapX = np.linspace(-2,2, WIDTH )
reMapY = np.linspace(-2,2, HEIGHT )

xs = list(reMapX)
ys = list(reMapY)


#?From list to string
strX = ""
for num in xs:
    strX = strX + " " + str(num)

strY = ""
for num in ys:
    strY = strY + " " + str(num)

strT = strX + " " + strY


#? String passed by text, wich c++ will read
with open("input.txt", "w+") as f:
    f.write(str(WIDTH) + " " + str(HEIGHT) + " " + str(exponent) + " " +strT)

lines = []


os.system(r" CalculationMandelbrotGenerator.exe < input.txt") #TODO C++ make calculus

#? Reading results
with open("output.txt", "r+") as f:
    lines = f.readlines()


#? Graphing
for line in lines:
    x,y,n = map(int, line.strip("\n").split(" "))
    if n >= 30:
            paintPoint(x,y, "gray{}".format(n))




root.mainloop()