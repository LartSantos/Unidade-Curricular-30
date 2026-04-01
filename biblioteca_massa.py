#Dicionário para armazenar os livrooooooooooo
catalogo = {}



#Dicionario para armazenar os empréstimos ativooooooos
emprestimoAtivo = {}

historico = []

#Função: Adicionar livroooooooo
def adicionarLivro (codigo, titulo, autor, quantidade):
    if codigo in catalogo:
        print (f"Erro: Livro com código {codigo} já existe!")
        return False

    catalogo [codigo] = {
    "titulo": titulo,
    "autor": autor,
    "quantidade": quantidade
}
    print (f"Livro ´{titulo}´ adicionado com sucesso!")
    return True

adicionarLivro ("L001", "Código Limpo", "Robert Martin", 2)

#FUNÇÃO EMPRESTAR LIVROSSSSSS
def empresta_livro(codigo, nome_aluno):
    #Validação 01: Livro existe no catálogo?
    if codigo not in catalogo:
        print (f"Erro: Livro com código {codigo} não encontrado!")
        return False
    
    #Validação 02: Há quantidade disponível? se quiser sim.
    if catalogo [codigo]["quantidade"] <= 0:
        print (f"Erro: ´{catalogo[codigo]['titulo']}  não está disponível!")
        return False
    
    #Validação 03: Será que o Aluno já pegou dois livroooos?
    livros_do_aluno = conta_livros_aluno(nome_aluno)
    if livros_do_aluno >= 2:
        print (f"Erro: {nome_aluno} já pegou dois livros (limite máxima)!")
        return False
    
    #Validação 04: será que o Aluno já pegou este livrooooo?
    if codigo in emprestimoAtivo and nome_aluno in emprestimoAtivo[codigo]:
        print (f"Erro: {nome_aluno} já pegou este livro!")
        return False
    
    if codigo not in emprestimoAtivo:
        emprestimoAtivo[codigo] = []

    #Adicionar o aluno à lista de quem pegou este livrooooo
    emprestimoAtivo[codigo].append(nome_aluno)

    #Diminui a quantidade disponivel :(
    catalogo[codigo]["Quantidade"] -= 1

    #Registrar no histórico 
    historico.append ({
        "tipo": "emprestimo",
        "codigo": codigo, 
        "titulo": catalogo[codigo]["titulo"],
        "aluno": nome_aluno
    })

    print (f"{nome_aluno} pegou ´{catalogo[codigo]['titulo']}´ com sucesso!")
    return True

#FUNÇÃO PRA DEVOLVER LIVRO
def devolver_livro(codigo, nome_aluno):

    #Verificar se o livro está emprestado para este alunooooooo
    if codigo not in emprestimoAtivo or nome_aluno not in emprestimoAtivo[codigo]:
        print(f"Erro: {nome_aluno} não pegou este livro")
        return False
    
    #Remove o alunooooo da lista de quem pegou este livro
    emprestimoAtivo [codigo].remove(nome_aluno)

    #Aumento a quantidade disponível :D
    catalogo [codigo]["quantidade"] += 1

    #Registrar no históricoooo
    historico.append ({
        "tipo": "devolucao",
        "codigo": codigo, 
        "titulo": catalogo[codigo]["titulo"],
        "aluno": nome_aluno
    })

    print (f"{nome_aluno} devolveu ´{catalogo[codigo]['titulo']}´ com sucesso!")
    return True

#FUNÇÃO CONTAR LIVROOOOOO
def conta_livros_aluno(nome_aluno):
    
    #Começa com o contadooor em 0
    contador = 0

    #Percorrer todos os livros que estão emprestadoooos
    for codigo, alunos in emprestimoAtivo.itens():
        #Se o alunoooo está na lista de quem pegou este livro, incrementeeee!!!!!!!!
        if nome_aluno in alunos:
            contador += 1

    return contador

def lista_emprestimo():
    print ("\n" + "="*60)
    print ("LIVROS EMPRESTADOS NO MOMENTO")
    print ("="*60)

    #Se não há empréstado, avisaaaa!!!!!!
    if not emprestimoAtivo:
        print ("Nenhum livro emprestado.")
        return
    
    #Percorre cada livro que está emprestadooooo
    for codigo, alunos in emprestimoAtivo.itens():
        titulo = catalogo [codigo] ["titulo"]
        print (f"\n {titulo} ({codigo})")

        #Mostrar quem pegou cada livroooo
        for aluno in alunos:
            print (f"Emprestimo para: {aluno}")

    # PASSO 1: Adiciona alguns livros ao catálogoooo
    print("\n--- Adicionando livros ao catálogo ---")
    adicionarLivro("L001", "Clean Code", "Robert Martin", 2)
    adicionarLivro("L002", "Python Fluente", "Luciano Ramalho", 1)
    adicionarLivro("L003", "Algoritmos", "Thomas Cormen", 3)
    
    # PASSO 2: Alunooooos pegam livros
    print("\n--- Alunos pegando livros ---")
    empresta_livro("L001", "Ana")
    empresta_livro("L001", "Bruno")
    empresta_livro("L002", "Ana")
    empresta_livro("L003", "Carlos")
    
    # PASSO 3: Tenta emprestar novamente (Deve com certeza falhar)
    print("\n--- Tentando emprestar novamente ---")
    empresta_livro("L001", "Ana")  # Erro: Ana já pegou este livro!!
    empresta_livro("L002", "Ana")  # Erro: Ana já pegou 2 livros!!
    
    # PASSO 4: Lista empréstimos ativooooos
    print("\n--- Listando empréstimos ativos ---")
    lista_emprestimo()
    
    # PASSO 5: Devolve um livrooooo
    print("\n--- Devolvendo um livro ---")
    devolver_livro("L001", "Ana")
    

  # PASSO 6: Lista empréstimos novamente!!!!
    print("\n--- Listando empréstimos após devolução ---")
    lista_emprestimo()
    
    print("\n" + "="*60)
    print("Teste finalizado!")
    print("="*60 + "\n")