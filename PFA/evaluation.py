


import pandas as pd
import numpy
from math import *
import hydroeval as he
import scipy.stats as sci

def eval( Obs , Model ) :
    
    nse  = 1 - ( numpy.sum((Model-Obs)**2) / numpy.sum((Obs-numpy.mean(Obs ))**2 ))
    rmse = numpy.mean((Obs-Model)**2)**0.5
    mbe  = numpy.mean( Model - Obs)
    mae = numpy.mean( numpy.absolute( Model - Obs))
    pbias =  100*numpy.sum(Model-Obs)/numpy.sum(Obs) 
    kge ,r, alpha ,beta = he.evaluator(he.kge, Model, Obs)
    spearman = sci.spearmanr(Obs , Model)[0]
    
    std_obs =  numpy.std(Obs)
    std_model =  numpy.std(Model)
    
    return  { 'r' :  r[0]  , 'rmse' : rmse  , 'nse' :  nse  , 'kge' : kge[0] , 'mbe': mbe , 'mae' :  mae ,  'pbias': pbias  , 'spearman' : spearman , 'std_obs' :  std_obs    , 'std_model' :std_model   }
