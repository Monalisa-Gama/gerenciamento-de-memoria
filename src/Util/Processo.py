class Processo:
    def __init__(self, computacao, alocado, visitado, id):
        self.id = id
        self.computacao = computacao
        self.alocado = alocado
        self.visitado = visitado
    
    def __str__(self):
        return "id: {}, computacao: {}, alocado: {}, visitado: {}".format(self.id, self.computacao, self.alocado, self.visitado)
