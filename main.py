import json
import copy

i0_json = open('estado_cero.json')
i0 = json.load(i0_json)

def lista_de_transiciones(estado_actual):
    transiciones = []
    for produccion in estado_actual:
        if len(list(produccion.values())[0]) > produccion["punto"]:
            transicion = list(produccion.values())[0][produccion["punto"]]
            if transicion not in transiciones:
                transiciones.append(transicion)
    return list(transiciones)


def transiciones_no_terminales(no_terminal, lista_producciones = []):
    for produccion in i0:
        if list(produccion.keys())[0] == no_terminal:
            if produccion not in lista_producciones:
                lista_producciones.append(produccion)
                if list(produccion.values())[0][0].isupper() and list(produccion.values())[0][0] != no_terminal:
                    transiciones_no_terminales(list(produccion.values())[0][0], lista_producciones)
    return lista_producciones

# print(transiciones_no_terminales('F'))
                



def crear_automata(estado_actual, estados):

    if estado_actual not in estados:
        estados.append(estado_actual)

    transiciones = lista_de_transiciones(estado_actual)

    for transicion in transiciones:
        nuevo_estado = []
        for produccion in estado_actual:

            if len(list(produccion.values())[0]) > produccion["punto"]:
                if list(produccion.values())[0][produccion["punto"]] == transicion:
                    produccion_a_anadir = copy.copy(produccion)
                    produccion_a_anadir['punto'] = produccion_a_anadir['punto']+1
                    nuevo_estado.append(produccion_a_anadir)

                    if len(list(produccion_a_anadir.values())[0]) > produccion_a_anadir["punto"]:

                        if list(produccion_a_anadir.values())[0][produccion_a_anadir["punto"]].isupper() and list(produccion_a_anadir.values())[0][produccion_a_anadir["punto"]] != transicion:
                            lista_derivados = transiciones_no_terminales(list(produccion_a_anadir.values())[0][produccion_a_anadir["punto"]], lista_producciones=[])
                            for produccion in lista_derivados:
                                if produccion not in nuevo_estado:
                                    nuevo_estado.append(produccion)
                


        if nuevo_estado in estados:
            return
        crear_automata(nuevo_estado, estados)


        return estados


if __name__ == '__main__':

    automata = crear_automata(i0, [])

    for estado in automata:
        for produccion in estado:
            print(f'{produccion}\n')
        print('\n')