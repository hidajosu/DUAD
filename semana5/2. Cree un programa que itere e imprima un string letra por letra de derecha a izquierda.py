""" 2. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
    1. Pista: investigue de que otras maneras se puede usar el `range`.
    2. Ejemplos:
    3. `my_string = ‘Pizza con piña’` → 
    a
    ñ
    i
    p
    
    n
    o
    c
    
    a
    z
    z
    i
    p """

example="Josue Solano Hidalgo"
backwardsexample="".join(reversed(example))
print(example)
print(backwardsexample)

for stringdownwards in backwardsexample:
    print(stringdownwards)
