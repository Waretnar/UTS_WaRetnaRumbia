buku = ["{0. Hujan: Harga 20000}", 
"{1. Pergi: Harga 25000}",
"{2. Arah Langkah: Harga 30000}",
"{3. NKCTHI: Harga 50000}", 
"{4. Galaksi: Harga 100000}"]
a=int(input( "Jika ke Pembelian Tekan 1 Dan Jika ke Admin Tekan 2 : "))
if a == 1:
    print ("--------------------------------------------------------")
    print ("Selamat Datang Pada Aplikasi Penjualan Buku 'TOKO RETNA'")
    print ("--------------------------------------------------------")
    b = input("Apakah anda ingin membeli buku? (input Ya): ")
    if b in ["ya", "YA"]:
        print ("Berikut kami tampilkan judul-judul buku yang tersedia: ")
        print("=======================================================")
        for x in buku:
            print(x)
        pilih = int(input("Masukan nomor buku yang ingin anda beli: "))
        if pilih == 0:
            harga = 20000
            print("Buku yang anda beli : \n",buku[0])
            print("==================================")
            tanya =str(input("Apakah anda ingin membeli buku lagi?,jika iya masukkan nomor buku, jika tidak ketik tidak :"))
            if tanya == "1":
                harga = 45000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[0],buku[1])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif tanya == "2":
                harga = 50000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[0],buku[2])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif  tanya == "3":
                harga = 70000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[0],buku[3])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif tanya == "4":
                harga = 120000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[0],buku[4])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif tanya == "tidak":
                harga = 20000
                jum = 1
                print("============================================")
                print("Buku yang anda beli :",buku[0])
                bayar = int(input("Jumlah Uang :"))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali) 
        elif pilih == 1:
            harga = 25000
            print("Buku yang anda beli : \n",buku[1])
            print("====================================================")
            tanya =str(input("Apakah anda ingin membeli buku lagi?,jika iya masukkan nomor buku, jika tidak ketik tidak :"))
            if tanya == "2":
                harga = 55000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[1],buku[2])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif tanya == "3":
                harga = 75000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[1],buku[3])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif  tanya == "4":
                harga = 125000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[1],buku[4])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif tanya == "0":
                harga = 45000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[1],buku[0])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif tanya == "tidak":
                harga = 25000
                jum = 1
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[1])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
        elif pilih == 2:
            harga = 30000
            print("Buku yang anda beli : \n",buku[2])
            print("====================================================")
            tanya =str(input("Apakah anda ingin membeli buku lagi?,jika iya masukkan nomor buku, jika tidak ketik tidak :"))
            if tanya == "3":
                harga = 80000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[2],buku[3])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif tanya == "4":
                harga = 130000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[2],buku[4])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif tanya == "0":
                harga = 50000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[2],buku[0])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif tanya == "1":
                harga = 55000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[2],buku[1])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif tanya == "tidak":
                harga = 30000
                jum = 1
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[2])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
        elif pilih == 3:
            harga = 50000
            print("Buku yang anda beli : \n",buku[3])
            print("====================================================")
            tanya =str(input("Apakah anda ingin membeli buku lagi?,jika iya masukkan nomor buku, jika tidak ketik tidak :"))
            if tanya == "4":
                harga = 150000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[3],buku[4])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif  tanya == "0":
                harga = 70000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[3],buku[0])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif  tanya == "1":
                harga = 75000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[3],buku[1])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif  tanya == "2":
                harga = 80000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[3],buku[2])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif  tanya == "tidak":
                harga = 50000
                jum = 1
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[3])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
        elif pilih == 4:
            harga = 100000
            print("Buku yang anda beli : \n",buku[4])
            print("====================================================")
            tanya =str(input("Apakah anda ingin membeli buku lagi?,jika iya masukkan nomor buku, jika tidak ketik tidak :"))
            if  tanya == "0":
                harga = 120000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[4],buku[0])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif  tanya == "1":
                harga = 125000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[4],buku[1])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif  tanya == "2":
                harga = 130000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[4],buku[2])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif  tanya == "3":
                harga = 150000
                jum = 2
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[4],buku[3])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            elif  tanya == "tidak":
                harga = 100000
                jum = 1
                print("============================================")
                print("Pembelian buku dibatasi, maxsimal dua buku ")
                print("Buku yang anda beli :",buku[4])
                print("============================================")
                bayar = int(input("Jumlah Uang: "))
                kembali = bayar - harga
                print("Total Buku :", jum)
                print("Pembayaran :", harga)
                print("Kembalian :", kembali)
            else:
                print("Nomor yang anda masukkan salah")
        else:
            print("Angka yang anda masukkan tidak tercantum pada nomor buku")
            print("Silahkan memulai kembali!")
elif a == 2:
    print ("-------------------------------------------------------------")
    print ("Selamat Datang Admin Pada Aplikasi Penjualan Buku 'TOKO RETNA'")
    print ("--------------------------------------------------------------")
    print("Stok buku")
    print(buku)
    print("==============================================================================================================================")
    print("Jikan admin ingin menambah data tekan 1, jika ingin mengubah tekan 2, dan jika ingin menghapus tekan 3")
    pilih = int(input("Masukan pilihan Admin :"))
    if pilih == 1:
        print("Admin akan menambahkan stok buku, dengan mengikuti format berikut")
        print("{Nomor Buku, Nama Buku, Harga Buku : diisi}")
        stok = str(input("Masukan Stok : "))
        buku.append(stok)
        print(buku)
    elif pilih == 2:
        print("Admin akan mengubah stok buku")
        ubh = int(input("Masukan nomor buku yang ingin diubah ? 0, 1, 2, 3, 4 :"))
        print("Buku yang akan Admin ubah :", buku[ubh])
        print("Masukkan format pengisian yaitu nomor, nama dan harga ")
        ganti = str(input("Masukan nomor buku, nama buku dan harga buku yang admin ganti:"))
        buku[ubh]=ganti
        print("anda mengubah buku pertama dengan", ganti)
        print(buku)
    elif pilih == 3:
        print("Admin Akan menghapus stok buku")
        hps = int(input("Masukkan nomor buku yang ingin admin hapus 0,1,2,3,4:"))
        if hps == 0:
            del buku[hps]
            print(buku)
        elif hps == 1:
            del buku[hps]
            print(buku)
        elif hps == 2:
            del buku[hps]
            print(buku)
        elif hps == 3:
            del buku[hps]
            print(buku)
        elif hps == 4:
            del buku[hps]
            print(buku)
        else:
            print("Admin memasukkan nomor yang tidak tersedia!")
            print("Silahkan login kembali !")