def sapa(nama):
    'Fungsi ini untuk menyapa seseorang sesuai nama yg dimasukkan sebagai parameter'
    print('Hi, ', nama, '. Apa kabar?')
#pemanggilan fungsi 
#output: Hi, Umar. Apa kabar?
sapa('Umar')

#definisi fungsi print_string
def print_string(str):
    'Menampilkan argumen string str ke layar'
    print(str)
#Kita memanggil fungsi dengan kata kunci
print_string(str = 'Hello Python')

#definisi fungsi
def print_info(nama, usia):
    'Fungsi ini menampilkan info yang dimasukkan'
    print('Nama : ', nama)
    print('Usia : ', usia)
#memanggil fungsi 
#output
#Name : Budi
#Usia : 25
print_info(usia = 25, nama = 'Budi')

#definisi fungsi 
def print_info(nama, usia = 17):
    'Fungsi ini menampilkan info yang dimasukkan'
    print('Nama : ', nama)
    print('Usia : ', usia)
#memanggil fungsi print_info
print_info(usia = 29, nama = 'Galih')
#pemanggil fungsi tidak menggunakan argumen usia
print_info(nama = 'Galih')

#definisi fungsi
def print_info(arg1, *vartuple):
    'Fungsi untuk menampilkan nilai argumen sembarang yg dilewatkan'
    print('Outputnya adalah : ')
    print(arg1)
    for var in vartuple:
        print(var)
#pemanggilan fungsi
#satu argumen
print_info(10)
#empat argumen
print_info(10,30,50,70)

#variabel global
#definisi fungsi
def sum(arg1, arg2):
    'Menambahkan variabel dan mengembalikan hasilnya'
    total = arg1 + arg2
    #total disini adalah variabel lokal
    print('Di dalam fungsi nilai total : ', total)
    return total
#pemanggilan fungsi sum
sum(10,20)
print('Diluar fungsi, nilai total : ', total)