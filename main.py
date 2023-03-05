import numpy as np
class Sugeno:

    number_of_inputs: int
    number_of_outputs: int
    inputs: dict = {}
    outputs: list = []
    inputs_variables: dict = {}
    outputs_variables: dict = {}

    def __init__(self, number_of_inputs: int = 2, number_of_outputs: int = 2):
        self.number_of_inputs = number_of_inputs
        self.number_of_outputs = number_of_outputs

    @staticmethod
    def check_if_in_domain(domain, fuzzy_set: list) -> bool:

        if type(domain) is not tuple:
            raise Exception("""The type of the domain should be tuple , the first part "
                            should be the first value and the second part is the last value of the domain
                            """)
        for k in fuzzy_set:

            if type(k) is not tuple:
                raise Exception("This is not a valid fuzzy set")
            elif k[0] < domain[0] or k[0] > domain[1]:
                return False

            else:
                pass
        return True

    @staticmethod
    def check_if_valid_fuzzy_list(fuzzy_set: list) -> bool:
        dupl: dict = {}
        for k in fuzzy_set:
            if k[0] not in dupl:
                dupl[k[0]] = k[0]
            else:
                raise Exception("There are duplicates in the fuzzy set !")

            if type(k) is not tuple:
                return False
            elif k[1] > 1 or k[1] < 0:
                return False
            else:
                pass

        return True

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
        if not Sugeno.check_if_valid_fuzzy_list(prob_list):
            raise Exception("Not a valid fuzzy set")
        if not Sugeno.check_if_in_domain(self.inputs[input_name], prob_list):
            raise Exception("Not in the domain of the input")

        self.inputs_variables[input_name][variable_name] = prob_list

    def add_output_formulas(self, output_name: str, formula_name: str, formula_list: list) -> None:

        if len(formula_list) != self.number_of_inputs+1:
            raise Exception("The formula list length should be the same with number of outputs")

        self.outputs_variables[output_name][formula_name] = formula_list

    def add_rule(self,output_formula, *args,**kwargs) -> None:

        return None
if __name__ == '__main__':
    bro = Sugeno()
    bro.add_input(name="xd", domain=(0, 10))
    bro.add_input(name="xd1", domain=(0, 15))
    bro.add_output("output1")

    bro.add_input_variable("xd", "argos", [(0, 1), (1, 1), (10, 0.5), (3, 0.9)])
    bro.add_input_variable("xd", "meseos", [(0, 0.5)])
    bro.add_input_variable("xd", "Grhgoros", [(0, 0.5)])
    bro.add_output_formulas("output1", "k1form", [2, 3, 0])

    for x in bro.outputs_variables:
        print(f"{x} : {bro.outputs_variables[x]}")
