import numpy as np
from utils import  Utilities

class Sugeno:

    number_of_inputs: int
    number_of_outputs: int
    inputs: dict = {}
    outputs: list = []
    inputs_variables: dict = {}
    outputs_variables: dict = {}
    rules: list = []

    def __init__(self, number_of_inputs: int = 2, number_of_outputs: int = 1):
        self.number_of_inputs = number_of_inputs
        self.number_of_outputs = number_of_outputs

    def add_input(self, name: str, domain: tuple) -> None:
        if self.number_of_inputs > len(self.inputs):
            self.inputs[name] = domain
            self.inputs_variables[name] = {}
        else:
            raise Exception("You added more inputs than the defined ones")

    def add_output(self, name) -> None:
        if self.number_of_outputs > len(self.outputs):
            self.outputs.append(name)
            self.outputs_variables[name] = {}
        else:
            raise Exception("You added more output than the defined ones")

    def add_input_variable(self, input_name: str, variable_name: str, prob_list: list) -> None:

        if input_name not in self.inputs:
            raise Exception("There is not an input like that !")
        if not Utilities.check_if_valid_fuzzy_list(prob_list):
            raise Exception("Not a valid fuzzy set")
        if not Utilities.check_if_in_domain(self.inputs[input_name], prob_list):
            raise Exception("Not in the domain of the input")

        self.inputs_variables[input_name][variable_name] = prob_list

    def add_output_formulas(self, output_name: str, formula_name: str, formula_list: list) -> None:

        if len(formula_list) != self.number_of_inputs+1:
            raise Exception("The formula list length should be the same with number of outputs")

        self.outputs_variables[output_name][formula_name] = formula_list

    def add_rule(self, inputs: list, output_formulas: list) -> None:
        if len(inputs) != self.number_of_inputs :
            raise Exception("The input list length should be the same with number of input")

        elif len(output_formulas) != self.number_of_outputs:
            raise Exception("The input list length should be the same with number of output")

        else:
            rule: tuple = ([(i, inputs[count])
                            for count, i in enumerate(self.inputs) if inputs[count] in self.inputs_variables[i]],
                           [(o, output_formulas[count])
                            for count, o in enumerate(self.outputs) if output_formulas[count] in self.outputs_variables[o]])

            if len(rule[0]) != self.number_of_inputs:
                raise Exception("One of the input variables does not exists !")
            elif len(rule[1]) != self.number_of_outputs:
                raise Exception("One of the output variables does not exists !")
            else:
                self.rules.append(rule)


if __name__ == '__main__':
    bro = Sugeno()
    bro.add_input(name="xd", domain=(0, 10))
    bro.add_input(name="xd1", domain=(0, 15))
    bro.add_output("output1")

    bro.add_input_variable("xd", "argos", [(0, 1), (1, 1), (10, 0.5), (3, 0.9)])
    bro.add_input_variable("xd", "meseos", [(0, 0.5)])
    bro.add_input_variable("xd", "Grhgoros", [(0, 0.5)])

    bro.add_input_variable("xd1", "Grhgoros", [(0, 0.5)])

    bro.add_output_formulas("output1", "k1form", [2, 3, 0])
    bro.add_rule(["argos", "Grhgoros"],["k1form"])
    print(bro.rules)
