from Polynomio import *
from fractions import Fraction as Frac

def interpolation(xs, ys):
    n = len(xs)
    PolyAns = Polynomio([])
    for i in range(n):
        xi = xs[i]
        denomi = Frac(1)
        A = Polynomio([Frac(1)])

        for j in range(n):
            xj = Frac(xs[j])
            if i != j:
                denomi = denomi * Frac(xi - xj)
                A = A * Polynomio([-xj,1])

        PolyAns = PolyAns + A*Polynomio([ Frac(ys[i], denomi) ])
    return PolyAns

