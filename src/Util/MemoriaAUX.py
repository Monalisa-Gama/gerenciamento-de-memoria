class MemoriaAUX:
    def __init__(self, idp = None, tamanho = None, idm = None):
        self.idp = idp
        self.tamanho = tamanho
        self.idm = idm

    def getIdp(self):
        return self.idp

    def setIdp(self, id):
        self.idp = id

    def getIdm(self):
        return self.idm

    def setIdm(self, id):
        self.idm = id

    def getTamanho(self):
        return self.tamanho

    def setTamanho(self, tamanho):
        self.tamanho = tamanho

    def __str__(self):
        return "MemoriaAUX [idP=" + str(self.idp) + ", idM=" + str(self.idm) + ", tamanho=" + str(self.tamanho) + "]"
