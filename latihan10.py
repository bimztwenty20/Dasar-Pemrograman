#contoh menggunakan perintah output
import penggunaan_modul
print(penggunaan_modul.penjumlahan(10,90))

#contoh menggunakan perintah alias pada modul
import penggunaan_modul as aritmatika
print(aritmatika.penjumlahan(10,90))

#contoh penggunaan sebagai fungsi modul
from math import pow
pangkat_bilangan = pow(3,3) #artinya bilangan 3 dipangkat 3
print('Hasil dari pemangkatan bilangan adalah : ', pangkat_bilangan)

from math import factorial
bil = int(input('Masukkan sebuah bilangan positif : '))
faktorial_bil = factorial(bil)
print('Bilangan faktorial dari bil adalah : ', faktorial_bil)

#contoh penggunaan semua fungsi pada suatu modul
from math import*
pangkat_bilangan = pow(3, 3)
print('Hasil dari pemangkatan bilangan adalah : ', pangkat_bilangan)

bil = int(input('Masukkan sebuah bilangan positif : '))
faktorial_bil = factorial(bil)
print('Bilangan faktorial dari bil adalah : ', faktorial_bil)



import sys
lists = ['a', 0, 4]
for each in lists:
    try:
        print('Masukkan : ', each)
        r = 1/int(each)
        break
    except:
        print('Upps!', sys.exc_info()[0], 'terjadi')
        print('Masukkan berikutnya')
        print()
print('Kebalikan dari ', each, ' =', r)


#Syntax Error
print('Nama saya adalah Wowo')

#Zero division error
'''bilangan_1 = 10
bilangan_2 = 0
proses = bilangan_1/bilangan_2
print(proses)'''

#Name Error
'''penjumlahan = 3+2
print(penjumlaha)'''

#Type Error
data_1 = 3
data_2 = '10 menit'
proses = data_1 + data_2
print(proses)