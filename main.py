import random
import math
from scipy.spatial.distance import euclidean

# change defualt behavior of print function to print a new line after each call
def printWithNewline(*args, **kwargs):
    kwargs['end'] = kwargs.get('end', '\n') + '\n'
    print(*args, **kwargs)

# opens the input file and reads its content
# input: none
# output: a list containing the number of cities and a list of tuples containing the coordinates of each city
def openInputFile():
    cityCoordinates = []

    # open the file and read its content
    with open("./io/inputs/input1.txt", "r") as file:
        numberOfCities = int(file.readline().strip())

        for line in file:
            x, y, z = map(int, line.strip().split())
            cityCoordinates.append((x, y, z))
            
    printWithNewline("NUMBER OF CITIES TO VISIT:", numberOfCities)

    return [numberOfCities, cityCoordinates]

# calculates the Euclidean distance between two points
# input: two tuples of any dimension
# output: the Euclidean distance between the two points
def calculateDistance(coordinate1, coordinate2): return(euclidean(coordinate1, coordinate2))

# generates a list of initial paths
# input: the number of paths to generate, the number of cities, list of city coordinates
# output: list of unique paths = size
def generateInitialPopulation(size, numberOfCities, cityList): # check back here to try optimizing & think about heuristic to use (Check back to see if uniqueness matters & to generate a better population, maybe once half of the size of pop is generated, find the average distance for each already egenerated path, and only accept new paths below that average, etc.)
    population = []
    seenPaths = set()
    
    while len(population) < size:
        newPath = random.sample(cityList[1:], numberOfCities - 1)
        newPathStr = tuple(newPath)
        
        if newPathStr not in seenPaths:
            newPath.insert(0, cityList[0])
            newPath.append(cityList[0])
            seenPaths.add(newPathStr)
            population.append(newPath)
            
    printWithNewline(f"INITIAL POPULATION GENERATED (SIZE: {size})")
    return population

# calculates the total distance of each path in the population and orders them from shortest to longest
# input: size of population, population list, number of cities to visit
# output: ranked list of population
def rankPopulation(sizeOfPopulation, population, numberOfCities):
    rankedPopulation = []
    
    for i in range(sizeOfPopulation): # check back here to try optimizing
        totalDistance = 0
        for j in range(numberOfCities):
            totalDistance += calculateDistance(population[i][j], population[i][j+1])
        rankedPopulation.append([population[i], totalDistance])
    
    rankedPopulation.sort(key=lambda x: x[1])
    printWithNewline(f"POPULATION RANKED (BEST PATH DISTANCE: {rankedPopulation[0][1]:.4f})")
    return rankedPopulation # change rank function to only return the nth best paths (no need to pass back all paths), also when new paths get added we can drop the worst paths

# creates a mating pool from the ranked population
# input: percentage of population to pull from ranked population, ranked population
# output: top X% of ranked population
def createMatingPool(percentage, rankedPopulation):
    matingPool = []
    matingPoolSize = math.ceil(len(rankedPopulation) * percentage)
    
    for i in range(matingPoolSize):
        matingPool.append(rankedPopulation[i][0])
    
    printWithNewline(f"MATING POOL CREATED (SIZE: {matingPoolSize})")
    return matingPool

# generates a new pool of 'children' from the mating pool by interchanging the 'genes' of two 'parents'
# input: the number of children to generate, the mating pool
# output: a new pool of valid children (starts and ends at the same city, while visiting each city once)
#def generateNewGeneration(numberOfChildren, matingPool):
    
    

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
    # printWithNewline(calculateDistance((0, 0, -1), (10, 100, 30)))
    numberOfCitiesAndCityList = openInputFile()
    initialPopulationSize = 5000
    rankedPopulation = rankPopulation(initialPopulationSize, generateInitialPopulation(initialPopulationSize, numberOfCitiesAndCityList[0], 
                                                                                     numberOfCitiesAndCityList[1]), numberOfCitiesAndCityList[0])
    createMatingPool(0.5, rankedPopulation)
    
    
        
if __name__ == "__main__":
    test()
    #genetic_algorithm()