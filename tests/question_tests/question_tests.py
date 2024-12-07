#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())
import unittest
from src.question_a.question_a import create_multiplication_table
from src.question_d.question_d import get_most_likely_ancestor_consensus

class TestFinalAssignment(unittest.TestCase):
    def test_multiplication_table(self):
        table = create_multiplication_table()
        self.assertEqual(table[0], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(table[9], [10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

    def test_dna_consensus(self):
        result = get_most_likely_ancestor_consensus("AGCTAGCTAG", "AGCT")
        self.assertEqual(result, [1, 5])

if __name__ == "__main__":
    unittest.main()


