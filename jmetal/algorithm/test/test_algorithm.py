import unittest

from jmetal.algorithm.multiobjective.nsgaii import NSGAII
from jmetal.algorithm.multiobjective.smpso import SMPSO
from jmetal.component import RankingAndCrowdingDistanceComparator, CrowdingDistanceArchive
from jmetal.operator import Polynomial, SBX, BinaryTournamentSelection
from jmetal.problem import ZDT1
from jmetal.util.termination_criteria import StoppingByEvaluations


class RunningAlgorithmsTestCases(unittest.TestCase):

    def setUp(self):
        self.problem = ZDT1()
        self.population_size = 100
        self.offspring_size = 100
        self.mating_pool_size = 100
        self.max_evaluations = 100
        self.mutation = Polynomial(probability=1.0 / self.problem.number_of_variables, distribution_index=20)
        self.crossover = SBX(probability=1.0, distribution_index=20)

    def test_NSGAII(self):
        NSGAII(
            problem=self.problem,
            population_size=self.population_size,
            offspring_size=self.offspring_size,
            mating_pool_size=self.mating_pool_size,
            mutation=self.mutation,
            crossover=self.crossover,
            selection=BinaryTournamentSelection(comparator=RankingAndCrowdingDistanceComparator()),
            termination_criteria=StoppingByEvaluations(max=1000)
        ).run()

    def test_SMPSO(self):
        SMPSO(
            problem=self.problem,
            swarm_size=self.population_size,
            mutation=self.mutation,
            leaders=CrowdingDistanceArchive(100),
            termination_criteria=StoppingByEvaluations(max=1000)
        ).run()


if __name__ == '__main__':
    unittest.main()