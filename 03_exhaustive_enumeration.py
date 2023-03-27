object = int(input('Select a integer number: '))
result = 0

while result**2 < object:
    # print statement
    result += 1

if result ** 2 == object:
    print(f'The square root of {object} is {result}')
else: 
    print(f'{object} does not is square root')

