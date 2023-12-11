#Variaveis de auxilio
num_campistas_chale_andar = []
chale_mais_semideuses = 0
num_semideuses_maior_chale = 0
num_semideuses_chale = 0

#Recebendo numero de chale e andares
num_chales = int(input())
andares_chales = int(input())

#Loop que passa pelo numero de chales
for chale in range(num_chales):
    #Adciona uma lista vazia a lista principal, para conseguir realizar o append especifico depois
    num_campistas_chale_andar.append([])
    num_semideuses_chale = 0

    #Loop que passa pela quantidade de andares do chale
    for campistas in range(andares_chales):
        #Adciona o numero de campistas na matriz, especificamente na lista do chale em seu andar
        num_campistas_chale_andar[chale].append(int(input()))
        num_semideuses_chale += num_campistas_chale_andar[chale][campistas]

    #Verifica se o numero total de semideuses nesse chale, é o maior de todos    
    if num_semideuses_chale > num_semideuses_maior_chale:
        num_semideuses_maior_chale = num_semideuses_chale
        chale_mais_semideuses = chale + 1

#Loop que passa por cada elemento da matriz chaleXandar e printa o numero de alunos de cada um
for i in range(len(num_campistas_chale_andar)):
    for j in range(andares_chales):
        print(num_campistas_chale_andar[i][j],end=(''))
        #Verificando se é o ultimo elemento para dar espaço entre os números
        if j < (andares_chales - 1):
            print(' ',end='')
    print()

#Printa o chale com mais semideuses
print('')
print(f'O chalé {chale_mais_semideuses} foi o que mais recebeu semi-deuses, tendo um acréscimo de {num_semideuses_maior_chale} novos campistas!')

