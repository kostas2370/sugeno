from sugeno import Sugeno
from data_classes import *


if __name__ == '__main__':
    bro = Sugeno(number_of_inputs=2, number_of_outputs=1)
    input1 = Input("x1", (-4, 4))
    input2 = Input("x2", (-4, 4))
    bro.add_input(input1, input2)
    bro.add_output(Output("y1"))

    prob1 = 0.9
    prob2 = 0
    lista1 = []
    lista2 = []

    for i in np.arange(-4, 4, 0.01):
        lista1.append((i, prob1))
        prob1 -= 0.00112519
        prob2 += 0.00112519

        lista2.append((i, prob2))

    mikro = Variable("fuzzy_set", "xamhlh", lista1)
    megalo = Variable("fuzzy_set", "megalh", lista2)

    bro.add_input_variable(input1, mikro, megalo)
    bro.add_input_variable(input2, mikro, megalo)
    y1 = OutputFormula("y1", [-1, 1, 1])
    y2 = OutputFormula("y2", [0, -1, 2])
    y3 = OutputFormula("y3", [-1, 0, 3])
    y4 = OutputFormula("y4", [-1, 1, 2])

    rule1 = Rule([mikro, mikro], [y1])
    rule2 = Rule([megalo, mikro], [y2])
    rule3 = Rule([mikro, megalo], [y3])
    rule4 = Rule([megalo, megalo], [y4])

    bro.add_rule(rule1, rule2, rule3, rule4)

    print(bro.calculate(-4, -4))


    exit()
