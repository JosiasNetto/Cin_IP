#Declaração de variaveis utilizadas no loop
opiniao = ""
musicas_escutadas = 0
minutos_escutados = 0

#Loop musicas e contagem de minutos dependendo da opnião
while musicas_escutadas < 21 and opiniao != "parei":
    opiniao = input()
    if opiniao == "amei":
        minutos_escutados += 4
    
    elif opiniao == "não parei de ouvir":
        while opiniao != "pulei":
            opiniao = input()
            minutos_escutados += 4
        minutos_escutados -= 4
    
    elif opiniao == "essa não deu":
        minutos_escutados += 0
    
    elif opiniao == "escutei só metade":
        minutos_escutados += 2
    
    if opiniao != "parei":
        musicas_escutadas += 1

#Imprimindo o resultado quando o loop for parado
print(f"Você ouviu {minutos_escutados} minutos hoje!!!")