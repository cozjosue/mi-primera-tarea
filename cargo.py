class Cargo:
    sec_codigo=0
    def __init__(self,des="Sin cargo"):
        Cargo.sec_codigo=Cargo.sec_codigo+1
        self.codigo=Cargo.sec_codigo
        self.descrip=des

if __name__ == "__main__":
    cargo1=Cargo()
    # cargo1.codigo=123456
    # cargo1.descrip="Docente"
    print(cargo1.codigo,cargo1.descrip)
    cargo2=Cargo()
    # cargo2.codigo=56789
    cargo2.descrip="Director"
    print(cargo2.codigo,cargo2.descrip)
    cargo3=Cargo("Analista")
    print(cargo3.codigo,cargo3.descrip)