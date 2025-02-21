from flask import *
import random as rd
import numpy as np
from sympy import *
import json

def ecuaciones_incognita(grado):
    x = Symbol('x')
    lim_superior = 10
    coeficientes = [rd.randint(1, lim_superior) for n in range(0, grado)]
    equation = 0
    for i in range(0, len(coeficientes)):
        equation += (x**(grado-i))*coeficientes[i]
        print(equation)
        
    return json.dumps({
        "exercise":sympy.latex(equation),
        "solution":[sympy.latex(n) for n in sympy.solve(equation)]
    })