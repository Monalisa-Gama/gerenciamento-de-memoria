class ProcessoN:
    def __init__(self, id, tamanho):
        self.id = id
        self.tamanho = tamanho

    def __str__(self):
        return "id: {}, tamanho: {}".format(self.id, self.tamanho)
