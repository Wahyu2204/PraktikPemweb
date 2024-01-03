def hello ():
    print('hello worrld')
hello ()
def say (nama):
    print ('hello my name is', nama)
say ('Wahyu')
def nama_lengkap (namaDepan, namaBel):
    print (namaDepan + '' + namaBel)
nama_lengkap ('Wahyu','Wibowo')
def myName (*nama):
    print ('nama saya adalah' + nama[2])
myName ('wahyu', 'andrianto', 'wibowo')
def myNama (nama = 'wibowo'):
    print ('nama saya adalah' + nama)
myNama ('wahyu')
myNama ('andrianto')
myNama ()
def nilaiGanjil (b):
    a=1
    while (a < b):
        print(a, end=" , ")
        a+=2
    print(a)
nilaiGanjil (100)