import unittest
from main import Sugeno
import numpy as np
from data_classes import *
class TestSugeno(unittest.TestCase):

    def setUp(self) :
        self.test = Sugeno(number_of_inputs=2, number_of_outputs=1)

        prob1 = 0.9
        prob2 = 0
        lista1 = []
        lista2 = []

        for i in np.arange(-4, 4, 0.01):
            lista1.append((i, prob1))
            prob1 -= 0.00112519
            lista2.append((i, prob2))
            prob2 += 0.00112519

        self.xamhla = Variable("small", lista1)
        self.ypsila = Variable("large", lista2)

        self.input1=Input("x1", (-4, 4))
        self.input2 = Input("x2", (-4, 4))

    def test_sugeno_input(self):
        self.assertEqual(self.test.add_input(self.input1), True)
        self.assertEqual(self.test.add_input(self.input2), True)
        self.assertEqual(self.test.add_input(Input(name="x2", domain=(9, 4))), False)
        self.assertRaises(Exception, self.test.add_input, sugeno_inp= self.input2)
        print("Test1 : Success")

    def test_sugeno_input_variable(self):
        self.assertEqual(self.test.add_input_variable(self.input1, self.xamhla),True)
        self.assertEqual(self.test.add_input_variable(self.input2, self.ypsila),True)

        with self.assertRaises(Exception):
            self.test.add_input_variable(self.input1, Variable("meseo",[(20)]))
            self.test.add_input_variable(self.input1, Variable("meseo",[(3,1.2)]))

        print("Test2 : Success")

    def test_sugeno_output(self):
        self.assertEqual(self.test.add_output(Output("y1")),True)
        with self.assertRaises(Exception):
            self.test.add_output(Output("Y2"))

        print("Test3 : Success")


if __name__ == '__main__':
    unittest.main()
