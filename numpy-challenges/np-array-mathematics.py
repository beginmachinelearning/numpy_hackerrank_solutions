import numpy as np

contents = ""

linenumber=1;
content_as_string_array1=""
content_as_string_array2=""
while True:
    try:
        line = input()
        if(linenumber==1):
            shape=line
            N, M= [int(s) for s in shape.split(' ')] 
        elif(linenumber>1 and linenumber<=N+1):
            content_as_string_array1+=line
            content_as_string_array1+=' '
        else: 
            content_as_string_array2+=line
            content_as_string_array2+=' '
        linenumber+=1
        contents+=line
        contents+='\n'
    except EOFError:
        break

array_a =np.array(content_as_string_array1[:-1].split(" ")).astype(int)
array_b =np.array(content_as_string_array2[:-1].split(" ")).astype(int)
print(np.add(array_a, array_b).reshape(N,M))
print(np.subtract(array_a, array_b).reshape(N,M))
print(np.multiply(array_a, array_b).reshape(N,M))
print(np.divide(array_a, array_b).reshape(N,M).astype(int))
print(np.mod(array_a, array_b).reshape(N,M))
print(np.power(array_a, array_b).reshape(N,M))