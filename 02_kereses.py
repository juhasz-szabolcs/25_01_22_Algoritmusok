'''
Az KERESÉS esetében azt vizsgáljuk, 
hogy szerepel-e egy bizonyos tulajdonságú elem az adatsorban (itt a listában),
és ha igen, hányadik helyen.

A program azt vizsgálja, hogy szerepel-e a piros szín a listában, és ha igen, hányadik helyen.
'''
lista = ['kék', 'zöld', 'piros', 'fehér', 'piros']

# talalat = False
# index = 0
# while index < len(lista) and not talalat:
#     if lista[index] == 'piros':
#         talalat = True
#     index = index + 1

# if talalat:
#     print('Van a listában piros szín, az indexe: ', index-1)
# else:
#     print('Nincs a listában piros szín.')

if 'piros' in lista:
    print('Van a listában piros szín.')
else:
    print('Nincs a listában piros szín.')

print(lista.count('piros'))

# for - lista elemek
mennyi= 0
for elem in lista:
    if elem == 'piros':
        mennyi += 1
print(mennyi)

# for ciklus index-szel
hanyszor_fordul_elo = 0
for index in range(len(lista)):
	if lista[index] == 'piros':
		hanyszor_fordul_elo += 1

print('Ennyiszer fordul elő ' + str(hanyszor_fordul_elo))
