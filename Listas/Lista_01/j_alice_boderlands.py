#Variaveis de apoio para o codigo
acertou_todas = True
vivo = True
pontos = int(0)
#Variaveis para dizer no final se acertou ou nao
acertou1 = str()    
acertou2 = str()
acertou3 = str()
acertou4 = str()
acertou5 = str()

#Recebendo as caracteristicas da primeira porta, calculando se acerta ou não(dependendo do número) e modificando a pontuação
direcao_escolhida = (input())
numero = int(input())

if (numero % 2 == 0 and direcao_escolhida == "esquerda") or (numero % 2 == 1 and direcao_escolhida == "direita"):
        pontos += 150
        acertou1 = "CERTA"
else:
    pontos -= 150
    acertou1 = "ERRADA"
    acertou_todas = False

#Segunda Porta
direcao_escolhida = input()
cor = input()
planta = input()
macaneta = input()

if (((cor == "dourada" or cor == "prateada") or ((planta == "avenca" or planta == "espadinha") and macaneta == "redonda")) and direcao_escolhida == "direita") or (not ((cor == "dourada" or cor == "prateada") or ((planta == "avenca" or planta == "espadinha") and macaneta == "redonda")) and direcao_escolhida == "esquerda"):
    pontos += 200
    acertou2 = "CERTA"
   
else:
    pontos -= 200
    acertou2 = "ERRADA"
    acertou_todas = False

#Terceira Porta
direcao_escolhida = input()
cor = input()
numero = int(input())
planta = input()
macaneta = input()

if (((numero % 5 == 0 and planta == "espadinha" and macaneta == "quadrada") or cor == "perolada") and direcao_escolhida == "esquerda") or (not (numero % 5 == 0 and planta == "espadinha" and macaneta == "quadrada") and direcao_escolhida == "direita"):
    pontos += 250
    acertou3 = "CERTA"

else:
    pontos -= 250
    acertou3 = "ERRADA"
    acertou_todas = False

#Quarta Porta
direcao_escolhida = input()
numero = int(input())

if ((numero % 3 == 0) and not(numero % 5 == 0 and numero % 2 == 0) and direcao_escolhida == "direita") or (not((numero % 3 == 0) and not(numero % 5 == 0 and numero % 2 == 0)) and direcao_escolhida == "esquerda"):
    pontos += 300
    acertou4 = "CERTA"
    
else:
    pontos -= 300
    acertou4 = "ERRADA"
    acertou_todas = False

#Quinta Porta
cor = input()
numero = int(input())
planta = input()
flor = input()
macaneta = input()

if flor == "acobreada" and (numero % 2 != 0 or (macaneta == "triangular" or macaneta == "quadrada")) and planta == "jiboia":
    pontos += 500
    acertou5 = "CERTA"

elif cor == "prateada" and (not (flor == "margarida" or flor == "papoula" or flor == "cosmos")) and (macaneta == "hexagonal" or macaneta == "redonda"):
    pontos += 450
    acertou5 = "CERTA"

elif cor == "dourada" and (flor == "lirio" or flor == "ixora") and macaneta == "hexagonal":
    pontos += 400
    acertou5 = "CERTA"

else:
    pontos -= 500
    acertou5 = "ERRADA"
    acertou_todas = False

#Imprimindo Se ta vivo e sequencia certa
print("ARISU, VOCÊ FEZ SUAS ESCOLHAS E AGORA VEREMOS SE ESCOLHEU AS PORTAS CERTAS:")

print(f"{acertou1} {acertou2} {acertou3} {acertou4} {acertou5}")

if pontos >= 0:
    if acertou_todas:
        print(f"Parece que a sorte está ao seu favor, Arisu... Você conseguiu passar com {pontos} pontos!")
    else:
        print(f"Você passou com {pontos} pontos, mas faça melhores escolhas da próxima vez.")

else:
    if pontos > -1400:
        print(f"Por mais que você tenha feito escolhas corretas, não foi suficiente para sobreviver. Você finalizou o jogo com {pontos} pontos")
    else:
        print(f"Todas suas escolhas foram erradas, Arisu, esperávamos mais de você... Você será executado pois obteve {pontos} pontos.")