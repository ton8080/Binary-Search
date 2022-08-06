import random

tupla = ("Joao", "Maria", "Pedro", "Rafael", "Paulo", "Priscila", "Jessica", "Virgilio", "Manuela", "Camila")

#função busca linear, percorre a tupla comparando os valores
def linearSearch(alist, item):
    tentativa = 0
    for i in range(len(alist)): 
        tentativa = tentativa + 1
        if alist[i] == item: #se o valor do indice for igual ao nome procurado ele printa o nome e para
            print("Busca Linear")
            print("acerto na tentativa", tentativa, "O nome é ", alist[i])
            break

#função busca linear, percorre a tupla comparando os valores
def linearSearchNum(alist, item):
    tentativa = 0
    for i in alist: 
        tentativa = tentativa + 1
        if  i == item : #se o valor do indice for igual ao nome procurado ele printa o nome e para
            print("Busca Linear")
            print("acerto na tentativa", tentativa, "O número é ", i)
            break



#função de buscabinaria, usa o algoritimo de busca binária para localizar um nome na tupla
def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    tentativa = 1

    while first<=last: #enquanto o começo for menor ou igual ao tamanho da tupla -1(para igualar com os valores dos indices)
        midpoint = (first + last)//2 #Recebe o meio da tupla, retorna uma divisão inteira(para poder comparar os indices)

        if alist[midpoint] == item: #Se o meio da tupla for o item procurado, printa e encerra
            print("Busca binária")
            print("acerto na tentativa", tentativa, "o nome encontrado foi", alist[midpoint])
            break

        elif alist.index(item) < midpoint: #caso o indice do nome testado for menor que o midpoint(meio da tupla atual)
            #o algoritimo descarta, a partir do midpoint, todos os itens a esquerda
            last = midpoint-1 
            tentativa = tentativa + 1
        elif alist.index(item) > midpoint: #caso o indice do nome testado for maior que o midpoint(meio da tupla atual)
            first = midpoint+1 #o algoritimo descarta, a partir do midpoint, todos os itens a direita
            tentativa = tentativa + 1
        else:
            return None 
	
    #função de buscabinaria, usa o algoritimo de busca binária para localizar um número na lista
def binarySearchNum(alist, item):
    first = 0
    last = len(alist)-1
    tentativa = 1

    while first<=last: 
        midpoint = (first + last)//2 

        if alist[midpoint] == item: 
            print("Busca binária")
            print("acerto na tentativa", tentativa, "o nome encontrado foi", alist[midpoint])
            break

        elif item < alist[midpoint]: 
            last = midpoint-1 
            tentativa = tentativa + 1
        elif item > alist[midpoint]: 
            first = midpoint+1 
            tentativa = tentativa + 1
        else:
            return None 


def criarLista(quant):
    numeros = []
    for i in range(0,quant):
        numeros.append(random.randint(1,100))
    return sorted(numeros)


print("============BEM VINDO==============")
print("Esse programa mostra a diferença entre os algoritimos de Busca linear e Busca binária.\n")
print("É possível testá-los com uma lista de nomes pré-definidos ou com uma lista de números aleatórios ")
print("em que você decide o tamanho!")
print("==================================================================================")

while True:
    print("1) Testar os algoritimos com nomes")
    print("2) Testar os algoritimos com números")
    print("3) Sair")
    escolha = int(input("Sua escolha: "))


    if(escolha == 1):
        print(tupla)
        nome = input("Digite o nome a ser encontrado: na tupla: ")
        while (nome not in tupla):
            nome = input("Digite um nome que pertence a tupla: ")

        binarySearch(tupla, nome)
        linearSearch(tupla, nome)
        



    elif(escolha == 2):
        quantidade = int(input("Quantos números você quer gerar? "))
        numeros = criarLista(quantidade)
        print(numeros)

        num = 0
        while (num not in numeros):
            num = int(input("Digite um número que pertence a lista: "))

        linearSearchNum(numeros, num)
        binarySearchNum(numeros, num)
    elif(escolha == 3):
        break
    else:
        print("Digite um número valido")
        


