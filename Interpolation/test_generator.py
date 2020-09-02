import numpy as np
import sys
import os

##### Constants ######
LOWER_LIMIT_X = -50
UPPER_LIMIT_X = 50
LOWER_LIMIT_Y = -50
UPPER_LIMIT_Y = 50
######################

n = int(input("How many points? "))

rng = np.random.default_rng()

xs = rng.choice(a = np.arange( start = LOWER_LIMIT_X, stop = UPPER_LIMIT_X), size = n, replace = False)
ys = rng.choice(a = np.arange(start = LOWER_LIMIT_Y, stop =  UPPER_LIMIT_Y), size = n, replace = True)

with open(os.path.join(sys.path[0], "input.txt"), "w") as f:
    f.write(f"{n}\n")
    for idx in range(n):
        f.write(f"{xs[idx]} {ys[idx]}\n")

