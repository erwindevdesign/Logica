# :robot: Lógica computacional.

Este repositorio contiene ejercicios y prácticas en código de lenguaje de programación **Python** para la compresión de la lógica computacional y la mejora de habilidades de programación como los descritos a continuación.

:eyes:

<details style="font-weight: bold; color:#19609E"><summary>Descripción de contenido </summary>
<p>

1. [Estructuras de datos](#id1)
    1. Lista de enteros 
    2. Lista de cadena de texto
    3. Tupla de enteros
    4. Tupla de cadena de texto
    5. Conjunto de enteros
    6. Conjunto de cadena de texto
    7. Diccionarios
2. [Comprehension](#id2)
3. [Lambda](#id3)
4. [Hoigher Order Function `HOF`](#id4)
5. [map](#id5)
6. [Inmutable](#id6)
7. [map dict](#id7)
8. [Filter structure](#id8)
9. [Reduce](#id9)
10. [Iterable](#id10)
11. [Errors](#id11)
12. [Exceptions](#id12)
13. [Bugger](#id13)
14. [Testing](#id14)
15. [Algoritmos](#id15)
16. [Patrones](#id16)
</p>
</details>

> Dentro de la **Descripción de contenido** se encontrarán conseptos bases para la compresión de los ejemplos en código a implementar.

📋

<details  style="font-weight: bold; color:#19609E"><summary>Indice de ejemplos en código</summary>
<p>

[01_branched_programs.py](/01_branched_programs.py "Mensaje emergente de ejemplo")

[02_loops.py](/02_loops.py "Mensaje emergente de ejemplo")

[03_exhaustive_enumeration.py](/03_exhaustive_enumeration.py "Mensaje emergente de ejemplo")

[04_approximation_solutions.py](/04_approximation_solutions.py "Mensaje emergente de ejemplo")

[05_binary_search.py](/05_binary_search.py "Mensaje emergente de ejemplo")

[06_abstraction_decomposition.py](/06_abstraction_decomposition.py "Mensaje emergente de ejemplo")

[07_documentation.py](/07_documentation.py "Mensaje emergente de ejemplo")

[08_recursive_factorial.py](/08_recursive_factorial.py) 
```
Calculate the factorial of 'n'.

    Args:

        'n' [int] >= 1
        
    Returns:

        'n!'
    
    |
    V   
    5! = 5 * (4!)
    4! = 4 * (3!) 
    3! = 3 * (2!)
    2! = 2 * (1!)
    1! = 1 ___/
```

[09_fibonacci.py](/09_fibonacci.py "Mensaje emergente de ejemplo")

[10_recursive_sum.py](/10_recursive_sum.py)

```
Suma el consecutivo en la recursión de "num"

    Args:
    
        'num' (int) > 0
    
    Returns:
        
        return 'n' + 'n' - 1 ...

    |
    V   
    5 + 10
    4 + 6
    3 + 3
    2 + 1
    1__/

```

[11_recursive_list.py](/11_recursive_list.py )

```
Recursitive created for a list reader
    
    Args:
        
        data [list] != 0
        index [int] == 0
    
    Returns:
    
        int > 0 to 'index'
```

[12_object_function.py](/12_object_function.py "Mensaje emergente de ejemplo")

[13_black_box.py](/13_black_box.py "Mensaje emergente de ejemplo")

[14_glass_box.py](/14_glass_box.py "Mensaje emergente de ejemplo")

[15_exceptions.py](/15_exceptions.py "Mensaje emergente de ejemplo")

[16_assert.py](/16_assert.py "Mensaje emergente de ejemplo")

[17_lineal_complexity.py](/17_lineal_complexity.py "Mensaje emergente de ejemplo")

[18_logarithmic_complexity.py](/18_logarithmic_complexity.py "Mensaje emergente de ejemplo")

[19_quadratic_complexity.py](/19_quadratic_complexity.py "Mensaje emergente de ejemplo")

[20_binary_successive_division.py](/20_binary_successive_division.py )

```
Numeric conversion from decimal to binary.
    
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
```

[21_braille_dict.py](/21_braille_dict.py )

[22_decimal.py](/22_decimal.py )

```
Numeric conversion from binary to decimal
    
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
```

[23_two_sum.py](/23_two_sum.py )

```
Return an array with the indices of two
numbers in the list `nums` that add up to 
the `target`. If there are no two numbers
that meet the condition, it returns `None`.
    
    Args:
        
        - nums [ list ] : list of integers in which 
        to search for the two numbers.
        
        - target [ int ] : integer that represents 
        the sum goal.
    
    Returns:
    
        - result [ array | None ] : a list with two integers 
        representing the indices of the two numbers
        that add up to `target`, or `None` if they
        are not found.
```

[24_add_two_numbers.py](/24_add_two_numbers.py )

[25_palindrome_number.py](/25_palindrome_number.py )

```
Determines whether an integer is a palindrome or not.
    
    A palindrome is a number that remains the same when its digit are reversed.
    
    Args:
        x (int): The Integer to chsck for palindomicity.
        
    Returns:
        True | False (bool): Tru if `x` is a palindrome, False otherwise.
```

[26_fizzbuzz.py](/26_fizzbuzz.py )

```
This function prints the numbers from 1 to 100, 
replacing multiples of 3 with the word "fizz",
multiples of 5 with the word "buzz, and multiples
of both 3 and 5 with the word "fizzbuzz".
```

[27_hacker_language.py](/27_hacker_language.py )

```
Translates a given string of text to "leet" language 
    (or "1337" language). a form of online slang that 
    replaces standard letters with numbers, symbols, or 
    other characters that resemble the letters in spelling.
    
    Parameters: 
        text (str): A string of text to be translated.
        
    Returns: 
        leet_text (str): A translated string of text in "leet" language.
```

[28_heterograma_isograma_pangrama.py](/28_heterograma_isograma_pangrama.py )

```
Counts the frequency of each character in the input text string.
    
    Args: 
        text (str): The input text to count the characters.
        
    Returns:
        char_counter (dict): A dictionary containing each character in 
        the input text as a key and its frequency as value.
```

[29_url_params.py](/29_url_params.py )

```
This code extracts the parameters from a URL using both 
split method and regular expression. The split methods separates
the URL into components separated by `&`, and then it looks for 
components containing a parameter using the `=` character. If
a parameter is found, it is extrated and printed. The regular 
expression method uses the `re.findall()` funtion to search 
parameter values using a regular expression pattern. The 
pattern matches strings that start with `=` and contain one or 
more alphanumeric characters, dots, underscores, percentage 
signs, or hyphens.

Returns: 
    - None
```

[30_friday_13.py](/30_friday_13.py )

```
Determines if given year and month contain a Friday the 13th.
    
    Args:
        - year (int): The year to check.
        - month (int): The month to check.
        
    Returns:
        - bool: True if the given year and month contain a Friday the 13th. False otherwise.
```

[31_roman_to_int.py](/31_roman_to_int.py )

```
Converts a given Roman numeral string to an integer.
    
    Args:
        s (str): The Roman numeral string to be converted.
    
    Returns:
        int: The integer value corresponding to the given ROman numeral string.
```

[32_int_to_roman.py](/32_int_to_roman.py )

```
 Convert an integer to a Roman numeral string.
    
    Args: 
        num (int): The integer to convert.
    
    Returns:
        str: The Roman numeral string representing the given integer.
```

[33_longest_common_prefix.py](/33_longest_common_prefix.py)

```
This function finds the longest common prefix string amongts a list of strign.
    
    Args:
        - list [str]: A list of strings to search for the longest commond prefix.
        
    Returns:
        - str: The longest commond prefix string among the input strings.
```

</p>
</details>


> Cada archivo descrito en el **Indice de ejemplos en código** representa un fragmento de código a implementar, describiendo su  estructura dentro de su propio  **docstring**.

## Estructura de datos <a name='id1'></a>

Python hace uso de varias estructuras de datos integradas en el lenguaje, entre ellas se encuentran:


1. **Listas**

Son una colección ordenada y modificable de elementos que pueden ser de diferentes tipos de datos. Se definen usando corchetes `[ ]` y los elementos están separados por comas `,`.

Ejemplo:

#### Lista de enteros
```
my_list = [1, 2, 3, 4, 5]
```
#### Lista de strings
```
fruits = ["apple", "banana", "cherry", "orange"]
```
2. **Tuplas**

Son una colección ordenada e inmutable de elementos que pueden ser de diferentes tipos de datos. Se definen usando paréntesis `( )` y los elementos están separados por comas `,`.

#### Tupla de enteros
```
my_tuple = (1, 2, 3, 4, 5)
```
#### Tupla de strings
```
fruits = ("apple", "banana", "cherry", "orange")
```
3. **Conjuntos (Sets)**

Son una colección desordenada y no indexada de elementos únicos. Se definen usando llaves {} o la función set().

#### Set de enteros
```
my_set = {1, 2, 3, 4, 5}
```
#### Set de strings
```
fruits = set(["apple", "banana", "cherry", "orange"])
```
  
4. **Diccionarios**

Son una colección desordenada y modificable de pares de clave-valor. Se definen usando llaves {} y los elementos están separados por comas, cada par de clave-valor está separado por dos puntos :.

#### Diccionario (clave - valor)
```
grades = {"Alice": 80, "Bob": 90, "Charlie": 70}
```
#### Diccionario (clave - valor)
```
user_info = {"name": "John", "age": 30, "city": "New York"}
```















## Bugger

#### Pasos: 
- usar print statement
- estudia los datos disponibles
- utiliza los datos disponibles
- utiliza los datos para crear hipótesis y experimentos mediante un método científico.
- pregúntate por qué está computando de esta manera.
- debbuggear es una lean skill, una habilidad que se aprende.
- ser sistemático y registra y respalda todo cambio.

> encuentra los sospechosos comunes: pasar argumentos en orden distinto al espesificado en la funsión, se describio incorrectaente un nombre, no se inicializo una variable antes de ser llamada (none), se comparan flotantes con igualdad exacta en lugar de por una aproximación, value equality vs object equality, una función tiene efectos sevundarios en la estructura de código, errores tiícos de la capasidad habilitiva.

> Es posible que el bug no se encuentre donde crees que esta.

> comparte y solicita apoyo siempre a tu equipo.

> lleva un registro de lo que has tratado, preferente en la forma de test.

## Testing 

Black boox

- se basan en las especificaciones de la función o el programa.
- prueba de inputs y validación de outputs
- Unit testing(un lead) o integration testing(circuito completo de leads)

Glass box

- se basan en el flujo del programa

- prueba todos los caminos posibles de una función. Ramificaciones, bucles for & while, recursión.

- Regression testing o mocks 

> TIPS: si hay que probar todas las condiciones: if, elif, else. Si tenemos un loop requerimos hace un testing sin entrar al loop, en donde entremos en una iteración y en donde entremos más de una vez al loop. Si lo que tenemos es un while loop hacemos un testing donde la condición sea falsa y una donde veamos los brakestaements y como se comportan, y por ultimos revisar todas las exepciones y donde pueden haber errores.

Lista de los **7 principios de Testing** de acuerdo al libro de ISTQB.

1 Las pruebas muestran la presencia de defectos
Significa que las pruebas pueden demostrar que EXISTEN problemas, pero no que los problemas NO EXISTEN.
El objetivo principal de llevar a cabo una prueba es para detectar defectos. Trabajando bajo la premisa de que cada producto contiene defectos de algún tipo, una prueba que revela los errores es generalmente mejor que una que no lo hace. Todas las pruebas por lo tanto, deben ser diseñados para revelar tantos errores como sea posible

2 Las pruebas exhaustivas son imposibles
Las pruebas exhaustivas tratan de cubrir todas las combinaciones posibles de datos en el software, a fin de garantizar que ninguna situación puede surgir, una vez probado el software se ha liberado. Excepto en aplicaciones muy simples, el número de combinaciones posibles de datos es demasiado alta, es más eficaz y eficiente que los ingenieros de pruebas se centren en las funcionalidades de acuerdo a riesgos y prioridades.

3 Pruebas tempranas.
Un producto (incluyendo los documentos, tales como la especificación del producto) se puede probar tan pronto como se ha creado. ISTQB recomienda probar un producto tan pronto como sea posible, corregir los errores más rápidamente posible. Los estudios han demostrado que los errores identificados al final del proceso de desarrollo por lo general cuestan más para resolver.
Por ejemplo: un error encontrado en las especificaciones puede ser bastante sencillo de solucionar. Sin embargo, si ese error se transfiere a la codificación de software, una vez descubierto el error puede ser muy costoso y consume tiempo.

4 Agrupamiento de Defectos
Los estudios sugieren que los problemas en un elemento de software tienden a agruparse en torno a un conjunto limitado de módulos o áreas. Una vez que estas áreas han sido identificadas, los administradores eficientes de prueba son capaces de enfocar las pruebas en las zonas sensibles, mientras que siguen buscando a los errores en los módulos de software restantes. Me recuerda al 80/20.

5 La paradoja del “Pesticida”
Al igual que el sobre uso de un pesticida, un conjunto de pruebas que se utilizan repetidamente en el disminuirá en su eficacia. Usando una variedad de pruebas y técnicas expondrá una serie de defectos a través de las diferentes áreas del producto.

6 La prueba es dependiente del contexto
Las mismas pruebas no se deben aplicar en todos los ámbitos. Distintos productos de software tienen diferentes requisitos, funciones y propósitos. Una prueba diseñada para realizarse en un sitio web, por ejemplo, puede ser menos eficaz cuando se aplica a una aplicación de intranet. Una prueba diseñada para una forma de pago con tarjeta de crédito puede ser innecesariamente rigurosa si se realiza en un foro de discusión.
En general, cuanto mayor es la probabilidad y el impacto de los daños causados ​​por el software fallado, mayor es la inversión en la realización de pruebas de software.

7 La falacia de ausencia de errores
Declarar que una prueba no ha descubierto ningún error no es lo mismo que declarar que el software es “libre de errores”. Con el fin de garantizar que los procedimientos adecuados de software de prueba se lleva a cabo en todas las situaciones, los evaluadores deben asumir que todo el software contiene algunos (aunque disimulada) errores.



# Algoritmos: patrones de Arrays y Strings 

A continuación se describen las operaciones estándar de un array y sus correspondientes complejidades temporales.

    Acceso a un valor en un índice determinado: 0(1)
    Actualización de un valor en un índice dado: 0(1)
    Inserción de un valor
        O(n) cuando se trata de un array dinámico
        O(1) cuando se trata de una matriz estática
    Eliminación de un valor al principio: O(n)
    Eliminación de un valor en el medio: O(n)
    Eliminación de un valor al final: 0(1)
    Copiar el array: O(n)





<!-- 


❯ git pull origin main --rebase
Desde github.com:erwindevdesign/Logica
 * branch            main       -> FETCH_HEAD
Rebase aplicado satisfactoriamente y actualizado refs/heads/main.
❯ git push origin main
Enumerando objetos: 35, listo.
Contando objetos: 100% (35/35), listo.
Compresión delta usando hasta 8 hilos
Comprimiendo objetos: 100% (33/33), listo.
Escribiendo objetos: 100% (34/34), 14.98 KiB | 1.50 MiB/s, listo.
Total 34 (delta 0), reusados 0 (delta 0), pack-reusados 0
To github.com:erwindevdesign/Logica.git
   2a7d75f..04fd35f  main -> main

 -->