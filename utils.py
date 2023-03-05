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
