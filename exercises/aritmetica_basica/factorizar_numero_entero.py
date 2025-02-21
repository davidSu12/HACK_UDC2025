from flask import *
import random as rd
import numpy as np
from sympy import *
import json


def factorizar_numero_entero(num_cifras):

	inf_expresion = 10**(num_cifras-1)
	sup_expresion = 10**(num_cifras)

	numero = rd.randint(inf_expresion, sup_expresion)
	numero_aux = numero
	factores = []


	for i in range(1, numero+1):
		if(numero == 0):
			break
		if(numero  % i == 0):
			factores.append(i)
			numero /= i

	return json.dumps(
		{
		"exercise":numero_aux,
		"result":factores

		}
	
	)		


