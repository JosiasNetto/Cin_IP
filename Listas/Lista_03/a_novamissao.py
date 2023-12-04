#Princpais Variaveis do codigo
##Recebendo nome da missão
nome_missao = input()
nome_herois = []

nome_heroi = input()
#Loop para receber o nome de cada heroi que ira na missão
while nome_heroi != "Grupo formado":
    nome_herois.append(nome_heroi)
    nome_heroi = input()

#Printando o nome da cada heroi, um por vez
print(f"O grupo formado por {len(nome_herois)} heróis para a missão {nome_missao} foi:")
for num_heroi in range(len(nome_herois)):
    print(f"- {nome_herois[num_heroi]}")