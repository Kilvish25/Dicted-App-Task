import math
def findN(X):
    n=math.ceil((-1+math.sqrt(1+8*X))/2)
    return n
print(findN(30))