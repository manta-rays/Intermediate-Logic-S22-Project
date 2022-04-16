from typing import int, str, char

class Operator(object):
    """The Operator Class"""
    # constructor
    def __init__(self, symbol_: char, dim_: int = 2):
        self.symbol: char = symbol_
        self.dim: int = dim_

class Expression(object):
    def __init__(self):
        self.exp: str

    
class Node(object):
    """The Node Class, which makes up the expression trees"""
    # constructor
    def __init__(self, op_ = None, exp_ = None):
        self.parent: Node
        

        self.op: Operator = op_
        self.exp: Expression = exp_
        
