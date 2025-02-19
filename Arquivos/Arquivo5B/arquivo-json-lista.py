import os, json

APROVACAO = 6
NOTA1 = 0
NOTA2 = 1

def definir_arquivo(nome_arquivo):
    dir_corrente = os.path.dirname(__file__)
    arquivo = os.path.join(dir_corrente, nome_arquivo)
    return arquivo

def ler_arquivo(arq):
    turma = None
    try:
        with open(arq, "r", encoding="UTF-8") as arquivo:
            turma = json.load(arquivo)
    except:
        print("Erro: abertura do arquivo")
        exit()
    return turma

def verificar_aprovacao(turma):
    aprovacao = []
    for aluno in turma:
        media = round((aluno["notas"][NOTA1] + aluno["notas"][NOTA2]) / 2, 1)
        if (media >= APROVACAO):
            aprovacao.append({"nome": aluno["nome"], "media": media, "status": "Aprovado"})
        else:
            aprovacao.append({"nome": aluno["nome"], "media": media, "status": "Prova final"})
    return aprovacao

def gravar_arquivo(arq, aprovacao):
    try:
        with open(arq, "w", encoding="UTF-8") as arquivo:
            arquivo.write(json.dumps(aprovacao, indent=4, ensure_ascii=False))
            print("Arquivo gravado")
    except:
        print("Erro: gravação do arquivo")


arquivo_entrada = definir_arquivo("turma.json")
turma = ler_arquivo(arquivo_entrada)
# print(type(turma))
print(turma)
aprovacao = verificar_aprovacao(turma)
print(aprovacao)
arquivo_saida = definir_arquivo("aprovacao.json")
gravar_arquivo(arquivo_saida, aprovacao)