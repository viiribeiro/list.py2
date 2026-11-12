from biblioteca import livros

for livro in livros:
    id_livro = livro[0]
    titulo = livro[1]
    autor = livro[2]
    ano = livro[3]
    print(f"ID: {id_livro} | O livro \{titulo}\" foi escrito por {autor} em {ano}.")
print()