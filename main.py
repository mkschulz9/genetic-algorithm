import random
import math
from scipy.spatial.distance import euclidean

# calculates the Euclidean distance between two points
# input: two tuples of any dimension
# output: the Euclidean distance between the two points
def calculateDistance(coordinate1, coordinate2): return(euclidean(coordinate1, coordinate2))


def createInitialPopulation(size, cities):
    # Generate the initial population of paths
    # currently working on this

def rank_population(population):
    # Evaluate the fitness of each individual in the population
    pass

def create_mating_pool(population, rank_list):
    # Select parents for crossover
    pass

def crossover(parent1, parent2, start_index, end_index):
    # Implement two-point crossover
    pass

def mutate(child):
    # Implement mutation
    pass

def genetic_algorithm():
    # Main Genetic Algorithm function
    
    # Initialize parameters
    population_size = 100
    cities = []  # Example: [(0,0,0), (10,0,30), ...]
    
    # Step 1: Create initial population
    population = create_initial_population(population_size, cities)
    
    # Step 2: Evaluate the initial population
    rank_list = rank_population(population)
    
    # Main GA loop
    generations = 1000
    for i in range(generations):
        
        # Step 3: Parent Selection
        mating_pool = create_mating_pool(population, rank_list)
        
        # Step 4: Crossover and Mutation
        new_population = []
        for j in range(0, len(mating_pool), 2):
            parent1 = mating_pool[j]
            parent2 = mating_pool[j+1]
            
            # Perform crossover
            child = crossover(parent1, parent2, 1, 3)
            
            # Perform mutation
            child = mutate(child)
            
            new_population.append(child)
        
        # Step 5: Evaluate and replace population
        population = new_population
        rank_list = rank_population(population)
        
        # Optionally print or store the best path found so far
        # ...

def test():
    print(calculateDistance((0, 0, -1, 300), (10, 100, 30, 5)))
    
if __name__ == "__main__":
    test()
    #genetic_algorithm()
