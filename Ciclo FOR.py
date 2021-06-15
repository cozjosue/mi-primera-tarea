class cicloFOR:
    def __init__(self):
        pass
    def usoFor(self):
        datos=["Josue",20,True]
        numeros=(2,5.6,4,1)
        listaNotas=[(30,40),[20,40],(50,40)]
        estudiantes = {"nombre": "Josue", "edad": 20, "facultad": "FACI"}
        estudiante = [{"nombre": "Josue","final":70},{ "nombre": "Erick","final":80},
                      { "nombre": "Andres","final":50}]
        # for i in range(5):
        #     print("i={}".format(i))
        # for i in range(2,10):
        #     print("i={}".format(i))
        # for i in range(4,10,2):
        #     print("i={}".format(i),end=" ") #end sirve para presentar en la misma linea
        # for i in range(12,3,-3):
        #     print("i={}".format(i),end=" ")

        # Recorrer colecciones
        # longitud=len(datos)
        # for i in range(longitud-1,-1,-1):
        #     print(datos[i])
        # for i,dato in enumerate(numeros):
        #     print("for",i,dato)
        # for dato in numeros:
        #     print(dato)
        # for dato in ["H","o","l","a","que","tal"]:
        #     print(dato)

        # Recorrer diccionario
        # for clave,valor in estudiantes.items():
        #     print(clave,":",valor,end=" ")

        for alumnos in estudiante:
            for clave, valor in alumnos.items():
                print(clave, ":", valor, end=" ")
            print()

obj=cicloFOR()
obj.usoFor()