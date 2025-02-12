import os

nome_arquivo = "nomes.txt"
dir_atual = os.path.dirname(__file__) # Pegar a pasta em que este programa esta
ARQ = os.path.join(dir_atual, nome_arquivo) #junta o nome do arquivo com o nome da pasta

def incluir_nome (nome):
    try:
        with open(ARQ, "a", encoding="UTF-8") as nomes:
            nomes.write(f"\n{nome}")
    except:
        print("Erro: abertura do arquivo")


incluir_nome("Maria Jesus")

