# mcts_Chess

Chess Engine which predicts the moves using monte carlo tree search algorithm.

## Infrastructure:-

We are implementing the algorithm using python. Python-chess library is also required for move generation and validation.

Python-chess library can be installed using the command:

pip install chess 


## Approach:-

MCTS a probabilistic and heuristic driven search algorithm that combines the classic tree search implementations alongside machine learning principles of reinforcement learning.

It consists of four stages : selection -> Expansion -> Roll Out -> Backpropagation

Upper Confidence Bound (UCB) :- It is a factor which decides which node evaluates next in order to maximize probability of victory from a given state.

![image](https://user-images.githubusercontent.com/53829692/153834747-588c4b23-e246-45af-84f8-d15b397032ae.png)

UCB formula that will be used in our implementation :-

UCB = V + 2*sqrt(lnN / ni)        here V = Winning score of the current node
                                                         N = Number of times parent node is visited
                                                         ni = Number of time child node “i” is visited





### 1.Selection :-

In this step we iterate through all child nodes of the current node and return the node with maximum ucb value.


### 2.Expansion :- 

In this step we keep on selecting the child node with maximum ucb value till we reach a leaf node.


### 3. Roll Out/Simulation :-

In this step we add all possible child nodes to the current node and then randomly select a child node.

We repeat this process until the game is over i.e no more moves are possible to be played.

We return 1 for win, -1 for loss and 0.5 for a draw.


### 4.Backpropagation :-

In this step we backpropagate from the new node to the root node. During the process, the number of simulations stored in each node is incremented. 

If the new node’s simulation results in a win, then the number of wins is also incremented. 



![image](https://user-images.githubusercontent.com/53829692/153834088-fd7626c1-180d-49bf-be28-4c3ce3f50ed1.png)

## Result :-

●	1-0 = White Player Won the match

●	0-1 = Black Player Won the match

●	1/2 -1/2 = Match Draw

### On 1 iteration :

![image](https://user-images.githubusercontent.com/53829692/153834153-b8dc51df-af00-4527-b8f7-23c4e086dd97.png)

![image](https://user-images.githubusercontent.com/53829692/153834184-a5ceb885-669a-485a-a651-3ec2bdcc80c4.png)

### On 10 iterations :

![image](https://user-images.githubusercontent.com/53829692/153834237-2765b6df-6561-4935-8860-b2b780955acb.png)

Further Optimization :-

AlphaZero :

●	AlphaZero is computer program developed by artificial intelligence research company DeepMind 

●	In this algorithm the rollout step is replaced by current neural networks.

●	It uses the probability distribution of each child node to select the best node.

![image](https://user-images.githubusercontent.com/53829692/153834517-1d1b33eb-eab1-4f6a-8d80-59daf785cc2e.png)
