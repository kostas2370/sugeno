import unittest
from main import Sugeno
import numpy as np
from data_classes import *


class TestSugeno(unittest.TestCase):

    def setUp(self):
        self.test = Sugeno(number_of_inputs=2, number_of_outputs=1)
        self.number = 0

        prob1 = 0.9
        prob2 = 0
        lista1 = []
        lista2 = []

        for i in np.arange(-4, 4, 0.01):
            lista1.append((i, prob1))
            prob1 -= 0.00112519
            lista2.append((i, prob2))
            prob2 += 0.00112519

        self.mikro = Variable("small", lista1)
        self.megalo = Variable("large", lista2)

        self.input1 = Input("x1", (-4, 4))
        self.input2 = Input("x2", (-4, 4))

        self.y1 = OutputFormula("y1", [-1, 1, 1])
        self.y2 = OutputFormula("y2", [0, -1, 2])
        self.y3 = OutputFormula("y3", [-1, 0, 3])
        self.y4 = OutputFormula("y4", [-1, 1, 2])

        self.rule1 = Rule([self.mikro, self.mikro], [self.y1])
        self.rule2 = Rule([self.megalo, self.mikro], [self.y2])
        self.rule3 = Rule([self.mikro, self.megalo], [self.y3])
        self.rule4 = Rule([self.megalo, self.megalo], [self.y4])

    def test_sugeno_input(self):
        self.assertEqual(self.test.add_input(self.input1), True)
        self.assertEqual(self.test.add_input(self.input2), True)
        self.assertEqual(self.test.add_input(Input(name="x2", domain=(9, 4))), False)
        self.assertRaises(Exception, self.test.add_input, sugeno_inp=self.input2)
        self.number+=1
        print(f"Test Add Input : Success")

    def test_sugeno_input_variable(self):
        self.assertEqual(self.test.add_input_variable(self.input1, self.mikro), True)
        self.assertEqual(self.test.add_input_variable(self.input2, self.megalo), True)

        with self.assertRaises(Exception):
            self.test.add_input_variable(self.input1, Variable("meseo", [20]))
            self.test.add_input_variable(self.input1, Variable("meseo", [(3, 1.2)]))

        self.number += 1
        print(f"Test Add_Variable : Success")

    def test_sugeno_output(self):
        self.assertEqual(self.test.add_output(Output("y1")), True)
        with self.assertRaises(Exception):
            self.test.add_output(Output("Y2"))

        self.number+=1
        print(f"Test Add Output : Success")

    def test_sugeno_add_rule(self):
        self.assertEqual(self.test.add_rule(self.rule1), True)
        self.assertEqual(self.test.add_rule(self.rule2), True)
        self.assertEqual(self.test.add_rule(self.rule3), True)
        self.assertEqual(self.test.add_rule(self.rule4), True)

        self.number += 1
        print(f"Test Add Rule : Success")


if __name__ == '__main__':
    unittest.main()
