from cargo import Cargo

class Empleados:
    sec_codigo=0
    def __init__(self,nom,ced,suel,carg):
        self.codigo=self.generarCodigo()
        self.nombre=nom
        self.sueldo=suel
        self.cedula=ced
        self.cargo=carg
    def mostrar(self):
        print("codigo: {} nombre: {} cargo:{}-{}".format(self.codigo,self.nombre,self.cargo.codigo,self.cargo.descrip))
    def generarCodigo(self):
        Empleados.sec_codigo = Empleados.sec_codigo + 1
        return Empleados.sec_codigo
cargo1=Cargo("Analista")
empleado1=Empleados("Josue","125027",600,cargo1)
empleado1.mostrar()

cargo2=Cargo("Docente")
empleado2=Empleados("Danilo","09987",500,cargo2)
empleado2.mostrar()