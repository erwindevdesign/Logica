def fibonacci(n):
    """ 
    -->
    <--    
    """

    if n == 0 or n == 1:
        return 1
    print(n)
    return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input('Select a integer: '))
print(f'The fibonacci number for {n} is {fibonacci(n)}')

""" 


 """