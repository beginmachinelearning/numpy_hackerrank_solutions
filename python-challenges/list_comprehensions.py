strings = ['apple', 'bat', 'cat', 'dog', 'elephant', 'frog']
[x.upper() for x in strings if len(x)>3]

ints = [4, 0, 1, 5, 6]

def getplus3(a, f):
    return [f(x) for x in a]

getplus3(ints, lambda x:x+3)