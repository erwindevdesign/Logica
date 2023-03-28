import datetime

def friday_13(year: int, month: int) -> bool:
    """ Determines if given year and month contain a Friday the 13th.
    
    Args:
        - year (int): The year to check.
        - month (int): The month to check.
        
    Returns:
        - bool: True if the given year and month contain a Friday the 13th. False otherwise.
    """
    try:
        return datetime.date(year, month, 13).weekday()==4
    except:
        return False
    
print(friday_13(2023, 10))
print(friday_13(2022, 5))
print(friday_13(2023, 13))
print(friday_13(-2023, 1))
print(friday_13(2023, "1"))
print(friday_13(2023, 0))
print(friday_13("LOL", "2"))

