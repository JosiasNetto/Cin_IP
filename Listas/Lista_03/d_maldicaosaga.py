colecao_sergio = input().split(", ")
livros_saga = ["O Ladrão de Raios", "O Mar de Monstros", "A Maldição do Titã", "A Batalha do Labirinto", "O Último Olimpiano"]
qtd_total_edicoes = int(input())
possui_livro = False
livros_diferentes = []


for livro in colecao_sergio:
    if livro in livros_saga:
        livros_saga.remove(livro)
        possui_livro = True
    else:
        livros_diferentes.append(livro)

if livros_saga == []:
    print("Sua coleção está completa! Você pode ler à vontade.")

elif possui_livro:
    print(f"Infelizmente, sua coleção está incompleta. Falta(m) esse(s) livro(s):", end='')
    for i in range(len(livros_saga)):
        if i != (len(livros_saga) - 1):
            print(f' {livros_saga[i]},',end='')
        else:
            print(f' {livros_saga[i]}.')
    
else:
    print(f"Caramba, você não tem nenhum livro. Compre todos imediatamente.")

if livros_diferentes != [] and livros_diferentes != ['']:
    print(f'Cuidado, Sérgio! Você está organizando seus livros de uma forma errada, o(s) livro(s):',end='')
    for i in range(len(livros_diferentes)):
        print(f' {livros_diferentes[i]},',end= '')
    print(' não faz(em) parte da saga "Percy Jackson e os Olimpianos".')