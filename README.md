# 🎓 CSCI-561: Foundations of Artificial Intelligence

## 🗺️ Assignment #1: 3D Travelling Salesman Problem with Genetic Algorithm

Welcome to the repository for Assignment #1 for CSCI-561, USC's Foundations of Artificial Intelligence graduate course. This project is an exploration of solving the 3D Travelling Salesman Problem (TSP) using a Genetic Algorithm implemented in Python. 

---

## 📋 Table of Contents
1. [Introduction](#🌟-introduction)
    - [TSP](#🚗-travelling-salesperson-problem)
    - [Genetic Algorithm](#🧬-genetic-algorithm)
2. [Implementation](#🔨-implementation)
    - [Main Modules](#📂-main-modules)
3. [Getting Started](#🚀-getting-started-running-the-program)

---

## 🌟 Introduction

### 🚗 Travelling Salesperson Problem
The TSP is a classic problem in computer science, considered NP-hard. To learn more, [click here](https://blog.routific.com/blog/travelling-salesman-problem).

### 🧬 Genetic Algorithm
The Genetic Algorithm is a heuristic search inspired by the process of natural selection. To learn more, [click here](https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3).

---

## 🔨 Implementation

### 📂 Main Modules

#### [`/breedAndMutate.py`](https://github.com/mkschulz9/GeneticAlgorithm/blob/main/geneticAlgorithm/breedAndMutatate.py)
- **Functions:**
    - `generateChildren(percentage, matingPool)`: Generates child paths.
    - `orderCrossover(parent1, parent2)`: Combines parent paths.
    - `swapMutation(child)`: Performs mutation on a child path.

#### [`/createMatingPool.py`](https://github.com/mkschulz9/GeneticAlgorithm/blob/main/geneticAlgorithm/createMatingPool.py)
- **Functions:**
    - `createMatingPool(population, tournamentSize, matingPoolSize)`: Creates a mating pool.
    - `selectElites(population, numberOfCities, numberOfElites)`: Selects elite paths.

#### [`/generateInitialPopulation.py`](https://github.com/mkschulz9/GeneticAlgorithm/blob/main/geneticAlgorithm/generateInitialPopulation.py)
- **Functions:**
    - `generateInitialPopulation(size, cityList, randomFactor)`: Generates an initial population.
    - `nearestNeighborWithRandomization(startCity, cityList, randomFactor)`: Generates a single path.
    - `getTopNNearestCities(currentCity, unvisitedCities, N)`: Finds closest 'N' cities.

#### [`/geneticAlgorithmOrchestrator.py`](https://github.com/mkschulz9/GeneticAlgorithm/blob/main/geneticAlgorithm/geneticAlgorithmOrchestrator.py)
- **Functions:**
    - `geneticAlgorithm()`: Orchestrates the algorithm flow.

#### [`/helperFunctions.py`](https://github.com/mkschulz9/GeneticAlgorithm/blob/main/geneticAlgorithm/helperFunctions.py)
- **Functions:**
    - `printWithNewline(*args, **kwargs)`: Debugging print function.
    - `openInputFile()`: Reads input files.
    - `calculateDistance(coordinate1, coordinate2)`: Calculates distance between coordinates.
    - `calculatePathDistance(path, numberOfCities)`: Calculates path distance.
    - `isValidPath(path)`: Validates a path.
    - `writeToFile(bestPathDistanceAndPath)`: Writes best path info to output file.

## 🚀 Getting Started: Running the Program

Here's how to clone the repository and run the main program on your local machine.

### 1️⃣ Clone the Repository

```bash
git clone [repository-URL]
```

### 2️⃣ Navigate to the Directory

```bash
cd [repository-name]
```

### 3️⃣ Install Dependencies

Using pip, you can install all required packages by running the following command:

```bash
pip install -r requirements.txt
```

> 📝 **Note**: If you're using a different dependency management tool, the installation command might differ.

### 4️⃣ Run the Main File

Execute the main program with the following command:

```bash
python main.py
```

> ✅ Now, the program should be up and running!
