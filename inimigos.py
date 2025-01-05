#Sistema de criação de inimigos

from personagem import selecionaRaca, selecionaClasse, criaHabilidades

inimigo = {}

def criaInimigo():
    inimigo = {
        "nome": input("Digite o nome do inimigo: "),
        "raca": selecionaRaca(),
        "classe": selecionaClasse(),
        "habilidades": criaHabilidades(raca)
    }
    return inimigo

def exibeInimigo(inimigo):
    print("Nome: " + inimigo["nome"])
    print("Raça: " + inimigo["raca"])
    print("Classe: " + inimigo["classe"])
    print("Habilidades: ")
    print("Força: " + str(inimigo["habilidades"]["força"]))
    print("Destreza: " + str(inimigo["habilidades"]["destreza"]))
    print("Resistência: " + str(inimigo["habilidades"]["resistência"]))
    print("Inteligência: " + str(inimigo["habilidades"]["inteligência"]))
    print("Magia: " + str(inimigo["habilidades"]["magia"]))
    
def salvarInimigo(inimigo):
    with open("inimigos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(inimigo["nome"] + "\n")
        arquivo.write(inimigo["raca"] + "\n")
        arquivo.write(inimigo["classe"] + "\n")
        arquivo.write(str(inimigo["habilidades"]["força"]) + "\n")
        arquivo.write(str(inimigo["habilidades"]["destreza"]) + "\n")
        arquivo.write(str(inimigo["habilidades"]["resistência"]) + "\n")
        arquivo.write(str(inimigo["habilidades"]["inteligência"]) + "\n")
        arquivo.write(str(inimigo["habilidades"]["magia"]) + "\n")
        arquivo.write("\n")
        
criaInimigo()
exibeInimigo(inimigo)
salvarInimigo(inimigo)
