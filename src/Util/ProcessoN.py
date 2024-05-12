class ProcessoN:
    def __init__(self, id = None, tamanho = None):
        self.id = id
        self.tamanho = tamanho
    
    def getId(self):
        return self.id
    
    def setId(self, id):
        self.id = id
    
    def getTamanho(self):
        return self.tamanho
    
    def setTamanho(self, tamanho):
        self.tamanho = tamanho
    
    def __str__(self):
        return "id: " + str(self.id) + ", tamanho: " + str(self.tamanho)
