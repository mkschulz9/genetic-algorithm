 # GeneticAlgorithm Repository

## Main Idea
This repository holds assignment #1 for CSCI-561, Foundations of Artificial Intelligence, which focuses on solving a 3D Travelling Salesman Problem (TSP) using the Genetic algorithm. Here, the AI agent is given a list of cities represented by coordinates of the format (x, y, z). It then employs the Genetic algorithm to find the shortest path through a set of cities, starting and ending at the same city while visiting all other cities exactly once. Key aspects of this agent include:
- Initial generation of paths
- Path ranking
- Crossover between parents
- And mutation of path 'offspring'

This project is implemented entirely from scratch in Python.

## Travelling Sales Person Problem
- The Travelling Sales Person Problem (TSP) is a well known problem in computer science. It is an NP-hard problem, meaning that it is not possible to find the optimal solution in polynomial time. More detailed information about the TSP can be found [here](https://blog.routific.com/blog/travelling-salesman-problem#:~:text=The%20Traveling%20Salesman%20Problem%20(TSP,and%20optionally%20an%20ending%20point.)).

## Genetic Algorithm
- The Genetic algorithm is a heuristic search algorithm that is inspired by the process of natural selection. It is a population based algorithm that uses the concepts of crossover and mutation to find the optimal solution to a problem. More detailed information about the Genetic algorithm can be found [here](https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3).

## Implementation of Genetic Algorithm ([main.py](https://github.com/mkschulz9/GeneticAlgorithm/blob/main/main.py))
### Core Functions:
```python
generateInitialPopulation(size, cityList)
```
- Parameters:
    - **size**: number of paths to generate for the initial population
    - **cityList**: list of city coordinates to visit
- Purpose:
    - Generates an initial population for the Genetic algorithm, verifying each path is unique. Each path is a list of city coordinates to visit, starting and ending at the same city. It generates a path using the 'nearestNeighborWithRandomization()' function below.

```python
nearestNeighborWithRandomization(startCity, cityList, randomFactor)
```
- Parameters:
    - **startCity**: starting city coordinate
    - **cityList**: list of city coordinates to visit
    - **randomFactor**: a number denoting how many closest cities to a given coordinate should be found
- Purpose:
    - Generates a single path using the Nearest Neighbor algorithm with randomization. It uses the 'getTopNNearestCities()' funciton below to find the closest 'n' cities to the current city according to the randomFactor value. It picks one of these 'N' cities at random to be the next city in the path. It continues this process until all cities have been visted.

```python
getTopNNearestCities(currentCity, unvisitedCities, N)
```
- Parameters:
    - **currentCity**: current city coordinate
    - **unvisitedCities**: list of city coordinates that have not been visited yet
    - **N**: number of closest cities you want to consider for the next move.
- Purpose:
    - Starts by creating a list of tuples, where each tuple contains an unvisited city and its distance from the current city. It then sorts this list by distance and returns the first 'N' cities.

### Helper Functions:
```python
calculateDistance(coordinate1, coordinate2)
```
- Parameters:
    - **coordinate1** & **coordinate2**: tuple of coordinates of any dimension
- Purpose:
    - Calculates the distance between the two points. Used in many core funcitons.

```python
printWithNewline(*args, **kwargs):
```
- Parameters:
    - ***args**: any number of arguments to print
    - ****kwargs**: any number of keyword arguments to print
- Purpose:
    - Prints the arguments passed in with a newline character at the end. Used for debugging.

```python
openInputFile():
```
- Parameters:
    - None
- Purpose:
    - Reads the input file are returns the number of cities to visit and a list of the city coordniates.

```python
writeToFile(bestPathDistanceAndPath)
```
- Parameters:
    - **bestPathDistanceAndPath**: tuple containing the best path distance and the best path
- Purpose:
    - Writes the best path distance and the best path to the output file in desired format and locaiton.

