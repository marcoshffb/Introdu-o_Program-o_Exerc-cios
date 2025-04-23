teams = [
    'Malaysia',
    'China',
    'Gabon',
    'Malta'
]

team = input('Digite a seleção desejada: ')
find = False

# Processamento de dados
for i in range(len(teams)):
    if team.upper() == teams[i].upper():
        find = True

# Saída de dados
if find:
    print('Achei!')
else:
    print('Não achei!')