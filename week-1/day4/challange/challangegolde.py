import random

# Gene class
class Gene:
    def __init__(self, value):
        self.value = value  # 0 or 1

    def mutate(self):
        """ Mutate the gene (flip the value). """
        self.value = 1 if self.value == 0 else 0

# Chromosome class
class Chromosome:
    def __init__(self):
        self.genes = [Gene(random.choice([0, 1])) for _ in range(10)]

    def mutate(self, mutation_probability=0.5):
        """ Mutate some genes of the chromosome with a given mutation probability. """
        for gene in self.genes:
            if random.random() < mutation_probability:
                gene.mutate()

# DNA class
class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]

    def mutate(self, mutation_probability=0.5):
        """ Mutate some chromosomes with the given mutation probability. """
        for chromosome in self.chromosomes:
            chromosome.mutate(mutation_probability)

    def is_all_ones(self):
        """ Check if the DNA is made entirely of 1s. """
        for chromosome in self.chromosomes:
            for gene in chromosome.genes:
                if gene.value != 1:
                    return False
        return True

# Organism class
class Organism:
    def __init__(self, environment_factor):
        self.dna = DNA()
        self.environment_factor = environment_factor  # Probability for mutation

    def mutate(self):
        """ Perform mutation on the organism's DNA based on the environment factor. """
        self.dna.mutate(self.environment_factor)

    def has_all_ones(self):
        """ Check if the organism's DNA is made entirely of 1s. """
        return self.dna.is_all_ones()

# Simulation function
def simulate_evolution():
    # Instantiate an organism with an environment mutation factor (e.g., 0.5)
    organism = Organism(environment_factor=0.5)
    generations = 0

    # Keep mutating until the organism's DNA becomes all 1s
    while not organism.has_all_ones():
        organism.mutate()
        generations += 1

    return generations

# Run the simulation
generations_needed = simulate_evolution()

# Print the result
print(f"The organism reached a DNA of all 1s in {generations_needed} generations.")

