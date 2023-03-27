def recursive_sum(num):
    """ Suma el consecutivo en una recursión de "num"

    --> 'num' (int) > 0
    <-- return 'n' + 'n' - 1 ...

    |
    V   
    5 + 10
    4 + 6
    3 + 3
    2 + 1
    1__/

    """
    # base-case: limited a interaction by complying with is declared.
    if num == 1:
        return 1
    # inductive-case: interactive sequence manager
    else:
        return num + recursive_sum(num - 1)

# print(return by function - with - (input by param))
print(recursive_sum(5))  
