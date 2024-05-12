import os
from src.Util.Memoria import Memoria
from src.Util.Processo import Processo 

class Arquivo:
    def __init__(self):
        self.escritor = None
        self.algoritmos = []

    def ler_arquivo(self, FILENAME):
        mList = []
        ptList = []
        idProcesso = 1
        try:
            with open(FILENAME, 'r') as file:
                for line in file:
                    if line.strip():  # Verifica se a linha não está vazia
                        if ' ' in line:
                            parts = line.split()
                            m = Memoria(parts[0], int(parts[1]), int(parts[2]), 0)
                            mList.append(m)
                        else:
                            p = Processo(int(line), 0, 0, idProcesso)
                            ptList.append(p)
                            idProcesso += 1

            if mList:
                return mList
            else:
                return ptList
        except Exception as e:
            print(e)
            return None

    def arquivo_saida(self, texto, algoritmo):
        """
        Método responsável por escrever os dados no arquivo de saída
        """
        try:
            if not os.path.exists("saida"):
                os.makedirs("saida")
            if algoritmo + ".txt" not in self.algoritmos:
                self.algoritmos.append(algoritmo + ".txt")

            with open("saida/" + algoritmo + ".txt", "a") as file:
                file.write(texto + "\n")
        except Exception as e:
            print(e)
