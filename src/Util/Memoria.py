class Memoria:
    def __init__(self, estado, inicio, tamanho, id):
        self.id_processo = id
        self.estado = estado
        self.inicio = inicio
        self.tamanho = tamanho

    def getIdProcesso(self):
        return self.id_processo

    def setIdProcesso(self, id):
        self.id_processo = id

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def getInicio(self):
        return self.inicio

    def setInicio(self, inicio):
        self.inicio = inicio

    def getTamanho(self):
        return self.tamanho

    def setTamanho(self, tamanho):
        self.tamanho = tamanho

    def __str__(self):
        return "(id processo:" + str(self.id_processo) + ")," + self.estado + "," + str(self.inicio) + "," + str(self.tamanho)
