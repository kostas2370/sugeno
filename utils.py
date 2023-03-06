import  numpy as np
from numpy import poly1d

class Utilities:

    @staticmethod
    def check_if_in_domain(domain: tuple, fuzzy_set: list) -> bool:

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

    @staticmethod
    def find_equation(fuzzy_set: list) -> np.poly1d or None:
        x: list=[inp[0] for inp in fuzzy_set]
        y: list=[inp[1] for inp in fuzzy_set]
        z: np.ndarray = np.polyfit(x, y, 3)
        f: np.poly1d = np.poly1d(z)

        return f

    @staticmethod
    def calculate_function (mult: list, x: list) -> float:
        calc: int= mult.pop()
        for p,x in zip(mult,x):
            calc+= p*x



        return calc
