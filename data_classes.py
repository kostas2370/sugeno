from dataclasses import dataclass, InitVar, field

import numpy as np
import matplotlib.pyplot as plt
from utils import Utilities


@dataclass
class Input:
    name: str
    domain: tuple
    variables: list = field(default_factory=list)

    def check_if_valid_domain(self) -> bool:
        return self.domain[0] >= self.domain[1]

    def plot(self):
        for x in self.variables:
            x.plot(self.domain)
        plt.legend()


@dataclass
class Variable:
    list_type: InitVar[str]
    variable_name: str
    prob_formula: list

    def __post_init__(self, list_type: str):

        if list_type == "fuzzy_set" and Utilities.check_if_valid_fuzzy_list(self.prob_formula):
            self.prob_formula = Utilities.find_equation(self.prob_formula)
        elif list_type == "direct" and (len(self.prob_formula) == 2 or 3):
            self.prob_formula = np.poly1d(self.prob_formula)
        elif list_type == "quadratic":
            self.prob_formula = Utilities.find_quadratic(self.prob_formula[0],
                                                         self.prob_formula[1],
                                                         self.prob_formula[2])
        elif list_type == "line":
            self.prob_formula = Utilities.find_line(self.prob_formula[0], self.prob_formula[1])
        else:
            raise Exception("Invalid fuzzyset or function")

    def plot(self, domain: tuple[int]) -> None:
        x = np.arange(domain[0], domain[1]+1)
        y = self.prob_formula(x)
        plot = plt.plot(x, y, label=self.variable_name)
        return plot


@dataclass
class Output:
    name: str


@dataclass()
class OutputFormula:
    formula_name: str
    formula_list: list

    def __str__(self):
        return self.formula_name


@dataclass
class Rule:
    inputs: list[Variable]
    output_formulas: list[OutputFormula]

