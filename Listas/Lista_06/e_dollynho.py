def recebendo_status_dolly(dic_dolly):  #Função que recebe os status do dolly, e add no seu dicionario
  dic_dolly['vida'] = int(input())
  dic_dolly['ataque'] = int(input())
  dic_dolly['defesa'] = int(input())

def recebendo_status_barriguinha(qtd_barriguinhas, dic_barriguinhas): #Função que recebe os status dos barriguinhas e add num dics de dics com o nome dos barriguinhas
  dic_aux = {}
  for i in range(qtd_barriguinhas): #Loop que passa pela quantidade de barriguinhas
    nome_barriguinha = input()  #Recebendo o nome
    dic_aux['vida'] = int(input())
    dic_aux['ataque'] = int(input())
    dic_aux['defesa'] = int(input())
    dic_barriguinhas[nome_barriguinha] = dic_aux.copy() #Declarando o nome do barriguinha e seu valor como o dic com as infos

  return

def batalhas_dolly(dic_dolly, dic_barriguinhas):  #Função que simula a batalha 
  #Declarando variaveis de aux
  dolly_vivo = True
  dolly_venceu = False
  kills_dolly = 0

  for barriguinha in dic_barriguinhas:  #Loop que itera pelo dic de barriguinhas
    if dolly_vivo:  #Verifica se o dolly esta vivo
      dolly_venceu = False  #Declara que o dolly perdeu
      while dolly_vivo and not dolly_venceu:  #Loop da batalha, que se repete ate que um dos dois morra
        valor_ataque_dolly = dic_dolly['ataque'] - dic_barriguinhas[barriguinha]['defesa']  #Calc ataque dolly
        valor_ataque_barriguinha = dic_barriguinhas[barriguinha]['ataque'] - dic_dolly['defesa']  #Calc ataque barriguinha

        dic_barriguinhas[barriguinha]['vida'] -= valor_ataque_dolly #Dolly atacando barriguinha
        if dic_barriguinhas[barriguinha]['vida'] <= 0:  #Verifica se o barriguinha morreu
          dolly_venceu = True #Declara que Dolly ganhou
          kills_dolly += 1  #Aumenta 1 no contador de mortes do dolly
          #Printa as msg de vitoria desta luta
          print(f'O {barriguinha} foi derrotado!')
          print('STATUS DOLLY')
          print(f'Vida: {dic_dolly["vida"]}')
        
        else: #Caso o barriguinha não morra no ataque
          dic_dolly['vida'] -= valor_ataque_barriguinha #Barriguinha atacando Dolly
          if dic_dolly['vida'] <= 0:  #Verifica se o dolly morreu
            dolly_vivo = False  #Declara que Dolly morreu
            print('Que tristeza! Dollynho se foi!') #Printa a respectiva msg
            return False, kills_dolly #Retorna que o Dolly perdeu, e quantos matou
  
  return True, kills_dolly  #Retorna que o dolly ganhou, e quantos matou


def main ():
  #Declarando dicionarios
  dic_dolly = {}
  dic_barriguinhas = {}

  recebendo_status_dolly(dic_dolly) #Executando função que recebe os status do dolly

  qtd_barriguinhas = int(input()) #Recebendo a qtd de barriguinhas mole

  if qtd_barriguinhas > 0:  #Verificando se tem barriguinhas mole
    print(f'Oh não! Eles querem acabar com o meu Dollynho!')  #Printando msg de inicio
    recebendo_status_barriguinha(qtd_barriguinhas, dic_barriguinhas)  #Executandofuncao que recebe os status das barriguinhas mole

    dolly_ganhou, kills_dolly = batalhas_dolly(dic_dolly, dic_barriguinhas) #Executando função que roda batalha e retorna se o dolly ganhou, e quantos matou

    if dolly_ganhou:  #Caso dolly ganhe, printa a msg de vitoria
      print(f'OBA! Dolly venceu todos os inimigos!')
    
    else: #Caso perca, printa a de derrota, e diz quantos matou
      print(f'Infelizmente Dollynho não conseguiu vencer todos os Barriguinhas Moles…')
      print(f'Pelo menos levou {kills_dolly} baderneiros com ele!')

  else: #Caso não tenha barriguinhas, dolly eh feliz
    print(f'Oba! Sem intercorrências pelo caminho! Podemos ir para o carnaval em paz!')

main()