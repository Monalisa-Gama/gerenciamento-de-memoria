class MemoriaAUX:
    def __init__(self, idp, tamanho, idm):
        self.idp = idp
        self.tamanho = tamanho
        self.idm = idm

    def get_idp(self):
        return self.idp

    def set_idp(self, id):
        self.idp = id

    def get_idm(self):
        return self.idm

    def set_idm(self, id):
        self.idm = id

    def get_tamanho(self):
        return self.tamanho

    def set_tamanho(self, tamanho):
        self.tamanho = tamanho

    def __str__(self):
        return "MemoriaAUX [idP=" + str(self.idp) + ", idM=" + str(self.idm) + ", tamanho=" + str(self.tamanho) + "]"
