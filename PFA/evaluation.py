# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 19:07:05 2023

@author: Reza
"""


import pandas as pd
import numpy
from math import *
import hydroeval as he
import scipy.stats as sci

def evaluate( obs , model ) :
    Obs = numpy.array(obs)
    Model = numpy.array(model)
    
    result = {}
    result['nse']  = 1 - ( numpy.sum((Model-Obs)**2) / numpy.sum((Obs-numpy.mean(Obs ))**2 ))
    result['rmse'] = numpy.mean((Obs-Model)**2)**0.5
    result['mbe']  = numpy.mean( Model - Obs)
    result['mae'] = numpy.mean( numpy.absolute( Model - Obs))
    result['pbias'] =  100*numpy.sum(Model-Obs)/numpy.sum(Obs) 
    result['kge'] ,result['r'], result['alpha'] ,result['beta'] = he.evaluator(he.kge, Model, Obs)
    result['spearman'] = sci.spearmanr(Obs , Model)[0]
    
    result['std_obs'] =  numpy.std(Obs)
    result['std_model'] =  numpy.std(Model)
    
    result  = pd.DataFrame(result)
    return  result


