from flask import *
import random as rd
import numpy as np
from sympy import *
import json



def aritmetica_fracciones_suma_resta(num_terms, len_term, has_parentheses=False):


    inf_expresion = 10**(len_term-1)
    sup_expresion = 10**(len_term)
    
    operations = ["+","-"]
    
    #even positions are the terms of my expression
    #odd positions are the operations
 
    if(num_terms % 2 == 0):
        pass
    else:
        num_terms+=1
        
    
    array_terms = [n for n in range(0, num_terms+1)]

    for i in range(0, len(array_terms)):
        
        num = rd.randint(inf_expresion, sup_expresion)
        denom = rd.randint(inf_expresion, sup_expresion)
        
        if(i % 2 == 0):
            array_terms[i] = str(Rational(num,denom))
        else:
            array_terms[i] = operations[rd.randint(0,1)]
            
    final_expr = ' '.join(array_terms)
    
    return json.dumps({
        "exercise":final_expr,
        "result":str(Rational(N(final_expr).evalf()))
    })


def aritmetica_fracciones_complete(num_terms, len_term, has_parentheses=False):


    inf_expresion = 10**(len_term-1)
    sup_expresion = 10**(len_term)
    
    operations = ["+","-", "*", "/"]
    
    #even positions are the terms of my expression
    #odd positions are the operations
 
    if(num_terms % 2 == 0):
        pass
    else:
        num_terms+=1
        
    
    array_terms = [n for n in range(0, num_terms+1)]

    for i in range(0, len(array_terms)):
        
        num = rd.randint(inf_expresion, sup_expresion)
        denom = rd.randint(inf_expresion, sup_expresion)
        
        if(i % 2 == 0):
            array_terms[i] = str(Rational(num,denom))
        else:
            array_terms[i] = operations[rd.randint(0,3)]
            
    final_expr = ' '.join(array_terms)
    
    return json.dumps({
        "exercise":final_expr,
        "result":str(Rational(N(final_expr).evalf()))
    })






