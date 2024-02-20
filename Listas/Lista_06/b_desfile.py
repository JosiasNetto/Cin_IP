def adcionando_info(escolas_info, nome_escola, tema_escola, tempo_desfile, dic_aux):
  dic_aux.update({'nome': nome_escola })
  dic_aux.update({'tema': tema_escola })
  dic_aux.update({'tempo': int(tempo_desfile) })

  dic_aux2 = dic_aux.copy()
  escolas_info.append(dic_aux2)

  return

def avaliando_escola(escolas_info, nome_e_nota_escola):
  temas = []
  contador = 0
  
  if nome_e_nota_escola != 'Não há mais quesitos':
    print('Desfile de samba do Rio de janeiro 2024')
  
  while nome_e_nota_escola != 'Não há mais quesitos':
    temas.append(nome_e_nota_escola)

    print(f'Vamos às notas para o quesito {nome_e_nota_escola}:')
    nome_e_nota_escola = input()
    for i in range(len(escolas_info)):
      nome_e_nota_escola = nome_e_nota_escola.split(' - ')
      for j in range(len(escolas_info)):
        if escolas_info[j].get('nome') == nome_e_nota_escola[0]:
          escolas_info[j].update({temas[contador] : nome_e_nota_escola[1]})
          print(f'{escolas_info[j].get("nome")}: {escolas_info[j].get(temas[contador])}')
      
      nome_e_nota_escola = input()
      
    
    contador += 1
  
  return temas

# def printando_notas(escolas_info, temas):
#   print('Desfile de samba do Rio de janeiro 2024')

#   for i in range(len(temas)):
#     print(f'Vamos às notas para o quesito {temas[i]}:')
#     for j in range(len(escolas_info)):
#       print(f'{escolas_info[j].get("nome")}: {escolas_info[j].get(temas[i])}')

def calculo_vencedor(escolas_info, temas):
  media = 0
  maior_media = 0
  melhor_escola = ''

  for i in range(len(escolas_info)):

    for j in range(len(temas)):
      media +=  float(escolas_info[i].get(temas[j]))
    
    media = media / len(temas)

    if escolas_info[i].get('tempo') > 75:
      media -= ((escolas_info[i].get('tempo') - 75) * 0.1)
    
    elif escolas_info[i].get('tempo') < 65:
      media -= (abs(escolas_info[i].get('tempo') - 65) * 0.1)

    if media > maior_media:
      maior_media = media
      melhor_escola = escolas_info[i].get('nome')

    media = 0
  
  return maior_media, melhor_escola

def resultado_final(maior_nota, melhor_escola):

  print('E o vencedor do desfile de escola de samba do Rio de Janeiro de 2024 é:')
  print(f'{melhor_escola} com uma nota final de {maior_nota:.2f}!')

def main():
  escolas_info = []
  dic_aux = {}

  nome_escola = input()
  while nome_escola != 'Não há mais escolas':
    tema_escola = input()
    tempo_desfile = input()
    adcionando_info(escolas_info, nome_escola, tema_escola, tempo_desfile, dic_aux)
    nome_escola = input()

  nome_e_nota_escola = input()
  temas = avaliando_escola(escolas_info,nome_e_nota_escola)

  #printando_notas(escolas_info, temas)

  maior_media, melhor_escola = calculo_vencedor(escolas_info, temas)

  resultado_final(maior_media, melhor_escola)

main()