 # GeneticAlgorithm Repository

## Main Idea
This repository holds assignment #1 for CSCI-561, Foundations of Artificial Intelligence, which focuses on solving a 3D Travelling Salesman Problem (TSP) using the genetic algorithm. Here, the AI agent is given a list of cities represented by coordinates of the format (x, y, z). It then employs the genetic algorithm to find the shortest path through a set of cities, starting and ending at the same city while visiting all other cities exactly once. Key aspects of this agent include:
- Initial generation of paths
- Path ranking
- Crossover between best paths
- And mutation of path 'offspring'

This project is implemented entirely from scratch in Python.

## Travelling Sales Person Problem

## Genetic Algorithm

## Implementation of Genetic Algorithm (main.py LINK MAIN)
### Key Functions:
#### calculateDistance()
- Accepts two coordinates of any dimension and returns the Euclidean distance between the two points. In this project’s scope, it is used to calculate the distance between two cities in the 3D space.

#### generateInitialPopulation()
- Generates unique, valid paths that start and end at the same city and visit all other cities exactly once. It is used to seed the genetic algorithm with a population of paths that can be used to create future generations.

#### rankPopulation()
- Ranks the given population. It finds the distance required to travel each path in the population and returns a sorted list of paths in ascending order of distance.

