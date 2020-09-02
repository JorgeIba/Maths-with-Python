import random

##AreaSquare = 4R^2
##AreaCircle = PI*R^2
# AreaSquare/4 = AreaCircle/PI
# PI = AreaCircle*4 / AreaSquare 

def calculatingPI(iterator):
    areaSquare = 0
    areaCircle = 0
    for i in range(iterator):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if( (x**2 + y**2)**(1/2) <= 1 ): #Is inside of the circle
            areaCircle += 1
        areaSquare +=1

    return areaCircle*4/areaSquare

print(  calculatingPI(1000000)  )
 

