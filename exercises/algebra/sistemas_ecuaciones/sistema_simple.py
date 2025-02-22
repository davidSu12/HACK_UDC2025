from flask import *
import random as rd
import numpy as np
from sympy import *
import json


def generate_systems(num_cifras):

	x,y = symbols('x,y')
	inf_expresion = 10**(num_cifras-1)
	sup_expresion = 10**(num_cifras)

	coef_matrix = [[rd.randint(inf_expresion, sup_expresion) for n in range(0,2)] for n in range(0,2)]
	list_equations = []


	for i in range(0, len(coef_matrix)):
		eq = 0
		for j in range(0, len(coef_matrix[i])):
			if(j == 0):
				eq += x*coef_matrix[i][j]
			else:
				eq += y*coef_matrix[i][j]
		list_equations.append(eq)
		eq = 0
	return list_equations


generate_systems(3)

