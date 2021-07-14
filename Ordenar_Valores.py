class Ordenar:
    def __init__(self,lista):
        self.lista=lista
    def burbuja(self):
        for i in range(len(self.lista)):
            for j in range(i+1,len(self.lista)):
                if self.lista[i]>self.lista[j]:
                    aux=self.lista[i]
                    self.lista[i]=self.lista[j]
                    self.lista[j]=aux


    def insertarValor(self,valor):
        self.burbuja()
        auxlist=[]
        enc=False
        for pos,ele in enumerate(self.lista):
            if ele > valor:
                auxlist.append(valor)
                enc=True
                break
        if enc: self.lista = self.lista[0:pos] + auxlist + self.lista [pos:]
        else: self.lista.append(valor)
        return self.lista

    def insertValor2(self,valor):
        self.burbuja()
        auxlist=[]
        enc=False
        for pos,ele in enumerate (self.lista):
            if ele > valor:
                enc=True
                break
        if enc:
            for i in range(pos):
                auxlist.append(self.lista[i])
            auxlist.append(valor)
            for j in range(pos,len(self.lista)):
                auxlist.append(self.lista[j])
            self.lista=auxlist
        else:
            self.lista.append(valor)
        return self.lista

ord = Ordenar([10,15,20,70,80])

#print(ord.insertarValor(2))
print(ord.insertValor2(35))