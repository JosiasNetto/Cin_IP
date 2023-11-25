numero_compradores = int(input())
criterios_cambista = 0
numero_cambistas = 0

#Loop para analisar cada comprador e ver se eh cambista
for i in range(numero_compradores):
    #Recebendo informacoes do comprador
    numeros_impares = 0
    criterios_cambista = 0
    nome_comprador = input()
    cpf_comprador = input()
    nome_identidade = input()
    cpf_identidade = input()
    qtd_ingressos = int(input())
    preco_ingressos = float(input())
    codigo_compra = input()

    #Checkagens dos fatoes de cambista, se for verdadeiro, adcionara um ponto
    if nome_comprador != nome_identidade:
        criterios_cambista += 1
    
    if cpf_comprador != cpf_identidade:
        criterios_cambista += 1
    
    if qtd_ingressos > 12:
        criterios_cambista += 1

    if preco_ingressos > 1500:
        criterios_cambista +=1
    
    #Loop para testar quantos numeros impares tem no codigo
    for i in codigo_compra:
        if int(i) % 2 != 0:
            numeros_impares += 1
    
    if numeros_impares >= 7:
        criterios_cambista +=1
    
    #Contagem cambistas
    if criterios_cambista >= 3:
        numero_cambistas += 1

#Imprimindo quantidade de compradores analisados, e numero de possiveis cambistas
print(f"Total de compradores analisados: {numero_compradores}")
print(f"Total de suspeitas de cambistas: {numero_cambistas}")