
from deque import Data_Intercection

def caso_1_media_esperada():
    deque = Data_Intercection()

    caso = [120, 130, 150, 140, 160, 170, 180, 200, 190, 210]
    resultado_esperado = [None, None, 133.3, 140.0, 150.0, 156.7, 170.0, 183.3, 190.0, 200.0]
    deque.set_janela(3)
    for valor in caso:
        deque.next(valor)

    return deque.show_media_movel() == resultado_esperado

def caso_2_media_esperada():
    deque = Data_Intercection()

    caso = [15, 18, 22, 28, 32, 35, 40, 38, 32, 28, 25, 20, 18, 15, 12]
    resultado_esperado = [None, None, None, None, None, None, 27.1, 30.4, 32.4, 33.3, 32.9, 31.1, 28.7, 25.1, 21.4]
    for valor in caso:
        deque.next(valor)
    print(deque.show_media_movel())
    return deque.show_media_movel() == resultado_esperado

def caso_3_lancar_exception():
    deque = Data_Intercection()

    try:
        deque.last()
        return False
    except Exception as e:
        return True
    
def caso_4_retornar_ultimo_valor():
    deque = Data_Intercection()

    try:
        deque.next(150)
        return deque.last() == 150
    except Exception as e:
        return False

print('Caso 1 funcionou? ', caso_1_media_esperada())
print('Caso 2 funcionou? ', caso_2_media_esperada())
print('Caso 3 funcionou? ', caso_3_lancar_exception())
print('Caso 4 funcionou? ', caso_4_retornar_ultimo_valor())