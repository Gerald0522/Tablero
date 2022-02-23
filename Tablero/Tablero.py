from Ficha import *

class Tablero:

    #Defina aquí los atributos de Tablero
    NumJugadores = 2
    orden = 0
    NumCasillas = 20

    #también va a necesitar una lista de Fichas (puede asumir un número de Fichas fijo si le parece más fácil), 
    #y un mecanismo para saber quién sigue en el turno
    
    ficha1 = Ficha("Azul")
    ficha2 = Ficha("Verde")



    #agregue parámetros necesarios después de self
    #para iniciar los valores de sus atributos
    def __init__(self):
        #inicialice aquí todos los atributos
        self.NumJugadores = 2
        self.NumCasillas = 20
        #no olvide usar self.atributo para acceder el atributo de la clase


    #defina aquí los métodos de Tablero
    #recuerde que el primer parámetro de cada método es siempre self

    def jugar (self):
        flag = True
        while flag:
            if flag:
                print(self.ficha1)

    def ganador (self):
        if self.ficha1 > self.NumCasillas:
            print ("Jugador 1 ha ganado")
        if self.ficha2 > self.NumCasillas:
            print ("jugador 2 ha ganado")

                
            

