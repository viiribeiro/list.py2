livros = [
    [1, "O Senhor dos Anéis", "J.R.R. Tolkien", 1954],
    [2, "O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943],
    [3, "1984", "George Orwell", 1949],
]

print("Antes da alteração:")
print(livros)

livros[0][3] = 2024

print("\nDepois da alteração:")
print(livros)
print("Ano do primeiro livro:", livros[0][3])
