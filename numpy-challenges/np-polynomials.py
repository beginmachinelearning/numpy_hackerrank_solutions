import numpy as np

linenumber=1;
while True:
    try:
        line = input()
        array_a=line
        line = input()
        x=line[0]
        x=float(x)
    except EOFError:
        break
K =np.array(array_a.split(" ")).astype(float)
print(np.polyval(K, x))
