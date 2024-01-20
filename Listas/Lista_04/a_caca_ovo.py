#Funcao que diz quantos ovos encontrou no dia
def qtd_ovos_encontrados_dia(num_dia, ovos_escondidos_dia, horoscopo_dia):
    ovo_encontrados = 0

    #Checkando que frase foi dita pelo horoscopo, e calculando a quantidade de ovos encontrados a partir dela
    if horoscopo_dia == ("Os astros estão radiantes hoje! Eles farão o possível para abençoar a todos com boa sorte."):
        ovo_encontrados = ovos_escondidos_dia
    
    elif horoscopo_dia == ("Os astros estão de bom humor hoje. Acho que você terá um pouco de sorte extra."):
        ovo_encontrados = int(ovos_escondidos_dia * 0.7)
    
    elif horoscopo_dia == ("As estrelas estão neutras hoje. O dia está em suas mãos."):
        ovo_encontrados = int(valor_max(x=(ovos_escondidos_dia * 0.7),y=(ovos_escondidos_dia / ((ovos_escondidos_dia % num_dia) + 1))))
    
    elif horoscopo_dia == ("Isso é raro. As estrelas estão absolutamente neutras hoje."):
        ovo_encontrados = int((ovos_escondidos_dia % num_dia) + 1)
        
    #Retornando o numero de ovos encontrados
    return ovo_encontrados
    
#Funcao que calcula o maior numero entre dois
def valor_max(x, y):
    if x > y:
        return x
    
    elif x < y:
        return y

#Recebendo o numero de dias da caca 
qtd_dias = int(input())

#Declarando variaveis de auxilio
total_ovos_encontrados = 0
total_ovos_escondidos = 0

#Loop que passa pela quantidade de dias 
for dia in range(1, qtd_dias + 1):
    #Recebendo a quantidade de ovos e a frase do horoscopo
    ovos_escondidos_dia = int(input())
    horoscopo_dia = input()

    #Calculando a quantidade total de ovos, e recebendo a quantidade do dia baseado na funcao
    total_ovos_escondidos += ovos_escondidos_dia
    ovos_encontrados_dia = qtd_ovos_encontrados_dia(dia, ovos_escondidos_dia,horoscopo_dia)
    total_ovos_encontrados += ovos_encontrados_dia
    
    #Imprimindo o numero de ovos encontrados no dia
    print(f'Dia {dia}')
    print(f'Hoje Carlos encontrou {ovos_encontrados_dia} ovos!!')


#Imprimindo o total de ovos encontrados em relacao aos escondidos
print(f"Kiq encontrou {total_ovos_encontrados} de um total de {total_ovos_escondidos}")

#Calculando aproveitamento
aproveitamento = ((total_ovos_encontrados / total_ovos_escondidos) * 100)

#Verificando o aproveitamento da caca, e imprimindo a frase dependendo 
if aproveitamento == 100:
    print("Incrível! Seu signo está em alta. Você encontrou todos os ovos!")

elif aproveitamento > 66:
    print("Ótimo trabalho! Os astros estão ao seu lado. Você encontrou a maioria dos ovos!")

elif aproveitamento > 33:
    print("Bom esforço! Os astros sorriem para você. Muitos ovos foram encontrados.")

elif aproveitamento > 0:
    print("Continue procurando! Seu horóscopo sugere que há mais ovos a serem encontrados.")

elif aproveitamento == 0:
    print("Ainda não encontrou nenhum ovo. O horóscopo aconselha persistência. Continue tentando!")
