from pyparsing import *
import pygame

#prueba de pull
WHITE = (255, 255, 255)

class Compilador:

    def __init__(self):
        self.id = 0
        self.sentence = ""

    def algo(self):
        print('Algo() -> Aqui hace algo\n')
        #Aburrido()

    def Print_txt(self,screen):
        txt = pygame.font.SysFont('Minecraft', 15).render(str(self.sentence), True, WHITE)
        #txt = pygame.transform.scale(txt, (200, 100))
        rect = txt.get_rect()
        rect.move_ip(500,360)
        screen.blit(txt,rect)


    def instruccion(self,opc):

        print('------------------------- Nivel 1 -------------------------')
        #id = divertido

        instr = Word(alphas) + "=" + Word(nums)
        comp = f"id={opc}"
        
        try:
            self.id = int(instr.parseString(comp)[2])
            print(f"id = {self.id}\n")
            return True
            
        except ParseException as err:
            print(f"id={opc}\n")
            print(" " * (err.column - 1) + "^")
            print('Error en la asignación de valores.\n')
            print('Se esperaba un número, se encontro un caracter (linea:1, columna:',err.column,')')
            self.sentence = 'Se esperaba un numero, se encontro un caracter (linea:1, columna:',err.column,')'
            return False
            
    def instruccion2(self,opc,opc2):

        print('------------------------- Nivel 2 -------------------------')

        instr = Word(alphas) + "=" + Word(alphas) + '+' + Word(nums)
        comp = f"id={opc}+{opc2}"
        
        try:

            if opc != 'id':
                raise ParseException('error variable')

            self.id = self.id + int(instr.parseString(comp)[4])
            print(f"id = {opc} + {opc2}")
            print(f"Ahora:\nid = {self.id}")
            return True
        except ParseException as err:
            if opc == 'Cinco':
                self.sentence = "Esta variable 'cinco' no esta declarada"
                return False
            else:
                print(f"id = {opc} + {opc2}")
                print(" " * (err.column - 1) + "^")
                print('Error en la asignación de valores.\n')
                if err.column == 4:
                    print('Se esperaba una variable y se recibio un numero. (linea:1, columna:',err.column,')')
                    self.sentence = 'Se esperaba una variable y se recibio un numero. (linea:1, columna:',err.column,')'
                    return False
                else:
                    print('Se esperaba un numero y se recibio una variable. (linea:1, columna:',err.column,')')
                    self.sentence = 'Se esperaba un numero y se recibio una variable. (linea:1, columna:',err.column,')'
                    return False

    def condicional(self,opc,opc2):
        print('------------------------- Nivel 3 -------------------------')

        instr = Word(alphas) + ":" + Word(alphas) + '=' + Word(nums) + Word(alphas) + ':' + Word(alphas) + '()' 
        comp = f"{opc}: id={self.id} Entonces: {opc2}()"

        try:
            print(f"{opc}: id={self.id} Entonces: {opc2}()")
            if self.id == 20:
                self.algo()
            return True
        except ParseException as err:
            print(f"{opc}: id={self.id} Entonces: {opc2}()")
            print(" " * (err.column - 1) + "^")
            print('Error en la asignación de valores.\n')
            if err.column == 1:
                print('Se esperaba una palabra reservada y se recibio otra opción. (linea:1, columna:',err.column,')')
                self.sentence ='Se esperaba una palabra reservada y se recibio otra opción. (linea:1, columna:',err.column,')'
                return False
            else:
                print('Se esperaba una funcion y se recibio otra opción. (linea:1, columna:',err.column,')')
                self.sentence = 'Se esperaba una funcion y se recibio otra opción. (linea:1, columna:',err.column,')'
                return False

    def ciclo(self, opc, opc2):
        print('------------------------- Nivel 4 -------------------------')

        instr = Word(alphas) + ":" + Word(alphas) + '=' + Word(nums) + Word(alphas) + ':' + Word(alphas) + '()' 
        comp = f"{opc}: id={self.id} Entonces: {opc2}()"
        
        try:
            print(f"{opc}: id={self.id} Entonces: {opc2}()")
            if self.id == 20:
                self.algo()
            return True
        except ParseException as err:
            print(f"{opc}: id={self.id} Entonces: {opc2}()")
            print(" " * (err.column - 1) + "^")
            print('Error en la asignación de valores.\n')
            if err.column == 1:
                print('Se esperaba una palabra reservada y se recibio otra opción. (linea:1, columna:',err.column,')')
                self.sentence = 'Se esperaba una palabra reservada y se recibio otra opción. (linea:1, columna:',err.column,')'
                return False
            else:
                print('Se esperaba una funcion y se recibio otra opción. (linea:1, columna:',err.column,')')
                return False

    def ciclo_y_condicional(self, opc, opc2):
        print('------------------------- Nivel 5 -------------------------')
        #mientras: aburrido() Entonces: divertido = divertido + 10 Si: divertido = 100 Entonces: regresar()  

        instr = Word(alphas) + ":" + Word(alphas) + '()' + Word(alphas) + ':' + Word(alphas) + '=' + Word(alphas) + "+" + Word(nums) + Word(alphas) + ":" + Word(alphas) + '=' + Word(nums) + Word(alphas) + ':' + Word(alphas) + '()'
        comp = f"{opc}: Aburrido() Entonces: divertido = {opc2} + 10 Si: divertido = 100 Entonces: Algo()"
        
        try:
            print(f"{opc}: Aburrido() Entonces: divertido = {opc2} + 10 Si: divertido = 100 Entonces: Algo()")
        except ParseException as err:
            print(f"{opc}: Aburrido() Entonces: divertido = {opc2} + 10 Si: divertido = 100 Entonces: Algo()")
            print(" " * (err.column - 1) + "^")
            print('Error en la declaracion de ciclo.\n')
            if err.column == 1:
                print('Se esperaba una palabra reservada y se recibio otra opción. (linea:1, columna:',err.column,')')
            else:
                print('Se esperaba una variable y se recibio otra opción. (linea:1, columna:',err.column,')')

