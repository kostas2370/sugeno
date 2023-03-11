import numpy as np


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
        x: list = [inp[0] for inp in fuzzy_set]
        y: list = [inp[1] for inp in fuzzy_set]
        z: any = np.polyfit(x, y, 3)
        f: np.poly1d = np.poly1d(z)

        return f

    @staticmethod
    def calculate_function(mult: list, x: tuple) -> float:
        calc: int = mult[-1]
        for p, z in zip(mult[:-1], x):

            calc += p*z

        return calc

    @staticmethod
    def find_quadratic(p1: tuple, p2: tuple, p3: tuple):

        x1, y1 = p1
        x2, y2 = p2
        x3, y3 = p3
        a = ((y2-y1)*(x3-x1)-(y3-y1)*(x2-x1))/((x2-x1)*(x3 ** 2-x1 ** 2)-(x3-x1)*(x2 ** 2-x1 ** 2))
        b = ((y2-y1)-a*(x2 ** 2-x1 ** 2))/(x2-x1)
        c = y1-a*x1 ** 2-b*x1
        return np.poly1d([a, b, c])

    @staticmethod
    def find_line(p1: tuple, p2: tuple):
        x1, y1 = p1
        x2, y2 = p2

        slope = (y2-y1)/(x2-x1)
        y_intercept = y1-slope*x1

        return np.poly1d([slope, y_intercept])

