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
            N, M, P= [int(s) for s in shape.split(' ')] 
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
content_as_string_array1 = content_as_string_array1[:-1]
content_as_string_array2 = content_as_string_array2[:-1]

array1=np.array(content_as_string_array1.split(" "))
array1=array1.astype(int)


array2=np.array(content_as_string_array2.split(" "))
array2=array2.astype(int)

array1=array1.reshape(N,P)

array2=array2.reshape(M,P)
print (np.concatenate((array1, array2), axis = 0)   )