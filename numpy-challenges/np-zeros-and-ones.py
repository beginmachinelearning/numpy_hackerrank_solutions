import numpy as np

while True:
    try:
        line = input()
        print(np.zeros(([int(s) for s in line.split(' ')]), dtype = np.int))  
        print(np.ones([int(s) for s in line.split(' ')], dtype = np.int))      
    except EOFError:
        break