import numpy as np

contents = ""

linenumber=1;
content_as_string_array="";
while True:
    try:
        line = input()
        if(linenumber==1):
            shape=line
            N, M= [int(s) for s in shape.split(' ')] 
        elif(linenumber>1):
            content_as_string_array+=line
            content_as_string_array+=' '
        linenumber+=1        
    except EOFError:
        break
array_a =np.array(content_as_string_array[:-1].split(" ")).astype(int)
array_a=array_a.reshape(N, M)
print(np.prod(np.sum(array_a, axis=0)))