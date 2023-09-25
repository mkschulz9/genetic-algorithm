def get_algorithm_parameters(city_count):
    default_settings = {
        "random_factor": 2,
        "generations": 50,
        "tournament_size": 10,
        "offspring_rate": 5
    }

    if city_count < 51:
        settings = {
            "population_size": 2 ** (city_count - 2) if city_count <= 11 else 2000,
            "size_factor": 0.2,
            "mutation_rate": 0.15,
        }
    elif city_count < 101:
        settings = {
            "population_size": 1500,
            "size_factor": 0.125,
            "mutation_rate": 0.075,
        }
    elif city_count < 201:
        settings = {
            "population_size": 1000,
            "size_factor": 0.075,
            "mutation_rate": 0.05,
        }
    else:
        settings = {
            "population_size": 600,
            "size_factor": 0.075,
            "mutation_rate": 0.05,
        }

    settings.update(default_settings)
    settings["pool_size"] = int(settings["population_size"] * settings["size_factor"])
    settings["number_elites"] = int(settings["pool_size"] * 0.5)
    
    return settings