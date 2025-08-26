import os
import subprocess
import random

def main():
    questoes = [{
        "pergunta": "digite a funcao pra mostar algo na tela: ",
        "resposta": "print()"
    },
    {                                        "pergunta": "que tipo de variavel e 'Maria'? ",
        "resposta": "str"
    },                                   {
        "pergunta": "que tipo de variavel e 5? ",
        "resposta": "int"
    },
    {
        "pergunta": "que tipo de variavel e 5.5? ",
        "resposta": "float"
    },
    {
        "pergunta": "que tipo de variavel e False/True? ",
        "resposta": "bool"
    },
    {
        "pergunta": "digite a funcao para pegar valores externos: ",
        "resposta": "input()"
    },
    {
        "pergunta": "Digite operadores artimeticos: nesta sequencia: adiccao, subtracao, multiplicacao, divisao, parte inteira da divisao, resto da divisao, potencia: ",
        "resposta": "+,-,*,/,//,%,**"
    },
    {
        "pergunta": "Digite operadores de comparacao, nesta sequencia: igual, diferente, maior que, menor que,maior ou igual, menor ou igual: ",
        "resposta": "==,!=,>,<,>=,<="
    },
    {
        "pergunta": "Digite os 3 operadores logicos:",
        "resposta": "and,or,not"
    },
    {
        "pergunta": "operadores de atribuicao nesta sequencia: receber, receber e adicionar e receber, subtrair e receber, multiplicar e receber, ",
        "resposta": "=,+=,-=,*="
    },
    {
        "pergunta": "estrutura de controld usados para executar blocos de código apenas se uma condição for verdadeira. ",
        "resposta": "if"
    },
    {
        "pergunta": "estrutura de controle usados para executar blocos caso nao aconteca a condicao, ou se a condicao for falsa. ",
        "resposta": "else"
    },
    {
        "pergunta": "estrutura de condicao de executa varias condicoes: ",
        "resposta": "elif"
    },
    {
        "pergunta": "Loop (enquanto uma condição for verdadeira) ",
        "resposta": "while"
    },
    {
        "pergunta": "Loop que (itera sobre uma sequência): itera numero ",
        "resposta": "for in range()"
    },
    {
        "pergunta": "interrafo sobre uma lista: ",
        "resposta": "for a in lista"
    },
    {
        "pergunta": "Interrompe o loop completamente. ",
        "resposta": "break"
    },
    {
        "pergunta": "Pula para a próxima iteração.",
        "resposta": "continue"
    },
    {
        "pergunta": "digite a estrutura de como criar uma lista: ",
        "resposta": "lista = []"
    },
    {
        "pergunta": "metodo como adicionar item no final: ",
        "resposta": "lista.append('item')"
    },
    {
        "pergunta": "metodo de como inserir em uma posicao esoecifica: ",
        "resposta": "lista.insert(0, 'item')"
    },
    {
        "pergunta": "metodo como remover um item pelo item: ",
        "resposta": "lista.remove('item')"
    },
    {
        "pergunta": "metodo como remover item pelo indice ou posicao: ",
        "resposta": "lista.pop(0)"
    },
    {
        "pergunta": "metodo para retornar tamanho: ",
        "resposta": "len(lista)"
    },
    {
        "pergunta": "metodo para retornar todas as chaves: ",
        "resposta": "lista.keys()"
    },
    {
        "pergunta": "metodo para retornar todos valores: ",
        "resposta": "lista.values()"
    },
    {
        "pergunta": "metodo para retornar pares chave-valor",
        "resposta": "elemento.items()"
    },
    {
        "pergunta": "metodo para adicionar ou actualizar itens: ",
        "resposta": "elemento.update({})"
    },
    {
        "pergunta": "como criar uma funcao? ",
        "resposta": " def nome_da_funcao()"
    },
    {
        "pergunta": "como criar funcao com parametros",
        "resposta": "def nome_da_funcao(a)"
    },
    {
        "pergunta": "como criar uma funcao com parametros padrao (exemplo pi): ",
        "resposta": "def nome_da_funcao(pi=3.14)"
    
    },
    {
        "pergunta": "criar um funcao com retorno: ",
        "resposta": "def nome_da_funcao(a):,return a"
    },
    {
        "pergunta": "criar funcao com tupla: ",
        "resposta": "def nome_da_funcao(*tupla)"
    },
    {
        "pergunta": "criar funcao com dicionario: ",
        "resposta": "def nome_da_funcao(**dicionario)"
    },
    {
        "pergunta": "imagine que criou um arquivo modolo.py, importe-o: ",
        "resposta": "import modolo"
    },
    {
        "pergunta": "metodo para usar funcao do modolo importado: ",
        "resposta": "modolo.funcao()"
    },
    {
        "pergunts": "importar uma funcao especifica(): ",
        "resposta": "from modolo import funcao"
    },
    {
        "pergunta": "importar modulo com como/alias: ",
        "resposta": "import modulo as a"
    },
    {
        "pergunta": "como importar modulo com.funcoes matematicas? ",
        "resposta": "import math"
        
    },
    {
        "resposta": "no modolo de matematica como usar raiz quadrada: ",
        "resposta": "math.sqrt()"
    },
    {
        "pergunta": "como usar o factorail?;",
        "resposta": "math.factorial()"
    },
    {
        "pergunta": "como importar modolo de numeros aleatorios: ",
        "resposta": "import random"
    },
    {
        "pergunta": "sortear nr de 1 a 10: ",
        "resposta": "random.randint(1, 10)"
    },
    {
        "pergunta": "como embaralhar uma lista: ",
        "resposta": "ranfom.shuffle(lista)"
    },
    {
        "pergunta": "escolher aleatoriamente em uma lisa: ",
        "resposta": "random.choice(lista)"
    },
    {
        "pergunta": "importar modolo para trabalhar com data: ",
        "resposta": "from datetime import datetime"
    },
    {
        "pergunta": "pegar data de hoje",
        "resposta": "hoje = datetime.now(), hoje.strftime(%d-%m-%Y)"
    },
    {
        "pergunta": "como instalar bibliotecas externas: ",
        "resposta": "pip install nome_da_biblioteca"
    },
    {
        "pergunta": "importe requisicoes HTTP api de github e mostre o estado:  ",
        "resposta": "a = requests.get(https://api.github.com),print(a.status_code)"
    }]

    random.shuffle(questoes)
    
    arquivo = "exemplo.py"

    for a in questoes:
        while True:
            resposta_user = input(a['pergunta'])
            if resposta_user == a['resposta']:
                print("acertou...")
                r = input(" quer treinar? ")
                if r.lower() in ["sim", "s", "yes", "y"]:
                    try:
                    
                        # Criar aquivo
                        with open(arquivo, "w") as f:
                            f.write(f"# {a['pergunta']}\n")
                            f.write(f"# Resposta correta: {a['resposta']}\n\n")
                            f.write("# Escreva seu código de treino abaixo:\n")
                            f.write("# -----------------------------------\n\n")
                    
                        # ABRIR O ARQUIVO NO MICRO EDITOR
                        print("📝 Abrindo arquivo no micro editor...")
                        subprocess.run(["micro", arquivo])

                    #tratar erro o aquivo nao ser encontrado   
                    except FileNotFoundError:
                        print("❌ Micro editor não encontrado!")
                        print("📋 Instalando micro editor...")
                        subprocess.run(["pkg", "install", "micro", "-y"])
                        print("✅ Micro instalado! Abrindo arquivo...")
                        subprocess.run(["micro", arquivo])

                    #tratar outros erros 
                    except Exception as e:
                        print(f"❌ Erro ao abrir arquivo: {e}")
                        print("📁 Caminho do arquivo:", os.path.abspath(arquivo))
                break
            else:
                print(f"errou, a resposta seria:\n{a['resposta']}")

if __name__=="__main__":
    main()
