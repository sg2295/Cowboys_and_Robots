# Cowboys and Robots
## About the problem 📜
Cowboys and Robots is a new spin on the classic river-crossing problem, "*Missionairies and Cannibals*". It was used as practice for representing problems in such a way that they could be solved by employing uninformed search algorithms. This particular problem was suggested as *advanced work* for a Univeristy module on Artificial Intelligence.

The problem is well-kown in AI literature, and was famously used by Saul Amarel (*On represntations of problems of reasoning about actions, Machine Intelligence*). The different name "Cowboys and Robots" was chosen in an attempt to move away from the problematic theme of the problem, which evokes images of colonialism.
### The rules 
Imagine three cowboys and three robots want to cross a river. With them, they have a boat that can hold one or two individuals at a time. We can never have a group of cowboys be outnumbered by the robots, in either side of the river. Find a way to get everyone to the other side of a river.

![Problem Representation](http://www.aiai.ed.ac.uk/~gwickler/images/mc-init-state.png "Problem Reperesentation")

*Representation of the problem,* [Gerhard Wickler](http://www.aiai.ed.ac.uk/~gwickler/missionaries.html)

Original description, as phrased in *Russel & Norvig (2016, third edition)* page 115:
> "Three missionaries and three cannibals are on one side of a river, along with a boat that can hold one or two people. Find a way to get everyone to the other side without ever leaving a group of missionaries in one place outnumbered by the cannibals in that place."

## Implementation 🔍
The project includes different uninformed searching algorithms capable of finding a solution to the problem. Currently supported algorithms include: Breadth-First Search, Depth-First Search, and Iterative Deepening Search.
### Breadth-First Search
Breadth-first search arrives at a solution by expanding the shallowest node in the frontier. In the case of *Cowboys and Robots* it is an optimal algorithm, as the path cost is a non-decreasing function of node depth (all actions have an identical cost). To use breadth-first search, call the ```g.breadth_first_search()``` after instantiating a *Game* object, ```g = Game()```.
### Depth-First Search
Depth-first search explores the deepest node in the frontier first, in other words, the node that was most recently added to the frontier. ```g.depth_first_search()```
### Iterative Deepening Search
```g.iterative_deepening_search()``` uses the ```depth_limited_search()```
#### Algorithm Cheet Sheet 📝 
Algorithm|Complete|Optimal|Time Complexity|Space Complexity
-|-|-|-|-
Breadth-first search| ✔️ | ✔️|$$O(b^d)$$
Depth-first search| ✔️|❌|
Iterative deepening search|✔️|✔️|

## How to run 🤠🤖
Download the project, and run the ```__main__``` code segment in the Game class.
