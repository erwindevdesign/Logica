# :robot: Lógica computacional.

Este repositorio contiene ejercicios y prácticas de código en lenguaje de programación **Python** para la compresión de la lógica computacional y la mejora de habilidades de programación como los descritos a continuación.

> Cada archivo representa un ejemplo de código a implementar, describiendo su uso dentro del docstring.

1. [Estructuras de datos]()
2. [Comprehension]()
3. [Lambda]()
4. [Hoigher Order Function `HOF`]()
5. [map]()
6. [Inmutable]()
7. [map dict]()
8. [Filter structure]()
9. [Reduce]()
10. [Iterable]()
11. [Errors]()
12. [Exceptions]()
13. [Bugger]()
14. [Testing]()
15. [Algoritmos]()
16. [Patrones]()

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


## 📋 Indice

01_branched_programs.py

02_loops.py

03_exhaustive_enumeration.py

04_approximation_solutions.py

05_binary_search.py

06_abstraction_decomposition.py

07_documentation.py

08_recursive_factorial.py

09_fibonacci.py

10_recursive_sum.py

11_recursive_list.py

12_object_function.py

13_black_box.py

14_glass_box.py

15_exceptions.py

16_assert.py

17_lineal_complexity.py

18_logarithmic_complexity.py

19_quadratic_complexity.py

20_binary_successive_division.py

21_braille_dict.py

22_decimal.py

23_two_sum.py

24_add_two_numbers.py

25_palindrome_number.py

26_fizzbuzz.py

27_hacker_language.py

28_heterograma_isograma_pangrama.py