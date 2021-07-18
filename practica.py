class Logica:
    def __init__(self,lista=None):
        self.__lista=lista

    @property
    def lista(self):
        return self.__lista
    @lista.setter
    def lista(self,valor):
        self.__lista=valor

    def numero_par(self,numero):
        rec = numero%2
        if rec == 0 :
            print("{} es par".format(numero))
        else:
            print("{} es impar".format(numero))

    def perfecto(self,numero):
        acu=0
        for contador in range(1,numero):
            rec=numero%contador
            if rec == 0 :
                acu=acu+contador
        if acu == numero:
            print("{} es perfecto".format(numero))
        else:
            print("{} No es perfecto".format(numero))

    def divisor(self,numero):
        pass

class Ejercicio(Logica):
    def __init__(self,lista,numeros):
        super().__init__(lista)
        self.num=numeros

    def sumar(self,n1,n2):
        return n1+n2

    def parimpar(self,numero):
        super().numero_par(numero)
        return numero%2

# ejercicio1=Ejercicio()
# if ejercicio1.parimpar(6) == 0:
#     print("PAR")
# else:
#     print("IMPAR")

ejer = Logica()
ejer.perfecto(8)