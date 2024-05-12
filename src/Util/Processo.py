class Processo:
    def __init__(self, computacao, alocado, visitado, id):
        self.id = id
        self.computacao = computacao
        self.alocado = alocado
        self.visitado = visitado
    
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
    
    def getComputacao(self):
        return self.computacao
    
    def setComputacao(self, computacao):
        self.computacao = computacao
    
    def getAlocado(self):
        return self.alocado
    
    def setAlocado(self, alocado):
        self.alocado = alocado
    
    def getVisitado(self):
        return self.visitado
    
    def setVisitado(self, visitado):
        self.visitado = visitado
    
    def __str__(self):
        return "Processo [id=" + str(self.id) + ", computacao=" + str(self.computacao) + ", alocado=" + str(self.alocado) + ", visitado=" + str(self.visitado) + "]"
