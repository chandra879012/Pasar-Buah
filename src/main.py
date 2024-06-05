print('Selamat Datang di Pasar Buah')

#minta input user
nApel= int(input('masukan jumlah Apel:'))
nJeruk= int(input('masukan jumlah Jeruk:'))
nAnggur= int(input('masukan jumlah Anggur:'))

#Definisikan harga buah
hargaApel =10000
hargaJeruk =15000
hargaAnggur =20000

#Hitung total harga per buah
totalHargaApel=nApel*hargaApel
totalHargaJeruk=nJeruk*hargaJeruk
totalHargaAnggur=nAnggur*hargaAnggur

#hitung total harga belanja
totalBelanja=totalHargaApel+totalHargaJeruk+totalHargaAnggur

#Tampilkan rincian belanja
print(f'''
Detail Belanja
Apel: {nApel}x{hargaApel} = {totalHargaApel}
Jeruk: {nJeruk}x{hargaJeruk} = {totalHargaJeruk}
Anggur: {nAnggur}x{hargaAnggur} = {totalHargaAnggur}
total:{totalBelanja}
''')