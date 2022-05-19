class Figura:
    def __init__(self, nombre):
        self.nombre = nombre
    

class Cuadrado(Figura):
    def __init__(self, lado):
        super().__init__('Cuadrado')
        self.lado = lado 

    def perimetro(self):
        return self.lado * 4

class Rectangulo(Figura):
    def __init__(self, lado1, lado2):
        super().__init__('Rectángulo')
        self.lado1 = lado1 
        self.lado2 = lado2 

    def perimetro(self):
        return 2*self.lado1 + 2*self.lado2

# TODO: Pensar en otra posible herencia (taxonomía)

# Pruebas
c1 = Cuadrado(6)
c2 = Cuadrado(4)
print('Perímetro cuadrado de 6: ', c1.perimetro())
print('Perímetro cuadrado de 4: ', c2.perimetro())
print(c2.nombre)

r1 = Rectangulo(3,4)
r2 = Rectangulo(4,10)
print('Perímetro de rectángulo de 3 y 4: ', r1.perimetro())
print('Perímetro de rectángulo de 4 y 10: ',r2.perimetro())
print(r2.nombre)