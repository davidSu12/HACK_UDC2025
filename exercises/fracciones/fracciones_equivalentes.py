from flask import *
import random as rd
import numpy as np
from sympy import *
import json



def fracciones_equivalentes(num_cifras):

        #vamos a dejar la eleccion en manos de la aleatoriedad
        # 0: equivalentes
        # 1: no equivalentes


        eleccion = rd.choice([False,True])
        exercise_dict = dict()

        inf_expresion = 10**(num_cifras-1)
        sup_expresion = 10**(num_cifras)

        num = rd.randint(inf_expresion, sup_expresion)
        denom = rd.randint(inf_expresion, sup_expresion)

        while(num == denom):denom=rd.randint(inf_expresion)

        num_reduced = num / int(sympy.gcd(num, denom))
        denom_reduced = denom / int(sympy.gcd(num, denom))


        new_frac = None

        if(eleccion):
            multiplo_comun  = rd.radnint(inf_expresion, sup_expresion)
            new_frac = (num * multiplo_comun, denom * multiplo_comun)
        else:
            num_1 = rd.randint(inf_expresion, sup_expresion)
            num_2 = rd.randint(inf_expresion, sup_expresion)

            while(num_1 * denom == num_2 * num):
                num_1 = rd.randint(inf_expresion, sup_expresion)
                num_2 = rd.randint(inf_expresion, sup_expresion)

            new_frac = (num_1, num_2)

        exercise_dict["exercise"] = {
            0:(num, denom),
            1:new_frac
        }

        return json.dumps({
            "exercise":exercise_dict,
            "result":eleccion
            
        })









