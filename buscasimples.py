livros = [
    [1, "O Senhor dos Anéis", "J.R.R. Tolkien", 1954],
    [2, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943],
    [3, "1984", "George Orwell", 1949],
]

titulo_procurado = "1984"

for livro in livros:
    if livro[1] == titulo_procurado:
        print("Livro localizado!")
        break
