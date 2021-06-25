class calculadora: 
    _counter = 0

    def __init__(self, num_1, num_2):

        try:
            num_1 = float(num_1)
            num_2 = float(num_2)
        except:
            raise ValueError('Valores introducidos no son numeros')

        calculadora._counter += 1
        self.id = calculadora._counter  
        self.num_1 = num_1
        self.num_2 = num_2

        if self.id == 1:
            print("Inicializando clase Calculadora por primera vez")
            print("Actividad 4. Programacion Avanzada en Python")
            print("Alumno: Jose Sepulveda \n")

    def sumar(self, num_1=None, num_2=None):
        if num_1 == None:
            num_1 = self.num_1

        if num_2 == None:
            num_2 = self.num_2

        return num_1 + num_2

    def restar(self, num_1=None, num_2=None):
        if num_1 == None:
            num_1 = self.num_1

        if num_2 == None:
            num_2 = self.num_2

        return num_1 - num_2

    def multiplicar(self, num_1=None, num_2=None):
        if num_1 == None:
            num_1 = self.num_1

        if num_2 == None:
            num_2 = self.num_2

        return num_1 * num_2

    def dividir(self, num_1=None, num_2=None):
        if num_1 == None:
            num_1 = self.num_1

        if num_2 == None:
            num_2 = self.num_2

        if num_2 == 0:
            print("Error! Division por cero no definida")
            return None
        
        return num_1 / num_2