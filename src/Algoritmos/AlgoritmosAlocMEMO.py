from Util.MemoriaAUX import MemoriaAUX
from Util.Memoria import Memoria
from Util.Processo import Processo
from Util.ProcessoN import ProcessoN
from Util.Arquivo import Arquivo

class AlgoritmosAlocMEMO:

    txtMemoria = "entrada/entrada-memoria.txt"
    txtProcessos = "entrada/entrada-processos.txt"
    a = Arquivo()
    MemoriaLIDA = []
    ProcessosLIDOS = []
    ProcessosNALOCADOS = []

    @staticmethod
    def main():
        print("PARA RODAR NOVAMENTE O PROGRAMA")
        print("DELETE TODOS OS ARQUIVOS DE SAIDA\n")

        AlgoritmosAlocMEMO.resetDATA()
        print("Rodando Frist Fit...")
        AlgoritmosAlocMEMO.FristFIT(AlgoritmosAlocMEMO.MemoriaLIDA, AlgoritmosAlocMEMO.ProcessosLIDOS)
        print("Terminado\n")
        AlgoritmosAlocMEMO.resetDATA()
        print("Rodando Next Fit...")
        AlgoritmosAlocMEMO.NextFIT(AlgoritmosAlocMEMO.MemoriaLIDA, AlgoritmosAlocMEMO.ProcessosLIDOS)
        print("Terminado\n")
        AlgoritmosAlocMEMO.resetDATA()
        print("Rodando Best Fit...")
        AlgoritmosAlocMEMO.BestFIT(AlgoritmosAlocMEMO.MemoriaLIDA, AlgoritmosAlocMEMO.ProcessosLIDOS)
        print("Terminado\n")
        AlgoritmosAlocMEMO.resetDATA()
        print("Rodando Worst Fit...")
        AlgoritmosAlocMEMO.WorstFIT(AlgoritmosAlocMEMO.MemoriaLIDA, AlgoritmosAlocMEMO.ProcessosLIDOS)
        print("Terminado\n")

        print("PARA RODAR NOVAMENTE O PROGRAMA")
        print("DELETE TODOS OS ARQUIVOS DE SAIDA")

    @staticmethod
    def FristFIT(Memoria, Processos):
        tamanhoM = -1
        auxN = ProcessoN()

        for processo in Processos:
            for memoriaI in Memoria:
                tamanhoM = memoriaI.getTamanho()
                tamanhoM = -tamanhoM if tamanhoM < 0 else tamanhoM

                if memoriaI.getEstado() == "H" and processo.getComputacao() <= tamanhoM and processo.getAlocado() == 0:
                    memoriaI.setEstado("P")
                    memoriaI.setIdProcesso(processo.getId())
                    processo.setAlocado(1)

        for p in Processos:
            if p.getAlocado() == 0:
                auxN.setId(p.getId())
                auxN.setTamanho(p.getComputacao())
                AlgoritmosAlocMEMO.ProcessosNALOCADOS.append(auxN)
            auxN = ProcessoN()

        AlgoritmosAlocMEMO.escreverArquivo("FRIST-FIT")

    @staticmethod
    def NextFIT(Memoria, Processos):
        tamanhoM = -1
        auxN = ProcessoN()
        num = 0

        for processo in Processos:
            for i in range(num, len(Memoria)):
                tamanhoM = Memoria[i].getTamanho()
                tamanhoM = -tamanhoM if tamanhoM < 0 else tamanhoM

                if Memoria[i].getEstado() == "H" and processo.getComputacao() <= tamanhoM and processo.getAlocado() == 0:
                    Memoria[i].setEstado("P")
                    Memoria[i].setIdProcesso(processo.getId())
                    processo.setAlocado(1)
                    num = i

                if i + 1 == len(Memoria):
                    num = 0

        for p in Processos:
            if p.getAlocado() == 0:
                auxN.setId(p.getId())
                auxN.setTamanho(p.getComputacao())
                AlgoritmosAlocMEMO.ProcessosNALOCADOS.append(auxN)
            auxN = ProcessoN()

        AlgoritmosAlocMEMO.escreverArquivo("NEXT-FIT")

    @staticmethod
    def BestFIT(Memoria, Processos):
        key = False
        tamanhoMV = -1
        auxN = ProcessoN()
        MemoriaV = []

        for i in range(len(Processos)):
            for j in range(len(Memoria)):
                if Memoria[j].getEstado() == "H" and Processos[i].getComputacao() <= Memoria[j].getTamanho() and Processos[i].getAlocado() == 0:
                    x = Memoria[j].getTamanho()
                    y = Processos[i].getComputacao()
                    tamanhoMV = x - y
                    auxMV = MemoriaAUX()
                    auxMV.setIdP(Processos[i].getId())
                    auxMV.setIdm(j)
                    auxMV.setTamanho(tamanhoMV)
                    MemoriaV.append(auxMV)
                    key = True

            if Processos[i].getAlocado() == 0 and key == True:
                auxMV = min(MemoriaV, key=lambda x: x.getTamanho())
                Processos[i].setAlocado(1)
                idPR = auxMV.getIdp()
                idME = auxMV.getIdm()
                Memoria[idME].setIdProcesso(idPR)
                Memoria[idME].setEstado("P")
                MemoriaV.clear()
                key = False

        for p in Processos:
            if p.getAlocado() == 0:
                auxN = ProcessoN(p.getId(), p.getComputacao())
                AlgoritmosAlocMEMO.ProcessosNALOCADOS.append(auxN)

        AlgoritmosAlocMEMO.escreverArquivo("BEST-FIT")

    @staticmethod
    def WorstFIT(Memoria, Processos):
        key = False
        tamanhoMV = -1
        auxN = ProcessoN()
        MemoriaV = []

        for i in range(len(Processos)):
            for j in range(len(Memoria)):
                if Memoria[j].getEstado() == "H" and Processos[i].getComputacao() <= Memoria[j].getTamanho() and Processos[i].getAlocado() == 0:
                    x = Memoria[j].getTamanho()
                    y = Processos[i].getComputacao()
                    tamanhoMV = x - y
                    auxMV = MemoriaAUX()
                    auxMV.setIdP(Processos[i].getId())
                    auxMV.setIdm(j)
                    auxMV.setTamanho(tamanhoMV)
                    MemoriaV.append(auxMV)
                    key = True

            if Processos[i].getAlocado() == 0 and key == True:
                auxMV = max(MemoriaV, key=lambda x: x.getTamanho())
                Processos[i].setAlocado(1)
                idPR = auxMV.getIdp()
                idME = auxMV.getIdm()
                Memoria[idME].setIdProcesso(idPR)
                Memoria[idME].setEstado("P")
                MemoriaV.clear()
                key = False

        for p in Processos:
            if p.getAlocado() == 0:
                auxN = ProcessoN(p.getId(), p.getComputacao())
                AlgoritmosAlocMEMO.ProcessosNALOCADOS.append(auxN)

        AlgoritmosAlocMEMO.escreverArquivo("WORST-FIT")

    @staticmethod
    def escreverArquivo(algoritmo):
        AlgoritmosAlocMEMO.a.arquivoSaida("Algoritmo " + algoritmo + "\n", algoritmo)
        for m in AlgoritmosAlocMEMO.MemoriaLIDA:
            AlgoritmosAlocMEMO.a.arquivoSaida(str(m), algoritmo)

        AlgoritmosAlocMEMO.a.arquivoSaida("\nPROCESSOS NÃO ALOCADOS / TAMANHO", algoritmo)
        for pnl in AlgoritmosAlocMEMO.ProcessosNALOCADOS:
            AlgoritmosAlocMEMO.a.arquivoSaida(str(pnl), algoritmo)

    @staticmethod
    def resetDATA():
        AlgoritmosAlocMEMO.MemoriaLIDA = AlgoritmosAlocMEMO.a.lerArquivo(AlgoritmosAlocMEMO.txtMemoria)
        AlgoritmosAlocMEMO.ProcessosLIDOS = AlgoritmosAlocMEMO.a.lerArquivo(AlgoritmosAlocMEMO.txtProcessos)
        AlgoritmosAlocMEMO.ProcessosNALOCADOS = []

if __name__ == "__main__":
    AlgoritmosAlocMEMO.main()
