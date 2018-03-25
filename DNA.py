import random
from Vector import get_random_unit_vector


class DNA:
    def __init__(self, lifespan, genes):

        if genes is not None:
            self.genes = genes
        else:
            self.genes = []

            for i in range(lifespan):
                self.genes.append(get_random_unit_vector())
                # These vectors are already unit vectors, so in order to set new magnitude, there is no need to
                # normalize them before multiplying by new magnitude
                self.genes[i].multiply(0.1)

    def crossover(self, partner, lifespan):
        new_genes = []
        mid_point = random.randint(0, len(self.genes))
        for i in range(len(self.genes)):
            if i > mid_point:
                new_genes.append(self.genes[i])
            else:
                new_genes.append(partner.genes[i])

        return DNA(lifespan, new_genes)

    def mutation(self):
        for gene in self.genes:
            random_number = random.randint(0, 99)
            # Mutation rate 3%
            if random_number < 3:
                gene = get_random_unit_vector()
                gene.multiply(0.1)


