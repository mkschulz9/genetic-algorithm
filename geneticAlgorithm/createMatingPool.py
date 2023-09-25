import time, random
from geneticAlgorithm.helperFunctions import calculatePathDistance

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
        winnerofTournamentStr = tuple(winnerofTournament)

        matingPool.append(winnerofTournament)
        addedPaths.add(winnerofTournamentStr)
        population.remove(winnerofTournament)
        
    endTime = time.time()
    elapsedTime = endTime - startTime

    print(f"MATING POOL CREATED (SIZE: {matingPoolSize}, TIME TAKEN: {elapsedTime:.4f} seconds)")
    return matingPool