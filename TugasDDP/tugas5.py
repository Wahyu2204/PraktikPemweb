Kendaraan = ["CBR 150","Motor","150cc","Hitam","2"]
print(Kendaraan)

Kendaraan.append("35 Juta")
Kendaraan.append("Sports")
print(Kendaraan)

Kendaraan.insert(1,"Honda")
print(Kendaraan)

pilihan = input('''
Pilihan Operasi
1. Hitung Persegi
2. Hitung Lingkaran
3. Hitung Segitiga
''')

match pilihan :
    case "1" :
        s = int(input("sisi : "))
        Persegi = s*s
        print("Luas Persegi", Persegi)
    case "2" :
       phi = 3.14
       r = int(input("Jari : "))
       Lingkaran = phi * r * r
       print("Luas Lingkaran", Lingkaran)
    case "3" :
        l = 1/2
        a = int(input("Alas : "))
        t = int(input("Tinggi : "))
        Segitiga = l * a * t
        print("Luas Segitiga", Segitiga)
    case _:
        print("Salah Pilih Angka")