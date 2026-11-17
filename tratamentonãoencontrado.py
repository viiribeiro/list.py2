livros = [
    [1, "O Senhor dos Anéis", "J.R.R. Tolkien", 1954],
    [2, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943],
    [3, "1984", "George Orwell", 1949],
]

id_procurado = 99
encontrado = False

for livro in livros:
    if livro[0] == id_procurado:
        encontrado = True
        print("Livro localizado!")
        break

if not encontrado:
    print("Livro não encontrado")
