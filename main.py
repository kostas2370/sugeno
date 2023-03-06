import numpy as np

from utils import Utilities


class Sugeno:
    # Properties :
    number_of_inputs: int
    number_of_outputs: int
    inputs: dict = {}
    outputs: list = []
    inputs_variables: dict = {}
    outputs_variables: dict = {}
    rules: list = []

    # Initiallizing the class
    def __init__(self, number_of_inputs: int = 2, number_of_outputs: int = 2):
        self.number_of_inputs = number_of_inputs
        self.number_of_outputs = number_of_outputs

    def add_input(self, name: str, domain: tuple) -> None:
        if self.number_of_inputs > len(self.inputs):
            self.inputs[name] = domain
            self.inputs_variables[name] = {}
        else:
            raise Exception("You added more inputs than the defined ones")

    def add_input_variable(self, input_name: str, variable_name: str, prob_list: list) -> None:

        if input_name not in self.inputs:
            raise Exception("There is not an input like that !")
        if not Utilities.check_if_valid_fuzzy_list(prob_list):
            raise Exception("Not a valid fuzzy set")
        if not Utilities.check_if_in_domain(self.inputs[input_name], prob_list):
            raise Exception("Not in the domain of the input")

        self.inputs_variables[input_name][variable_name] = prob_list

    def add_output(self, name) -> None:
        if self.number_of_outputs > len(self.outputs):
            self.outputs.append(name)
            self.outputs_variables[name] = {}
        else:
            raise Exception("You added more output than the defined ones")

    def add_output_formulas(self, output_name: str, formula_name: str, formula_list: list) -> None:

        if len(formula_list) != self.number_of_inputs+1:
            raise Exception("The formula list length should be the same with number of outputs")

        self.outputs_variables[output_name][formula_name] = formula_list

    def add_rule(self, inputs: list, output_formulas: list) -> None:
        if len(inputs) != self.number_of_inputs:
            raise Exception("The input list length should be the same with number of input")

        elif len(output_formulas) != self.number_of_outputs:
            raise Exception("The input list length should be the same with number of output")

        else:
            rule: tuple = ([(i, inputs[count]) for count, inp in enumerate(self.inputs) if
                            inputs[count] in self.inputs_variables[inp]],
                           [(o, output_formulas[count]) for count, o in enumerate(self.outputs) if
                            output_formulas[count] in self.outputs_variables[o]])

            if len(rule[0]) != self.number_of_inputs:
                raise Exception("One of the input variables does not exists !")
            elif len(rule[1]) != self.number_of_outputs:
                raise Exception("One of the output variables does not exists !")
            else:
                self.rules.append(rule)

    def calculate(self, inputs: list) -> float or int:
        function_values: list = []
        membership_values: list = []
        for rule in self.rules:
            functions = []
            for output in rule[1]:
                functions.append(Utilities.calculate_function(self.outputs_variables[output[0]][output[1]], inputs))
            function_values.append(functions)

            minimum = 0
            for inputs, x in zip(rule[0], inputs):

                a: any = Utilities.find_equation(self.inputs_variables[inputs[0]][inputs[1]])(x)
                if a > 1:
                    a = 1
                elif a < 0:
                    a = 0

                if minimum == 0:
                    minimum = a
                elif minimum >= a:
                    minimum = a
                else:
                    pass

            membership_values.append(minimum)
        mb_count: int = sum(membership_values)
        apotelesma: list = []
        for counterx, y in enumerate(self.outputs):
            synolo = 0

            for counter, mb in enumerate(membership_values):
                synolo += function_values[counter][counterx]*mb
            apotelesma.append((y, synolo/mb_count))

        return apotelesma


if __name__ == '__main__':
    bro = Sugeno(number_of_inputs=2, number_of_outputs=1)
    bro.add_input(name="x1", domain=(-4, 4))
    bro.add_input(name="x2", domain=(-4, 4))
    bro.add_output("y")

    bro.add_output_formulas("y", "y1", [-1, 1, 1])
    bro.add_output_formulas("y", "y2", [0, -1, 2])
    bro.add_output_formulas("y", "y3", [-1, 0, 3])
    bro.add_output_formulas("y", "y4", [-1, 1, 2])

    prob1 = 0.9
    prob2 = 0
    lista1 = []
    lista2 = []
    for i in np.arange(-4, 4, 0.01):
        lista1.append((i, prob1))
        prob1 -= 0.00112519
        lista2.append((i, prob2))
        prob2 += 0.00112519

    bro.add_input_variable("x1", "small", lista1)
    bro.add_input_variable("x1", "large", lista2)

    bro.add_input_variable("x2", "small", lista1)
    bro.add_input_variable("x2", "large", lista2)

    bro.add_rule(["small", "small"], ["y1"])
    bro.add_rule(["large", "small"], ["y2"])
    bro.add_rule(["small", "large"], ["y3"])
    bro.add_rule(["large", "large"], ["y4"])

    print(bro.calculate([-3, 3.8]))
