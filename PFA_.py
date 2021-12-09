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

