# Lineal Complexity  

def lineal_complexity(list):

    sum = 0 # "O"(1)---------v
    multiplication = 1 # "O"(1)

    for number in range(len(list)): # "O"(n)
        sum += number
    
    for number in range(len(list)): # "O"(n)
        multiplication += number

    return sum, multiplication

print(int(lineal_complexity))

# sum "O"(2n)
# --> "O"(n) dekect 2 in the equation


def lineal_complexity_two(list):
    estimate = 0

    for i in range(len(list)): # --------|
        for j in range(1,5): # O"(5)     |
            estimate += (i*j) #          | ---> "O"(n)  == "O"(5n) == "O"(n)
                            #            |
                            # -----------|
    return estimate

print(lineal_complexity_two)
print(type(lineal_complexity_two))