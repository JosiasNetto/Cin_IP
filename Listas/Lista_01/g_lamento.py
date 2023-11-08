#Lendo os números e verificando se são positivos
n1 = int(input())
if n1 < 0:
    print(f"{n1:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
    exit()
n2 = int(input())
if n2 < 0:
    print(f"{n2:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
    exit()
n3= int(input())
if n3 < 0:
    print(f"{n3:.2f} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
    exit()

#Recebendo a palavra e verificando se todas as letras são minusculas
palavra = input()
if not palavra.islower():
    print(f"{palavra} não está gravado(a) na caixa, não adianta nem continuar que ela não vai abrir.")
    exit()

#aleatorio
n5 = int(input())


#Cálculo par ou impar
#Número 1
if n1 % 2 == 0:
    n1 *= 2

else:
    n1 /= 2
#Número 2
if n2 % 2 == 0:
    n2 *= 2

else:
    n2 /= 2
#Número 3
if n3 % 2 == 0:
    n3 *= 2

else:
    n3 /= 2

#Calculo Número Final
numero_final = (n5*n1*n2*n3) ** (1/2)

#Impressão se número final for maior que 10
if numero_final >= 10:
    print(f"O número {numero_final:.2f} e a palavra {palavra} eram as respostas. A caixa foi aberta.")

else:
    numero_final -= 10
    print(f"A combinação era muito pequena, a caixa só vai poder ser aberta daqui a {numero_final:.2f} anos.")
