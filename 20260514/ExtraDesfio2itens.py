minhaLista = ['café', 'água', 'açucar', 'raspas de limao',
              'nibs de chocolate', 'canela', 'chantilly',
              'pimenta', 'gengibre']

itens_procurados = ['chantilly', 'gengibre']

# flag para verificar se todos estão presentes
todos_presentes = True

for item in itens_procurados:
    if item not in minhaLista:
        todos_presentes = False
        break

print("Tem chantilly e gengibre?", todos_presentes)
