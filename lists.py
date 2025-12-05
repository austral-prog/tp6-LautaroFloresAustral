def remove_elements(list_to_remove_elements):
    lista = list_to_remove_elements[:]
    if len(lista) > 5:
        del lista[5]
    if len(lista) > 4:
        del lista[4]
    if len(lista) > 0:
        del lista[0]
    return lista


def add_elements(list_to_add_elements):
    lista = list_to_add_elements[:]
    lista.append('Yellow')
    lista.insert(0, 'Pink')
    return lista


def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    else:
        return False


def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        if list_to_compare1[2] == list_to_compare2[2]:
            return True
    return False

def list_of_lists(list_of_lists_to_modify):
    lista = list_of_lists_to_modify[:]
    lista[0] = lista[0][:2]
    lista[1] = lista[1][1:4]
    lista[2] = lista[2][-2:]

    return lista 
