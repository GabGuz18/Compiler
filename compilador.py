from pyparsing import *

#prueba de pull

class Compilador:

    def __init__(self):
        self.id = 0

    def algo(self):
        print('Algo() -> Aqui hace algo\n')

    def instruccion(self,opciones,opc):

        print('------------------------- Nivel 1 -------------------------')

        instr = Word(alphas) + "=" + Word(nums)
        comp = f"id={opciones[opc]}"
        
        try:
            self.id = int(instr.parseString(comp)[2])
            print(f"id = {self.id}\n")
            
        except ParseException as err:
            print(f"id={opciones[opc]}\n")
            print(" " * (err.column - 1) + "^")
            print('Error en la asignación de valores.\n')
            print('Se esperaba un número, se encontro un caracter (linea:1, columna:',err.column,')')

    def instruccion2(self,opciones2,opc,opc2):

        print('------------------------- Nivel 2 -------------------------')

        instr = Word(alphas) + "=" + Word(alphas) + '+' + Word(nums)
        comp = f"id={opciones2[opc]}+{opciones2[opc2]}"
        
        try:
            self.id = self.id + int(instr.parseString(comp)[4])
            print(f"id = {opciones2[opc]} + {opciones2[opc2]}")
            print(f"Ahora:\nid = {self.id}")
        except ParseException as err:
            print(f"id = {opciones2[opc]} + {opciones2[opc2]}")
            print(" " * (err.column - 1) + "^")
            print('Error en la asignación de valores.\n')
            if err.column == 4:
                print('Se esperaba una variable y se recibio un numero. (linea:1, columna:',err.column,')')
            else:
                print('Se esperaba un numero y se recibio una variable. (linea:1, columna:',err.column,')')

    def condicional(self,opciones3,opc,opc2):
        print('------------------------- Nivel 3 -------------------------')

        instr = Word(alphas) + ":" + Word(alphas) + '=' + Word(nums) + Word(alphas) + ':' + Word(alphas) + '()' 
        comp = f"{opciones3[opc]}: id={self.id} Entonces: {opciones3[opc2]}()"
        
        try:
            print(f"{opciones3[opc]}: id={self.id} Entonces: {opciones3[opc2]}()")
            if self.id == 20:
                self.algo()
        except ParseException as err:
            print(f"{opciones3[opc]}: id={self.id} Entonces: {opciones3[opc2]}()")
            print(" " * (err.column - 1) + "^")
            print('Error en la asignación de valores.\n')
            if err.column == 1:
                print('Se esperaba una palabra reservada y se recibio otra opción. (linea:1, columna:',err.column,')')
            else:
                print('Se esperaba una funcion y se recibio otra opción. (linea:1, columna:',err.column,')')

    def ciclo(self, opciones4, opc, opc2):
        print('------------------------- Nivel 4 -------------------------')

        instr = Word(alphas) + ":" + Word(alphas) + '=' + Word(nums) + Word(alphas) + ':' + Word(alphas) + '()' 
        comp = f"{opciones4[opc]}: id={self.id} Entonces: {opciones4[opc2]}()"
        
        try:
            print(f"{opciones4[opc]}: id={self.id} Entonces: {opciones4[opc2]}()")
            if self.id == 20:
                self.algo()
        except ParseException as err:
            print(f"{opciones4[opc]}: id={self.id} Entonces: {opciones4[opc2]}()")
            print(" " * (err.column - 1) + "^")
            print('Error en la asignación de valores.\n')
            if err.column == 1:
                print('Se esperaba una palabra reservada y se recibio otra opción. (linea:1, columna:',err.column,')')
            else:
                print('Se esperaba una funcion y se recibio otra opción. (linea:1, columna:',err.column,')')

    def ciclo_y_condicional(self, opciones5, opc, opc2):
        pass

opciones1 = {1:10,2:'id',3:'diez'}
opciones2 = {1:10,2:'id',3:'diez',5:'Si:'}
opciones3 = {1:'Si',2:'id',3:'diez',4:'x',5:10,6:'Algo'}
opciones4 = {1:'Si',2:'id',3:'Mientras',4:'x',5:10,6:'Algo',7:'diez'}

comp = Compilador()
comp.instruccion(opciones1,1)
comp.instruccion2(opciones2,2,1)
comp.condicional(opciones3,1,6)
comp.ciclo(opciones4,3,6)