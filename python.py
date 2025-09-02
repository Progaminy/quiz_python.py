
import os
import subprocess
import random
import questionario as q
import exercicio as exe

def main():

    #random.shuffle(q.questoes)
    
    arquivo = "exemplo.py"

    contagem =1
    

    for a in q.questoes:
        while True:
            resposta_user = input(f"{contagem}. {a['pergunta']}")
            certeza = input("tem certeza: ")
            if certeza.lower() in ["s"]:
                if resposta_user == a['resposta']:
                    print("acertou...")
                    contagem += 1
                    
                    r = input(" quer treinar? ")
                    if r.lower() in ["sim", "s", "yes", "y"]:

                        try:
                            # Criar aquivo
                            with open(arquivo, "w") as f:
                                f.write(f"# {a['pergunta']}\n")
                                f.write(f"# Resposta correta: \n{a['resposta']}\n\n")
                                f.write("# Escreva seu código de treino abaixo:\n")
                                f.write("# --------------------------------\n\n")
                    
                            # ABRIR O ARQUIVO NO MICRO EDITOR
                            print("Abrindo arquivo no micro editor...")
                            subprocess.run(["micro", arquivo])

                        #tratar erro o aquivo nao ser encontrado   
                        except FileNotFoundError:
                            print("Micro editor não encontrado!")
                            print(" Instalando micro editor...")
                            subprocess.run(["pkg", "install", "micro", "-y"])
                            print("Micro instalado! Abrindo arquivo...")
                            subprocess.run(["micro", arquivo])

                        #tratar outros erros 
                        except Exception as e:
                            print(f"Erro ao abrir arquivo: {e}")
                            print("Caminho do arquivo:", os.path.abspath(arquivo))
                    break
                
            else:
                print(f"errou, a resposta seria:\n{a['resposta']}")

if __name__=="__main__":
    main()

