'''
Az ELDÖNTÉS esetében azt vizsgáljuk,
hogy szerepel-e egy bizonyos tulajdonságú elem az adatsorban (itt a listában).

A program azt vizsgálja, hogy van-e hárommal osztható szám a listában.
'''
lista = [2, 5, 4, 8, 9, 11, 10, 12]

talalat = False
index = 0
while index < len(lista) and not talalat:
    if lista[index] % 3 == 0:
        talalat = True
    index = index + 1

if talalat:
    print('Van a listában hárommal osztható szám.')
else:
    print('Nincs a listában hárommal osztható szám.')