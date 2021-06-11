#esta fue la forma en la que yo realice el ejemplo
class Ciclo:
    cont=0
    def __init__(self,num1=0):
        self.numero1=num1

    def usoWhile(self):
        c=input("ingrese vocal: ")
        vocal=["a","e","i","o","u"]
        a=True
        while a:
         if c.lower() not in vocal:
             c=input("ingrese vocal: ")
         else:
             print("usted ingreso la vocal {}".format(c))
             a=False

abc=Ciclo()
abc.usoWhile()

#forma realizada en clase
class Ciclo:
    def __init__(self,n1=0):
        self.numero=n1

    def usoWhilee(self):
        caracter= input("Ingrese una vocal")
        caracter= caracter.lower()
        while caracter not in ("a","e","i","o","u"):
            caracter = input("Ingrese una vocal").lower()
        print("El caracter ingresado {} si es una vocal".format(caracter))
objciclo=Ciclo()
objciclo.usoWhilee()


