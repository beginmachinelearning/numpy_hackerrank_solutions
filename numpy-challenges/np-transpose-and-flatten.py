import numpy as np

contents = ""

linenumber=1;
content_as_string=""
while True:
    try:
        line = input()
        if(linenumber==1):
            shape=line
        else:
            content_as_string+=line
            content_as_string+=' '
        linenumber+=1
        contents+=line
        contents+='\n'
    except EOFError:
        break
N, M= shape.split() 

content_as_string = content_as_string[:-1]
K=np.array(content_as_string.split(" "))
K=K.astype(int)
ip=K.reshape(int(N),int(M))
print(np.transpose(ip))
print(ip.flatten())