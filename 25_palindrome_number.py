def is_palindrome(x: int):
    """ Determines whether an integer is a palindrome or not.
    
    A palindrome is a number that remains the same when its digit are reversed.
    
    Args:
        - x (int): The Integer to chsck for palindomicity.
        
    Returns:
        - True | False (bool): Tru if `x` is a palindrome, False otherwise.
        
    Example:

        121121 is a palindrome, while 123123 is not.
        
        print(is_palindrome(x=12100121))
        
        ❯ python3 25_palindrome_number.py
        
        the reverse value is 1
        the x value is: 1210012
        the reverse value is 12
        the x value is: 121001
        the reverse value is 121
        the x value is: 12100
        the reverse value is 1210
        the x value is: 1210
        
        True
    """
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    # print(x)
    
    reverse = 0
    
    while x > reverse:
        reverse = reverse * 10 + x % 10
        x //= 10
        #print(f"the reverse value is {reverse}")
        #print(f"the x value is: {x}")
    return x == reverse or x == reverse // 10

#print(is_palindrome(x=12100121))
print(is_palindrome(int(input("Enter the possible palindrome number for console: "))))

#lot = is_palindrome(123689986321)
#print(lot)