livros = [
    [1, "O Senhor dos Anéis", "J.R.R. Tolkien", 1954],
    [2, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943],
    [3, "1984", "George Orwell", 1949],
]

id_remover = 2

for indice, livro in enumerate(livros):
    if livro[0] == id_remover:
        livros.pop(indice)
        break

print(livros)
