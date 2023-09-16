import random
import math
from scipy.spatial.distance import euclidean
import time

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
    with open("./input.txt", "r") as file:
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
    startTime = time.time()
    
    while len(population) < size:
        newPath = random.sample(cityList[1:], numberOfCities - 1)
        newPathStr = tuple(newPath)
        
        if newPathStr not in seenPaths:
            newPath.insert(0, cityList[0])
            newPath.append(cityList[0])
            seenPaths.add(newPathStr)
            population.append(newPath)
    
    endTime = time.time()
    elapsedTime = endTime - startTime
        
    printWithNewline(f"INITIAL POPULATION GENERATED (SIZE: {size}, TIME TAKEN: {elapsedTime:.4f} seconds)")
    return population

# calculates the total distance of each path in the population and orders them from shortest to longest
# input: population list, number of cities to visit, initial population size
# output: ranked list of population
def rankPopulation(population, numberOfCities, initialPopulationSize):
    rankedPopulation = []
    startTime = time.time()
    
    for i in range(len(population)): # check back here to try optimizing
        totalDistance = 0
        for j in range(numberOfCities):
            totalDistance += calculateDistance(population[i][j], population[i][j+1])
        rankedPopulation.append([population[i], totalDistance])
    
    rankedPopulation.sort(key=lambda x: x[1])
    
    endTime = time.time()
    elapsedTime = endTime - startTime
    
    # reduce population size if its over the initial population size (optimization)
    if len(rankedPopulation) > initialPopulationSize:
        rankedPopulation = rankedPopulation[:initialPopulationSize]
        
    printWithNewline(f"POPULATION RANKED (BEST PATH DISTANCE: {rankedPopulation[0][1]:.4f}, TIME TAKEN: {elapsedTime:.4f} seconds)")
    return rankedPopulation # change rank function to only return the nth best paths (no need to pass back all paths), also when new paths get added we can drop the worst paths

# creates a mating pool from the ranked population using  Roulette wheel-based selection
# input: percentage of population to pull from ranked population, ranked population
# output: a list of populations selected for mating (List containspaths)

#def createMatingPool(percentage, rankedPopulation):
    #atingPool = []
    
    
    
    
    #printWithNewline(f"MATING POOL CREATED (SIZE: {matingPoolSize}, TIME TAKEN: {elapsedTime:.4f} seconds)")
    #return matingPool

# creates a mating pool from the ranked population
# input: percentage of population to pull from ranked population, ranked population
# output: top X% of ranked population
def createMatingPool(percentage, rankedPopulation):
    matingPool = []
    matingPoolSize = math.ceil(len(rankedPopulation) * percentage)
    startTime = time.time()
    
    for i in range(matingPoolSize):
        matingPool.append(rankedPopulation[i][0])
    
    endTime = time.time()
    elapsedTime = endTime - startTime
    
    printWithNewline(f"MATING POOL CREATED (SIZE: {matingPoolSize}, TIME TAKEN: {elapsedTime:.4f} seconds)")
    return matingPool

# generates a new pool of 'children' from the mating pool by interchanging the 'genes' of two 'parents'
# input: the number of children to generate, the mating pool
# output: a new pool of valid children (starts and ends at the same city, while visiting each city once)
def generateChildren(percentage, matingPool):
    children = []
    numberOfChildren = math.ceil(len(matingPool) * percentage)
    startTime = time.time()
    
    while len(children) < numberOfChildren:
        parent1 = random.choice(matingPool) # check back here to try optimizing -> pick higher ranked parents more often
        parent2 = random.choice(matingPool)

        if parent1 != parent2:
            crossoverPoint1, crossoverPoint2 = sorted(random.sample(range(1, len(parent1) - 1), 2))

            # Create slices from parent1 between crossover points
            temporaryChild = parent1[crossoverPoint1:crossoverPoint2]

            # Get the remaining elements from parent2
            remainingElements = [item for item in parent2 if item not in temporaryChild]

            # Concatenate to get the child
            child = remainingElements[:crossoverPoint1] + temporaryChild + remainingElements[crossoverPoint1:]

            # Ensuring start and end points remain the same as parents
            child[0] = parent1[0]
            child[-1] = parent1[-1]

            children.append(child)
    
    endTime = time.time()
    elapsedTime = endTime - startTime
    
    printWithNewline(f"CHILDREN GENERATED (SIZE: {numberOfChildren}, TIME TAKEN: {elapsedTime:.4f} seconds)")        
    return children

def mutate(child):
    # Implement mutation
    pass

# this funciton runs the high-level genetic algorithm
# input: number of generations to run
# output: the best path found and its details
def geneticAlgorithm(numberOfGenerations):
    printWithNewline("***GENETIC ALGORITHM STARTED")
    #open input file
    numberOfCitiesAndCityList = openInputFile()
    startTime = time.time()
    # generate initial population
    initialPopulationSize = 500
    population = generateInitialPopulation(initialPopulationSize, numberOfCitiesAndCityList[0], numberOfCitiesAndCityList[1])
    
    # generation loop
    for i in range(numberOfGenerations):
        printWithNewline(f"***CURRENT GENERATION: {i+1}/{numberOfGenerations}")
        # rank population
        rankedPopulation = rankPopulation(population, numberOfCitiesAndCityList[0], initialPopulationSize)
        if i == 0:
            initialBestPathDistance = rankedPopulation[0][1]
        # create mating pool
        matingPool = createMatingPool(0.3, rankedPopulation)
        # generate children
        children = generateChildren(2, matingPool)
        # add children to population
        population.extend(children)
        
    endTime = time.time()
    elapsedTime = endTime - startTime
    percentImprovement = ((initialBestPathDistance - rankedPopulation[0][1]) / initialBestPathDistance) * 100
    
    printWithNewline(f"***GENETIC ALGORITHM COMPLETE\nTIME TAKEN: {elapsedTime:.4f} seconds\nINITIAL BEST PATH DISTANCE: {initialBestPathDistance:.4f}\nENDING BEST PATH DISTANCE: {rankedPopulation[0][1]:.4f}\nPERCENT IMPROVEMENT: {percentImprovement:.2f}%\nBEST PATH: {rankedPopulation[0][0]}")
    return (rankedPopulation[0][1], rankedPopulation[0][0]) 

# writes output of the genetic algorithm (path distance and path) to a file
# input: the best path distance and the best path
# output: none
def writeToFile(bestPathDistanceAndPath):
    with open("./output.txt", "w") as file:
        file.write(f"{bestPathDistanceAndPath[0]:.3f}\n")
        for i in range(len(bestPathDistanceAndPath[1])):
            file.write(f"{bestPathDistanceAndPath[1][i][0]} {bestPathDistanceAndPath[1][i][1]} {bestPathDistanceAndPath[1][i][2]}\n")

if __name__ == "__main__":
    writeToFile(geneticAlgorithm(10))
   