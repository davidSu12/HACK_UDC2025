from flask import *
import random as rd
import numpy as np
from sympy import *
import json



def porcentajes(num_cifras):
    
            
    inf_expresion = 10**(num_cifras-1)
    sup_expresion = 10**(num_cifras)
    
    ejercicio = rd.randint(inf_expresion, sup_expresion)
    exercise_dict = dict()
    #signo negativo: 0
    #signo positivo: 1
    
    signo = rd.choice([-1,1])
    
    l = [n*10 for n in range(1,11)]
    
    percentage_reduce = rd.choice(l)*signo
    
    
    exercise_dict["exercise"] = {
        0:ejercicio,
        1:percentage_reduce
        
    }
    
    return json.dumps(
        
        {
            "exercise": exercise_dict,
            "result":(percentage_reduce/100)*ejercicio
        }
    
    )
