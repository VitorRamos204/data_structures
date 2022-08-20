def busca(lista, elemento):
    """
    Retorna o índice elemento se ele estiver na lista ou None, caso o contrário
    """
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return None


lista_randomizada = [2, "eu", 7, 'pytas', 2, "eu", 7, 'negocio', 89, "sdadq", 54, 'js', 234, "djsaio", 787, 'busca', 564]
elemento = 'busca'

indice = busca(lista_randomizada, elemento)
if indice is not None:
    print(f'O índice do elemento {elemento} é {indice}')
else:
    print(f'O elemento {elemento} não se encontra na lista')
