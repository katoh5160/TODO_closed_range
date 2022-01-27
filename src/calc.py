""" This is a example program for pytest. """

class Calc:
    """ 四則演算クラス """
    def __init__(self, num_a, num_b):
        self.num_a = num_a
        self.num_b = num_b

    def add(self):
        """ 足し算 """
        return self.num_a + self.num_b

    def diff(self):
        """ 引き算 """
        return self.num_a - self.num_b

    def multiple(self):
        """ 掛け算 """
        return self.num_a * self.num_b

    def division(self):
        """ 割り算 """
        return self.num_a / self.num_b
