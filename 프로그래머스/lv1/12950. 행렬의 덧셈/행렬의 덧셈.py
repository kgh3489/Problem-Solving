import numpy as np

def solution(arr1, arr2):
    #행렬 덧셈을 위해 array로 변환
    a = np.array(arr1) 
    b = np.array(arr2)
    return (a + b).tolist() #다시 list로 변환
