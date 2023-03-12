import matplotlib.pyplot as plt
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
                if type(inp.prob_formula) is list:
                    a: any = inp.prob_formula[1](x) if x < inp.prob_formula[0] else inp.prob_formula[2](x)
                else:

                    a: any = inp.prob_formula(x)
                a = 1 if a > 1 else 0 if a < 0 else a

                if minimum >= a:
                    minimum = a
                else:
                    pass

            membership_values.append(minimum)

        mb_count: float = sum(membership_values)
        print(membership_values)
        apotelesma: list = []
        for counterx, y in enumerate(self.outputs):
            synolo = 0

            for counter, mb in enumerate(membership_values):
                synolo += function_values[counter][counterx]*mb

            apotelesma.append((y.name, synolo/mb_count))

        return apotelesma

    def plot(self):
        y = 1
        fig = plt.figure()
        for x in self.inputs:
            fig.suptitle("Inputs :", fontsize=16)
            plt.subplot(2, 1, y).set_title(x.name)
            y += 1
            x.plot()
        plt.show()


