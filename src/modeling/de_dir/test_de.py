from __future__ import division, print_function
import numpy as np

try:
    from builtins import xrange
except ImportError:
    xrange = range

from DiffEvolOptimizer import DiffEvolOptimizer

'''
Akond Rahman
Feb 23, 2017
Test DE algorihm implementation
'''
"""
Differential evolution (DE)
===========================

Test and examples
"""



def rosenbrock_fn(x):
    """ Rosenbrock function
        global minimum at x = [1, ..., 1], f(x) = 0
    """
    #print("x: ", x)
    _x = np.array(x)
    #print("_x: ", _x)
    return sum(100.0 * (_x[1:] - _x[:-1] ** 2) ** 2. + (1 - _x[:-1]) ** 2.)


def sphere_fn(x):
    """
        global minimum at x = [0, ..., 0], f(x) = 0
    """
    _x = np.array(x)
    return sum(_x ** 2)


def ackley_fn(x):
    """
    global minimum at x = [0, ..., 0], f(x) = 0
    """
    _x = np.array(x)
    n = len(_x)
    return -20 * np.exp(-0.2  * np.sqrt(1. / float(n) * sum(_x ** 2))) - np.exp(1. / float(n) * sum(np.cos(2 * np.pi * _x))) + 20. + np.exp(1)
def styblinski_fn(x):
    """
    Styblinski & Tang
    global minimum at x = [-2.903534, ..., -2.903534], f(x) = -39.16599 * len(n)
    """
    _x = np.array(x)
    return 0.5 * sum(_x ** 4 - 16. * _x ** 2 + 5. * _x)



if __name__ == '__main__':
    ngen, npop, ndim = 100, 100, 2
    limits = [[-5, 5]] * ndim
    #limits = [[1, 10]] * ndim
    #print("limits: ", limits)
    fn_list = (rosenbrock_fn, sphere_fn, ackley_fn, styblinski_fn)

    for en, fn in enumerate(fn_list):
        pop = np.zeros([ngen, npop, ndim])
        loc = np.zeros([ngen, ndim])
        de = DiffEvolOptimizer(fn, limits, npop, maximize=False)

        for i, res in enumerate(de(ngen)):
            pop[i,:,:] = de.population.copy()
            loc[i,:] = de.location.copy()

        print("The function is:", fn.__name__)
        print("The solution is:",  de.location)
        print("The optimized value is:", de.value)
        print("="*100)
