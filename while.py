sekunde = 10

'''
if sekunde > 0:
    print(sekunde)

sekunde -= 1
if sekunde > 0:
    print(sekunde)

sekunde -= 1
if sekunde > 0:
    print(sekunde)

sekunde -= 1
if sekunde > 0:
    print(sekunde)

sekunde -= 1
if sekunde > 0:
    print(sekunde)

sekunde -= 1
if sekunde > 0:
    print(sekunde)

sekunde -= 1
if sekunde > 0:
    print(sekunde)

sekunde -= 1
if sekunde > 0:
    print(sekunde)

sekunde -= 1
if sekunde > 0:
    print(sekunde)

sekunde -= 1
if sekunde > 0:
    print(sekunde)

sekunde -= 1
if sekunde > 0:
    print(sekunde)

sekunde -= 1
if sekunde > 0:
    print(sekunde)

sekunde -= 1
if sekunde > 0:
    print(sekunde)
'''

# while sekunde > 0:
#     print(sekunde)
#     sekunde -= 1

# baterija = 90
# while baterija > 0:
#     print('Mozes koristiti telefon: ', baterija, '%')
#     baterija -= 5


# print('Baterija je prazna')

# for broj in range(1,11):
#     if broj == 2:
#         continue
#     print(broj)


sifra = int(input('unesi sifru '))
if sifra == 100:
    print('SERBIA - BRASIL')
    tip = int(input('unesi tip igre '))
    if tip == 1:
        print('kvota je 5.75')
    elif tip == 'X':
        print('kvota je 2.80')
    else:
        print('kvota je 1.60')
else:
    print('SERBIA - SWITZERLAND')
    tip = input('unesi tip igre ')
    if tip == 1:
        print('kvota je 2.40')
    elif tip == 'X':
        print('kvota je 3.40')
    else:
        print('kvota je 2.30')


broj1 = float(input('Kvotu koju zelis: '))
broj2 = int(input('Tvoja uplata: '))
print ('Vas dobitak je', int(broj1 * broj2),'dinara.')

# range(20)
# for broj in range(2010, 2022):
#     print(f'ovo je {broj}.godina')