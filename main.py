class Sugeno:

    number_of_inputs: int
    number_of_outputs: int
    inputs: dict = {}
    outputs: dict = {}
    inputs_variables: dict = {}
    outputs_variables: dict = {}

    def __init__(self, number_of_inputs: int = 2, number_of_outputs: int = 2):
        self.number_of_inputs=number_of_inputs
        self.number_of_outputs = number_of_outputs

    def add_input(self, name: str,domain: tuple) -> None:
        if self.number_of_inputs > len(self.inputs):
            self.inputs[name] = domain
            self.inputs_variables[name] = {}
        else:
            raise Exception("You added more inputs than the defined ones")

    def add_output(self, name: str, domain: list) -> None:
        if self.number_of_inputs > len(self.inputs):

            self.outputs[name]: domain
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

    @staticmethod
    def check_if_valid_fuzzy_list(fuzzy_set: list) -> bool:
        dupl: dict = {}
        for x in fuzzy_set:
            if x[0] not in dupl:
                dupl[x[0]] = x[0]
            else:
                raise Exception("There are duplicates in the fuzzy set !")

            if type(x) is not tuple:
                return False
            elif x[1] > 1 or x[1] < 0:
                return False
            else:
                pass

        return True

    @staticmethod
    def check_if_in_domain(domain, fuzzy_set: list) -> bool:

        if type(domain) is not tuple:
            raise Exception("""The type of the domain should be tuple , the first part "
                            should be the first value and the second part is the last value of the domain
                            """)

        for x in fuzzy_set:

            if type(x) is not tuple:
                raise Exception("This is not a valid fuzzy set")
            elif x[0] < domain[0] or x[0] > domain[1]:
                return False

            else:
                pass
        return True


if __name__ == '__main__':
    bro = Sugeno()
    bro.add_input(name="xd",domain=(0, 10))
    bro.add_input(name="xd1", domain=(0, 15))
    bro.add_input_variable("xd", "argos", [(0, 1), (1, 1), (10, 0.5), (3, 0.9)])
    bro.add_input_variable("xd", "meseos", [(0, 0.5)])
    bro.add_input_variable("xd", "Grhgoros", [(0, 0.5)])
    for x in bro.inputs_variables:
        print(f"{x} : {bro.inputs_variables[x]}")