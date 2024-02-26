def add_pessoa_mascara(dic_pessoas, nome_mascara_cor):
  nome = nome_mascara_cor.split(' -> ')[0]
  mascara = nome_mascara_cor.split(' -> ')[1]
  dic_mascara = {mascara.split(': ')[0] : mascara.split(': ')[1], 'nivel' : 0}
  dic_pessoas[nome] = dic_mascara

  return

def trocar_mascara(dic_pessoas, msg_troca):
  msg_troca = msg_troca.split(' <-> ')
  var_aux = dic_pessoas[msg_troca[1]]
  dic_pessoas[msg_troca[1]] = dic_pessoas[msg_troca[0]]
  dic_pessoas[msg_troca[0]] = var_aux
  qtd_trocas_feitas(dic_pessoas, msg_troca)

  return

def chuva_mascaras(msg_evento, dic_pessoas):
  mascara_especial = msg_evento.split(' -> ')[1]
  nome_mascara = mascara_especial.split(': ')[0]
  nivel_mascara = int(mascara_especial.split(': ')[1])
  lista_beneficiados = []
  
  for i in dic_pessoas:
    if 'qtd_trocas' in dic_pessoas[i]:
      if dic_pessoas[i]['qtd_trocas'] % 2 != 0 and dic_pessoas[i]['qtd_trocas'] <= nivel_mascara:
        cor = list(dic_pessoas[i].values())[0]
        dic_aux = {nome_mascara : cor, 'qtd_trocas' : 1, 'nivel' : nivel_mascara}
        dic_pessoas[i] = dic_aux
        lista_beneficiados.append(i)
  
  if len(lista_beneficiados) > 0:
    if len(lista_beneficiados) == 1:
      print(f'Apenas {lista_beneficiados[0]} é que aproveitou mesmo o evento Chuva de máscaras.')
    
    else:
      print(f'Arretaaado demais!! Teve um evento maneiro aqui e',end='')
      for i in range(len(lista_beneficiados)):
        if i < len(lista_beneficiados) - 1:
          print(f' {lista_beneficiados[i]},',end='')
        else:
          print(f' {lista_beneficiados[i]}',end='')
      print(' foram beneficiados.')
        
  else:
    print('Vixe... Serviu pra nada o evento Chuva de máscaras :/')

  return


def qtd_trocas_feitas(dic_pessoas, nomes_troca):
  for i in range(2):
    if 'qtd_trocas' in dic_pessoas[nomes_troca[i]]:
      dic_pessoas[nomes_troca[i]]['qtd_trocas'] = dic_pessoas[nomes_troca[i]]['qtd_trocas'] + 1
      dic_pessoas[nomes_troca[i]]['nivel'] = dic_pessoas[nomes_troca[i]]['nivel'] + 1
    
    else:
      dic_pessoas[nomes_troca[i]]['qtd_trocas'] = 1
      dic_pessoas[nomes_troca[i]]['nivel'] = dic_pessoas[nomes_troca[i]]['nivel'] + 1
  
  return

def verificando_limite_troca(num_troca_mascaras, msg_troca, dic_pessoas):
  nomes_troca = msg_troca.split(' <-> ')
  num_trocas_limt = 0
  nomes_limit_troca = []
  pode_trocar = True

  if dic_pessoas[nomes_troca[0]].get('qtd_trocas', 0) == num_troca_mascaras:
    num_trocas_limt += 1
    print(f'Eita, amigo, tas preso com a {list(dic_pessoas[nomes_troca[0]].keys())[0]}, visse? Pode trocar mais ela não.')
    pode_trocar = False
  
  if dic_pessoas[nomes_troca[1]].get('qtd_trocas', 0) == num_troca_mascaras:
    num_trocas_limt += 1
    nomes_limit_troca.append(nomes_troca[1])
    print(f'Eita, amigo, tas preso com a {list(dic_pessoas[nomes_troca[1]].keys())[0]}, visse? Pode trocar mais ela não.')
    pode_trocar = False
  
  return pode_trocar

def chamado_cores_mascaras(dic_pessoas, msg_cor):
  msg_cor = msg_cor.replace('Temos máscaras de cor ', '')
  cor = msg_cor.replace('?', '')
  contador_cores = 0
  for i in dic_pessoas:
    if list(dic_pessoas[i].values())[0] == cor:
      contador_cores += 1
  print(f'Um total de {contador_cores} pessoa(s) está(o) com máscara de cor {cor}!')
  
def main():
  num_individuos = int(input())
  dic_pessoas = {}

  for i in range(num_individuos):
    nome_mascara_cor = input()
    add_pessoa_mascara(dic_pessoas, nome_mascara_cor)
  
  num_troca_mascaras = int(input())
  msg_troca = input()
  while msg_troca != 'FIM':
    if 'Evento especial!!! Chuva de máscaras' in msg_troca:
      chuva_mascaras(msg_troca, dic_pessoas)
    
    elif 'Temos máscaras de cor' in msg_troca:
      chamado_cores_mascaras(dic_pessoas, msg_troca)
      
    else:
      if verificando_limite_troca(num_troca_mascaras, msg_troca, dic_pessoas):
        trocar_mascara(dic_pessoas, msg_troca)
    msg_troca = input()
  
  print(f'Agora é hora de ver quem ficou com que máscara!')
  lista_pessoas = list(dic_pessoas.items())
  lista_pessoas = sorted(lista_pessoas)

  for i in range(len(lista_pessoas)):
    print(f'{lista_pessoas[i][0]} -> {list(lista_pessoas[i][1])[0]}: {lista_pessoas[i][1].get("nivel", 0)}')
  print(f'Troca de máscaras encerrada! Esperamos que todos tenham se divertido!')

main()