funcionarios = [
    [1, "Ana Silva", "Analista de Sistemas", 4500.00],
    [2, "Bruno Costa", "Gerente de Projetos", 7200.50],
]

for indice, funcionario in enumerate(funcionarios):
    if funcionario[0] == 2:
        funcionarios[indice][3] += 500
        print(f"Salário atualizado para {funcionarios[indice][3]:.2f}")
        break

print(funcionarios)
