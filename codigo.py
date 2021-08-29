from datetime import date

class Empresa:
    def __init__(self,id,dir,tel,nom,ruc):
        self.empleado = []
        self.__id = id
        self.departamento = []
        self.direccion = dir
        self.telefono = tel
        self.nombre = nom
        self.ruc = ruc
        
    def mostrarEmpresa(self):
        print(self.nombre,self.direccion,self.ruc,self.id,self.empleado.id,self.empleado.nombre)

    def registrarEmpleado(self,nom,suel,fing,ced,corr,tel):
        empleado = Empleado(nom,suel,fing,ced,corr,tel)
        self.empleado.append(empleado)
    
    def registrarDepartamento(self,des):
        dep = Departamento(des)
        self.departamento.append(dep)

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,nid):
        self.__id = nid

class Departamento:
    sec = 0
    def __init__(self,des,empleado=''):
        Departamento.sec += 1
        self.empleado = empleado
        self.__id = Departamento.sec
        self.descripcion = des
    
    def mostrarDep(self):
        print(self.id,self.descripcion)

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,nid):
        self.__id = nid
    
class Empleado:
    sec  = 0
    def __init__(self,nom,suel,fing,ced,corr,tel):
        Empleado.sec += 1
        self.__id = Empleado.sec
        self.nombre = nom
        self.sueldo = suel
        self.fechaingreso = fing
        self.cedula = ced
        self.telefono = tel
        self.correo = corr
    
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,nid):
        self.__id = nid

class Obrero(Empleado):
    def __init__(self, id, nom, suel, fing, ced, corr, tel,sind=True,cont=True):
        super().__init__(id, nom, suel, fing, ced, corr, tel)
        self.sindicato = sind
        self.contratocolectivo = cont

class Administrativo(Empleado):
    def __init__(self, id, nom, suel, fing, ced, corr, tel, com=True):
        super().__init__(id, nom, suel, fing, ced, corr, tel)
        self.comision = com

class Prestamos:
    sec = 0
    def __init__(self,fec,val,numpag,empleado,est=True):
        Prestamos.sec+=1
        self.__id = Prestamos.sec
        self.fecha = fec
        self.valor = val
        self.numpagos = numpag
        self.cuotas = 0
        self.empleado = empleado
        self.saldo = self.valor
        self.estado = est

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,valor):
        self.__id = valor
    
    def calcular(self):
        if self.estado == True:
            self.cuotas = self.valor / self.numpagos
            self.saldo -=self.cuotas
            return self.cuotas , self.saldo
    
    def mostrarPrestamo(self):
        self.calcular()
        print('ID : {}  Empleado : {}   Valor: {}  Numero pagos: {}  Cuotas: {:.2f}  Saldo: {:.2f}'.format(self.id,self.empleado.nombre,self.valor,self.numpagos,self.cuotas,self.saldo) )




class Sobretiempo:
    sec = 0
    def __init__(self,hrec,hext,emp,fec,estado=True):
        Sobretiempo.sec += 1 
        self.__id = Sobretiempo.sec
        self.horarecargo = hrec
        self.horasextraordianria = hext
        self.empleado = emp
        self.fecha = fec
        self.estado = estado
    
    def calculo(self,valor):
        if self.estado==True:
            valorecargo = valor * 0.25
            self.pagorecargo = self.horarecargo * valorecargo
            self.pagoextra = valor * self.horasextraordianria
        else:
            self.pagorecargo = 0
            self.pagoextra = 0

    def mostrar(self,valor):
        self.calculo(valor)
        print('ID :{}      Empleado :{}       Pago Horas Extra:{}   Pago Horas Recargo:{}'.format(self.id,self.empleado.nombre,self.pagorecargo,self.pagoextra))

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,valor):
        self.__id = valor

        
class Deducciones:
    sec = 0
    def __init__(self,iess,com,anti):
        Deducciones.sec +=1
        self.__id = Deducciones.sec
        self.iess = iess
        self.comision = com
        self.antiguedad = anti

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,valor):
        self.__id = valor
    
    def mostrarDeducciones(self):
        print('ID:{}     IEES:{}    Comision:{}   Antiguedad:{}'.format(self.id,self.iess,self.comision,self.antiguedad))

class Nomina:
    def __init__(self,empleado,fecha,sobretiempo,totalingreso,prestamo,totaldescuento,liquides):
        self.empleado = empleado
        self.fecha = fecha
        self.sobretiempo = sobretiempo
        self.sueldo = self.empleado.sueldo
        self.totalingreso = totalingreso
        self.prestamo = prestamo
        self.totaldescuento = totaldescuento
        self.liquides= liquides

    def mostrarNomina(self,valor,iees,comision,antiguedad):
        print('        NOMINA        ')
        print('Fecha : {}'.format(self.fecha))
        print('Empleado : {} '.format(self.empleado.nombre))
        self.sobretiempo.calculo(valor)
        print('Descripcion      Subtotal')
        print('Sueldo             {} '.format(self.sueldo))
        print('Horas Extra        {}'.format(self.sobretiempo.pagoextra))
        print('Horas Recargo      {}'.format(self.sobretiempo.pagorecargo))
        self.prestamo.calcular()
        print('Prestamo           {:.2f}'.format(self.prestamo.cuotas))
        print('IEES               {}'.format(self.sueldo*iees))
        print('Comision           {}'.format(comision))
        print('Antiguedad         {}'.format(antiguedad))
        self.totalingreso = self.sueldo+self.sobretiempo.pagoextra+self.sobretiempo.pagorecargo+comision+antiguedad
        self.totaldescuento = self.prestamo.cuotas+(self.sueldo*iees)
        print('Total Ingreso      {}'.format(self.totalingreso))
        print('Total a Descontar  {:.2f}'.format(self.totaldescuento))
        print('Total a recibir   ${:.2f}'.format(self.totalingreso-self.totaldescuento))


today = date.today()
empleado1 = Empleado('Josue',800,'27/08/2019','9999','correo','09999')
prestamo1 = Prestamos(today,800,12,empleado1,False)
deduccion1=Deducciones(0.1115,80,80)
# prestamo1.mostrarPrestamo()



# empleado2=Empleado('Marcos',700,'15/08/2019','9999','correo','09999')
# prestamo2 = Prestamos(today,1500,12,empleado2,True)
# prestamo2.mostrarPrestamo()

extra1 = Sobretiempo(4,8,empleado1,today,False)
nomina1 = Nomina(empleado1,today,extra1,0,prestamo1,0,0)
nomina1.mostrarNomina(8,deduccion1.iess,deduccion1.comision,deduccion1.antiguedad)