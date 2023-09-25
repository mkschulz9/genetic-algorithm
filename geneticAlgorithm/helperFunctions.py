from scipy.spatial.distance import euclidean

distanceBetweenCoordinatesCache = {}
distanceBetweenCoordinatesCacheHits = 0
pathDistanceCache = {}
pathDistanceCacheHits = 0
numberOfInvalidPathsGenerated = 0

# change defualt behavior of print function to print a new line after each call (remove before submitting)
def printWithNewline(*args, **kwargs):
    kwargs['end'] = kwargs.get('end', '\n') + '\n'
    print(*args, **kwargs)

# opens the input file and parses its content
# input: none
# output: [number of cities to visit, list of city coordinates (x, y, z)]
def openInputFile():
    cityList = []

    with open("./io/inputs/basecase.txt", "r") as file:
        filePointerStartingPosition = file.tell()
        if file.readline() == "" or file.readline() == "0":
            return (0, [])
    
        file.seek(filePointerStartingPosition)
        numberOfCities = int(file.readline().strip())

        for line in file:
            x, y, z = map(int, line.strip().split())
            cityList.append((x, y, z))
    
    file.close()
    if numberOfCities == 1:
            cityList.append(cityList[0])
    
    print("NUMBER OF CITIES TO VISIT:", numberOfCities)
    return [numberOfCities, cityList]

# calculates the Euclidean distance between two coordinates
# input: two tuples of coordinates (X, y, z)
# output: the Euclidean distance between the two coordinates
def calculateDistance(coordinate1, coordinate2):
    global distanceBetweenCoordinatesCacheHits
    key = tuple(sorted((coordinate1, coordinate2)))
    if key in distanceBetweenCoordinatesCache:
        distanceBetweenCoordinatesCacheHits += 1
        return distanceBetweenCoordinatesCache[key]
    
    distance = euclidean(coordinate1, coordinate2)
    distanceBetweenCoordinatesCache[key] = distance
    
    return distance

# calculates the total distance of a path
# Input: a single path, number of cities to visit
# Output: the total distance of the path
def calculatePathDistance(path, numberOfCities):
    global pathDistanceCacheHits
    key = tuple(path)
    if key in pathDistanceCache:
        pathDistanceCacheHits += 1
        return pathDistanceCache[key]

    pathDistance = sum(calculateDistance(path[j], path[j+1]) for j in range(numberOfCities))
    pathDistanceCache[key] = pathDistance
    return pathDistance

# verifies that a path is valid
# Input: a single path
# Output: True if the path is valid, False otherwise
def isValidPath(path):
    global numberOfInvalidPathsGenerated
    startAndEndCityity = path[0]
    
    if startAndEndCityity in path[1:-1] or len(set(path[1:-1])) != len(path[1:-1]):
       numberOfInvalidPathsGenerated += 1        
       return False
   
    return True

# writes output of the genetic algorithm (path distance and path) to a file
# input: the best path distance and the best path
# output: none
def writeToFile(bestPathDistanceAndPath):
    with open("./io/outputs/output.txt", "w") as file:
        file.write(f"{bestPathDistanceAndPath[0]:.3f}\n")
        for i in range(len(bestPathDistanceAndPath[1])):
            file.write(f"{bestPathDistanceAndPath[1][i][0]} {bestPathDistanceAndPath[1][i][1]} {bestPathDistanceAndPath[1][i][2]}\n")
    file.close()
            
# prints stats about cache usage
# input: none
# output: none
def printHelperFunctionStats(): print(f"HELPER FUNCTION STATS:\nDISTANCE BETWEEN COORDINATES CACHE HITS: {distanceBetweenCoordinatesCacheHits}\nPATH DISTANCE CACHE HITS: {pathDistanceCacheHits}\nNUMBER OF INVALID PATHS GENERATED: {numberOfInvalidPathsGenerated}\n")