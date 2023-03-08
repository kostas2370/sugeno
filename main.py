import numpy as np

from utils import Utilities
from data_classes import Input, Variable, Output, OutputFormula, Rule


class Sugeno:
    # Properties :
    number_of_inputs: int
    number_of_outputs: int
    inputs: list = []
    outputs: list = []
    outputs_variables: list = []
    rules: list = []

    # Initiallizing the class
    def __init__(self, number_of_inputs: int = 2, number_of_outputs: int = 2):
        self.number_of_inputs = number_of_inputs
        self.number_of_outputs = number_of_outputs

    def add_input(self, *sugeno_inp: Input) -> bool:

        for sugeno_input in sugeno_inp:

            if sugeno_input.check_if_valid_domain():
                return False
            elif self.number_of_inputs > len(self.inputs):
                self.inputs.append(sugeno_input)
            else:
                raise Exception("You added more inputs than the defined ones")

        return True

    def add_input_variable(self, inp: Input, *variables: Variable) -> bool:
        for variable in variables:
            if inp not in self.inputs:
                raise Exception("There is not an input like that !")

            if not Utilities.check_if_in_domain(inp.domain, variable.prob_list):
                raise Exception("Not in the domain of the input")

            inp.variables.append(variable)
        return True
    def add_output(self, *outputs: Output or list) -> bool:
        for output in outputs:
            if self.number_of_outputs > len(self.outputs):
                self.outputs.append(output)

            else:
                raise Exception("You added more output than the defined ones")
        return True

    def add_rule(self, *rules: Rule) -> bool:

        for rule in rules:

            if len(rule.inputs) != self.number_of_inputs:
                raise Exception("The input list length should be the same with number of input")

            elif len(rule.output_formulas) != self.number_of_outputs:
                raise Exception("The input list length should be the same with number of output")

            for x, y in zip(rule.inputs, self.inputs):
                if x not in y.variables:
                    raise Exception(f"{x.variable_name} is not in this model")

            self.rules.append(rule)
        return True
    def calculate(self, *inputs: float or int) -> float or int:
        function_values: list = []
        membership_values: list = []

        for rule in self.rules:

            functions: list = []
            for out in rule.output_formulas:
                functions.append(Utilities.calculate_function(out.formula_list, inputs))
            function_values.append(functions)

            minimum = 1
            for inp, x in zip(rule.inputs, inputs):

                a: any = Utilities.find_equation(inp.prob_list)(x)
                a = 1 if a > 1 else 0 if a < 0 else a

                if minimum >= a:
                    minimum = a
                else:
                    pass

            membership_values.append(minimum)

        mb_count: float = sum(membership_values)
        apotelesma: list = []
        for counterx, y in enumerate(self.outputs):
            synolo = 0

            for counter, mb in enumerate(membership_values):
                synolo += function_values[counter][counterx]*mb

            apotelesma.append((y.name, synolo/mb_count))

        return apotelesma


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

    mikro = Variable("xamhlh", lista1)
    megalo = Variable("megalh", lista2)

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
