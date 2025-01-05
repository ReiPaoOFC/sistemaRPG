#Sistema de rolagem de dados
from random import *
from PIL import Image
import time

#Temporizador 
tempoInicio = time.time()

#Funções para "criar" os dados, variável qnt represente o número de dados para rolar
def rolarD20(qnt):
    i = 0
    #Cria variável temporaria para armazenar o valor aleatório do "dado"
    valorD20Temp = 0
    while i < qnt: 
        valorD20 = randint(1, 20)
        print(f"{i + 1}° dado rolou o valor: {valorD20}")
        i = i + 1
        #Comparativo de valores para armazenar o maor valor, entre o aleatório ou a variável temporária
        if valorD20 > valorD20Temp:
            valorD20Temp = valorD20
        elif valorD20 <= valorD20Temp:
            continue
        else:
            print("Erro")
        
    print("Maior valor rolado para D20 foi:", valorD20Temp)
    #Caso o valor da variável temporária seja 20 ou 1 irá abrir uma imagem do valor do dado
    if valorD20Temp == 20 or valorD20Temp == 1:
        img = Image.open(f'C:/seu/diretorio/para/a/imagem/{valorD20Temp}.png')
        img.show()
          
def rolarD4(qnt):
    i = 0
    totalD4 = 0
    while i < qnt:
        valorD4 = randint(1, 4)
        #print(f"{i + 1}° dado rolou o valor: {valorD4}")
        totalD4 = valorD4 + totalD4
        i = i + 1
    print(f"O valor total da soma dos D4s foi: {totalD4}")
    #print(f"E a média foi: {totalD4 / qnt}")
    
def rolarD6(qnt):
    i = 0
    totalD6 = 0
    while i < qnt:
        valorD6 = randint(1, 6)
        #print(f"{i + 1}° dado rolou o valor: {valorD6}")
        totalD6 = valorD6 + totalD6
        i = i + 1
    print(f"O valor total da soma dos D6s foi: {totalD6}")
    #print(f"E a média foi: {totalD6 / qnt}")

def rolarD8(qnt):
    i = 0
    totalD8 = 0
    while i < qnt:
        valorD8 = randint(1, 8)
        #print(f"{i + 1}° dado rolou o valor: {valorD8}")
        totalD8 = valorD8 + totalD8
        i = i + 1
    print(f"O valor total da soma dos D6s foi: {totalD8}")
    #print(f"E a média foi: {totalD8 / qnt}")
    
    
def rolarD12(qnt):
    i = 0
    totalD12 = 0
    while i < qnt:
        valorD12 = randint(1, 12)
        #print(f"{i + 1}° dado rolou o valor: {valorD12}")
        totalD12 = valorD12 + totalD12
        i = i + 1
    print(f"O valor total da soma dos D10s foi: {totalD12}")
    #print(f"E a média foi: {totalD12 / qnt}")
    
def rolarD10(qnt):
    i = 0
    totalD10 = 0
    while i < qnt:
        valorD10 = randint(1, 10)
        #print(f"{i + 1}° dado rolou o valor: {valorD10}")
        totalD10 = valorD10 + totalD10
        i = i + 1
    print(f"O valor total da soma dos D10s foi: {totalD10}")
    #print(f"E a média foi: {totalD10 / qnt}")
    
def rolarD100(qnt):
    i = 0
    totalD100 = 0
    while i < qnt:
        valorD100 = randint(1, 100)
        #print(f"{i + 1}° dado rolou o valor: {valorD100}")
        totalD100 = totalD100 = valorD100
        i = i + 1
    print(f"O valor total da soma dos D100s foi: {totalD100}")
    #print(f"E a média foi: {totalD100 / qnt}")

#Cria o primeiro menu a aparecer
# def menuInicio():
#     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#     print("|                                      |")
#     print("|                                      |")
#     print("|                                      |")
#     print("|             Bem Vindo ao             |")
#     print("|             Sistema de               |")
#     print("|             Rolagem de Dado          |")
#     print("|                                      |")
#     print("|                                      |")
#     print("|                                      |")
#     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
 
# Menu que demonstra os possíveis dados para rolar, após cria um sleep de 5 segundos para mostrar como deve ser digitado as opções
# def menuOpcao():
#     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#     print("|               Opções para rolar               |")
#     print("|                                               |")
#     print("|                    D4                         |")
#     print("|                    D6                         |")
#     print("|                    D8                         |")
#     print("|                    D10                        |")
#     print("|                    D12                        |")
#     print("|                    D20                        |")
#     print("|                    D100                       |")
#     print("|                                               |")
#     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
#     time.sleep(5)
#     print("Digite a opção desejada das seguintes maneiras: \n"
#       "D4 ou d4\n"
#       "D6 ou d6\n"
#       "D8 ou d8\n"
#       "D10 ou d10\n"
#       "D12 ou d12\n"
#       "D20 ou d20\n"
#       "D100 ou d100\n"
#       "Sair ou sair")

#    menuInicio()
#
#    #Boolen para detectar a saída do programa
#    boolSaida = False
#    while boolSaida != True:
#        menuOpcao()
#        time.sleep(2)
#        #Opção de dado que o usuário deseja rolar
#        respostaDado = input("Deseje o dado desejado para rolar: ")
#        time.sleep(2)
#        #Quantidade de dados que o usuário deseja rolar
#        qntDado = int(input("Digite a quantidade de dados: "))
#
#        #Verifica se a quantidade de dados é válida
#        if qntDado == 0 or qntDado < 0:
#            print("Digite um valor válido!")
#        
#        #Verifica qual dado o usuário deseja rolar
#        if respostaDado.lower() == 'd4':
#            rolarD4(qntDado)
#        elif respostaDado.lower() == 'd6':
#           rolarD6(qntDado)
#        elif respostaDado.lower() == 'd8':
#            rolarD8(qntDado)
#        elif respostaDado.lower() == 'd10':
#            rolarD10(qntDado)
#        elif respostaDado.lower() == 'd12':
#            rolarD12(qntDado)
#       elif respostaDado.lower() == 'd20':
#            rolarD20(qntDado)
#       elif respostaDado.lower() == 'd100':
#            rolarD100(qntDado)
#       elif respostaDado.lower() == 'sair':
#            #Caso o usuário deseje sair do programa
#            print("Saindo do programa...")
#            #Boolen para sair do programa
#            boolSaida = True
#        else:
#            print("Opção inválida!")
#        
#        time.sleep(5)

    #Temporizador
#   tempoFim = time.time()
#    tempoPassado = tempoFim - tempoInicio
#    print(tempoPassado)