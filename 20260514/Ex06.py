"""Exercício 06
Solicite uma quantidade indeterminada de notas de alunos (até que seja informada uma
nota menor que zero). Após a entrada de dados, exiba:
a. A quantidade de notas que foram informadas.
b. Todas as notas na ordem em que foram informadas.
c. A média aritmética de todas as notas.
d. A quantidade de notas acima da média aritmética calculada."""

notas = []
while True:
    nota = float(input('Entre com uma nota: '))
    if nota < 0:
        break
    if 0 <= nota <= 10:
        notas.append((nota))
maior_media = 0
if len(notas) > 0:
    print(f'Quantidade de notas informadas: {len(notas)}')
    print(f'Notas: {notas}')
    print(f'Notas ordenadas: {sorted(notas)}')
    media = sum(notas)/len(notas)
    print(f'Media: {media:.1f}')
    for nota in notas:
        if nota > media:
            maior_media += 1
    print(f'Qt de notas maior que a media: {maior_media}')
