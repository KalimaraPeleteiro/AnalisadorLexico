import csv
import sys


PALAVRAS_RESERVADAS_C = {
    'auto', 'break', 'case', 'char', 'const', 'continue',
    'default', 'do', 'double', 'else', 'enum', 'extern',
    'float', 'for', 'goto', 'if', 'inline', 'int',
    'long', 'register', 'restrict', 'return', 'short', 'signed',
    'sizeof', 'static', 'struct', 'switch', 'typedef', 'union',
    'unsigned', 'void', 'volatile', 'while'
}

DIRETIVAS_C = {
    '#define', '#include', '#undef', '#if', '#ifdef', '#ifndef', '#else', '#elif', '#endif',
    '#error', '#pragma', '#line', '#'
}

PALAVRAS_RESERVADAS_JAVA = {
    "abstract", "assert", "boolean", "break", "byte", "case",
    "catch", "char", "class", "const", "continue", "default",
    "do", "double", "else", "enum", "extends", "false",
    "final", "finally", "float", "for", "goto", "if",
    "implements", "import", "instanceof", "int", "interface", "long",
    "native", "new", "null", "package", "private", "protected",
    "public", "return", "short", "static", "strictfp", "super",
    "switch", "synchronized", "this", "throw", "throws", "transient",
    "true", "try", "var", "void", "volatile", "while"
}

OPERADORES = {
    "+", "-", "*", "/", "%", "++", "--", "+=", "-=", "*=", "/=", "%=",
    "==", "!=", ">", "<", ">=", "<=", "&&", "||", "!", "=",
    "&", "|", "^", "~", "<<", ">>", ">>>", "<<=", ">>=", ">>>=",
    "&=", "|=", "^="
}

PAUSADORES = {'(', ')', ',', ';', '"', '=', '+', ' '}


def analisador(linhas, linguagem):
    palavras = list()
    linha_atual = 0
    literal_string = False

    for linha in linhas:

        linha_atual += 1

        # Linha Vazia
        if linha == "":
            continue

        # Comentário
        if "//" in linha.split():
            continue

        
        token = []

        for char in linha:

            # Valores entre String são pulados
            if char == '"':
                literal_string = not literal_string

            if literal_string is True:
                continue
            
            if char in OPERADORES:
                palavras.append({"Token": char, "Linha": linha_atual})

            if char not in PAUSADORES:  # Elementos que separam Tokens
                token.append(char)

            elif token == []:           # Pulando Tokens Vazios
                continue

            else:
                palavras.append({"Token": ''.join(token), "Linha": linha_atual})
                token = []
    
    # Para Debug
    """
    for elemento in palavras:
        print(f'{elemento["Token"]} -> Linha {elemento["Linha"]}')
    """

    # CRIAÇÃO DA TABELA
    with open("tabela_tokens.csv", 'w', newline='') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Lexema', 'Tipo de Token', 'Linha do Elemento'])

        with open("tabela_identificadores.csv", 'w', newline='') as identificador_csv:
            escritor_identificador = csv.writer(identificador_csv)
            escritor_identificador.writerow(['Lexema', 'Tipo de Token', 'Linha do Elemento'])

            if linguagem == "java":

                for elemento in palavras:
                    if elemento["Token"] in PALAVRAS_RESERVADAS_JAVA:
                        data = [elemento["Token"], "Palavra Reservada", elemento["Linha"]]
                        escritor.writerow(data)
                        escritor.writerow(data)
                    elif elemento["Token"] in OPERADORES:
                        data = [elemento["Token"], "Operador", elemento["Linha"]]
                        escritor.writerow(data)
                    elif elemento["Token"].startswith("&"):
                        data = [elemento["Token"], "Ponteiro", elemento["Linha"]]
                        escritor.writerow(data)
                    elif elemento["Token"].isdigit():
                        data = [elemento["Token"], "Literal Inteiro", elemento["Linha"]]
                        escritor.writerow(data)
                    else:
                        data = [elemento["Token"], "Identificador", elemento["Linha"]]
                        escritor_identificador.writerow(data)
            
            if linguagem == "c":
                
                for elemento in palavras:
                    if elemento["Token"] in PALAVRAS_RESERVADAS_C:
                        data = [elemento["Token"], "Palavra Reservada", elemento["Linha"]]
                        escritor.writerow(data)
                    elif elemento["Token"] in DIRETIVAS_C:
                        data = [elemento["Token"], "Diretiva do Processador", elemento["Linha"]]
                        escritor.writerow(data)
                    elif elemento["Token"] in OPERADORES:
                        data = [elemento["Token"], "Operador", elemento["Linha"]]
                        escritor.writerow(data)
                    elif elemento["Token"].startswith("&"):
                        data = [elemento["Token"], "Ponteiro", elemento["Linha"]]
                        escritor.writerow(data)
                    elif elemento["Token"].isdigit():
                        data = [elemento["Token"], "Literal Inteiro", elemento["Linha"]]
                        escritor.writerow(data)
                    else:
                        data = [elemento["Token"], "Identificador", elemento["Linha"]]
                        escritor_identificador.writerow(data)

    


if __name__ == "__main__":

    # == Verificação de Parâmetro ==
    if len(sys.argv) < 2:
        print("Você não selecionou nenhum arquivo para análise.")
        sys.exit(0)

    path_arquivo = sys.argv[1]
    
    if path_arquivo.endswith(".java"):
        linguagem = "java"
    elif path_arquivo.endswith(".c") or path_arquivo.endswith(".h"):
        linguagem = "c"
    else:
       print("O analisador analisa apenas arquivos Java ou C!")
       sys.exit(0) 

    # == Verificação de Arquivo ==
    try:
        with open(path_arquivo, "r") as arquivo:
            linhas = [linha.rstrip() for linha in arquivo.readlines()]          # Removendo o \n no final.
    except FileNotFoundError:
        print("Arquivo não encontrado. Você colocou o caminho correto?")
        sys.exit(0)
    except IOError:
        print("Erro ao ler o arquivo.")
        sys.exit(0)

    analisador(linhas, linguagem)