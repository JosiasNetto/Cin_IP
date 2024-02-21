def adcionando_info(escolas_info, nome_escola, tema_escola, tempo_desfile, dic_aux):
#Função que recebe as info da escola e cria um dicionario com elas, apos, adciona o dicionario em uma lista
  
  #Atualizando as info no dicionario aux
  dic_aux.update({'nome': nome_escola })
  dic_aux.update({'tema': tema_escola })
  dic_aux.update({'tempo': int(tempo_desfile) })

  escolas_info.append(dic_aux.copy()) #Adcionando a copia do dic atual a lista

  return

def avaliando_escola(escolas_info, nome_e_nota_escola):
#Função que recebe a lista das escolas, le as respectivas notas, e ja printa a msg certa
  
  temas = []  #Lista que recebera todos os temas avaliados
  contador = 0
  
  if nome_e_nota_escola != 'Não há mais quesitos':  #Verificando se o primeiro input é diferente da msg de fim
    print('Desfile de samba do Rio de janeiro 2024')  #Printa a msg inicial
  
  while nome_e_nota_escola != 'Não há mais quesitos': #Loop que so finaliza ao receber a msg certa
    temas.append(nome_e_nota_escola)  #Adciona o tema na lista de temas

    print(f'Vamos às notas para o quesito {nome_e_nota_escola}:') #Printa a msg do respectivo tema
    nome_e_nota_escola = input()  #Recebe o nome e a nota de uma escola
    for i in range(len(escolas_info)):  #Loop que passa pela qtd de escolas
      nome_e_nota_escola = nome_e_nota_escola.split(' - ')  #Separa o nome da nota da escola
      for j in range(len(escolas_info)):  #Loop que passa novamente pela qtd de escolas
        if escolas_info[j].get('nome') == nome_e_nota_escola[0]:  #Verifica se o nome da escolha lida, é igual ao da nota recebida
          escolas_info[j].update({temas[contador] : nome_e_nota_escola[1]}) #Adciona a nota do tema como elemento do dicionario
          print(f'{escolas_info[j].get("nome")}: {escolas_info[j].get(temas[contador])}') #Printa o nome e a nota da escola
      
      nome_e_nota_escola = input()  #Recebe o prox quesito
      
    
    contador += 1 #Aumenta o contador que aux o tema
  
  return temas  #Retorna a lista de temas


def calculo_vencedor(escolas_info, temas):  #Função que calcula a maior media entre as escolas
  media = 0
  maior_media = 0
  melhor_escola = ''

  for i in range(len(escolas_info)):  #Loop que passa pela qtd de escolas

    for j in range(len(temas)): #Loop que passa pela qtd de temas
      media +=  float(escolas_info[i].get(temas[j]))  #Soma das notas de todos os temas de uma escola
    
    media = media / len(temas)  #Divide a media pela qtd de temas

    #Verificando se passa ou não atinge o tempo certo, e aplica a penalidade caso aconteça
    if escolas_info[i].get('tempo') > 75: 
      media -= ((escolas_info[i].get('tempo') - 75) * 0.1)  #Calculo penalidade
    
    elif escolas_info[i].get('tempo') < 65:
      media -= (abs(escolas_info[i].get('tempo') - 65) * 0.1) #Calculo penalidade

    if media > maior_media: #Verifica se a media atual verificada, é maior que a maior media atual
      maior_media = media #Maior media igual a atual
      melhor_escola = escolas_info[i].get('nome') #Muda o nome da escola para a com a maior media

    media = 0 #Reseta a media para calcular o prox
  
  return maior_media, melhor_escola #Retorna a maior media e o nome da respectiva escola

def resultado_final(maior_nota, melhor_escola): #Printa o resultado final

  print('E o vencedor do desfile de escola de samba do Rio de Janeiro de 2024 é:')
  print(f'{melhor_escola} com uma nota final de {maior_nota:.2f}!')

def main():
  escolas_info = [] #Lista que recebera os dicionarios das escolas
  dic_aux = {}  

  nome_escola = input() #Recebendo o nome da primeira escola
  while nome_escola != 'Não há mais escolas': #Loop que so finaliza com a msg certa
    tema_escola = input() #Recebendo tema da escola
    tempo_desfile = input() #Recebendo tempo do desfile da escola
    adcionando_info(escolas_info, nome_escola, tema_escola, tempo_desfile, dic_aux) #Executando função que add as infos da escola na lista
    nome_escola = input() #Recebe o nome da escola novamente

  nome_e_nota_escola = input()  #Recebe o primeiro tema a ser avaliado
  temas = avaliando_escola(escolas_info,nome_e_nota_escola) #Executando função que recebe e printa tanto os temas quanto as notas 

  maior_media, melhor_escola = calculo_vencedor(escolas_info, temas)  #Executa função que calcula as notas, e retorna a maior media e a escola com a respectiva

  resultado_final(maior_media, melhor_escola) #Executa funçãoq que printa msg final

main()