import sys

path_arquivo = sys.argv[1]
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
    for char in linha:
        print(char)