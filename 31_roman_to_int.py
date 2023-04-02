def romanToInt(s:str) -> int:
    
    """ Converts a given Roman numeral string to an integer.
    
    Args:
        s (str): The Roman numeral string to be converted.
    
    Returns:
        int: The integer value corresponding to the given ROman numeral string.
        
    Example: 
    
        >>> romanToInt("IV")
        4
        
        >>> romanToInt("DIV")
        504
        
        >>> romanToInt("MM")
        2000
    
    """
    roman_to_int= {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    result = 0
    prev_value = 0
    
    for c in s:
        value = roman_to_int[c]
        if value > prev_value:
            result += value - 2 * prev_value
        else:
            result += value
        prev_value = value
    return result

print(romanToInt("IV"))
print(romanToInt("DIV"))
print(romanToInt("MM"))