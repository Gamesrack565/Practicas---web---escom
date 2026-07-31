import random

class Poblacion:
    #Debe recoivbir una lista con los valores, peso y valor
    def __init__(self, list_objetos, capacidad_maxima, num_inidividuos):
        self.num_individuos = num_inidividuos
        self.lista_objetos = list_objetos
        self.capacidad_maxima = capacidad_maxima
        self.sujetos = []

        cromosoma_listo = self.crear_individuo_inteligente(self.lista_objetos, self.capacidad_maxima)
        primer_sujeto = Sujeto(cromosoma_listo)
        self.sujetos.append(primer_sujeto)

        for i in range(self.num_individuos - 1):
            cromosoma = [random.radint(0,1) for _ in range(len(self.lista_objetos))]

            self.sujetos.append(Sujeto(cromosoma))

    #Se tiene una lista que almacena diccionarios 
    #Cada diccionario almacena el valor y peso del objeto
    def crear_individuo_inteligente(self, lista_objetos, capacidad_maxima):
        #Tenemos la variable peso_acumulado, para ir acumulando el peso y verificar que no se haya pasado del limite
        peso_acumulado = 0
        #Enumeramos la lista
        numeracion_lista = list(enumerate(lista_objetos))
        #La ordenamos con la funcion sorted
        #Accedemos a las variables del diccionario por medio de key = lambda
        lista_ordenada = sorted(numeracion_lista, key=lambda item: item[1]["valor"]/item[1]["peso"], reverse=True)
        #Creamos un cromosoma con todo en 0
        #Indicando que no tiene ningun objeto dentro
        cromosoma = [0] * len(lista_objetos)
        #Ciclo que recorre la lista ordenada
        for indice, movimiento in lista_ordenada:
            #Verificamos que no nos pasamos del peso
            #Si no, agregamos al cromosoma el indice del objeto
            if peso_acumulado + movimiento["peso"] <= capacidad_maxima:
                peso_acumulado += movimiento["peso"]
                cromosoma[indice] = 1

        return cromosoma

class Sujeto:
    def __init__(self, cromosoma):
        self.sujeto = cromosoma
        self. aptitud = 0
















