#Variaveis de apoio para o codigo
acertou_todas = True
vivo = True
pontos = int(0)

#Recebendo as caracteristicas da primeira porta, calculando se acerta ou não(dependendo do número) e modificando a pontuação
direcao_escolhida = (input())
numero = int(input())

if (numero % 2 == 0 and direcao_escolhida == "esquerda") or (numero % 2 == 1 and direcao_escolhida == "direita"):
        pontos += 150
else:
    pontos -= 150

#Segunda Porta
direcao_escolhida = input()
cor = input()
planta = input()
macaneta = input()

if ((cor == "dourada" or cor == "prateada") or ((planta == "avenca" or planta == "espadinha") and macaneta == "redonda")) and direcao_escolhida == "direita":
    pontos += 150
elif not ((cor == "dourada" or cor == "prateada") or ((planta == "avenca" or planta == "espadinha") and macaneta == "redonda")) and direcao_escolhida == "esquerda":
    pontos += 250

else:
    pontos -= 250

#Terceira Porta
direcao_escolhida = input()
cor = input()
numero = int(input())
planta = input()
macaneta = input()

if (numero % 5 == 0 and planta == "espadinha" and macaneta == "quadrada") and direcao_escolhida == "esquerda":
    pontos += 250
elif not (numero % 5 == 0 and planta == "espadinha" and macaneta == "quadrada") and direcao_escolhida == "direita":
    pontos += 250
else:
    pontos -= 250

#Quarta Porta
direcao_escolhida = input()
numero = int(input())

if (numero % 3 == 0) and not(numero % 5 == 0 and numero % 2 == 0) and direcao_escolhida == "direita":
    pontos += 300
elif  not((numero % 3 == 0) and not(numero % 5 == 0 and numero % 2 == 0)) and direcao_escolhida == "esquerda":
    pontos += 300
else:
    pontos -= 300

#Quinta Porta
cor = input()
numero = int(input())
planta = input()
flor = input()
macaneta = input()

if flor == "acobreada" and (numero % 2 != 0 or (macaneta == "triangular" or macaneta == "quadrada")) and planta == "jiboia":
    pontos += 500

elif cor == "prateada" and (not (flor == "margarida" or flor == "papoula" or flor == "cosmos")) and (macaneta == "hexagonal" or macaneta == "redonda"):
    pontos += 450

elif cor == "dourada" and (flor == "lirio" or flor == "ixora") and macaneta == "hexagonal":
    pontos += 400

else:
    pontos -= 500

#Imprimindo Se ta vivo e sequencia certa
print("ARISU, VOCÊ FEZ SUAS ESCOLHAS E AGORA VEREMOS SE ESCOLHEU AS PORTAS CERTAS")
