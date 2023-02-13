# Path_Finder_Algorithm (PFA)
Pathfinder Algorithm (PFA) is a swarm-based meta-heuristic technique which is employed to solve optimization problems of various structures. This technique simulates the leadership hierarchy of swarming to locate the best food source or prey, which is inspired by the group movements of various animal species.

For a long time, many scientists have been particularly interested in the searching, exploitation, and hunting capabilities of animal swarms. In a swarm, every action is carried out as a result of everyone acting in unison. Additionally, the swarm is led by a single person who also controls several acts.
Additionally, this person drives the herds to destinations including grass, water, and feeding areas.Depending on the ability to meet the goal, the leader may change [1]. 

# Description
The Pathfinder Algorithm (PFA), a swarm-based optimization algorithm inspired by the way in which animals work together to identify the best food sources, was introduced by Yapici and Cetinkaya in 2019. The collection of solutions for an n-dimensional space problem in this method represents a herd of animals, whose motions are controlled by the leader and other members. The members of this algorithm are updated using the following equation during each of its N iterations: 

 ![image](https://user-images.githubusercontent.com/93834390/218518989-779f71fb-c341-45d6-a811-80845d7f8dce.png)
 
 
xi represents the position vector of the i-th member, xj the position vector of the j-th member, R1 and R2 random vectors, and K the current iteration. Assuming that r1 and r2 are uniformly produced random vectors with values between zero and one, R1 is equal to αr1 and R2 is equal to βr2. The amount of movement of every member with respect to its neighbor is determined by the interaction coefficient, or α. In contrast, the random distance required to keep the herd's proximity to the leader is determined by the attraction coefficient, β. The vibration vector is denoted by ε, and the position vector of the best answer from each iteration of the following equations is denoted by xpK: 

![image](https://user-images.githubusercontent.com/93834390/218519448-c47daa63-3ea1-43e1-9ab8-27c1b5bb6f76.png)

![image](https://user-images.githubusercontent.com/93834390/218519501-4fc15738-db60-4c4b-aa7e-66dc1f74db08.png)

![image](https://user-images.githubusercontent.com/93834390/218519576-42c72fc9-3e4d-4573-9665-c272f505d96e.png)

where K_Max is the total number of repetitions, Dij is the distance between two members, u1 and u2 are random vectors generated between -1 and 1, and r3 is a vector of random numbers between zero and one.

# Example



# References
1. Yapici, Hamza, and Nurettin Cetinkaya. "A new meta-heuristic optimizer: Pathfinder algorithm." Applied soft computing 78 (2019): 545-568.
2. 


