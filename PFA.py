# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 08:10:29 2021

@author: reza
"""

import numpy
import math 
import random
from math import *


class PFA_model():
    
    def __init__(self ,   fitness_function  , num_of_parameters   , initialize_iteration  , PFA_iteration ,alpha =1  , beta=1 , converging_threshold = 0.001):
        
        self.fitness_function = fitness_function
        self.num_of_param     = num_of_parameters
        
        self.IT   = initialize_iteration
        self.IT2  = PFA_iteration
        self.alpha= alpha
        self.beta = beta
        self.conv = converging_threshold
    
    def fit(self):
        self.Conv_curve = [ ]
        sol = numpy.zeros(self.num_of_param)
        self.best_sol= numpy.random.rand(self.num_of_param)
        self.best_fit = self.fitness_function(sol )
        Dict = {}
        Loss={}
        mem=0
        
        """  --  initialize -- """
        it=0
        while it<self.IT or mem<2 :
            it+=1
            sol =numpy.random.normal(-5, 5, self.num_of_param) 
            fitness = self.fitness_function(sol)
            if fitness<self.best_fit :
                self.Conv_curve.append(fitness)
                mem+=1
                self.best_fit=fitness
                self.best_sol=sol
                Dict[str(mem)]=sol
                Loss[str(mem)]=fitness
                print("Solution :",sol)
                print("fitness = ",fitness)
        self.num_of_mem = len(Dict)
            
        self.best_sol=Dict[str(self.num_of_mem)]
        self.best_fit=self.fitness_function(Dict[str(self.num_of_mem)])
        
        for i in Dict :
            print(i , Dict[i])
        
        print("---Path finder---")
        position={}
        
        position["0"]=Dict[str(self.num_of_mem-1)]
        position["1"]=Dict[str(self.num_of_mem)]
        
        
        self.Conv_curve.append(self.best_fit)
        
        for it in range(1,self.IT2):
            
            for mem in range(2,self.num_of_mem+1):
                r1=numpy.random.uniform(0, 1, self.num_of_param)
                r2=numpy.random.uniform(0, 1, self.num_of_param)
                u1=numpy.random.uniform(-1, 1, self.num_of_param)
                u2=numpy.random.uniform(-1, 1, self.num_of_param)
                
                R1=self.alpha*r1
                R2=self.beta*r2
                
                D=abs(Dict[str(mem)]-Dict[str(mem-1)])
                dif = Dict[str(mem)]-Dict[str(mem-1)]
                r3=numpy.random.uniform(0, 1, self.num_of_param)
                
                A=u2*exp(-2*it/self.IT2)
                position[str(it+1)] =  position[str(it)] + 2*r3*(position[str(it)]-position[str(it-1)])+A
                epsilon = (1-it/self.IT2)*u1*D
                sol = Dict[str(mem)]
                dpos= position[str(it+1)]-sol
                sol =  sol+R1*dif+R2*dpos+epsilon
                fitness=self.fitness_function(sol )
                if fitness<Loss[str(mem)]:
                    print(it,"of",self.IT2)
                    Dict[str(mem)] = sol
                    Loss[str(mem)] = fitness
                if fitness<self.best_fit:
                    self.best_sol = sol
                    self.best_fit = fitness
                    self.Conv_curve.append(fitness)
                    
                    print("Solution :",sol)
                    print("fitness = ",fitness)
                position[str(it)] = self.best_sol
            position[str(it+1)] = self.best_sol
        
        if abs(self.Conv_curve[-2]-self.Conv_curve[-1]) > self.conv :
            print( '  warning :  Converging threshold is not satisfied ' )



def order(Ex , Keys):
    Output =[ ]
    for k in Keys :
        List = list(Ex[k])
        
        Output.append(List)
    Order = numpy.transpose(Output)
    return Order

def fitness_function(Solution):
    bias = Solution[-1]
    
    out=numpy.array(numpy.dot(    Solution[0:-1]  , numpy.transpose( x_train)) ) +bias
    #r = numpy.corrcoef( obs_train , out )[0,1]
    #nse  = 1 - ( numpy.sum((out-obs_train)**2) / numpy.sum((obs_train-numpy.mean(obs_train ))**2 ))
    rmse = numpy.mean((out-obs_train)**2)**0.5
    #SE=numpy.sum((y-out)**2)
    #MSE=SE/len(y)
    #RMSE= MSE**0.5
    # Th = 1
    
    # csi = Reza.CSI(Obs=obs_train , Product=out ,threshold=Th)
    return rmse



import pandas as pd


ord_keys =[  'IMERG' ,'PDIR','P_fldas'  ,'NDVI' ,'T_fldas'  ,'DEM' , 'Slope'] 
Train_file ='E:\Precipitaion Climates\Data\Cal_Test\stations/Complete_Cal.xlsx'
Test_file = 'E:\Precipitaion Climates\Data\Cal_Test\stations/Complete_Test.xlsx'



Excel = { }
Excel['train']= pd.read_excel(Train_file)
Excel['test']= pd.read_excel(Test_file)

Keys = pd.DataFrame.keys(Excel['train'])
shape = ( len(Keys) , len(Excel['train']) )

Train={ }
Train_data = Excel['train'].values
# Train["X"] = Train_data[:,1:shape[0]]

Train["X"] = order( Excel['train'] , ord_keys)
Train["O"] =  numpy.array(Excel['train']['rrr24'])


Test = {}
Test_data = Excel['test'].values
Test["X"] = order( Excel['test'] , ord_keys)
Test["O"] = numpy.array(Excel['test']['rrr24'])


Train["mean"]=numpy.zeros(len(ord_keys))
Train["std"]=numpy.zeros(len(ord_keys))
Train["max"]=numpy.zeros(len(ord_keys))
Train["min"]=numpy.zeros(len(ord_keys))
for i in range(len(ord_keys)):
    Train["mean"][i]=numpy.mean(Train["X"][:,i]) 
    Train["std"][i]=numpy.std(Train["X"][:,i])
    Train["max"][i]=numpy.max(Train["X"][:,i]) 
    Train["min"][i]=numpy.min(Train["X"][:,i]) 

Train["X"] = (Train["X"] - Train["mean"]) / Train["std"]
Test["X"] = (Test["X"] - Train["mean"]) /  Train["std"]


x_train  = Train["X"]
obs_train = Train["O"]


num_of_param = len(x_train[0])+1

port 
Model = PFA_model(fitness_function=fitness_function , 
                  num_of_param =num_of_param  , IT = 3000 , IT2=20000)

Model.fit()

