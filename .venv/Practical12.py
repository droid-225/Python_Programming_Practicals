from scipy import special, linalg
import numpy as np
import scipy
from scipy.optimize import approx_fprime

# Check the version of SciPy
print("Scipy Version:", scipy.__version__)

# Compute the nth derivative of a function
# Define a function for which you want to compute the derivative
def my_function(x):
    return x**2 + x + 1

# Specify the point at which you want to compute the derivative
x0 = np.array([2.0])
delta = np.sqrt(np.finfo(float).eps)

# Compute the derivative of the function at the specified point
derivative_value = approx_fprime(x0, my_function, delta)[0]
print("Derivative at x =", x0[0], "is", derivative_value)

# Combination
com = special.comb(4, 2)
print("Value of 4C2:", com)

# Permutation
per = special.perm(4, 2)
print("Value of 4P2:", per)
