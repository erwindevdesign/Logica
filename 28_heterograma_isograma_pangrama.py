import re
import unidecode

def __char_counter(text:str) -> dict(str, int):
    
    no_number_text = re.sub(r"\d+", "", unidecode(text.lower()) )
    no_punt_text = re.sub(r"[^\w\s]", "", no_number_text)
    
    print(no_number_text)
    
    char_counter = dict()
    
    for char in no_number_text:
        if char in char_counter.keys():
            char_counter[char] += 1
        else:
            char_counter[char] = 1

    return char_counter
def isHeterogram(text: str) -> bool:
    pass


def isIdogram(text: str) -> bool:
    pass

def isPanagram(text: str) -> bool:
    pass






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

