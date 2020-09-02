#Linear Regression - Least Squares 

import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction as Frac

#########################
#? Entry of the points

n = int(input("Entry the cuantity of points.\n"))
listPoints = []

for i in range(n): 
    #x,y = map(int, input("Entry x, y: ").split(" ") )
    x,y = map(int, input().split(" ") )
    listPoints.append( (x,y) )
    
#########################
#? initialization and Math stuff
    
a1 = a2 = a3 = a4 = 0

# a1 = sum( xi^2 )
# a2 = sum( xi )
# a3 = sum( xi*yi )
# a4 = sum( yi  )

for point in listPoints:
    a1 += point[0]**2
    a2 += point[0]
    a3 += point[0]*point[1]
    a4 += point[1]
    
b = Frac(   (a3*a2 - a1*a4)/(a2**2 - n*a1)  ).limit_denominator(100)
m = Frac( (a4 - n*b)/a2  ).limit_denominator(100)

#########################
#? Plotting

limNegX = -10
limPosX = 10

x = np.linspace( limNegX , limPosX , 2)
y = m*x + b

figure, graph = plt.subplots(1)

for point in listPoints:
    graph.scatter( point[0], point[1]  )
    
graph.set_title("f(x) = {}*x + {}".format( m , b ))
graph.set_xlabel("x")
graph.set_ylabel("y")
graph.grid()
graph.plot(x,y)




    


