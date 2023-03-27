object = int(input('Select a number: '))
epsilon = 0.01
low = 0.0
upper = max(1.0, object)
result = (upper + low) / 2

while abs(result**2 - object) >= epsilon:
    print(f'low={low}, upper={upper}, result={result}')
    if result**2 < object:
        low = result
    else:
        upper = result

    result = (upper + low) / 2

print(f'The square root the {object} is {result}')