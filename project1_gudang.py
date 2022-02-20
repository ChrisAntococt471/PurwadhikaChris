# stokbarang=[{
#     'kode': 'A01',
#     'nama': 'Kain A1',
#     'stock': 20,
#     'harga': 10000},
#     {
#     'kode': 'A02',
#     'nama': 'Kain A2',
#     'stock': 15,
#     'harga': 15000},
#     {
#     'kode': 'B01',
#     'nama': 'Kain B1',
#     'stock': 25,
#     'harga': 20000}
# ]

# def tampilListBarang() :

#     while True :
#         menu1 = input('''
#         Data Stok Barang

#         List Menu :
#         1. Menampilkan Daftar Barang
#         2. Menampilkan Daftar Barang Tertentu
#         3. Kembali ke Menu Utama

#         Masukkan angka Menu yang ingin dijalankan : ''')

#         if (menu1=="1"):
#             print('===============')
#             print('Daftar Barang')
#             print('===============')  
#             print('Kode \t| Nama Barang \t| Stock \t| Harga')    
#             for i in range(len(stokbarang)) :
#                 print('{} \t| {} \t| {} \t\t| {}'.format(stokbarang[i]['kode'],stokbarang[i]['nama'],stokbarang[i]['stock'],stokbarang[i]['harga']))

#         elif (menu1=="2"):
#             if len(stokbarang)!=0:
#                 kode = input('\tMasukkan Kode Barang : ')
#                 for i in stokbarang:
#                     if i['kode']==kode:
#                         print('===============')
#                         print('Daftar Barang')
#                         print('===============')  
#                         print('Kode \t| Nama Barang \t| Stock \t| Harga')  
#                         print(f"{i['kode']} \t| {i['nama']} \t| {i['stock']} \t\t| {i['harga']}") 
#                         break
#                     else:
#                         print("\tBarang tidak tersedia")
#                         break

#         elif (menu1=='3'):
#             break

#         else:
#             print("\tMenu yang anda masukkan salah.")    

# def tambahBarang() :
#     while True :
#         menu2 = input('''
#         Edit Stok Barang

#         List Menu :
#         1. Menambah Daftar Barang
#         2. Update Data Barang
#         3. Menghapus Data Barang
#         4. Kembali ke Menu Utama

#         Masukkan angka Menu yang ingin dijalankan : ''')

#         if (menu2=="1"):
#             for i in stokbarang:
#                 kodebarang = input('Masukkan Kode Barang : ')
#                 namabarang = input('Masukkan Nama Barang : ')
#                 stockbarang = int(input('Masukkan Stock Barang : '))
#                 hargabarang = int(input('Masukkan Harga Barang : '))
#                 stokbarang.append({
#                     'kode': kodebarang,
#                     'nama': namabarang,
#                     'stock': stockbarang,
#                     'harga': hargabarang
#                     })
#                 if any (d['kode']==kodebarang for d in stokbarang):
#                     print("\tBarang sudah ada di daftar")
#                     break
#                 checker = input('\tSimpan data? (ya/tidak) = ')
#                 if(checker == 'ya') :
#                     print ("\tData Tersimpan")
#                     break
#                 if(checker == 'tidak') :
#                     break
#         elif (menu2=="2"): 
#             kodebarang = input('\tMasukkan Kode Barang : ')
#             for i in stokbarang:
#                 if not any (d['kode']==kodebarang for d in stokbarang):
#                     print("Barang tidak ada")
#                     break
#                 if any (d['kode']==kodebarang for d in stokbarang):
#                    updatestock = int(input('\tMasukkan Update Stock Barang : ')) 
                
                          
#         elif (menu2=="4"):              
#             break  
#         else:
#             print("Menu yang Anda masukkan salah.")


# while True :
#     pilihanMenu = input('''
#         Gudang Karya Stock System

#         List Menu :
#         1. Menampilkan Daftar Barang
#         2. Edit Stok Barang
#         3. Exit Program

#         Masukkan angka Menu yang ingin dijalankan : ''')

#     if(pilihanMenu == '1') :
#         tampilListBarang()
#     elif(pilihanMenu == '2') :
#         tambahBarang()
#     elif(pilihanMenu=='3'):
#         break
#     else:
#         print("\tMenu yang Anda masukkan tidak tersedia.")     
# 
# 
# 
# kode={'1':'A01','2':'A02','3':'A03'}

nama={'A01':'Kain A1','A02':'Kain A2','A03':'Kain B1'}
stok={'A01': 20,'A02': 15,'A03':25}
harga={'A01': 20000,'A02': 15000,'A03':25000}

# print('\tDaftar Barang')
# print('\t===============')
# print('\tKode Barang : {}'.format(list(nama.keys())))  
# print('\tNama Barang : {}'.format(nama))
# print('\tStok Barang : {}'.format(stok))
# print('\tHarga Barang : {}'.format(harga))
# kodeinput = input('\tMasukkan Kode Barang : ')
# print("Kode : ",kodeinput," Nama : ",nama.get(kodeinput)," Stok : ",stok.get(kodeinput)," Harga : ",harga.get(kodeinput))   