import sys

path_arquivo = sys.argv[1]
if not path_arquivo.endswith(".java") and not path_arquivo.endswith(".c"):
    print("Você não selecionou um arquivo .java ou .c")
    sys.exit(0)

linhas = list()

try:
    with open(path_arquivo, "r") as arquivo:
        linhas = [linha.strip() for linha in arquivo.readlines()]
except FileNotFoundError:
    print("Arquivo não encontrado.")
    sys.exit(0)
except IOError:
    print("Erro ao ler o arquivo.")
    sys.exit(0)

for linha in linhas:
    if linha == "":
        print("Linha Vazia")
    else:
        blocos = linha.split()
        if "//" in blocos:
            print("Comentário")
            continue
        else:
            print(blocos)