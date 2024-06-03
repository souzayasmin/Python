import time

# Encontrar o maior valor na lista - Exemplo 1
lista = [17, 3, 11, 5, 1 , 9, 7, 15, 18]
maiornumero = lista[0] # recebeu o número 17

for i in range(1, len(lista)):
    if lista[i] > maiornumero:
        maiornumero = lista[i]
print("")
print('maoir número: ', maiornumero)
print("")

# Exemplo 2
mylist = [14, 4, 11, 5, 6 , 9, 7, 19, 12, 999999]
maior = mylist[0]
for i in mylist:
    if i > maior:
            maior = i
print('maior da lista 2: ', maior)
print("")

# Exemplo 3
ultimalista = mylist[:]
mel = ultimalista[0]
for i in ultimalista[1:]:
    if i > mel:
        mel = i
print("maior valor da 3: ", mel)
print("")

# Encontrar a localização de um determinado elemento dentro de uma lista
frutas = ['abacaxi', 'maça', 'pera', 'mamao', 'uva', 'melancia']
elemento = 'melancia'
achado = False

for i in range(len(frutas)):
    achado = frutas[i] == elemento
    if achado == True:
        break

if achado == True: 
    print('elemento encontrado no indice: ', i)
else:
    print('não encontrado')
print("")

#Conferir de aposta em loteria
sorteados = [5, 11, 9, 42, 3, 49]
apostados = [3, 7, 11, 42, 34, 49]
acertos = 0

for numero in sorteados:
    if numero in apostados:
        acertos += i
print(acertos)

#Remoçao de numeros repetidos em uma lista
lista = [1, 2, 4, 4, 1, 2, 6, 2, 9]
print("Lista original:", lista)

#lista de apoio
vistos = []

#interar pela lista original de trás pra frente
for i in range(len(lista) - 1, -1, -1):
    #se o número já está da lista "vistos", removê-lo da lista original
    if lista[i] in vistos:
        del lista[i]
    else:
        #caso contrário, adicionar à lista "vistos"
        vistos.append(lista[i])
#exibir a lista original modificada
print("Lista modificada:", lista)

time.sleep(1)