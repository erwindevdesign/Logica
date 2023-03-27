binary = input("Select a binary number: ")
decimal = 0

for digit in binary:
    """ Numeric conversion from binary to decimal
    
    Args:
        binary [iterable]: iterable binary number.
        
    Returns:
        decimal [int]: decimal integer number.
        
    Example:
        
        # 1101
        
         1 x 2 + 1 is:  1
         3 x 2 + 1 is:  3
         6 x 2 + 0 is:  6
        13 x 2 + 1 is: 13 <--
    
    """
    decimal = decimal*2 + int(digit)
    
    # printstatement
    print(f"--> {decimal} x 2 + {digit} is: {decimal}")

print(f"The decimal number is: {decimal}")

