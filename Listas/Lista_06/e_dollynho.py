def recebendo_status_dolly(dic_dolly):
  dic_dolly['vida'] = int(input())
  dic_dolly['ataque'] = int(input())
  dic_dolly['defesa'] = int(input())

def recebendo_status_barriguinha(qtd_barriguinhas, dic_barriguinhas):
  dic_aux = {}
  for i in range(qtd_barriguinhas):
    nome_barriguinha = input()
    dic_aux['vida'] = int(input())
    dic_aux['ataque'] = int(input())
    dic_aux['defesa'] = int(input())
    dic_barriguinhas[nome_barriguinha] = dic_aux

  return

def batalhas_dolly(dic_dolly, dic_barriguinhas):
  dolly_vivo = True
  dolly_venceu = False

  for barriguinha in dic_barriguinhas:
    if dolly_vivo:
      valor_ataque_dolly = dic_dolly['ataque'] - dic_barriguinhas[barriguinha]['defesa']
      valor_ataque_barriguinha = dic_barriguinhas[barriguinha]['ataque'] - dic_dolly['defesa']

      dic_barriguinhas[barriguinha]['vida'] -= valor_ataque_dolly
      if dic_barriguinhas[barriguinha]['vida'] <= 0:
        dolly_venceu = True
      
      dic_dolly['vida'] -= valor_ataque_barriguinha
      if dic_dolly['vida'] <= 0:
        dolly_vivo = False




def main ():
  dolly_vivo = True
  dic_dolly = {}
  dic_barriguinhas = {}
  contador = 0

  recebendo_status_dolly(dic_dolly)

  qtd_barriguinhas = int(input())

  recebendo_status_barriguinha(qtd_barriguinhas, dic_barriguinhas)

  
