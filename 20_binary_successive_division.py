# successive division method

decimal = 13 
binary = ""

while decimal > 0:
    """ Numeric conversion from decimal to binary.
    
    Args:
        decimal [int]: decimal integer number. != 0
        
    Returns: 
        binary [str]: string that represents the binary conversion.    
        
    Example:
    
        13 % 2 = 1 [6.5] : {6}
         6 % 2 = 0   [3] : {3}
         3 % 2 = 1 [1.5] : {1}
         1 % 2 = 1 [0.5] : {0}
         0 _____/ # 1101
         
    """
    residuo = decimal % 2
    binary = str(residuo) + binary
    decimal = decimal // 2
    
    print(f"The binary number {decimal} % 2 is: {binary}")
    
print(binary)


# Successive division method with input from the console.

decimal = int(input("\nSelect a integer number: "))
binary = ""

while decimal > 0:
    
    residuo = decimal % 2
    print(f"The binary number {decimal} % 2 is: {binary}")
    decimal = decimal // 2
    
    binary = str(residuo) + binary
    
    
    
print(f"The binary number is: {binary}")


# Suceessive division method with bin() function

decimal = int(input("\nSelect a second integer number: "))
binary = bin(decimal)

print(f"The binary notation number is: {binary}")
print(f"The binary number is: {binary[2:]}")
