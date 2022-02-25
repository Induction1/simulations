import unittest
from dovehawk.subject import Subject
from dovehawk.survivability import instantiate_population

class SurvivabilityTestCase(unittest.TestCase):
    def test_population_size(self):
        self.assertEqual(50, len(instantiate_population(50)))  # add assertion here