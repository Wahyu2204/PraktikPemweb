# def balikan (namabuah):
#   buahbalikan = []
#   for i in range (len(namabuah)-1,-1,-1):
#     buahbalikan.append(namabuah[i])
#   return buahbalikan
# buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
# buahdibalik=balikan(buah)
# print(buahdibalik)

# def balik (daftarbuah):
#   return daftarbuah[::-1]
# buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
# buahbalikan = balik(buah)
# print (buahbalikan)

# def balikan(namabuah):
#     buahbalikan = []
#     for buah in namabuah[::-1]:
#         buahbalikan.append(buah)
#     return buahbalikan

# buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
# buahdibalik = balikan(buah)
# print(buahdibalik)

# for i in range (4):
#    print ("Wahyu")

# for i in range (10, 0, -2):
#    print (i)

# for i in range (0, 10, 2):
#    print (i)

# for i in range (1,11):
#    for j in range (1,11):
#        k=i*j
#        print (k, end="")
#    print ()

# bilangan = [1,2,3]
# a = bilangan.pop()
# bilangan.append(6)
# bilangan.append(5)
# print (bilangan)
# print (a)

# def balikan (namabuah):
#   buahbalikan = []
#   for buah in namabuah [::-1]:
#     buahbalikan.append(buah)
#   return buahbalikan
# buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
# buahdibalik=balikan(buah)
# print(buahdibalik)

def hurufkonsonan(teks):
    konsonan = ''
    for huruf in teks:
        if 'A' <= huruf.upper() <= 'Z' and huruf.upper() not in 'AEIOU':
            konsonan += huruf
    return konsonan

teksasli = 'Nurul Fikri'
hasil = hurufkonsonan(teksasli)
print(hasil)
