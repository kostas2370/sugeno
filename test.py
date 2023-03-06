import unittest
from main import Sugeno
import numpy as np
class TestSugeno(unittest.TestCase):

    def setUp(self) :
        self.test = Sugeno(number_of_inputs=2, number_of_outputs=1)

    def test_sugeno_input(self):
        self.assertEqual(self.test.add_input(name="x1", domain=(-4, 4)),True)
        self.assertEqual(self.test.add_input(name="x2", domain=(9, 4)), False)
        self.assertEqual(self.test.add_input(name="x2", domain=(-4, 4)),True)
        self.assertRaises(Exception, self.test.add_input, name="x4",  domain=(1, 4))

    def test_sugeno_output(self):
        self.assertIsNone(self.test.add_output(name="y"))
        self.assertRaises(Exception, self.test.add_output, name="y44")

    def test_sugeno_input_variable(self):

        prob1 = 0.9
        prob2 = 0
        lista1 = []
        lista2 = []

        for i in np.arange(-4, 4, 0.01):
            lista1.append((i, prob1))
            prob1 -= 0.00112519
            lista2.append((i, prob2))
            prob2 += 0.00112519

        self.assertIsNone(self.test.add_input_variable("x1", "small", lista1))
        self.assertIsNone(self.test.add_input_variable("x1", "large", lista2))
        self.assertIsNone(self.test.add_input_variable("x2", "small", lista1))
        self.assertIsNone(self.test.add_input_variable("x2", "large", lista2))
        self.assertIsNone(self.test.add_input_variable("x2", "large", [(1,1),(2,0.5)]))
        self.assertRaises(Exception, self.test.add_input_variable, input_name="y44", variable_name="Xamhla", prob_list=lista1)
        self.assertRaises(Exception, self.test.add_input_variable, input_name="y44", variable_name="Xamhla", prob_list=[(3,0.5),(9)])
        self.assertRaises(Exception, self.test.add_input_variable, input_name="x1", variable_name="Xamhla", prob_list=[(3,0.5),(9,0.8)])


if __name__ == '__main__':
    unittest.main()
