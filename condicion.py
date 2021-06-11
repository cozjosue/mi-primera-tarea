class Condicion:
    cont=0
    def __init__(self,n1=0,n2=0):
        self.numero1=n1
        self.numero2=n2
        self.numero3=n1
    def usoIf(self):
        if self.numero1 == self.numero2:
            print("El primero numero {} y el segundo numeroo {} son iguales".format(self.numero1,self.numero2))
        elif self.numero1 == self.numero3:
            print("El primer numero {} y el tercer numero {} son iguales".format(self.numero1,self.numero3))
        else:
            print("Los numeros son diferentes")


#uso clase
objeto1= Condicion(7,3)
print("El primero numero es {}".format(objeto1.numero1))
print("El segundo numero es {}".format(objeto1.numero2))
print("El tercer numero es {}".format(objeto1.numero3))
objeto1.usoIf()

