import time 

#Biblioteca para retorna um numero inteiro aleatorio 
from random import randint as rd
sorteado = rd(-100, 100) #Sorteia um numero de -100 a 100

#Criando uma lista de numeros inteiros aleatorios 
lista = [rd(1,6) for i in range(1,11)]
lista2 = [x for x in range(1, 11)]
lista3 = ["Rolo compressor!!!" for f in range(1, 3)]
# print(lista)
# print(lista2)
# print(lista3)

#Criando lista par 
par = [i for i in range(10) if i%2 == 0]
# print(par)

#Povoando uma lista com "input"
listaUsuario = [input("Digite um numero:") for i in range(5)]
# print(listaUsuario)

#Ultilizando o metodo split (cda palavra se torna um elemento da lista)
nome = "Mickey Mouse"
print(nome)
print(nome.split())
print(nome)

#Aplicando o "split" com o input
notas = [n for n in input("Notas: ").split()]
print(notas)

# notas2 = [float(n) for n in input("notas:").split("")]
# print(notas2)

listaMista = [17, 70.5, "Sem Mundial", True]
# print(listaMista)

#Manipulação / Fatiamento de Listas
veiculos1 = ["carro", "bicicleta", "motor"]
print("veiculos 1:", veiculos1)

#Copiando todo o conteudo de uma lista para outra
veiculos2 = veiculos1[:]
del veiculos1[2]
print("veiculos 1:", veiculos1)
print("veiculos 2:", veiculos2)

#Copiando parte do conteudo de uma lista 
veiculos3 = veiculos2[0:1]
print(veiculos3)

#Copiando parte do conteudo, incluindo o ultimo elemento
veiculos4 = veiculos2[1:-1]
print(veiculos4)

veiculos5 = veiculos2[-1:1]
print(veiculos5)

#Outras maneira de fatiamento (omissaodo start ou do end)
my_list = ["A", "B", "C", "D", "E", "F"]
print(my_list)
new_list = my_list[:3]
print(new_list)
new_lis_fim = my_list[5:]
print(new_lis_fim_fim)

#Apagamento conteudo de listas 
del my_list[1:3]
print(my_list)
del my_list[:] #apaga todo o conteudo 
print(my_list)

del my_list
print(my_list)

#Testando  se alguns itens existem em uma lista ou nao
#Para isso,usamos palavras chave in e not in:
naosei = ["A", "B", 18, 15]
print("A" in naosei)
print("C" not in naosei)
print(15 not in naosei)

time.sleep(3)