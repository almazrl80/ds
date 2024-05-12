import numpy as np
def get_chess(a):
    arr=np.zeros((a,a),dtype=np.float16)
    for i in range(0,a):
        if i%2==0:
            for j in range(1,a,2):
                arr[i][j]=1
        else:
            for j in range(0,a,2):
                arr[i][j]=1
    return arr
print(get_chess(1))