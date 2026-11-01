#Array untuk menyimpan data kode barang, nama barang, harga barang, stok barang, dan pecahan uang
kode_barang = [1, 2, 3, 4, 5]
nama_barang = ["Kopi Kenagan", "Aqua", "Nipis Madu", "Sari Roti", "Chitato"]
harga_barang = [10000, 3000, 10000, 5000, 4000]
stok_barang = [50, 30, 35, 45, 50]
pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]

#Menampilkan tulisan selamat datang dan menanyakan apakah ingin membeli atau tidak
print("=========================================================")
print("| Selamat datang di Vending Machine Makanan dan Minuman |")
print("=========================================================")
pilihan = input("Apakah Anda ingin membeli Makanan atau Minuman [ya/tidak] : ")
print()

#Perulangan pembelian barang
while pilihan == "ya":

    #Menampilkan kode barang, nama barang, harga barang, dan stok barang serta memilih kode barang yang akan dibeli
    print("=========================================")
    print("|        Daftar Makan dan Minuman       |")
    print("=========================================")
    print("| Kode | Nama barang   | Harga   | Stok |")
    print(f"|   1  | Kopi Kenangan | Rp10000 | {stok_barang[0]}   |")
    print(f"|   2  | Aqua          | Rp3000  | {stok_barang[1]}   |")
    print(f"|   3  | Nipis Madu    | Rp10000 | {stok_barang[2]}   |")
    print(f"|   4  | Sari Roti     | Rp5000  | {stok_barang[3]}   |")
    print(f"|   5  | Chitato       | Rp4000  | {stok_barang[4]}   |")
    print("=========================================")
    kode = int(input("Masukkan Kode barang yang ingin dibeli: "))
    print()

    # Pengecekan kode barang
    if kode in kode_barang:
        i = kode - 1

        #Pengecekan stok barang
        if stok_barang[i]>0:
            print("Barang yang Anda pilih tersedia")
            print("Anda memilih barang", nama_barang[i], "dengan harga Rp", harga_barang[i])

            batal = False
            berhasil = False
            
            #Perulangan pembayaran
            while not berhasil and not batal:
            
                #Pemilihan Pembayaran
                print("================================")
                print("|   1  | Cash                  |")
                print("|   2  | E-Money               |")
                print("|   3  | Qris                  |")
                print("|   4  | Batalkan transaksi    |")
                print("================================")
                metode = int(input("Masukkan kode pembayaran yang dipilih : "))
                print()

                #Pembayaran Cash
                if metode == 1:
                    uang = int(input("Silahkan masukkan uang untuk proses pembayaran : Rp"))
                    if uang < harga_barang[i] :
                        kekurang_uang = harga_barang[i] - uang
                        print("Uang Anda kurang silahkan masukkan kekurangan sebesar Rp", kekurang_uang)
                        tambahan_uang = int(input("Masukkan kekurangan uang: Rp"))
                        uang = uang + tambahan_uang
                    if uang < harga_barang[i] :
                            print("Uang Anda masih kurang, silahkan ambil kembali uang Anda sebesar Rp", uang)
                            print("Silakan pilih metode pembayaran lain atau batalkan transaksi.")
                    else:
                        berhasil = True

                            #Menghitung rincian uang kembalian dan pecahannya   
                        if uang > harga_barang[i] :
                            kembalian_uang = uang - harga_barang[i]
                            print("Kembalian anda sebesar sebesar Rp", kembalian_uang)
                            print("Rincian kembalian:")
                            
                            #perulangan rincian kembalian
                            for pecahan in pecahan_uang:
                                jumlah = kembalian_uang // pecahan
                                if jumlah > 0:
                                    if pecahan >= 1000:
                                        print("-", jumlah, "lembar Rp", pecahan)
                                    else:
                                        print("-", jumlah, "keping Rp", pecahan)
                                    kembalian_uang = kembalian_uang % pecahan


                #Pembayaran E-money
                elif metode == 2:
                    print("Silahkan tempelkan kartu e-money Anda")
                    saldo_emoney = int(input("Saldo e-money Anda : Rp"))
                    if saldo_emoney >= harga_barang[i]:
                        saldo_emoney = saldo_emoney - harga_barang[i]
                        print("Pembayaran e-money berhasil. Sisa saldo : Rp", saldo_emoney)
                        berhasil = True
                    else :
                        print("Maaf saldo e-money Anda kurang.")
                        print("Silakan pilih metode pembayaran lain atau batalkan transaksi.")

                #Pembayaran Qris
                elif metode == 3 :
                    print("Silahkan pindai kode QRIS pada layar untuk membayar sebesar Rp", harga_barang[i])
                    konfirmasi = input("Apakah pembayaran sudah selesai? [ya/tidak] : ")
                    if konfirmasi == "ya":
                        print("Pembayaran QRIS berhasil")
                        berhasil = True
                    else:
                        print("Pembayaran QRIS dibatalkan")
                        print("Silakan pilih metode pembayaran lain atau batalkan transaksi.")

                #Membatalkan transaksi
                elif metode == 4:
                    batal = True

                #Jika kode pembayaran yang dimasukkan salah
                else:
                    print("Kode pembayaran yang Anda masukkan salah")

                #Pembaharuan stok jika pembayaran berhasil
                if berhasil:
                    stok_barang[i] = stok_barang[i] - 1
                    print("Silahkan ambil", nama_barang[i], "Anda. Terima kasih dan semoga hari Anda bahagia")
                else:
                    print("Transaksi dibatalkan")

        #Jika stok barang sudah habis
        else :
            print("Maaf, stok", nama_barang[i], "sedang habis")

    #Jika kode yang dimasukan salah
    else:
        print("Kode barang yang Anda masukkan salah")

    #Pembelian selesai dan menanyakan apakah ingin melakukan pembelian lagi
    pilihan = input("\nApakah Anda tertarik untuk membeli lagi? [ya/tidak] : ")
    print()

    #Perulangan pengecekan masukkan 
    while pilihan != "ya" and pilihan != "tidak":
        print("Pilihan yang Anda masukkan salah")
        pilihan = input("Apakah Anda tertarik untuk membeli lagi? [ya/tidak] : ")

#Jika pilihan yang dimasukkan tidak
if pilihan == "tidak":
    print("Terima kasih telah berkunjung")

#Jika pilihan yang dimasukkan bukan ya atau tidak
else:
    print("Pilihan yang Anda masukkan salah")