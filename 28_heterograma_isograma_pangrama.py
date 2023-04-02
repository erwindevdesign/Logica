
import re
from unidecode import unidecode

def __char_counter(text: str) -> dict[str, int]:
    
    """ Counts the frequency of each character in the input text string.
    
    Args: 
        - text (str): The input text to count the characters.
        
    Returns:
        - char_counter (dict): A dictionary containing each character in 
        the input text as a key and its frequency as value.
    
    """
    # Removes all numbers and spaces from the input text and converts it to lowercase.
    no_number_text = re.sub(r"\d+", "", text.lower().replace(" ", "") )
    # Removes all puntuation from the input text.
    no_punt_text = re.sub(r"[^\w\s]", "", no_number_text)
    
    # Converts all Unicode characters to their closest ASCII representation and replaces `ñ` by `.`
    unicode = unidecode(no_punt_text.replace("ñ", ".")).replace(".", "ñ")
    
    # Initializes the char_counter dictionary
    char_counter = dict()
    
    # counts the frrequency of each character in the input text.
    for char in unicode:
        if char in char_counter.keys():
            char_counter[char] += 1
        else:
            char_counter[char] = 1

    return char_counter

def isHeterogram(text: str) -> bool:
    """ Determines whether the input text is a heterogram or not.
    
    Args: 
        - text (str): The input text to check.
        
    Returns: 
        - bool: True if the input text is a heterogram. Flase otherwise.
    
    """
    
    # Chacks if each character in the input appears only once.
    for counter in __char_counter(text). values():
        if counter > 1:
            return False
    return True


def isIsogram(text: str) -> bool:
    
    """ Determines whether the input text is an isogram or not.
    
    Args: 
        - text (str): The input text to chack.
        
    Returns:
    - bool: True if the input text is an isogram. False otherwise.
    
    """
    order = 0
    
    # chack if all characters in the input text appear with the same frequency.
    for counter in __char_counter(text).values():
        if order is 0:
            order = counter
        if order is not counter:
            return False
    return True

def isPangram(text: str) -> bool:
    """ Determines whether the input ext is a pangram or not.
    
    Args:
        - text (str): The inpur text to chack.
    
    Returns:
        - bool: True if the input text is a pangram. False otherwise.
    
    """
    
    # chack if the input text contains all letters of the alphabet.
    return len(__char_counter(text).keys()) is 27


print(isHeterogram("hiperblanduzcos"))
print(isHeterogram("hiperblanduzcós    !!w"))
print(isIsogram("anna"))
print(isPangram("Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú"))

""" Términos relacionados:
Un heterograma (del griego héteros, 'diferente' y gramma, 
'letra') es una palabra o frase que no contiene ninguna 
letra repetida.
Un isograma (del griego isos, 'igual' y gramma, 'letra') 
es una palabra o frase en la que cada letra aparece el 
mismo número de veces. Si cada letra aparece solo una 
vez será un heterograma, si aparece dos, un isogroma de 
segundo orden y así sucesivamente.
Un pangrama (del griego pan, 'todo' y gramma, 'letra') 
es una frase en la que aparecen todas las letras del 
abecedario. Si cada letra aparece sólo una vez, formando 
por tanto un heterograma, se le llama pangrama perfecto. 
"""