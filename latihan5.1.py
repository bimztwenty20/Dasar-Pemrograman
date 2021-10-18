print('''GEROBAK FRIED CHICKEN
----------------------------------
Kode    Jenis Potong    Harga
D       Dada            Rp. 2500
P       Paha            Rp. 2000
S       Sayap           Rp. 1500
----------------------------------
\n''')

ayam = int(input('Banyak Jenis : '))

#input
listkode = []
listbanyak = []
for i in range(ayam):
    print('Jenis ke- ', i+1)
    kode = input('Kode potong [D/P/S] : ')
    listkode.append(kode)
    banyak = int(input('Banyak potong : '))
    listbanyak.append(banyak)

#output
print('\n\nGEROBAK FRIED CHICKEN')
print(40*'-')

#output program
print('''No.  Jenis       Harga     Banyak   Jumlah
     Potong      Satuan    Beli     Harga''')
print(50*'-')

#proses
total = 0
for i in range(ayam):
    if listkode[i] == 'D' or listkode[i] == 'd':
        jenis = 'Dada'
        harga = int(2500)
    elif listkode[i] == 'P' or listkode[i] == 'p':
        jenis = 'Paha'
        harga = int(2000)
    elif listkode[i] == 'S' or listkode[i] == 's':
        jenis = 'Sayap'
        harga = int(1500)
    else :
        jenis = '-'
        harga = int(0)

    total1 = harga * listbanyak[i]
    total = total + total1
    ppn = total * 0.1
    totalbayar = total + ppn

    print(i+1, '  ', jenis, '\t', harga, '\t  ', listbanyak[i], '\t   ', total1)
print(50*'-')
print('\t\tTotal Pembelian   :', total)
print('\t\tPpn               :', ppn)
print('\t\tTotal Bayar       :', totalbayar)





#For Jupyter Notebook

"""print("GEROBAK FRIED CHICKEN".center(70," "))
print("="*70)
print('''No. \t Jenis \t\t Harga \t\t Banyak \t Jumlah
 \t Potong \t Satuan \t Beli \t\t Harga''')
print("="*70)
banyak_jenis = int(input("Masukkan Banyak Jenis = "))
jenis_ke = 1
jumlah_bayar = 0
while (jenis_ke <= banyak_jenis):
    kode_potong = input("Masukkan Kode Potong (D/P/S) = ")
    if kode_potong == "D" or kode_potong == "d":
        jenis_potong = "Dada"
        harga = 2500
    elif kode_potong == "P" or kode_potong == "p":
        jenis_potong = "Paha"
        harga = 2000
    elif kode_potong == "S" or kode_potong == "s":
        jenis_potong = "Sayap"
        harga = 1000
    else:
        jenis_potong = "-"
        harga = 0
    banyak_potong = int(input("Masukkan Banyak Potong = "))
    jumlah_harga = harga * banyak_potong
    print("%i \t %s \t\t %i \t\t %i \t\t Rp.%i" % (jenis_ke,jenis_potong,harga,banyak_potong,jumlah_harga))
    jumlah_bayar = jumlah_bayar + jumlah_harga
    jenis_ke = jenis_ke + 1
print("="*70)
print("\t\t\t\t Jumlah Bayar \t = \t Rp.%i" % (jumlah_bayar))
pajak = jumlah_bayar*10/100
print("\t\t\t\t Pajak \t\t = \t Rp.%i" % (pajak))
total_bayar = jumlah_bayar + pajak
print("\t\t\t\t Total Bayar \t = \t Rp.%i" % (total_bayar))"""