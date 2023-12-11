lista_labirinto = []
lista_reliquias = []
achou_reliquia = False

#Loop para receber parte do labirinto, e adcionar como lista, na lista parte do labirinto
parte_labirinto = input()
while parte_labirinto != "Fim do labirinto":
    lista_labirinto.append(parte_labirinto.split(' '))
    parte_labirinto = input()

#Loop passando por cada parte do labirinto
for parte in range(len(lista_labirinto)):
    #Loop passando pelo elemento da lista do labirinto, e vendo se nessa lista possui tesouro
    #Se possuir, adcionara a sua localização a lista de tesouros
    for j in range(len(lista_labirinto[parte])):
        if lista_labirinto[parte][j] == '1':
            lista_reliquias.append(f'linha: {parte}, coluna: {j}')
            achou_reliquia = True

#Se existir tesouro, printara cada eleemento da lista da localização dos tesouros
if achou_reliquia:
    print('Relíquias encontradas nos seguintes locais:')
    for i in range(len(lista_reliquias)):
        print(lista_reliquias[i])

else:
    print("Nenhuma relíquia encontrada no labirinto.")
