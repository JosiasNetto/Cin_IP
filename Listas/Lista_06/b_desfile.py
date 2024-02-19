def adcionando_info(escolas_info, nome_escola, tema_escola, tempo_desfile, dic_aux):
  dic_aux.update({'nome': nome_escola })
  dic_aux.update({'tema': tema_escola })
  dic_aux.update({'tempo': tempo_desfile })

  escolas_info.append(dic_aux)

  return

def main():
  escolas_info = []
  dic_aux = {}

  nome_escola = input()
  while nome_escola != 'Não há mais escolas':
    tema_escola = input()
    tempo_desfile = input()
    adcionando_info(escolas_info, nome_escola, tema_escola, tempo_desfile, dic_aux)
    nome_escola = input()

  

main()