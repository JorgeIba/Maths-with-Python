from Interpolation import *
import sys

# Complexity:
# Multiplication of Polynomials: O(n^2)
# Lagrange Interpolation: O(n^2)
# Total: Aprox O(n^4)


def read_Input_Text():
    with open(os.path.join(sys.path[0], "input.txt"), "r") as inputText:
        lines = inputText.readlines()
        n = int(lines[0])
        xs = []
        ys = []
        for i in range(0, n):
            x, y = map(int, lines[i+1].split(" "))
            xs.append(x)
            ys.append(y)
    return xs, ys

def read_Manually():
    n = int(input("Enter the number of points\n"));
    xs = []
    ys = []
    for i in range(n):
        x, y = map(int, input(f"Enter the {i+1}th point (x y)\n").split(" "))
        xs.append(x)
        ys.append(y)
    return xs, ys
        


if __name__ == "__main__":
    #Uncomment this if you want to put the points by 'input.txt'
    xs, ys = read_Input_Text()  

    #Uncomment this if you want to put the points manually by command line
    #xs, ys = read_Manually()
        
    Polynomio_interpoled = interpolation(xs, ys)
    Polynomio_interpoled.plotPolynomio(xs, ys)

    
