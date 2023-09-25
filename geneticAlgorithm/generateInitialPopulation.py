import random, time
from geneticAlgorithm.helperFunctions import calculateDistance

# finds the top N nearest cities to the current city
# input: the current city, the list of unvisited cities, the number of nearest cities to find
# output: a list of the top N nearest cities to the current city
def getTopNNearestCities(currentCity, unvisitedCities, N):
    distancesToCurrentCity = [(city, calculateDistance(currentCity, city)) for city in unvisitedCities]
    
    distancesToCurrentCity.sort(key=lambda x: x[1])
    nearestCitiesToCurrentCity = [x[0] for x in distancesToCurrentCity[:min(N, len(distancesToCurrentCity))]]
    return nearestCitiesToCurrentCity

# Generates a single path using the Nearest Neighbor algorithm with randomization
# input: the starting city, the list of city coordinates, the randomization factor
# output: a single path
def nearestNeighborWithRandomization(startCity, cityList, randomFactor):
    unvisitedCities = set(cityList)
    unvisitedCities.discard(startCity)  
    currentCity = startCity
    path = [startCity]
    
    while unvisitedCities:
        nearestCities = getTopNNearestCities(currentCity, unvisitedCities, randomFactor)
        nextCity = random.choice(nearestCities)
        path.append(nextCity)
        unvisitedCities.discard(nextCity)
        currentCity = nextCity

    path.append(startCity)
    return path

# Generates an initial population for the Genetic algorithm, verifying each path is unique
# input: the size of the initial population, the list of cities to visit, the randomization factor
# output: list of unique paths = size
def generateInitialPopulation(size, cityList, randomFactor):
    population = []
    seenPaths = set()
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