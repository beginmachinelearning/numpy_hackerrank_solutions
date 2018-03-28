import numpy as np

linenumber=1;
while True:
    try:
        line = input()
        array_a=line
        line = input()
        array_b=line
    except EOFError:
        break
array_a =np.array(array_a.split(" ")).astype(int)
array_b =np.array(array_b.split(" ")).astype(int)
print(np.inner(array_a, array_b))
print(np.outer(array_a, array_b))