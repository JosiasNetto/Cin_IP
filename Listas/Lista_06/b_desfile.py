def adcionando_info(escolas_info, nome_escola, tema_escola, tempo_desfile, dic_aux):
  dic_aux.update({'nome': nome_escola })
  dic_aux.update({'tema': tema_escola })
  dic_aux.update({'tempo': tempo_desfile })

  escolas_info.append(dic_aux)

  return

def avaliando_escola(escolas_info, nome_e_nota_escola):
  temas = []
  contador = 0
  

  while nome_e_nota_escola != 'Não há mais quesitos':
    temas.append(nome_e_nota_escola)

    for i in range(len(escolas_info)):
      nome_e_nota_escola.split('-')
      escolas_info[i].update({temas[contador] : nome_e_nota_escola[1]})
      nome_e_nota_escola = input()
    
    contador += 1
  
  return temas

def printando_notas(escolas_info, temas):
  print('Desfile de samba do Rio de janeiro 2024')

  for i in range(len(temas)):
    print(f'Vamos às notas para o quesito {temas[i]}:')
    for j in range(len(escolas_info)):
      print(f'{escolas_info[j].get('nome')}: {escolas_info[j].get(temas[i])}')

def calculo_vencedor(escolas_info, temas):
  media = 0
  maior_media = 0

  for i in range(len(escolas_info)):

    for j in range(len(temas)):
      media += escolas_info[i].get(temas[j])
    
    if media > maior_media:
      maior_media = media

    media = 0
  
  return maior_media

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

main()