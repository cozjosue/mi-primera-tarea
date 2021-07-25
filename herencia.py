class Persona:
    _siguiente=0
    def __init__(self,nombre="Invitado",activo=True):
        # self.__nombre=nombre
        self.__nombre = self.__nombremayus(nombre)
        self.activo=activo
        self.__codigo=self.siguiente()
    def siguiente(self):
        Persona._siguiente=Persona._siguiente+1
        return Persona._siguiente

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,nom):
         self.__nombre=nom

    @property
    def codigo(self):
        return self.__codigo
    @codigo.setter
    def codigo(self,cod):
        self.__codigo=cod

    def __nombremayus(self, nom):
        return nom.upper()
    def mostrar(self):
        return ("Codigo : {} , Nombre : {} , Activo : {}".format(self.codigo,self.nombre,self.activo))

class Empleado(Persona):
    def __init__(self,nom="Invitado",ac=True,sueldo=600):
        Persona.__init__(self,nom,ac)
        self.sueldo=sueldo
    def mostrar(self):
        return Persona.mostrar(self)+" - Sueldo: "+str(self.sueldo)

obj = Persona(activo=False)
print(obj.mostrar())
obj2=Persona("Josue")
print(obj2.mostrar())
obj3 = Persona("marcos",False)
print(obj3.mostrar())
obj4=Persona("juan")
print(obj4.mostrar())

obj5=Empleado("adrian")
print(obj5.mostrar())







