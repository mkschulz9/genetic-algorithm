import time, random
from geneticAlgorithm.generateInitialPopulation import generateInitialPopulation
from geneticAlgorithm.createMatingPool import selectElites, createMatingPool
from geneticAlgorithm.breedAndMutatate import generateChildren, swapMutation
from geneticAlgorithm.helperFunctions import openInputFile, calculatePathDistance, printWithNewline, printHelperFunctionStats

# runs the high-level genetic algorithm
# input: none
# output: the best path found and its details
def geneticAlgorithm():
    printWithNewline("***GENETIC ALGORITHM START")
    childrenMutated = 0
    startTime = time.time()
    numberOfCitiesAndCityList = openInputFile()
    
    if numberOfCitiesAndCityList[0] == 0:
        return (0, numberOfCitiesAndCityList[1])
    elif numberOfCitiesAndCityList[0] == 1:
        return (0, numberOfCitiesAndCityList[1])
    elif numberOfCitiesAndCityList[0] < 51:
        initialPopulationSize = 2 ** (numberOfCitiesAndCityList[0] - 2) if numberOfCitiesAndCityList[0] <= 11 else 2000
        randomFactor = 2
        matingPoolSize = int(initialPopulationSize * 0.2)
        numberOfElites = int(matingPoolSize * 0.5)
        generations = 50
        tournamentSize = 10
        mutation_rate = 0.15
        offspringRate = 5
    elif numberOfCitiesAndCityList[0] < 101:
        initialPopulationSize = 1500
        randomFactor = 2
        matingPoolSize = int(initialPopulationSize * 0.125)
        numberOfElites = int(matingPoolSize * 0.5)
        generations = 50
        tournamentSize = 10
        mutation_rate = 0.075
        offspringRate = 5
    elif numberOfCitiesAndCityList[0] < 201:
        initialPopulationSize = 1000
        randomFactor = 2
        matingPoolSize = int(initialPopulationSize * 0.075)
        numberOfElites = int(matingPoolSize * 0.5)
        generations = 50
        tournamentSize = 10
        mutation_rate = 0.05
        offspringRate = 5
    else:
        initialPopulationSize = 600
        randomFactor = 2
        matingPoolSize = int(initialPopulationSize * 0.075)
        numberOfElites = int(matingPoolSize * 0.5)
        generations = 50
        tournamentSize = 10
        mutation_rate = 0.05
        offspringRate = 5
    
    population = generateInitialPopulation(initialPopulationSize, numberOfCitiesAndCityList[1], randomFactor)
    initialBestPathDistance = calculatePathDistance(min(population, key=lambda x: calculatePathDistance(x, len(x) - 1)), len(population[0]) - 1)
    initialBestPath = min(population, key=lambda x: calculatePathDistance(x, len(x) - 1))
    printWithNewline(f"INITIAL BEST PATH DISTANCE: {initialBestPathDistance:.4f}")
    if numberOfCitiesAndCityList[0] <= 11:
            print(f"NUMBER OF CITIES IS {numberOfCitiesAndCityList[0]}, SO THE INITIAL PATH IS THE OPTIMAL PATH:\n{initialBestPath}")
            return(initialBestPathDistance, initialBestPath)
    
    for i in range(generations):
        print(f"***CURRENT GENERATION: {i+1}/{generations}")
        
        elitePaths = selectElites(population, numberOfCitiesAndCityList[0], numberOfElites)
        nonElitePopulation = [path for path in population if path not in elitePaths]
        
        if len(population) > initialPopulationSize * 2:
            population = random.sample(population, initialPopulationSize * 2)
        
        matingPool = createMatingPool(nonElitePopulation, tournamentSize, matingPoolSize - numberOfElites)
        matingPool += elitePaths

        children = generateChildren(offspringRate, matingPool)
        
        for child in children:
            if random.random() < mutation_rate:
                childrenMutated += 1
                child = swapMutation(child)
        
        population += children

    endTime = time.time()
    elapsedTime = endTime - startTime
    finalBestPathDistance = calculatePathDistance(min(population, key=lambda x: calculatePathDistance(x, len(x) - 1)), len(population[0]) - 1)
    percentImprovement = ((initialBestPathDistance - finalBestPathDistance) / initialBestPathDistance) * 100
    
    printWithNewline(f"***GENETIC ALGORITHM COMPLETE\nTIME TAKEN: {elapsedTime:.4f} seconds\nINITIAL BEST PATH DISTANCE: {initialBestPathDistance:.4f}\nENDING BEST PATH DISTANCE: {finalBestPathDistance:.4f}\nPERCENT IMPROVEMENT: {percentImprovement:.2f}%\nNUMBER OF CHILDREN MUTATED: {childrenMutated}\nBEST PATH: {min(population, key=lambda x: calculatePathDistance(x, len(x) - 1))}")
    printHelperFunctionStats()
    if finalBestPathDistance > initialBestPathDistance:
        return (initialBestPathDistance, initialBestPath)
    return (finalBestPathDistance, min(population, key=lambda x: calculatePathDistance(x, len(x) - 1)))