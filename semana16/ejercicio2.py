from semana6.3_Cree_una_funcion_que_retorne_la_suma_de_todos_los_numeros_de_una_lista import sum

def test_sum_basic():
    assert sum([1, 2, 3, 4]) == 10

def test_sum_mixed():
    assert sum([4, 6, 2, 29]) == 41

def test_sum_negative():
    assert sum([-1, 1, 2, 3]) == 5


from semana6.4_Cree_una_funcion_que_le_de_la_vuelta_a_un_string_y_lo_retorne_cree_una_funcin_que_le_de_la_vuelta_a_un_string_y_lo_retorne import backwards_phrase

def test_reverse_basic():
    assert backwards_phrase("Hola mundo") == "odnum aloH"

def test_reverse_empty():
    assert backwards_phrase("") == ""

def test_reverse_numbers():
    assert backwards_phrase("12345") == "54321"
    

from semana6.5_Cree_una_funcion_que_imprima_el_numero_de_mayusculas_y_el_numero_de_minusculas_en_un_string import count_upper_lower

def test_basic_phrase():
    assert count_upper_lower("I love Nación Sushi") == (3, 13)

def test_all_upper():
    assert count_upper_lower("ABCDEF") == (6, 0)

def test_all_lower():
    assert count_upper_lower("abcdef") == (0, 6)



from semana6.6_Ejercicio_de_funciones import sort_dash_string

def test_basic():
    assert sort_dash_string("python-variable-funcion-computadora-monitor") == "computadora-funcion-monitor-python-variable"

def test_single_word():
    assert sort_dash_string("solitario") == "solitario"

def test_mixed_case():
    assert sort_dash_string("Zebra-apple-Banana") == "Banana-Zebra-apple"



from semana6.6_Ejercicio_de_funciones import sort_dash_string

def test_basic():
    assert sort_dash_string("python-variable-funcion-computadora-monitor") == "computadora-funcion-monitor-python-variable"

def test_single_word():
    assert sort_dash_string("solitario") == "solitario"

def test_mixed_case():
    assert sort_dash_string("Zebra-apple-Banana") == "Banana-Zebra-apple"