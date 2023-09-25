import time, random, math
from geneticAlgorithm.helperFunctions import isValidPath, printWithNewline

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