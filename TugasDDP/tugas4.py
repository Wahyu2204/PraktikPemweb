Pelanggan = "Budi Santoso"
TotalBelanja = 100000

if (TotalBelanja > 50000):
    Keterangan = "Selamat Anda Mendapat Hadiah \n Terima Kasih Telah Belanja"

else: 
    Keterangan = "Terima Kasih Telah Belanja"

print ("Pelanggan", Pelanggan, "\nTotalBelanja Anda Rp.", TotalBelanja, "\n", Keterangan)

print ()

nama = "Budi Santoso"
Matpel = "Matematika"
Nilai = 90

Keterangan = "lulus" if Nilai >= 75 else "Gagal"

print ("Nama Siswa \t:", nama, 
       "\nMata Pelajaran \t:", Matpel, 
       "\nNilai \t\t:", Nilai, 
       "\nKeterangan \t:", Keterangan)

print ()

Nama = "Budi Santoso"
MatPel = "Matematika"
Nilai = 90

if (Nilai >= 85 and Nilai <=100):
    Grade = "A"

elif (Nilai >= 75 and Nilai <= 85):
    Grade = "B"

elif (Nilai >= 60 and Nilai <= 75):
    Grade = "C"

elif (Nilai >= 30 and Nilai <= 60):
    Grade = "D"

else:
    Grade = "E"

print ("Nama Siswa \t:", Nama, 
       "\nMata Pelajaran \t:", Matpel, 
       "\nNilai \t\t:", Nilai, 
       "\nGrade \t\t:", Grade)

print ()

Nama = "Wahyu Andrianto Wibowo"
Umur = 18

if (Umur >= 6 and Umur <= 18):
    Usia = "Anak-Anak"

elif (Umur >= 18 and Umur <= 65):
    Usia = "Dewasa"

else:
    Usia = "Lanjut Usia"

print ("Nama \t:", Nama, 
       "\nUmur \t:", Umur, 
       "\nUsia \t:", Usia)

print ()

x = 10
y = 20

hasil = (x < y)
print (hasil)

if (x < y):
    Ket = "x Lebih Kecil dari y"

else:
    Ket = "x Lebih besar dari y"

print ("x \t\t:", x,
       "\ny \t\t:", y,
       "\nKeterangan \t:", Ket)