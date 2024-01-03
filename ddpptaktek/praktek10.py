nilai = [65,60,75,0,98]
nilai[0] == 65
nilai[len(nilai)-1] == 98

#LIFO
bilangan = [1,2,3]
a = bilangan.pop()
bilangan.append(6)
print (bilangan)
print (a)

#FIFO
bilangan = [1,2,3]
bilangan.append(6)
a = bilangan.pop()
print (bilangan)
print (a)

set1 = {1,2,3}
set2 = {2,4,6}
set3 = set1.union(set2)
print(set3)

print ('==========Materi 1==========')
#Array/List
numbers = [1,2,4,3,5,5,100,10]
print (numbers[0]) #indexing
print (numbers[1:4]) #slicing

print ('==========Materi 2==========')
#Stack (Tumoukan)
#LIFO
numbers = []
print (numbers)
numbers.append(1) # append hanya bisa menampung 1 data saja
numbers.append(2)
numbers.append(3)
print(numbers)
a = numbers.pop() #POP > Data yang di ambil
print (a)
print (numbers)

print ('==========Materi 3==========')
#Queue (Urutan)
#FIFO
numbers = []
print (numbers)
numbers.append(1) # append hanya bisa menampung 1 data saja
numbers.append(2)
numbers.append(3)
print(numbers)
a = numbers.pop(0) #POP > Data yang di ambil
numbers.append(4)
print (a)
print (numbers)

print ('==========Materi 4==========')
#Set (Sama Sperti list)
names = {'udin','asep','ujang','otong'}
print (names)

numbers = {9,9,6,8,1,2,2,3}
print(numbers)

#set
null = set() # set hanya menaruh data yang berbeda
null.add(1) # .add (menambahkan data ke dalam set)
print (null)

names = {'udin','asep','ujang','otong'}
ListName = []
for name in names :
  ListName.append(name)
print (ListName)

set1 = {1,2,3}
set2 = {2,4,6}
set3 = set1.union(set2)
print(set3)

set1 = {1,2,3}
set2 = {2,4,6}
set1.update(set1)
print(set1)

print ('==========Materi 6==========')
#Dictionary
mhs = {
  'nama' : 'Ucup',
  'semester' : 1,
  'hobi' : ['mancing','membaca','nyolong']
}
mhs['umur'] = 18
print (mhs)
print (mhs.keys())
print (mhs.values())
print (mhs.items())

print()
data = {
  'mhs' : {
    'nama' : 'Ucup',
    'semester' : 1,
    'hobi' : ['mancing','membaca','nyolong'],
    'pacar' : {
      'nama' : ['lala','lili','lulu','lele'],
      'selingkuhan' : {
        'nama' : ['Igun','Ical','Mikel','Acam']
      }
    }
  },
  'dosen' : {
    'nama' : 'Reza Maulana',
    'matkul' : 'DDP'
  }
}
data['mhs']['jk'] = 'Laki-laki'
print (data['mhs'])