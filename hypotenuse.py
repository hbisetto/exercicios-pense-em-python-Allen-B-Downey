import math

def hipotenuse(c1, c2):
    qc1 = c1**2
    qc2 = c2**2
    soma = qc1 + qc2
    result = math.sqrt(soma)
    return result
    
result = hipotenuse(3, 4)
print(result)