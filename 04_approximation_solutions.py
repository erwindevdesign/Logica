object = int(input('Select a unmber: '))
epsilon = 0.0001
paso = epsilon**2
result = 0.0

while abs(result**2 - object) >= epsilon and result <= object:
    result += paso 

if abs(result**2 - object) >= epsilon:
    print(f'square root not found')
else:
    print(f'The square root {object} is {result} ')