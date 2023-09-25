import time, random
from genetic_algorithm import GeneticAlgorithm
from algorithm_config import get_algorithm_parameters

# main function
if __name__ == "__main__":
    # instantiate object and set file path
    GA = GeneticAlgorithm()
    GA.input_file = "./io/inputs/input1.txt"
    
    print("***GENETIC ALGORITHM START")
    start_time = time.time()
    
    # collect input from file
    cities = GA.collect_input()
    # set hyperparameters
    if cities[0] == 0 or cities[0] == 1:
        print(f"NUMBER OF CITIES IS {cities[0]}, SO THE PATH DISTANCE IS 0\n")
        GA.write_output(0, cities[1])
        exit()
    else:
        hyperparams = get_algorithm_parameters(cities[0])

    # generate intial populaiton
    population = GA.generate_population(hyperparams['population_size'], cities[1], hyperparams['random_factor'])
    # find initial best path & its distance
    initial_best_distance = GA.distance_path(min(population, key=lambda x: GA.distance_path(x, len(x) - 1)), len(population[0]) - 1)
    initial_best_path = min(population, key=lambda x: GA.distance_path(x, len(x) - 1))
    print(f"INITIAL BEST PATH DISTANCE: {initial_best_distance:.4f}\n")
    # check if initial path is optimal
    if cities[0] <= 11:
        print(f"NUMBER OF CITIES IS {cities[0]}, SO THE INITIAL PATH IS THE OPTIMAL PATH:\n{initial_best_path}")
        GA.write_output(initial_best_distance, initial_best_path)
        exit()
    
    # start genetic algorithm loop
    for i in range(hyperparams['generations']):
        print(f"***CURRENT GENERATION: {i+1}/{hyperparams['generations']}")

        # cut population down if it grows too large
        if len(population) > hyperparams['population_size'] * 2:
            population = random.sample(population, hyperparams['population_size'] * 2)
        
        # select elites and non-elites from population
        elite_paths = GA.select_elites(population, cities[0], hyperparams['number_elites'])
        non_elites = [path for path in population if path not in elite_paths]
        
        # create mating pool
        mating_pool = GA.create_pool(non_elites, hyperparams['tournament_size'], hyperparams['pool_size'] - hyperparams['number_elites'])
        mating_pool += elite_paths

        # generate children from mating pool
        children = GA.generate_children(hyperparams['offspring_rate'], mating_pool)

        # mutate children
        for child in children:
            if random.random() < hyperparams['mutation_rate']:
                GA.children_mutated += 1
                child = GA.swap_mutation(child)
    
        population += children

    end_time = time.time()
    elapsed_time = end_time - start_time
    
    final_best_disatnce = GA.print_stats(elapsed_time, initial_best_distance, population)
    
    # check if genetic algorithm made negative improvement
    if final_best_disatnce > initial_best_distance:
        GA.write_output(initial_best_distance, initial_best_path)
        exit()
    GA.write_output(final_best_disatnce, min(population, key=lambda x: GA.distance_path(x, len(x) - 1)))