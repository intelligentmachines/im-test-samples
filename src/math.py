class MathUtils(object):
    @classmethod
    def divide(cls, a: int, b: float) -> float:
        """
        :param a:
        :param b:
        :return:
        """
        return a / b

    @classmethod
    def is_even(cls, a) -> bool:
        if a % 2 == 0:
            return True
        return False
