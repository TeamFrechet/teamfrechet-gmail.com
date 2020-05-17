import matplotlib.pyplot as plt
import math
import numpy as np
import sympy as sym
import frechetcalcu

def symbolFunction():#chose here the function
    x = sym.symbols('x')
    func1 = sym.sin(x) # P
    func2 = sym.cos(x)# Q
    return [func1,func2]

if __name__ == '__main__':
    print("main")
    aproxximate = 5
    frechetcalcu.Start(symbolFunction()[0],symbolFunction()[1],aproxximate)



