from flask import *
import random as rd
import numpy as np
from sympy import *
import json




#Conversión de medidas de longitud.

def medidas_de_longitud(num_cifras):
    
    inf_expresion = 10**(num_cifras-1)
    sup_expresion = 10**(num_cifras)
    
    exercise = rd.randint(inf_expresion, sup_expresion)
    
    exercise_dict = dict()
    
    vocabulary = {
        "kilometros":"km",
        "hectometros":"hm",
        "decametros":"dam",
        "metros":"m",
        "decimetros":"dm",
        "centimetros":"cm",
        "milimetros":"mm"
    }
    
    keys_list = list(vocabulary.keys())
    
    prev_value = rd.randint(0, len(keys_list)-1)
    next_value = rd.randint(0, len(keys_list)-1)
    
    exercise_dict["exercise"] = {
        0:{keys_list[prev_value]:exercise},
        1:keys_list[next_value]
    }
    
    while(next_value == prev_value):
        next_value = rd.randint(0,len(keys_list)-1)
        
    if(prev_value < next_value): 
        ## tenemos que multiplicar por 10
        exercise *= 10**abs(prev_value-next_value)
    
    else:
        ##tenemos que dividir por 10
        exercise /= 10**abs(prev_value-next_value)
        
    return json.dumps(
        {
            "exercise":exercise_dict,
            "result":exercise
        }
    )    
        
        
    
    
#Conversión de medidas de capacidad.

def medidas_de_capacidad(num_cifras):
    
    inf_expresion = 10**(num_cifras-1)
    sup_expresion = 10**(num_cifras)
    
    exercise =rd.randint(inf_expresion, sup_expresion)
    
    exercise_dict = dict()
    
    vocabulary = {
        "kilolitros":"kl",
        "hectolitros":"hl",
        "decalitros":"dal",
        "litros":"l",
        "decilitros":"dl",
        "centilitros":"cl",
        "mililitros":"ml"
    }
    
    keys_list = list(vocabulary.keys())
    
    prev_value = rd.randint(0, len(keys_list)-1)
    next_value = rd.randint(0, len(keys_list)-1)
    
    exercise_dict["exercise"] = {
        0:{keys_list[prev_value]:exercise},
        1:keys_list[next_value]
    }
    
    while(next_value == prev_value):
        next_value =rd.randint(0,len(keys_list)-1)
        
    if(prev_value < next_value): 
        ## tenemos que multiplicar por 10
        exercise *= 10**abs(prev_value-next_value)
    
    else:
        ##tenemos que dividir por 10
        exercise /= 10**abs(prev_value-next_value)
        
    return json.dumps(
        {
            "exercise":exercise_dict,
            "result":exercise
        }
    )    
            
            
    
#Conversión de medidas de masa.


def medidas_de_masa(num_cifras):
        
    inf_expresion = 10**(num_cifras-1)
    sup_expresion = 10**(num_cifras)
    
    exercise = rd.randint(inf_expresion, sup_expresion)
    
    exercise_dict = dict()
    
    vocabulary = {
        "kilogramos":"kg",
        "hectogramos":"hg",
        "decagramos":"dag",
        "gramos":"g",
        "decigramos":"dg",
        "centigramos":"cg",
        "miligramos":"mg"
    }
    
    
    keys_list = list(vocabulary.keys())
    
    prev_value = rd.randint(0, len(keys_list)-1)
    next_value = rd.randint(0, len(keys_list)-1)
    
    exercise_dict["exercise"] = {
        0:{keys_list[prev_value]:exercise},
        1:keys_list[next_value]
    }
    
    while(next_value == prev_value):
        next_value = rd.randint(0,len(keys_list)-1)
        
    if(prev_value < next_value): 
        ## tenemos que multiplicar por 10
        exercise *= 10**abs(prev_value-next_value)
    
    else:
        ##tenemos que dividir por 10
        exercise /= 10**abs(prev_value-next_value)     
        
    return json.dumps(
        {
            "exercise":exercise_dict,
            "result":exercise
        }
    )    
            
            
    

#Conversión de medidas de superficie.

def medidas_de_superficie(num_cifras):
        
    inf_expresion = 10**(num_cifras-1)
    sup_expresion = 10**(num_cifras)
    
    exercise = rd.randint(inf_expresion, sup_expresion)
    
    exercise_dict = dict()
    
    vocabulary = {
        "kilometros^2":"km^2",
        "hectometros^2":"hm^2",
        "decametros^2":"dam^2",
        "metros^2":"m^2",
        "decimetros^2":"dm^2",
        "centimetros^2":"cm^2",
        "milimetros^2":"mm^2"
    }
    
    keys_list = list(vocabulary.keys())
    
    prev_value = rd.randint(0, len(keys_list)-1)
    next_value = rd.randint(0, len(keys_list)-1)
    
    exercise_dict["exercise"] = {
        0:{keys_list[prev_value]:exercise},
        1:keys_list[next_value]
    }
    
    while(next_value == prev_value):
        next_value = rd.randint(0,len(vocabulary.keys()))
        
        
    if(prev_value < next_value): 
        ## tenemos que multiplicar por 10
        exercise *= 100**abs(prev_value-next_value)
    
    else:
        ##tenemos que dividir por 10
        exercise /= 100**abs(prev_value-next_value)    
    
    
    return json.dumps(
        {
            "exercise":exercise_dict,
            "result":exercise
        }
    )    
            
            
                
               
