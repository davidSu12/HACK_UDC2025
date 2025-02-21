from flask import *
import random as rd
import numpy as np
from sympy import *
import json


def generate_expression_arithmetic(num_terms, len_term, has_parentheses=False):


    inf_expresion = 10**(len_term-1)
    sup_expresion = 10**(len_term)
    
    operations = ["+","-","*","/"]
    
    #even positions are the terms of my expression
    #odd positions are the operations
 
    if(num_terms % 2 == 0):
        pass
    else:
        num_terms+=1
        
    
    array_terms = [n for n in range(0, num_terms+1)]
    array_terms_with_parentheses = []

    for i in range(0, len(array_terms)):
        if(i % 2 == 0):
            array_terms[i] = str(rd.randint(inf_expresion, sup_expresion))
        else:
            array_terms[i] = operations[rd.randint(0,3)]
            
    """
    if(has_parentheses):
        prev = 0
        for i in range(0, num_terms+1):
            if(i == prev+1 or i == prev+2):
                continue
            if(i+1 <= num_terms):
                if(array_terms[i+1] == "/" or array_terms[i+1] == "*"):
                    array_terms_with_parentheses.append(
                        (array_terms[i],array_terms[i+1],array_terms[i+2])
                    )
                    prev = i
                else:
                    array_terms_with_parentheses.append(array_terms[i])
            else:
                pass
        return array_terms_with_parentheses    
            
    else:
    """
    final_expr = ' '.join(array_terms)
    
    return json.dumps({
        "exercise":final_expr,
        "result":int(N(final_expr).evalf())
    })

    def multiples_and_divisors(len_term, num_cifras):
    
        
	    inf_expresion = 10**(num_cifras-1)
	    sup_expresion = 10**(num_cifras)
	    
	    array_terms = [rd.randint(inf_expresion, sup_expresion) for n in range(0,len_term)]
	    
	    gcd = array_terms[0]
	    for i in range(1,len(array_terms)):
	        gcd = sympy.gcd(gcd, array_terms[i])
	        
	    return json.dumps(
	        {
	            "nums":array_terms,
	            "result":int(gcd)
	        }
	    ) 

	
#Conversión de medidas de longitud.

def medidas_de_longitud(num_cifras):
    
    inf_expresion = 10**(num_cifras-1)
    sup_expresion = 10**(num_cifras)
    
    exercise = np.random(inf_expresion, sup_expresion)
    
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
    
    prev_value = np.random(0, len(vocabulary.keys()))
    next_value = np.random(0, len(vocabulary.keys()))
    
    while(next_value == prev_value):
        next_value = np.random(0,len(vocabulary.keys()))
    
    
#Conversión de medidas de capacidad.

def medidas_de_capacidad(num_cifras):
    
    inf_expresion = 10**(num_cifras-1)
    sup_expresion = 10**(num_cifras)
    
    exercise = np.random(inf_expresion, sup_expresion)
    
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
    
    prev_value = np.random(0, len(vocabulary.keys()))
    prev_value = np.random(0, len(vocabulary.keys()))
    
    while(next_value == prev_value):
        next_value = np.random(0,len(vocabulary.keys()))
    
#Conversión de medidas de masa.


def medidas_de_masa(num_cifras):
        
    inf_expresion = 10**(num_cifras-1)
    sup_expresion = 10**(num_cifras)
    
    exercise = np.random(inf_expresion, sup_expresion)
    
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
    
    prev_value = np.random(0, len(vocabulary.keys()))
    next_value = np.random(0, len(vocabulary.keys()))
    
    while(next_value == prev_value):
        next_value = np.random(0,len(vocabulary.keys()))
    

#Conversión de medidas de superficie.

def medidas_de_superficie(num_cifras):
        
    inf_expresion = 10**(num_cifras-1)
    sup_expresion = 10**(num_cifras)
    
    exercise = np.random(inf_expresion, sup_expresion)
    
    exercise_dict = dict()
    
    vocabulary = {
        "kilometros":"km^2",
        "hectometros":"hm^2",
        "decametros":"dam^2",
        "metros":"m^2",
        "decimetros":"dm^2",
        "centimetros":"cm^2",
        "milimetros":"mm^2"
    }
    
    prev_value = np.random(0, len(vocabulary.keys()))
    next_value = np.random(0, len(vocabulary.keys()))
    
    while(next_value == prev_value):
        next_value = np.random(0,len(vocabulary.keys())) 
	    
        
    
                
               
