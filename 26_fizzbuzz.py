def fizzbuzzz():
    """ This function prints the numbers from 1 to 100, 
    replacing multiples of 3 with the word "fizz",
    multiples of 5 with the word "buzz, and multiples
    of both 3 and 5 with the word "fizzbuzz".
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(number)
            
fizzbuzzz()