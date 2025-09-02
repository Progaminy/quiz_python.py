import exercicio

questoes = [
    # Saída de dados e entrada de dados
    {
        "pergunta": "Digite a função para mostrar algo na tela:\n",
        "resposta": "print()",
    },
    {
        "pergunta": "Digite a função para obter valores do usuário:\n",
        "resposta": "input()",
    },
    
    # Tipos de dados e variáveis
    {
        "pergunta": "Que tipo de variável é 'Maria'?\n",
        "resposta": "str"
    },
    {
        "pergunta": "Que tipo de variável é 5?\n",
        "resposta": "int"
    },
    {
        "pergunta": "Que tipo de variável é 5.5?\n",
        "resposta": "float"
    },
    {
        "pergunta": "Que tipo de variável é False/True?\n",
        "resposta": "bool"
    },
    
    # Operadores
    {
        "pergunta": "Digite operadores aritméticos nesta sequência: adição, subtração, multiplicação, divisão, parte inteira da divisão, resto da divisão, potência:\n",
        "resposta": "+,-,*,/,//,%,**"
    },
    {
        "pergunta": "Digite operadores de comparação nesta sequência: igual, diferente, maior que, menor que, maior ou igual, menor ou igual:\n",
        "resposta": "==,!=,>,<,>=,<="
    },
    {
        "pergunta": "Digite os 3 operadores lógicos:\n",
        "resposta": "and,or,not"
    },
    {
        "pergunta": "Digite operadores de atribuição nesta sequência: receber, adicionar e receber, subtrair e receber, multiplicar e receber:\n",
        "resposta": "=,+=,-=,*="
    },
    
    # Estruturas de controle condicional
    {
        "pergunta": "Estrutura de controle usada para executar blocos de código apenas se uma condição for verdadeira:\n",
        "resposta": "if"
    },
    {
        "pergunta": "Estrutura de controle usada para executar blocos caso a condição do if seja falsa:\n",
        "resposta": "else:"
    },
    {
        "pergunta": "Estrutura de condição que testa múltiplas condições:\n",
        "resposta": "elif"
    },
    
    # Estruturas de repetição
    {
        "pergunta": "Loop que executa enquanto uma condição for verdadeira:\n",
        "resposta": "while"
    },
    {
        "pergunta": "Loop que itera sobre uma sequência numérica:\n",
        "resposta": "for a in range():"
    },
    {
        "pergunta": "Loop que itera sobre todos os elementos de uma lista:\n",
        "resposta": "for a in lista:"
    },
    {
        "pergunta": "Comando que interrompe completamente o loop:\n",
        "resposta": "break"
    },
    {
        "pergunta": "Comando que pula para a próxima iteração do loop:\n",
        "resposta": "continue"
    },
    
    # Listas
    {
        "pergunta": "Digite a estrutura para criar uma lista vazia:\n",
        "resposta": "lista = []"
    },
    {
        "pergunta": "Método para adicionar um item ao final de uma lista:\n",
        "resposta": "lista.append('item')"
    },
    {
        "pergunta": "Método para inserir um item em uma posição específica da lista:\n",
        "resposta": "lista.insert(0, 'item')"
    },
    {
        "pergunta": "Método para remover um item da lista pelo seu valor:\n",
        "resposta": "lista.remove('item')"
    },
    {
        "pergunta": "Método para remover um item da lista pelo seu índice:\n",
        "resposta": "lista.pop(0)"
    },
    {
        "pergunta": "Função que retorna o tamanho de uma lista:\n",
        "resposta": "len(lista)"
    },
    {
        "pergunta": "Como adicionar itens wm uma lista de dicionatio (for i in range(len(lista1)) chave-> chave_lista1:\n",
        "resposta": "lista1[a]['chave1_lista1'] = exercicio.ex[i]['chave_lista1']
    },

    # Dicionários
    {
        "pergunta": "Método para retornar todas as chaves de um dicionário:\n",
        "resposta": "dicionario.keys()"
    },
    {
        "pergunta": "Método para retornar todos os valores de um dicionário:\n",
        "resposta": "dicionario.values()"
    },
    {
        "pergunta": "Método para retornar pares chave-valor de um dicionário:\n",
        "resposta": "dicionario.items()"
    },
    {
        "pergunta": "Método para adicionar ou atualizar itens em um dicionário:\n",
        "resposta": "dicionario.update({})"
    },
    
    # Funções
    {
        "pergunta": "Como criar uma função básica:\n",
        "resposta": "def funcao():"
    },
    {
        "pergunta": "Como criar uma função com parâmetros:\n",
        "resposta": "def funcao(parametro):"
    },
    {
        "pergunta": "Como criar uma função com parâmetros padrão (exemplo pi=3.14):\n",
        "resposta": "def funcao(pi=3.14):"
    },
    {
        "pergunta": "Como criar uma função que aceita número variável de argumentos (tupla):\n",
        "resposta": "def funcao(*args):"
    },
    {
        "pergunta": "Como criar uma função que aceita número variável de argumentos nomeados (dicionário):\n",
        "resposta": "def funcao(**kwargs):"
    },
    {
        "pergunta": "Boas práticas para executar código principal em um módulo Python:\n",
        "resposta": "if __name__ == '__main__':"
    },
    
    # Módulos e importações
    {
        "pergunta": "Imagine que criou um arquivo modulo.py, como importá-lo:\n",
        "resposta": "import modulo"
    },
    {
        "pergunta": "Como importar uma função específica de um módulo:\n",
        "resposta": "from modulo import funcao"
    },
    {
        "pergunta": "Como importar um módulo com um alias/apelido:\n",
        "resposta": "import modulo as m"
    },
    {
        "pergunta": "Como usar uma função de um módulo importado:\n",
        "resposta": "modulo.funcao()"
    },
    {
        "pergunta": "Módulo para gerar números aleatórios:\n",
        "resposta": "import random"
    },
    {
        "pergunta": "Módulo para operações matemáticas:\n",
        "resposta": "import math"
    },
    {
        "pergunta": "Módulo para trabalhar com strings e caracteres:\n",
        "resposta": "import string"
    },
    {
        "pergunta": "Módulo para gerar senhas seguras:\n",
        "resposta": "import secrets"
    },
    {
        "pergunta": "Módulo para trabalhar com datas:\n",
        "resposta": "from datetime import datetime"
    },
    {
        "pergunta": "Módulo para trabalhar com arquivos CSV:\n",
        "resposta": "import csv"
    },
    {
        "pergunta": "Módulo para trabalhar com arquivos JSON:\n",
        "resposta": "import json"
    },
    {
        "pergunta": "Modulo para manipular arquivo/diretorios criar pasta, operacoes com sistemas operacional\n",
        "resposta": "import os"
    },
    {
        "pergunta": "Modulo para executar processos externos, como abrir pasta:\n",
        "resposta": "import subprocess"
    },
    
    # Funções do módulo math
    {
        "pergunta": "Função para calcular raiz quadrada no módulo math:\n",
        "resposta": "math.sqrt()"
    },
    {
        "pergunta": "Função para calcular fatorial no módulo math:\n",
        "resposta": "math.factorial()"
    },
    {
        "pergunta": "Função para calcular hipotenusa no módulo math:\n",
        "resposta": "math.hypot(a, b)"
    },
    {
        "pergunta": "Função para calcular logaritmo no módulo math:\n",
        "resposta": "math.log(x)"
    },
    
    # Funções do módulo random
    {
        "pergunta": "Função para sortear um número inteiro entre 1 e 10:\n",
        "resposta": "random.randint(1, 10)"
    },
    {
        "pergunta": "Função para embaralhar uma lista:\n",
        "resposta": "random.shuffle(lista)"
    },
    {
        "pergunta": "Função para escolher um elemento aleatório de uma lista:\n",
        "resposta": "random.choice(lista)"
    },
    
    # Funções dos módulos string e secrets
    {
        "pergunta": "Como criar uma variável com letras e dígitos para geração de senhas:\n",
        "resposta": "caracteres = string.ascii_letters + string.digits"
    },
    {
        "pergunta": "Como criar uma variável com letras, dígitos e símbolos para senhas fortes:\n",
        "resposta": "caracteres = string.ascii_letters + string.digits + string.punctuation"
    },
    {
        "pergunta": "Como gerar uma senha aleatória com o módulo random:\n",
        "resposta": "return ''.join(random.choice(caracteres) for _ in range(tamanho))"
    },
    {
        "pergunta": "Como gerar uma senha segura com o módulo secrets:\n",
        "resposta": "return ''.join(secrets.choice(caracteres) for _ in range(tamanho))"
    },
    
    # Técnicas úteis
    {
        "pergunta": "Como inverter uma string (palíndromo) na variável 'a':\n",
        "resposta": "a[::-1]"
    },
    {
        "pergunta": "Método para comparar strings ignorando maiúsculas/minúsculas:\n",
        "resposta": "a.lower() in"
    },
    
    # Funções do módulo datetime
    {
        "pergunta": "Como obter a data e hora atuais:\n",
        "resposta": "hoje = datetime.now()"
    },
    {
        "pergunta": "Como formatar uma data no formato dia-mês-ano:\n",
        "resposta": "hoje.strftime('%d-%m-%Y')"
    },
    
    # Bibliotecas externas
    {
        "pergunta": "Como instalar bibliotecas externas usando pip:\n",
        "resposta": "pip install biblioteca"
    },
    
    # Requisições HTTP
    {
        "pergunta": "Como fazer uma requisição GET para a API do GitHub:\n",
        "resposta": "a = requests.get('https://api.github.com')"
    },
    {
        "pergunta": "Como verificar o status code de uma requisição HTTP:\n",
        "resposta": "print(a.status_code)"
    },
    
    # Manipulação de arquivos
    {
        "pergunta": "Como abrir um arquivo para escrita:\n",
        "resposta": "a = open('arquivo.txt', 'w', encoding='utf-8')"
    },
    {
        "pergunta": "Como escrever em um arquivo:\n",
        "resposta": "a.write('texto')"
    },
    {
        "pergunta": "Como fechar um arquivo:\n",
        "resposta": "a.close()"
    },
    {
        "pergunta": "Como abrir e fechar automaticamente um arquivo (context manager):\n",
        "resposta": "with open('arquivo.txt', 'r', encoding='utf-8') as a:"
    },
    {
        "pergunta": "Como ler o conteúdo completo de um arquivo:\n",
        "resposta": "b = a.read()"
    },
    {
        "pergunta": "Como ler todas as linhas de um arquivo:\n",
        "resposta": "b = a.readlines()"
    },
    
    # Arquivos CSV
    {
        "pergunta": "Como abrir um arquivo CSV para escrita:\n",
        "resposta": "with open('arquivo.csv', 'w', newline='') as a:"
    },
    {
        "pergunta": "Como criar um escritor CSV:\n",
        "resposta": "b = csv.writer(a)"
    },
    {
        "pergunta": "Como escrever uma linha em um arquivo CSV:\n",
        "resposta": "b.writerow([])"
    },
    {
        "pergunta": "Como abrir um arquivo CSV para leitura:\n",
        "resposta": "with open('arquivo.csv', 'r') as a:"
    },
    {
        "pergunta": "Como criar um leitor CSV:\n",
        "resposta": "b = csv.reader(a)"
    },
    
    # Arquivos JSON
    {
        "pergunta": "Como abrir um arquivo JSON para escrita:\n",
        "resposta": "with open('arquivo.json', 'w') as a:"
    },
    {
        "pergunta": "Como salvar um dicionário em um arquivo JSON:\n",
        "resposta": "json.dump(b, a, indent=4)"
    },
    {
        "pergunta": "Como abrir um arquivo JSON para leitura:\n",
        "resposta": "with open('arquivo.json', 'r') as a:"
    },
    {
        "pergunta": "Como carregar dados de um arquivo JSON:\n",
        "resposta": "c = json.load(a)"
    },

    #Extra
    {
        "pergunta": "Criar pasta:\n",
        "resposta": "os.makedirs('pasta', exist_ok=True)"
    },
    {
        "pergunta": "Criar arquivo dentro duma pasta (caminho):\n",
        "resposta": "caminho = os.path.join('pasta','exercicio.py')
    },
    {
        "pergunta": "Abrir um arquivo utilizando micro (caminho):\n",
        "resposta": "subprocess.run(['micro', 'caminho'])
    },
    
    # Tratamento de erros
    {
        "pergunta": "Estrutura básica para tratamento de erros:\n",
        "resposta": "try-except"
    },
    {
        "pergunta": "Como capturar erro de arquivo não encontrado:\n",
        "resposta": "except FileNotFoundError:"
    },
    {
        "pergunta": "Como capturar erro de permissão:\n",
        "resposta": "except PermissionError:"
    },
    {
        "pergunta": "Como capturar erro de valor:\n",
        "resposta": "except ValueError:"
    },
    {
        "pergunta": "Como capturar erro de divisão por zero:\n",
        "resposta": "except ZeroDivisionError:"
    },
    {
        "pergunta": "Como capturar qualquer exceção:\n",
        "resposta": "except Exception as a:"
    },
    {
        "pergunta": "Bloco que sempre é executado, independente de erro:\n",
        "resposta": "finally:"
    },
    {
        "pergunta": "Como criar uma exceção personalizada para saldo insuficiente:\n",
        "resposta": "class SaldoInsuficienteError(Exception):"
    },
    {
        "pergunta": "Como levantar uma exceção personalizada:\n",
        "resposta": "raise SaldoInsuficienteError('Saldo insuficiente')"
    },
    {
        "pergunta": "Como capturar uma exceção personalizada:\n",
        "resposta": "except SaldoInsuficienteError as a:"
    },
    
    # Programação Orientada a Objetos
    {
        "pergunta": "Como criar uma classe Carro:\n",
        "resposta": "class Carro:"
    },
    {
        "pergunta": "Como criar o método construtor com parâmetros marca e modelo:\n",
        "resposta": "def __init__(self, marca, modelo):"
    },
    {
        "pergunta": "Como atribuir valores a atributos de instância:\n",
        "resposta": "self.marca = marca"
    },
    {
        "pergunta": "Como criar um método de instância para acelerar:\n",
        "resposta": "def acelerar(self, valor):"
    },
    {
        "pergunta": "Como modificar um atributo de instância:\n",
        "resposta": "self.velocidade += valor"
    },
    {
        "pergunta": "Como criar um objeto da classe Carro:\n",
        "resposta": "meu_carro = Carro('marca', 'modelo')"
    },
    {
        "pergunta": "Como chamar um método de um objeto:\n",
        "resposta": "meu_carro.acelerar(20)"
    },
    {
        "pergunta": "Como criar um atributo privado:\n",
        "resposta": "self.__saldo = 0"
    },
    {
        "pergunta": "Decorador para definir uma propriedade:\n",
        "resposta": "@property"
    }
]



# adicionar os exercícios e respostas
for i in range(len(questoes)):
    if i < len(exercicio.ex):
        questoes[i]['exer'] = exercicio.ex[i]['exer']
        questoes[i]['resp'] = exercicio.ex[i]['resp']

        
