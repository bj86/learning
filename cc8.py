def digit_sum(n): # Converts input to string, iterates and returns sum as int. 
    mystring = str(n)
    total = int(0)
    for i in mystring:
        i = int(i)
        total += i
    return total

print digit_sum(1234) # example