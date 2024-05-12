class Memoria:
    def __init__(self, estado, inicio, tamanho, id):
        self.id_processo = id
        self.estado = estado
        self.inicio = inicio
        self.tamanho = tamanho

    def get_id_processo(self):
        return self.id_processo

    def set_id_processo(self, id):
        self.id_processo = id

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    def get_inicio(self):
        return self.inicio

    def set_inicio(self, inicio):
        self.inicio = inicio

    def get_tamanho(self):
        return self.tamanho

    def set_tamanho(self, tamanho):
        self.tamanho = tamanho

    def __str__(self):
        return "(id processo:" + str(self.id_processo) + ")," + self.estado + "," + str(self.inicio) + "," + str(self.tamanho)
