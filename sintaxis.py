class Sintaxis:
    instacia=0
    def __init__(self,dato="Iniciar"):
        self.frase=dato
        Sintaxis.instacia = Sintaxis.instacia + 1

    def usoVariable(self):
        edad, altura = 20,1.75
        nombres = "Josue Cozzarelli"
        Tipo_Sexo = "M"
        carrera="Ingenieria en Software"
        civil = True
        #tuplas = ()

        usuario = ("jcozzarellij", 1234, "jcozzarellij@unemi.edu.ec")

        #listas = []
        materias = ["Administracion General","POO","Sistemas Operativos","Base de datos"]
        materias[0]="Arquitectura de Software"
        materias.append("Estructura de datos")

        #diccionario = {}
        estudiante = {"nombre": "Josue","edad": 20,"facultad":"FACI"}
        estudiante["carrera"]="Ingenieria en software"

        #presentacion usando format
        print("""Nombre {},
tiene {} años, estudia la carrera de {}""".format(nombres,edad,carrera))

        #utilizando indices
        # print(usuario,materias,estudiante)
        # print(usuario,usuario[0], usuario[0:2], usuario[-1])
        # print(materias, materias[2:], materias[:3], materias[-2:])
        print(estudiante,estudiante["nombre"])
ejer1=Sintaxis()
ejer1.usoVariable()


