import numpy as np
input_string=input()
array_a =np.array(input_string.split(" ")).astype(float)
print(np.floor(array_a))
print(np.ceil(array_a))
print(np.rint(array_a))