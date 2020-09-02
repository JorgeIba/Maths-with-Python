# Explanation of the code

If we have a circle fitting in a square, and let ![f1] be te radius of the circle, then the side length of the circle will be ![f2]

<p align="center">
  <img src="https://github.com/JorgeIba/Maths-with-Python/blob/master/Images-for-Explanations/ICalculatingPI-MonteCarlo/Circle_inside_Square.png">
</p>

Let be the ![f3] Area of Circle (in red), and ![f4] be the Area of Square (red + green), as far we know that:

![f5]

![f6]

If we isolate the expression ![f12] in both equations we get:

![f7]

![f8]

That means that ![f7] has to be equal than ![f8], and we can solve for ![f11].

![f9]

![f10]

and that means that ![f11] is 4 times the Area of Circle divided by Area of Square.

The program uses the method of Monte Carlo to calculate the proportion of how many random points lands inside of square and how many lands inside of circle, and finally return the formula of ![f10]


[f1]: http://chart.apis.google.com/chart?cht=tx&chl=R
[f2]: http://chart.apis.google.com/chart?cht=tx&chl=2R
[f3]: http://chart.apis.google.com/chart?cht=tx&chl=A_c
[f4]: http://chart.apis.google.com/chart?cht=tx&chl=A_s
[f5]: http://chart.apis.google.com/chart?cht=tx&chl=A_s=4R^2
[f6]: http://chart.apis.google.com/chart?cht=tx&chl=A_c={\pi}R^2
[f7]: http://chart.apis.google.com/chart?cht=tx&chl=\frac{A_s}{4}=R^2
[f8]: http://chart.apis.google.com/chart?cht=tx&chl=\frac{A_c}{\pi}=R^2
[f9]: http://chart.apis.google.com/chart?cht=tx&chl=\frac{A_c}{\pi}=\frac{A_s}{4}
[f10]: http://chart.apis.google.com/chart?cht=tx&chl=\\pi=\\frac{4A_c}{A_s}
[f11]: http://chart.apis.google.com/chart?cht=tx&chl=\\pi
[f12]: http://chart.apis.google.com/chart?cht=tx&chl=R^2
