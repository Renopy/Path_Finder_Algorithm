# Path_Finder_Algorithm
Yapici and Cetinkaya (2019) introduced the Pathfinder Algorithm (PFA), a swarm-based optimization algorithm inspired by the collective movement of animals to find the best food sources. In this algorithm, the set of solutions for an n-dimensional space problem is a group of animals whose movements depend on other members and the leader. This algorithm has N iterations; in each iteration, members are updated using the following equation:

 ![image](https://user-images.githubusercontent.com/93834390/218518989-779f71fb-c341-45d6-a811-80845d7f8dce.png)
 
 
where K represents the current iteration, xi is the position vector of the i-th member, xj denotes the position vector of the j-th member, and R1 and R2 are random vectors. R1 is equal to αr1, and R2 is equal to βr2, where r1 and r2 are random vectors uniformly generated between zero and one. The interaction coefficient, α, determines the extent of movement of any member relative to its neighbor. In contrast, the attraction coefficient, β, determines the random distance used to maintain the herd’s relative proximity to the leader. ε denotes the vibration vector, and xpK is the position vector of the best solution obtained from the following equations in each iteration: 
 			(16)
 			(17)
 					(18)
where KMax is the total number of repetitions, Dij is the distance between two members, u1 and u2 are random vectors generated between -1 and 1, and r3 is a vector of random numbers between zero and one. In this research, PFA was used to calibrate the parameters of the linear models with α=1 and β=1.
# About

# Description


# Example



# References



