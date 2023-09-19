import random
import math
import time
from scipy.spatial.distance import euclidean

# change defualt behavior of print function to print a new line after each call (remove before submitting)
def printWithNewline(*args, **kwargs):
    kwargs['end'] = kwargs.get('end', '\n') + '\n'
    print(*args, **kwargs)

# opens the input file and parses its content
# input: none
# output: [number of cities to visit, list of city coordinates (x, y, z)]
def openInputFile():
    cityList = []

    # open the file and read its content
    with open("./io/inputs/input3.txt", "r") as file:
        numberOfCities = int(file.readline().strip())

        for line in file:
            x, y, z = map(int, line.strip().split())
            cityList.append((x, y, z))
            
    print("NUMBER OF CITIES TO VISIT:", numberOfCities)

    return [numberOfCities, cityList]

# calculates the Euclidean distance between two coordinates
# input: two tuples of coordinates (X, y, z)
# output: the Euclidean distance between the two coordinates
def calculateDistance(coordinate1, coordinate2): return(euclidean(coordinate1, coordinate2))

# finds the top N nearest cities to the current city
# input: the current city, the list of unvisited cities, the number of nearest cities to find
# output: a list of the top N nearest cities to the current city
def getTopNNearestCities(currentCity, unvisitedCities, N):
    distancesToCurrentCity = [(city, calculateDistance(currentCity, city)) for city in unvisitedCities]
    
    distancesToCurrentCity.sort(key=lambda x: x[1])
    nearestCitiesToCurrentCity = [x[0] for x in distancesToCurrentCity[:min(N, len(distancesToCurrentCity))]]
    
    return nearestCitiesToCurrentCity

# generates a list of initial paths using nearest neighbor with randomization heuristic
# input: the starting city, the list of city coordinates, the randomization factor
# output: list of unique paths = size
def nearestNeighborWithRandomization(startCity, cityList, randomFactor):
    unvisitedCities = set(cityList) - {startCity}
    currentCity = startCity
    path = [startCity]
    
    while unvisitedCities:
        nearestCities = getTopNNearestCities(currentCity, unvisitedCities, randomFactor)
        nextCity = random.choice(nearestCities)
        path.append(nextCity)
        unvisitedCities.remove(nextCity)
        currentCity = nextCity

    path.append(startCity)
    return path

# generates a list of initial paths
# input: the size of the initial population, the list of cities to visit
# output: list of unique paths = size
def generateInitialPopulation(size, cityList):
    population = []
    seenPaths = set()
    randomFactor = 3
    startCity = cityList[0]
    startTime = time.time()
    
    while len(population) < size:
        newPath = nearestNeighborWithRandomization(startCity, cityList, randomFactor)
        newPathStr = tuple(newPath)
        
        if newPathStr not in seenPaths:
            seenPaths.add(newPathStr)
            population.append(newPath)

    endTime = time.time()
    elapsedTime = endTime - startTime
    
    print(f"INITIAL POPULATION GENERATED (SIZE: {size}, TIME TAKEN: {elapsedTime:.4f} seconds)")
    return population

# calculates the total distance of a path
# Input: a single path, number of cities to visit
# Output: the total distance of the path
def calculatePathDistance(path, numberOfCities):
    return sum(calculateDistance(path[j], path[j+1]) for j in range(numberOfCities))

# selects elites from the population
# Input: population list, number of cities, number of elites to select
# Output: list of elite individuals
def selectElites(population, numberOfCities, numberOfElites):
    pathDistances = []
    
    for path in population:
        pathDistance = calculatePathDistance(path, numberOfCities)
        pathDistances.append((path, pathDistance))
    
    selectedElitePathsAndDistances = sorted(pathDistances, key=lambda x: x[1])[:numberOfElites]
    elitePaths = [elitePaths[0] for elitePaths in selectedElitePathsAndDistances]
    
    return elitePaths

# tournament selection of non-elite population to create a mating pool
# Input: population list, tournament size, mating pool size
# Output: mating pool list
def createMatingPool(population, tournamentSize, matingPoolSize):
    matingPool = []
    addedPaths = set()
    startTime = time.time()

    while len(matingPool) < matingPoolSize:
        tournamentParticipants = random.sample(population, tournamentSize)
        winnerofTournament = min(tournamentParticipants, key=lambda x: calculatePathDistance(x, len(x) - 1))
        winnerofTournamentString = tuple(winnerofTournament)
        
        if winnerofTournamentString not in addedPaths:
            matingPool.append(winnerofTournament)
            addedPaths.add(winnerofTournamentString)

    
    endTime = time.time()
    elapsedTime = endTime - startTime

    print(f"MATING POOL CREATED (SIZE: {matingPoolSize}, TIME TAKEN: {elapsedTime:.4f} seconds)")
    return matingPool

# verifies that a path is valid
# Input: a single path
# Output: True if the path is valid, False otherwise
def isValidPath(path):
    startAndEndCityity = path[0]
    
    if startAndEndCityity in path[1:-1] or len(set(path[1:-1])) != len(path[1:-1]):
       return False
   
    return True

# performs order crossover on two parents to produce a child
# Input: two parents
# Output: a child
def orderCrossover(parent1, parent2):
    while True:
        startIndex, endIndex = sorted(random.sample(range(1, len(parent1) - 1), 2))
        
        child = [None] * len(parent1)
        child[startIndex:endIndex] = parent1[startIndex:endIndex]
        
        parent2Index = 1
        for i in range(1, len(child) - 1):
            if child[i] is None:
                while parent2[parent2Index] in child:
                    parent2Index += 1
                    if parent2Index == len(parent2) - 1:
                        parent2Index = 1
                
                child[i] = parent2[parent2Index]
        
        child[0] = parent1[0]
        child[-1] = parent1[-1]
        
        if isValidPath(child):
            return child

# performs swap mutation on a child
# Input: child
# Output: a mutated child
def swapMutation(child):
    while True:
        index1, index2 = random.sample(range(1, len(child) - 1), 2)
        mutatedChild = child.copy()
        mutatedChild[index1], mutatedChild[index2] = mutatedChild[index2], mutatedChild[index1]
        
        if isValidPath(mutatedChild):
            return mutatedChild

# generates a list of children using order crossover
# Input: percentage to determine number of children to produce, mating pool
# Output: a mutated child
def generateChildren(percentage, matingPool):
    children = []
    numberOfChildren = math.ceil(len(matingPool) * percentage)
    startTime = time.time()
    
    while len(children) < numberOfChildren:
        parent1 = random.choice(matingPool)
        parent2 = random.choice(matingPool)
        
        if parent1 != parent2:
            child = orderCrossover(parent1, parent2)
            if child == None:
                continue
            child[0] = parent1[0]
            child[-1] = parent1[-1]
            children.append(child)
   
    endTime = time.time()
    elapsedTime = endTime - startTime
    
    printWithNewline(f"CHILDREN GENERATED (SIZE: {numberOfChildren}, TIME TAKEN: {elapsedTime:.4f} seconds)")
    return children

# runs the high-level genetic algorithm
# input: none
# output: the best path found and its details
def geneticAlgorithm():
    printWithNewline("***GENETIC ALGORITHM START")
    startTime = time.time()
    numberOfCitiesAndCityList = openInputFile()
    
    if numberOfCitiesAndCityList[0] < 51:
        initialPopulationSize = 2000
        matingPoolSize = int(initialPopulationSize * 0.175)
        numberOfElites = 7
        generations = 10
        tournamentSize = 7
        mutation_rate = 0.15
        offspringRate = 0.55
    elif numberOfCitiesAndCityList[0] < 101:
        initialPopulationSize = 1000
        matingPoolSize = int(initialPopulationSize * 0.125)
        numberOfElites = 4
        generations = 4
        tournamentSize = 8
        mutation_rate = 0.075
        offspringRate = 0.4
    elif numberOfCitiesAndCityList[0] < 201:
        initialPopulationSize = 400
        matingPoolSize = int(initialPopulationSize * 0.125)
        numberOfElites = 3
        generations = 4
        tournamentSize = 6
        mutation_rate = 0.05
        offspringRate = 0.25
    else:
        initialPopulationSize = 300
        matingPoolSize = int(initialPopulationSize * 0.075)
        numberOfElites = 1
        generations = 3
        tournamentSize = 6
        mutation_rate = 0.03
        offspringRate = 0.15
    
    population = generateInitialPopulation(initialPopulationSize, numberOfCitiesAndCityList[1])
    initialBestPathDistance = calculatePathDistance(min(population, key=lambda x: calculatePathDistance(x, len(x) - 1)), len(population[0]) - 1)
    printWithNewline(f"INITIAL BEST PATH DISTANCE: {initialBestPathDistance:.4f}")
    
    for i in range(generations):
        print(f"***CURRENT GENERATION: {i+1}/{generations}")

        elitePaths = selectElites(population, numberOfCitiesAndCityList[0], numberOfElites)
        nonElitePopulation = [path for path in population if path not in elitePaths]
        
        matingPool = createMatingPool(nonElitePopulation, tournamentSize, matingPoolSize - numberOfElites)
        selectedParents = elitePaths + matingPool

        children = generateChildren(offspringRate, selectedParents)
        
        for child in children:
            if random.random() < mutation_rate:
                child = swapMutation(child)
        
        population += children
        population = selectElites(population, numberOfCitiesAndCityList[0], initialPopulationSize)
        
    endTime = time.time()
    elapsedTime = endTime - startTime
    finalBestPathDistance = calculatePathDistance(min(population, key=lambda x: calculatePathDistance(x, len(x) - 1)), len(population[0]) - 1)
    percentImprovement = ((initialBestPathDistance - finalBestPathDistance) / initialBestPathDistance) * 100
    
    printWithNewline(f"***GENETIC ALGORITHM COMPLETE\nTIME TAKEN: {elapsedTime:.4f} seconds\nINITIAL BEST PATH DISTANCE: {initialBestPathDistance:.4f}\nENDING BEST PATH DISTANCE: {finalBestPathDistance:.4f}\nPERCENT IMPROVEMENT: {percentImprovement:.2f}%\nBEST PATH: {min(population, key=lambda x: calculatePathDistance(x, len(x) - 1))}")
    return (finalBestPathDistance, min(population, key=lambda x: calculatePathDistance(x, len(x) - 1)))


# writes output of the genetic algorithm (path distance and path) to a file
# input: the best path distance and the best path
# output: none
def writeToFile(bestPathDistanceAndPath):
    with open("./output.txt", "w") as file:
        file.write(f"{bestPathDistanceAndPath[0]:.3f}\n")
        for i in range(len(bestPathDistanceAndPath[1])):
            file.write(f"{bestPathDistanceAndPath[1][i][0]} {bestPathDistanceAndPath[1][i][1]} {bestPathDistanceAndPath[1][i][2]}\n")

# main function
if __name__ == "__main__":
    writeToFile(geneticAlgorithm())
   