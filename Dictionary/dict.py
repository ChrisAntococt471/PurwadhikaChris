listbuah=[{
    "Nama" : "Apel",
    "Stock" : 20,
    "Harga" : 10000
},
{
    "Nama" : "Jeruk",
    "Stock" : 15,
    "Harga" : 15000
},
{
    "Nama" : "Anggur",
    "Stock" : 25,
    "Harga" : 20000
}]
while (True):
    pilihanmenu=input('''
        Selamat Datang di Pasar Buah
        
        List Menu:
        1. Menampilkan Daftar Buah
        2. Menambah Buah
        3. Menghapus Buah
        4. Membeli Buah
        5. Exit Program
        Masukkan angka Menu yang ingin dijalankan : ''')
    if (pilihanmenu=="1"):
        print("Daftar Buah\n")
        print("Index\t|Nama\t|Stock\t|Harga\t")
        for i in range(len(listbuah)):
            print("{}\t|{}\t|{}\t|{}".format(i,listbuah[i]['Nama'],listbuah[i]["Stock"],listbuah[i]["Harga"]))        
    elif (pilihanmenu=="2"):
        namabuah=input("Masukkan nama buah : ")
        stokbuah=input("Masukkan stok buah : ")
        hargabuah=input("Masukkan harga buah : ")
        listbuah.append({
            "Nama" : namabuah,
            "Stock" : stokbuah,
            "Harga" : hargabuah
        })
        print("Daftar Buah\n")
        print("Index\t|Nama\t|Stock\t|Harga\t")
        for i in range(len(listbuah)):
            print("{}\t|{}\t|{}\t|{}".format(i,listbuah[i]['Nama'],listbuah[i]["Stock"],listbuah[i]["Harga"]))
    elif(pilihanmenu=="3"):
        print("Daftar Buah\n")
        print("Index\t|Nama\t|Stock\t|Harga\t")
        for i in range(len(listbuah)):
            print("{}\t|{}\t|{}\t|{}".format(i,listbuah[i]['Nama'],listbuah[i]["Stock"],listbuah[i]["Harga"]))
        inputindex=int(input("Masukkan index buah yang akan dihapus : "))
        del listbuah[inputindex]
        for i in range(len(listbuah)):
            print("{}\t|{}\t|{}\t|{}".format(i,listbuah[i]['Nama'],listbuah[i]["Stock"],listbuah[i]["Harga"]))
    elif(pilihanmenu=="4"):
        print("Daftar Buah\n")
        print("Index\t|Nama\t|Stock\t|Harga\t")
        for i in range(len(listbuah)):
            print("{}\t|{}\t|{}\t|{}".format(i,listbuah[i]['Nama'],listbuah[i]["Stock"],listbuah[i]["Harga"]))
                                