import numpy as np

linenumber=1;
content_as_string_array1="";
content_as_string_array2=""
while True:
    try:
        line = input()
        if(linenumber==1):
            shape=line
            T=[int(s) for s in shape.split(' ')] 
            N=T[0]
           
        elif(linenumber>1 and linenumber<=N+1):
            content_as_string_array1+=line
            content_as_string_array1+=' '
        else:
            content_as_string_array2+=line
            content_as_string_array2+=' '    
        linenumber+=1        
    except EOFError:
        break
array_a =np.array(content_as_string_array1[:-1].split(" ")).astype(int)
array_b =np.array(content_as_string_array2[:-1].split(" ")).astype(int)
print(np.dot(array_a.reshape(N, -1), array_b.reshape(N, -1)))