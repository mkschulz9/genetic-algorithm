# 🎓 CSCI-561: Foundations of Artificial Intelligence

## 🗺️ Assignment #1: 3D Traveling Salesman Problem with Genetic Algorithm

Welcome to the repository for Assignment #1 for CSCI-561, USC's Foundations of Artificial Intelligence graduate course. This project is an exploration of solving the 3D Traveling Salesman Problem (TSP) using a Genetic Algorithm implemented in Python. 

---

## 📋 Table of Contents
1. [Introduction](#🌟-introduction)
    - [TSP](#🚗-traveling-salesperson-problem)
    - [Genetic Algorithm](#🧬-genetic-algorithm)
2. [Implementation](#🔨-implementation)
    - [GeneticAlgorithm Class](#geneticalgorithm-class-genetic_algorithmpy)
    - [Main](#main-mainpy)
    - [Algorithm Configuration](#algorithm-configuration-algorithm_configpy)
3. [Getting Started: Running the Program](#🚀-getting-started-running-the-program)

---

## 🌟 Introduction

### 🚗 Traveling Salesperson Problem
The TSP is a classic problem in computer science, considered NP-hard. To learn more, [click here](https://blog.routific.com/blog/traveling-salesman-problem).

### 🧬 Genetic Algorithm
The Genetic Algorithm is a heuristic search inspired by the process of natural selection. To learn more, [click here](https://towardsdatascience.com/introduction-to-genetic-algorithms-including-example-code-e396e98d8bf3).

---

## 🔨 Implementation

### GeneticAlgorithm Class ([`genetic_algorithm.py`](https://github.com/mkschulz9/GeneticAlgorithm/blob/main/genetic_algorithm.py))
- **Methods:**
    - `nearest_cities(self, current_city, unvisited_cities, N)`: 
      - Finds closest 'N' cities to the current city.
    - `generate_path(self, start_city, city_list, random_factor)`: 
      - Generates a single path using the nearest neighbor algorithm with randomization.
    - `generate_population(self, size, city_list, random_factor)`: 
      - Generates an initial population.
    - `createMatingPool(population, tournamentSize, matingPoolSize)`: 
      - Creates a mating pool.
    - `select_elites(self, population, number_cities, number_elites)`: 
      - Selects elite paths from the population.
    - `create_pool(self, population, tournament_size, pool_size)`: 
      - Creates a mating pool.
    - `order_crossover(self, parent1, parent2)`: 
      - Performs order crossover on two parents.
    - `swap_mutation(self, child)`: 
      - Performs swap mutation on a child.
    - `generate_children(self, percentage, mating_pool)`: 
      - Generates children from the mating pool.
    - `distance_coordinates(self, coordinate1, coordinate2)`: 
      - Calculates distance between coordinates.
    - `distance_path(self, path, number_cities)`: 
      - Calculates path distance.
    - `valid_path(self, path)`: 
      - Validates a path.
    - `collect_input(self)`: 
      - Collects input information.
    - `write_output(path_distance, path)`: 
      - Writes best path info to output file.
    - `print_stats(self, elapsed_time, initial_best_distance, population)`: 
      - Prints statistics after Genetic algorithm execution.

### Main ([`main.py`](https://github.com/mkschulz9/GeneticAlgorithm/blob/main/main.py))
- Orchestrates the execution of the Genetic algorithm.

### Algorithm Configuration ([`algorithm_config.py`](https://github.com/mkschulz9/GeneticAlgorithm/blob/main/algorithm_config.py))
- Configues the hyperparameters for the Genetic algorithm based on city size.

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
