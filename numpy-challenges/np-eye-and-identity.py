import numpy as np

while True:
    try:
        line = input()
        shape=line
        N, M= [int(s) for s in shape.split(' ')] 
    except EOFError:
        break

array_gen=np.eye(N,M)  
print(array_gen)