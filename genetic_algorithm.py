import random, math
from scipy.spatial.distance import euclidean

class GeneticAlgorithm:
    def __init__(self):
        self.coordinates_cache = {}
        self.coordinates_cache_hits = 0
        self.path_cache = {}
        self.path_cache_hits = 0
        self.invalid_paths = 0
        self.children_mutated = 0
        self.input_file = None

    # finds the top N nearest cities to the current city
    # input: self, the current city, the list of unvisited cities, the number of nearest cities to find
    # output: a list of the top N nearest cities to the current city
    def nearest_cities(self, current_city, unvisited_cities, N):
        city_distances = [(city, self.distance_coordinates(current_city, city)) for city in unvisited_cities]
        city_distances.sort(key=lambda x: x[1])
        nearest_cities = [x[0] for x in city_distances[:min(N, len(city_distances))]]
        return nearest_cities

    # Generates a single path using the Nearest Neighbor algorithm with randomization
    # input: self, the starting city, the list of city coordinates, the randomization factor
    # output: a single path
    def generate_path(self, start_city, city_list, random_factor):
        unvisited_cities = set(city_list)
        unvisited_cities.discard(start_city)
        current_city = start_city
        path = [start_city]

        while unvisited_cities:
            nearest_cities = self.nearest_cities(current_city, unvisited_cities, random_factor)
            next_city = random.choice(nearest_cities)
            path.append(next_city)
            unvisited_cities.discard(next_city)
            current_city = next_city

        path.append(start_city)
        return path

    # Generates an initial population for the Genetic algorithm, verifying each path is unique
    # input: self, the size of the initial population, the list of cities to visit, the randomization factor
    # output: list of unique paths = size
    def generate_population(self, size, city_list, random_factor):
        population = []
        seen_paths = set()
        start_city = city_list[0]

        while len(population) < size:
            new_path = self.generate_path(start_city, city_list, random_factor)
            new_path_str = tuple(new_path)

            if new_path_str not in seen_paths:
                seen_paths.add(new_path_str)
                population.append(new_path)

        return population

    # selects elites from the population
    # Input: self, population list, number of cities, number of elites to select
    # Output: list of elite individuals
    def select_elites(self, population, number_cities, number_elites):
        path_distances = []
        
        for path in population:
                path_distance = self.distance_path(path, number_cities)
                path_distances.append((path, path_distance))
        
        selected_elites = sorted(path_distances, key=lambda x: x[1])[:number_elites]
        elite_paths = [elite_paths[0] for elite_paths in selected_elites]
        
        return elite_paths

    # tournament selection of non-elite population to create a mating pool
    # Input: self, population list, tournament size, mating pool size
    # Output: mating pool list
    def create_pool(self, population, tournament_size, pool_size):
        mating_pool = []

        while len(mating_pool) < pool_size:
                tournament_participants = random.sample(population, tournament_size)
                tournament_winner = min(tournament_participants, key=lambda x: self.distance_path(x, len(x) - 1)) 
                mating_pool.append(tournament_winner)
                population.remove(tournament_winner)

        return mating_pool

    # performs order crossover on two parents to produce a child
    # Input: two parents
    # Output: a child
    def order_crossover(self, parent1, parent2):
        while True:
            start_index, end_index = sorted(random.sample(range(1, len(parent1) - 1), 2))
            child = [None] * len(parent1)
            child[start_index:end_index] = parent1[start_index:end_index]
            parent2_index = 1
            
            for i in range(1, len(child) - 1):
                if child[i] is None:
                    while parent2[parent2_index] in child:
                        parent2_index += 1
                        if parent2_index == len(parent2) - 1:
                            parent2_index = 1
                    child[i] = parent2[parent2_index]
                
            child[0] = parent1[0]
            child[-1] = parent1[-1]
                
            if self.valid_path(child):
                return child

    # performs swap mutation on a child
    # Input: child
    # Output: a mutated child
    def swap_mutation(self, child):
        while True:
            index1, index2 = random.sample(range(1, len(child) - 1), 2)
            mutated_child = child.copy()
            mutated_child[index1], mutated_child[index2] = mutated_child[index2], mutated_child[index1]
        
            if self.valid_path(mutated_child):
                return mutated_child

    # generates a list of children using order crossover
    # Input: percentage to determine number of children to produce, mating pool
    # Output: a mutated child
    def generate_children(self, percentage, mating_pool):
        children = []
        number_children = math.ceil(len(mating_pool) * percentage)
   
        while len(children) < number_children:
            parent1 = random.choice(mating_pool)
            parent2 = random.choice(mating_pool)
        
            if parent1 != parent2:
                child = self.order_crossover(parent1, parent2)
                if child == None:
                    continue
                child[0] = parent1[0]
                child[-1] = parent1[-1]
                children.append(child)
    
        return children

    # calculates the Euclidean distance between two coordinates
    # input: two tuples of coordinates (X, y, z)
    # output: the Euclidean distance between the two coordinates
    def distance_coordinates(self, coordinate1, coordinate2):
        key = tuple(sorted((coordinate1, coordinate2)))
        if key in self.coordinates_cache:
            self.coordinates_cache_hits += 1
            return self.coordinates_cache[key]
    
        distance = euclidean(coordinate1, coordinate2)
        self.coordinates_cache[key] = distance
    
        return distance

    # calculates the total distance of a path
    # Input: a single path, number of cities to visit
    # Output: the total distance of the path
    def distance_path(self, path, number_cities):
        key = tuple(path)
        if key in self.path_cache:
            self.path_cache_hits += 1
            return self.path_cache[key]

        path_distance = sum(self.distance_coordinates(path[j], path[j+1]) for j in range(number_cities))
        self.path_cache[key] = path_distance
        return path_distance

    # verifies that a path is valid
    # Input: a single path
    # Output: True if the path is valid, False otherwise
    def valid_path(self, path):
        start_city = path[0]
    
        if start_city in path[1:-1] or len(set(path[1:-1])) != len(path[1:-1]):
           self.invalid_paths += 1        
           return False
   
        return True

    # opens the input file and parses its content
    # input: self
    # output: [number of cities to visit, list of city coordinates (x, y, z)]
    def collect_input(self):
        city_list = []

        with open(self.input_file, "r") as file:
            pointer_default = file.tell()
            if file.readline() == "" or file.readline() == "0":
                return (0, [])
    
            file.seek(pointer_default)
            number_cities = int(file.readline().strip())

            for line in file:
                x, y, z = map(int, line.strip().split())
                city_list.append((x, y, z))
    
        file.close()
        if number_cities == 1:
            city_list.append(city_list[0])
    
        return [number_cities, city_list]

    # writes output of the genetic algorithm (path distance and path) to a file
    # input: the best path distance and the best path
    # output: none
    @staticmethod
    def write_output(path_distance, path):
        with open("./io/outputs/output.txt", "w") as file:
            file.write(f"{path_distance:.3f}\n")
            for i in range(len(path)):
                file.write(f"{path[i][0]} {path[i][1]} {path[i][2]}\n")
        file.close()
            
    # prints stats about cache usage
    # input: self, elapsed time, initial best distance, population
    # output: final best distance
    def print_stats(self, elapsed_time, initial_best_distance, population): 
        final_best_disatnce = self.distance_path(min(population, key=lambda x: self.distance_path(x, len(x) - 1)), len(population[0]) - 1)
        percent_improvement = ((initial_best_distance - final_best_disatnce) / initial_best_distance) * 100
        
        print(f"\n***GENETIC ALGORITHM COMPLETE\nTIME TAKEN: {elapsed_time:.4f} seconds\nINITIAL BEST PATH DISTANCE: {initial_best_distance:.4f}\nENDING BEST PATH DISTANCE: {final_best_disatnce:.4f}\nPERCENT IMPROVEMENT: {percent_improvement:.2f}%\nNUMBER OF CHILDREN MUTATED: {self.children_mutated}\nDISTANCE BETWEEN COORDINATES CACHE HITS: {self.coordinates_cache_hits}\nPATH DISTANCE CACHE HITS: {self.path_cache_hits}\nNUMBER OF INVALID PATHS GENERATED: {self.invalid_paths}\nBEST PATH: {min(population, key=lambda x: self.distance_path(x, len(x) - 1))}\n")
        return final_best_disatnce        