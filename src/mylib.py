def inputBuah(nama, stock, harga):
    """Fungsi meminta user untuk input jumlah buah
    dan menghitung harganya.

    Args:
        nama (string): nama buah yang akan di beli
        stock (interger): stock buah yang akan di beli
        harga (interger): harga buah per kg

    reTurns:
        nBuah (interger):Jumlah buah yang di pesan
        hargaBuah (interger):Total harga buah
    """

    #Minta input jumlah buah apel
    while True:
        #input jumlah 
        nBuah = int(input(f'masukan jumlah {nama}: '))

        #membandingkan antara jumlah dan permintaan stock
        if nBuah > stock:
            print(f'jumlah terlalu banyak, stock tersisa {stock} buah')
            continue

    #Berhenti minta input, Ketika jumlah permintaan terpenuhi
        break

    #Hitung total harga untuk buah tersebut
    hargaBuah = nBuah * harga

    return nBuah, hargaBuah