# 同じディレクトリ内からand.pyを読み込む__init__.pyを構成する

# from .and_module import AND1, AND2
from .and_module import AND1, AND2
# from .and2_module import AND2
from .or_module import OR
from .nand_module import NAND
from .xor_module import XOR

# __all__ = ["AND1", "AND2"]

# and.pyはandを読み込む時に、元からあるandと混合してしまうので、and_module.pyに分けた