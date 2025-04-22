# 4. Cree una función que le de la vuelta a un string y lo retorne.
#     1. Esto ya lo hicimos en iterables.
#     2. “Hola mundo” → “odnum aloH”


def backwards_phrase():
    phrase="This is my phrase"
    phrase="".join(reversed(phrase))
    print(phrase)

backwards_phrase()