from dataclasses import dataclass, field
from utils import Utilities


@dataclass
class Input:
    name: str
    domain: tuple
    variables: list = field(default_factory=list)

    def check_if_valid_domain(self) -> bool:
        return self.domain[0] >= self.domain[1]


@dataclass
class Variable:
    variable_name: str
    prob_list: list

    def __post_init__(self):
        if not Utilities.check_if_valid_fuzzy_list(self.prob_list):
            raise Exception("Not a valid fuzzy set")


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

