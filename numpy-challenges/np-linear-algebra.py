import numpy as np

linenumber=1;
content_as_string_array="";

while True:
    try:
        line = input()
        if(linenumber==1):
            shape=line
            T=[int(s) for s in shape.split(' ')] 
            N=T[0]

        else:
            content_as_string_array+=line
            content_as_string_array+=' '    
        linenumber+=1        
    except EOFError:
        break
array_a =np.array(content_as_string_array[:-1].split(" ")).astype(float)

print(np.linalg.det(array_a.reshape(N, -1)))