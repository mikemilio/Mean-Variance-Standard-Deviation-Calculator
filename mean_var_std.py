import numpy as np

def calculate(list):
    if (len(list) != 9):
        raise ValueError("List must contain nine numbers.")
    numpyArray = np.array(list).reshape(3,3)
    meanList = [
        numpyArray.mean(axis=0).tolist(), 
        numpyArray.mean(axis=1).tolist(), 
        numpyArray.mean()
    ]
    varList = [
        numpyArray.var(axis=0).tolist(),
        numpyArray.var(axis=1).tolist(),
        numpyArray.var(),
    ]
    stdList = [
        numpyArray.std(axis=0).tolist(),
        numpyArray.std(axis=1).tolist(),
        numpyArray.std(),
    ]
    maxList = [
        numpyArray.max(axis=0).tolist(),
        numpyArray.max(axis=1).tolist(),
        numpyArray.max(),
    ]
    minList = [
        numpyArray.min(axis=0).tolist(),
        numpyArray.min(axis=1).tolist(),
        numpyArray.min(),
    ]
    sumList = [
        numpyArray.sum(axis=0).tolist(),
        numpyArray.sum(axis=1).tolist(),
        numpyArray.sum(),
    ]
    calculations = {
        'mean': meanList,
        'variance': varList,
        'standard deviation': stdList,
        'max': maxList,
        'min': minList,
        'sum': sumList
    }
    return calculations

# myList = [0,1,2,3,4,5,6,7,8]
# print(calculate(myList)['variance'])