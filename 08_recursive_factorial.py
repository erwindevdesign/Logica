def factorial(n):

    """ Calculate the factorial of 'n'.

    --> 'n' int >= 1
    <-- returns 'n!'
    
    |
    V   
    5! = 5 * (4!)
    4! = 4 * (3!) 
    3! = 3 * (2!)
    2! = 2 * (1!)
    1! = 1 ___/

    """
    #print(n) # printstatement

    # base-case: limited a interaction by complying with is declared.
    if n == 1:  
        return 1
    # inductive-case: interactive sequence manager
    return n * factorial(n - 1)
 
n = int(input('Select a integer to init: ')) # input by user
print(f'return: {factorial(n)}' )  # return by function


