#Sistema de criação de personagem
from random import randint

#Função para rolar D6, especifica neste arquivo
def rolarD6(qnt):
    i = 0
    totalD6 = 0
    while i < qnt:
        valorD6 = randint(1, 6)
        totalD6 = valorD6 + totalD6
        i = i + 1
    return totalD6

personagem = {}

#Função para criação de personagens
def criaPersonagem():
    nome = input("Qual o nome do personagem? ")
    raca = selecionaRaca()
    classe = selecionaClasse()
    habilidades = criaHabilidades(raca)
    personagem = {
        "nome": nome,
        "raca": raca,
        "classe": classe,
        "habilidades": habilidades
    }
    return personagem

#Função para salvar personagem em arquivo txt e limpar seleção
def limpaSelecao(personagem):
    with open(personagem["nome"] + ".txt", "w", encoding="utf-8") as file:
        file.write(str("Nome: ") + personagem["nome"] + "\n")
        file.write(str("Raça: ") + personagem["raca"] + "\n")
        file.write(str("Classe: ") + personagem["classe"] + "\n")
        file.write(str("Força: ") + str(personagem["habilidades"]["força"]) + "\n")
        file.write(str("Destreza: ") + str(personagem["habilidades"]["destreza"]) + "\n")
        file.write(str("Resistência: ") + str(personagem["habilidades"]["resistência"]) + "\n")
        file.write(str("Inteligência: ") + str(personagem["habilidades"]["inteligência"]) + "\n")
        file.write(str("Magia: ") + str(personagem["habilidades"]["magia"]) + "\n")
    print("Personagem salvo com sucesso!")

#Função para seleção de raça
def selecionaRaca():
    print("Raças disponíveis: ")
    print("1 - Humano, vantagem: +1 em todas as habilidades")
    print("2 - Elfo, vantagem: +2 em destreza e inteligência")
    print("3 - Anão, vantagem: +2 em força e resistência")
    print("4 - Orc, vantagem: +2 em força e resistência")
    print("5 - Goblin, vantagem: +2 em destreza e inteligência")
    print("6 - Troll, vantagem: +2 em força e resistência")
    print("7 - Dragão, vantagem: +2 em todas as habilidades")
    print("8 - Fada, vantagem: +2 em destreza e magia")
    raca = input("Qual a raça do personagem desejada? ")
    
    #If else para return da criação de personagem
    #To lower para padronizar a entrada do usuário
    if raca.lower() == "humano":
        return "Humano"
    elif raca.lower() == "elfo":
        return "Elfo"
    elif raca.lower() == "anão" or raca.lower() == "anao":
        return "Anão"
    elif raca.lower() == "orc":
        return "Orc"
    elif raca.lower() == "goblin":
        return "Goblin"
    elif raca.lower() == "troll":
        return "Troll"
    elif raca.lower() == "dragão" or raca.lower() == "dragao":
        return "Dragão"
    elif raca.lower() == "fada":
        return "Fada"
    else:
        print("Raça inválida, tente novamente.")
        return selecionaRaca()
 
#Função para seleção de classe        
def selecionaClasse():
    print("Classes disponiveis: ")
    print("1 - Guerreiro, vantagem: +2 em força e resistência")
    print("2 - Mago, vantagem: +2 em inteligência e magia")
    print("3 - Ladino, vantagem: +2 em destreza e inteligência")
    print("4 - Clérigo, vantagem: +2 em resistência e magia")
    print("5 - Bárbaro, vantagem: +2 em força e resistência")
    print("6 - Paladino, vantagem: +2 em resistência e magia")
    print("7 - Bardo, vantagem: +2 em destreza e inteligência")
    print("8 - Druida, vantagem: +2 em resistência e magia")
    classe = input("Qual a classe do personagem desejada? ")
    
    #If else para return da criação de personagem
    #To lower para padronizar a entrada do usuário
    if classe.lower() == "guerreiro":
        return "Guerreiro"
    elif classe.lower() == "mago":
        return "Mago"
    elif classe.lower() == "ladino":
        return "Ladino"
    elif classe.lower() == "clérigo" or classe.lower() == "clerigo":
        return "Clérigo"
    elif classe.lower() == "bárbaro" or classe.lower() == "barbaro":
        return "Bárbaro"
    elif classe.lower() == "paladino":
        return "Paladino"
    elif classe.lower() == "bardo":
        return "Bardo"
    elif classe.lower() == "druida":
        return "Druida"
    else:
        print("Classe inválida, tente novamente.")
        return selecionaClasse()
    
#Função para criação de habilidades
def criaHabilidades(raca):
    habilidades = {
        "força": rolarD6(3),
        "destreza": rolarD6(3),
        "resistência": rolarD6(3),
        "inteligência": rolarD6(3),
        "magia": rolarD6(3)
    }
    
    # Aplicar modificadores de raça
    if raca == "Humano":
        for habilidade in habilidades:
            habilidades[habilidade] += 1
    elif raca == "Elfo" or raca == "Goblin":
        habilidades["destreza"] += 2
        habilidades["inteligência"] += 2
    elif raca == "Anão" or raca == "Orc" or raca == "Troll":
        habilidades["força"] += 2
        habilidades["resistência"] += 2
    elif raca == "Dragão":
        for habilidade in habilidades:
            habilidades[habilidade] += 2
    elif raca == "Fada":
        habilidades["destreza"] += 2
        habilidades["magia"] += 2
    
    return habilidades

#Função para exibição de personagem
def exibePersonagem(personagem):
    print("Nome: " + personagem["nome"])
    print("Raça: " + personagem["raca"])
    print("Classe: " + personagem["classe"])
    print("Habilidades: ")
    print("Força: " + str(personagem["habilidades"]["força"]))
    print("Destreza: " + str(personagem["habilidades"]["destreza"]))
    print("Resistência: " + str(personagem["habilidades"]["resistência"]))
    print("Inteligência: " + str(personagem["habilidades"]["inteligência"]))
    print("Magia: " + str(personagem["habilidades"]["magia"]))


personagem = criaPersonagem()
limpaSelecao(personagem)
exibePersonagem(personagem)
