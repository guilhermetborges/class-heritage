class Animal:
    def __init__(self, nome, nro_patas,ambiente,tipo_alimentação,cor_pelo=None):
        self.nome = nome
        self.nro_patas = nro_patas
        self.ambiente = ambiente
        self.tipo_alimentação = tipo_alimentação   
        self.cor_pelo = cor_pelo 

        if nro_patas == 2:
            self.locomocao = "Bípede"
        elif nro_patas == 4:
            self.locomocao = "Quadrúpede"
        else:
            self.locomocao = "Multipéde"

        if cor_pelo == None:
            self.cor_pelo = "Ausente"

    @property
    def comer(self):
        if self.tipo_alimentação == "onívoro":
            return "Come de tudo"
        elif self.tipo_alimentação == "herbívoro":
            return "Come vegetais"
        elif self.tipo_alimentação == "carnívoro":
            return "Come carne"
        else:
            return "Come de tudo"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}= {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, **kw):
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico,voar=False, **kw):
        self.cor_bico = cor_bico
        self.voar = voar
        super().__init__(**kw)

    def voar(self):
        self.voar = True or False

        
def pode_voar(self):
    if self.voar == True:
        return "pode voar"  
    else:
        return "Nao voa"


class Terrestres(Animal):
    def __init__(self, **kw):
        super().__init__(**kw)
    


class Aquaticos(Animal):
    def __init__(self, tipo_respiracao , **kw):
        self.tipo_respiração = tipo_respiracao
        super().__init__(**kw)


class insetos(Animal):
    pass



class mamifero_aquatico(Mamifero,Aquaticos):
    def __init__(self, tipo_respiracao, **kw):
        super().__init__(tipo_respiracao=tipo_respiracao, **kw)

class mamifero_terrestre(Mamifero,Terrestres):
    def __init__(self, **kw):
        super().__init__(**kw)

class mamifero_voador(Mamifero,Ave):
    def __init__(self, cor_bico, **kw):
        super().__init__(cor_bico=cor_bico, **kw)

class mamifero_voador_terrestre(Mamifero,Ave,Terrestres):
    def __init__(self, cor_bico, **kw):
        super().__init__(cor_bico=cor_bico, **kw)   

class mamifero_voador_aquatico(Mamifero,Ave,Aquaticos):
    def __init__(self, cor_bico,tipo_respiracao, **kw):
        super().__init__(cor_bico=cor_bico,tipo_respiracao=tipo_respiracao, **kw)




###  
class tentaculos(Animal):
    def __init__(self,tentaculos, **kw):
        self.tentaculos = tentaculos
        super().__init__(**kw)
###

class polvo(Aquaticos,tentaculos):
    def __init__(self, tentaculos, tipo_respiracao, **kw):
        super().__init__(tentaculos=tentaculos,tipo_respiracao=tipo_respiracao, **kw)





class abelha(insetos):
    pass    

gato = mamifero_terrestre(nome="gato",nro_patas=4, cor_pelo="Preto",ambiente="doméstico",tipo_alimentação="onívoro")
print(gato,"\n")
print(gato.comer,"\n")

abelha = insetos(nome="abelha",nro_patas=6,ambiente="doméstico",tipo_alimentação="onívoro")
print(abelha,"\n")


morcego = mamifero_voador(nome="morcego",nro_patas=2, cor_pelo="marrom",cor_bico="vermelho",ambiente="aéreo",tipo_alimentação="onívoro",voar=False)
print(morcego,"\n")
print(pode_voar(morcego))