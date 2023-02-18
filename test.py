# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 19:07:05 2023

@author: Reza
"""


from PFA import Pathfinder
import numpy as np
import pandas as pd



import numpy



Excel_cal = pd.read_excel("../Cal.xlsx")

Excel_test = pd.read_excel("../test.xlsx")

# choose the keys for the input variables (X) and observation
var_keys = [ 'x1' , 'x2' ] 
obs_key = 'obs'

x_train = Excel_cal[ var_keys ] 
x_test = Excel_test[ var_keys ] 


obs_train = Excel_cal[ obs_key ] 
obs_test = Excel_test[ obs_key ]

def model_mlr(w , x):
    # w =  [ w[0]  ,  1]
    # w =  [   0  , w[0] ]
    out =  numpy.array(numpy.dot(    w[1:]  , numpy.transpose( x)) ) +w[0]
    return out

def fitness_function(Solution):

    wx =  model_mlr(w =Solution  ,   x = x_train  )

    RMSE = numpy.mean((wx-obs_train)**2)**0.5

    return  RMSE


initialize_iteration = 100
num_of_parameters = 3  # Here we need 3 parameters to run the model correctly 
model = Pathfinder.model(fitness_function  , num_of_parameters   , initialize_iteration  = 100 , PFA_iteration = 300 ,alpha =1  , beta=1 , converging_threshold = 0.01)


model.fit() 
weights = model.best_sol
pred = model_mlr(weights , x_test)  # here we used a MLR model 



from PFA import evaluation
result = evaluation.evaluate(obs_test , pred)

print('correlation = ' , float(result.r))


