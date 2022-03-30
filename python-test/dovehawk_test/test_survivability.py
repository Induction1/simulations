import unittest
from dovehawk.subject import Subject
from dovehawk.survivability_methods import instantiate_population


class SurvivabilityTestCase(unittest.TestCase):
    def test_population_size(self):
        self.assertEqual(50, len(instantiate_population(50)))
