from .and_module import AND2
from .or_module import OR
from .nand_module import NAND

class XOR:
    def __init__(self, x1, x2):
        Nand = NAND(x1, x2)
        Or = OR(x1, x2)
        s1 = Nand.output()
        s2 = Or.output()
        self.And = AND2(s1, s2)
    def output(self):
        return self.And.output()
