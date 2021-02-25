
def returnIndexF(index):
    fibbSeries = [0, 1]
    result = None
    for x in range(index + 1):
        if(x == 0):
            result = fibbSeries[x]
            continue
        elif(x == 1):
            result = fibbSeries[x]
            continue
        else:
            added = fibbSeries[x-2] + fibbSeries[x-1]
            fibbSeries.append(added)
    result = fibbSeries[index]
    return result

def calcFactorial(num):
    result = num
    
    for x in range(num):
        if x == 0:
            continue
        result = result * (num-x)
    return result