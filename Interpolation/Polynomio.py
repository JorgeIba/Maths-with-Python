from fractions import Fraction as Frac
import matplotlib.pyplot as plt
import numpy as np

#Polynomio's class with only the methods that interpolation needs
class Polynomio: 
    def __init__(self, values):
        self.coeff = []
        self.coeff[:] = values

    def __add__(self, A): #Overloading + operator
        coeffi = []
        if len(A.coeff) > len(self.coeff):
            coeffi[:] = A.coeff
            for i in range(len(self.coeff)):
                coeffi[i] += Frac(self.coeff[i])
        else:
            coeffi[:] = self.coeff
            for i in range(len(A.coeff)):
                coeffi[i] += Frac(A.coeff[i])

        return Polynomio(coeffi)
        
    def __mul__(self, A): #Overloading * operator
        n = len(self.coeff) - 1
        t = len(A.coeff) - 1

        coeff = [Frac(0) for i in range(n+t+1)]
        for i in range(n+1):
            for j in range(t+1):
                coeff[j+i] += Frac(self.coeff[i]*A.coeff[j])
        return Polynomio(coeff)
   

    def plotPolynomio(self, xs = [0], ys = [0]):
        min_xs, max_xs = min(xs), max(xs)
        min_ys, max_ys = min(ys), max(ys)

        X = np.linspace(min(min_xs, -100) , max(max_xs, 100), 1000)
        poly = np.poly1d( list(reversed(self.coeff)) )

        fig, grafica = plt.subplots(1, figsize = (10,6))

        grafica
        grafica.plot(X, poly(X))
        grafica.scatter(xs, ys)
        grafica.set_xlim(min_xs - 20, max_xs + 20)
        grafica.set_ylim(min_ys - 20, max_ys + 20)

        grafica.grid()
        plt.show()
