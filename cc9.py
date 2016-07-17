def factorial(x):
    result = 0
    if x == 0 or x == 1:
        return 1
    else:
        for i in range(0, x+1):
            result = x * factorial(x - 1)
        return result
    
print factorial(3)