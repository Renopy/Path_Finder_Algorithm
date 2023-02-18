# Path_Finder_Algorithm (PFA)
Pathfinder Algorithm (PFA) is a swarm-based meta-heuristic technique which is employed to solve optimization problems of various structures. This technique simulates the leadership hierarchy of swarming to locate the best food source or prey, which is inspired by the group movements of various animal species.

# Description
The Pathfinder Algorithm (PFA) inspired by the way in which animals work together to identify the best food sources was introduced by Yapici and Cetinkaya in 2019. The collection of solutions for an n-dimensional space problem in this method represents a herd of animals, whose motions are controlled by the leader and other members. The members of this algorithm are updated using the following equation during each of its N iterations: 

 ![image](https://user-images.githubusercontent.com/93834390/218518989-779f71fb-c341-45d6-a811-80845d7f8dce.png)
 
 
xi represents the position vector of the i-th member, xj the position vector of the j-th member, R1 and R2 random vectors, and K the current iteration. Assuming that r1 and r2 are uniformly produced random vectors with values between zero and one, R1 is equal to αr1 and R2 is equal to βr2. The amount of movement of every member with respect to its neighbor is determined by the interaction coefficient, or α. In contrast, the random distance required to keep the herd's proximity to the leader is determined by the attraction coefficient, β. The vibration vector is denoted by ε, and the position vector of the best answer from each iteration of the following equations is denoted by xpK: 

![image](https://user-images.githubusercontent.com/93834390/218519448-c47daa63-3ea1-43e1-9ab8-27c1b5bb6f76.png)

![image](https://user-images.githubusercontent.com/93834390/218519501-4fc15738-db60-4c4b-aa7e-66dc1f74db08.png)

![image](https://user-images.githubusercontent.com/93834390/218519576-42c72fc9-3e4d-4573-9665-c272f505d96e.png)

where K_Max is the total number of repetitions, Dij is the distance between two members, u1 and u2 are random vectors generated between -1 and 1, and r3 is a vector of random numbers between zero and one[^1].

# Example
Because PFA is stochastic, like many other meta-heuristic algorithms of a similar nature, each time you run it, you will have a slightly different output. The output is the best solution for which the minimum Loss Function was obtained.

The algorithm can be easily used as following steps:

1) Import the packages

```python
from PFA import Pathfinder
import numpy as np
import pandas as pd
```
2) Prepare the input data
```python
Excel_cal = pd.read_excel("../Cal.xlsx")

Excel_test = pd.read_excel("../test.xlsx")

# choose the keys for the input variables (X) and observation
var_keys = [ 'X1' , 'X2' ] 
obs_key = 'obs'

x_train = Excel_cal[ var_keys ] 
x_test = Excel_test[ var_keys ] 


obs_train = Excel_cal[ obs_key ] 
obs_test = Excel_test[ obs_key ]

```


3) Define a model and Loss Function 

```python

def model_mlr(w , x):
    # w =  [ w[0]  ,  1]
    # w =  [   0  , w[0] ]
    out =  numpy.array(numpy.dot(    w[1:]  , numpy.transpose( x)) ) +w[0]
    return out

def fitness_function(Solution):

    wx =  model_mlr(w =Solution  ,   x = x_train  )

    RMSE = numpy.mean(wx-obs_train)**0.5

    
    return  RMSE
```

4) build the model


```python
initialize_iteration = 100
num_of_parameters = 3  # Here we need 3 parameters to run the model correctly 
modle = Pathfinder.model(fitness_function  , num_of_parameters   , initialize_iteration  , PFA_iteration ,alpha =1  , beta=1 , converging_threshold = 0.001)
```
5) run the model abd predict


```python
model.fit() 
weights = model.solution
pred = model_mlr(weights , x_test)  # here we used a MLR model 
```

6) Using Evaluation function you can assess the accuracy of the model

```python
from PFA import evaluation
results = evaluation.evaluate(obs_test , pred)

```

```python

print('correlation = 'result.r)
out [1] =  
```

## References
[^1]: Yapici, Hamza, and Nurettin Cetinkaya. "A new meta-heuristic optimizer: Pathfinder algorithm." Applied soft computing 78 (2019): 545-568.
[^2]: Nosratpour, Reza, Majid Rahimzadegan, and Niloufar Beikahmadi. "Introducing a merged precipitation satellite model using satellite precipitation products, land surface temperature, and precipitable water vapor." Geocarto International (2022): 1-31.






