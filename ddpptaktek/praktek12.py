class Person :
  def __init__(self, name, age): 
    self.name = name
    self.age = age
  def myfunc(self): 
    print("Hello my name is " + self.name)
p1 = Person("John", 36) 
p1.myfunc()

class Bank:
  #member1 variabel
  norek = ''
  nama = ''
  saldo = 0
  jmlNasabah = 0 # variabel static
  BANK = 'Bank Syariah Nurul Fikri' # variabel konstanta
  #member2 konstruktor
  def __init__(self,no,nasabah,saldo):
    self.norek = no
    self.nama = nasabah
    self.saldo = saldo
    Bank.jmlNasabah += 1
  #member3 method
  def nabung(self,uang):
  #self.saldo = self.saldo + uang
    self.saldo += uang
  def tarik(self,uang):
  #self.saldo = self.saldo - uang
    self.saldo -= uang
  def cetak(self):
    print(Bank.BANK,
    '\n==========================',
    '\nNo. Rekening\t:',self.norek,
    '\nNama Nasabah\t:',self.nama,
    '\nSaldo\t\t: Rp. ',format(self.saldo, ','),
    '\n--------------------------'
    )

class orang :
  # properti
  nama = ''
  umur = ''
  def __init__(self,name,age):
    self.nama = name
    self.umur = age
  def bernafas (self):
    print ('saya bisa bernafas dengan umur',self.umur)
  # methode
  def berjalan (self):
    self.bernafas ()
    print (self.nama,'bisa berjalan')
# objek
mahasiswa = orang ('acong','10 tahun')
print (mahasiswa.nama)
print (mahasiswa.umur)
mahasiswa.berjalan()

# objek2
# dosen = orang ()
# dosen.nama = 'Dr.Alphonso'
# print (dosen.nama)

# class Person:
#   def __init__(self, name, age):
#    self.name = name
#    self.age = age
# p1 = Person("Reza", 30)
# print(p1.name)
# print(p1.age)