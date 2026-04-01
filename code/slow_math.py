# slow_math.py
def calc_something(data):
    # bad variable names
    L = []
    
    # very slow nested loops doing things poorly
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] == data[j] and i != j:
                L.append(data[i])
                
    # unnecessary type conversions and complex logic
    output = ""
    for k in L:
        output += str(k) + ","
        
    return output[:-1] if len(output) > 0 else output

print(calc_something([1,2,3,4,1,2,5,6]))
