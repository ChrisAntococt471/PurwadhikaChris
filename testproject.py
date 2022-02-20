# nama={'A01':'Kain A1','A02':'Kain A2','A03':'Kain A3'}
# stok={'A01': 20,'A02': 15,'A03':25}
# harga={'A01': 20000,'A02': 15000,'A03':25000}

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
#             print('\t===============')
#             print('\tDaftar Barang')
#             print('\t===============')
#             print('\tKode Barang : {}'.format(list(nama.keys())))  
#             print('\tNama Barang : {}'.format(nama))
#             print('\tStok Barang (Unit) : {}'.format(stok))
#             print('\tHarga Barang (Rp) : {}'.format(harga))
#         elif (menu1=="2"):    
#            kodeinput = input('\tMasukkan Kode Barang : ')
#            if(kodeinput in nama):
#                print("\tKode : ",kodeinput," Nama : ",nama.get(kodeinput)," Stok : ",stok.get(kodeinput)," Harga : ",harga.get(kodeinput))
#            elif not(kodeinput in nama):
#                print("\t****Barang tidak tersedia****")
#                continue
#         elif (menu1=='3'):
#             break
#         else:
#             print("\t****Menu yang anda masukkan salah****")        

# def tambahBarang() :
#     while True :
#         menu2 = input('''
#         Tambah Daftar Barang

#         List Menu :
#         1. Menambah Daftar Barang Baru
#         2. Kembali ke Menu Utama

#         Masukkan angka Menu yang ingin dijalankan : ''')

#         if (menu2=="1"):
#             kodebarang = input('\tMasukkan Kode Barang : ')
#             if kodebarang in nama.keys():
#                 print("\t****Barang sudah ada di daftar****")
#                 continue
#             if (len(kodebarang))<3:
#                 print("\t****Kode tidak valid****")
#                 continue
#             namabarang = input('\tMasukkan Nama Barang : ')
#             if namabarang in nama.values():
#                 print("\t****Barang sudah ada di daftar****")
#                 continue
#             try:            
#                 stockbarang = int(input('\tMasukkan Stock Barang : '))
#                 if stockbarang<0:
#                     print("\t****Data tidak valid. Stok tidak mungkin negatif****")
#                     continue
#                 hargabarang = int(input('\tMasukkan Harga Barang : '))
#                 if hargabarang<0:
#                     print("\t****Data tidak valid. Harga tidak mungkin negatif****")
#                     continue   
#                 nama.update({kodebarang:namabarang})
#                 stok.update({kodebarang:stockbarang})
#                 harga.update({kodebarang:hargabarang})
#                 print("\n\tKode : ",kodebarang," Nama : ",nama.get(kodebarang)," Stok : ",stok.get(kodebarang)," Harga : ",harga.get(kodebarang))
#                 while True:
#                     checker = input('\tSimpan data? (y/n) = ')
#                     if(checker == 'n'or checker=='N') :
#                         del nama[kodebarang]
#                         del stok[kodebarang]
#                         del harga[kodebarang]
#                         print('\t****Data tidak tersimpan****')
#                         break
#                     if(checker == 'y'or checker=='Y') :
#                         print ("\t****Data Tersimpan****")
#                         break
#                 continue
#             except ValueError:
#                 print("\t****Data tidak valid****") 
#                 continue 

#         if (menu2=="2"): 
#             break

#         else:
#             print("\t****Menu yang anda masukkan salah****")    

# def editBarang() :
#     while True :
#         menu3 = input('''
#         Edit Daftar Barang

#         List Menu :
#         1. Update Daftar Barang
#         2. Kembali ke Menu Utama

#         Masukkan angka Menu yang ingin dijalankan : ''')

#         if (menu3=="1"):            
#             kodebarang = input('\tMasukkan Kode Barang : ')
#             if kodebarang not in nama.keys():
#                 print("\t****Barang tidak ada di daftar****")
#                 continue
#             print("\tKode : ",kodebarang," Nama : ",nama.get(kodebarang)," Stok : ",stok.get(kodebarang)," Harga : ",harga.get(kodebarang))  

#             while True:
#                 varinput=input("\tMasukkan variabel yang akan diubah (nama/stok/harga) : ")
                
#                 if (varinput=='stok'):
#                     while True:  
#                         checkerstok = input('\n\tUpdate data stok? (y/n) = ')
#                         if(checkerstok =='y'or checkerstok=='Y') :
#                             while True:
#                                 try:
#                                     stockbarang = int(input('\tMasukkan stok barang : '))
#                                     while True:
#                                         checker1 = input('\n\tSimpan data stok? (y/n) = ')
#                                         if(checker1 =='y'or checker1=='Y') :
#                                             stok.update({kodebarang:stockbarang})
#                                             print ("\t****Data tersimpan****")
#                                             break
#                                         elif(checker1 == 'n'or checker1 == 'N') :
#                                             print('\t****Data tidak tersimpan****')
#                                             break
#                                         elif stockbarang<0:
#                                             print("\n\t****Data tidak valid. Stok tidak mungkin negatif****")
#                                         else:
#                                             print("\t****Menu yang anda masukkan salah****")  
#                                             continue 
#                                     break                   
#                                 except ValueError:
#                                     print("\t****Data tidak valid****") 
#                                     continue
#                             break            
#                         elif(checkerstok =='n' or checkerstok =='N') :
#                             print("\t****Data stok tidak diupdate****")
#                             break
#                         else:
#                             print("\t****Menu yang anda masukkan salah****")  
#                             continue                  
#                     break        
#             #     if (varinput=='harga'):
#             #         checkerharga = input('\n\tUpdate data harga? (y/n) = ') 
#             #         if(checkerharga =='y'or checkerharga =='Y') :  
#             #             try:                 
#             #                 hargabarang = int(input('\tMasukkan harga barang : '))
#             #                 checker2 = input('\n\tSimpan data harga? (y/n) = ')
#             #                 if(checker2 =='y'or checker2 =='Y') :
#             #                     harga.update({kodebarang:hargabarang})
#             #                     print ("\t****Data tersimpan****")
#             #                     break
#             #                 elif(checker2 == 'n'or checker2 == 'N') :
#             #                     print('\t****Data tidak tersimpan****')
#             #                     break
#             #                 elif hargabarang<0:
#             #                     print("\n\t****Data tidak valid. Harga tidak mungkin negatif****") 
#             #             except ValueError:
#             #                 print("\t****Data tidak valid****") 
#             #                 continue          
#             #         elif(checkerharga =='n'or checkerharga =='N') :
#             #             print("\t****Data harga tidak diupdate****")
#             #             break
#             #         else:
#             #             print("\t****Menu yang anda masukkan salah****")  
#             #             continue  
                         
#             #     if (varinput=='nama'):
#             #         checkernama = input('\n\tUpdate nama barang? (y/n) = ') 
#             #         if(checkernama =='y'or checkernama =='Y') :                   
#             #             namabarang = (input('\tMasukkan nama barang : '))
#             #             checker3 = input('\n\tSimpan nama barang? (y/n) = ')
#             #             if(checker3 =='y'or checker3 =='Y') :
#             #                 nama.update({kodebarang:namabarang})
#             #                 print ("\t****Data tersimpan****")
#             #                 break
#             #             elif(checker3 == 'n'or checker3 == 'N') :
#             #                 print('\t****Data tidak tersimpan****')
#             #                 break
#             #             else:
#             #                 print("\t****Menu yang anda masukkan salah****")  
#             #                 continue 
#             #         elif(checkernama =='n'or checkernama =='N') :
#             #             print("\t****Nama barang tidak diupdate****")
#             #             break
#             #         else:
#             #             print("\t****Menu yang anda masukkan salah****")  
#             #             continue 

#             #     else:
#             #         print("\t****Menu yang anda masukkan salah****")  
#             #         continue         
                
#             # continue 

#         if (menu3=="2"): 
#             break
#         else:
#             print("\t****Menu yang anda masukkan salah****")
#             continue    

# # def hapusBarang() :
# #     while True :
# #         menu4 = input('''
# #         Hapus Daftar Barang

# #         List Menu :
# #         1. Hapus Daftar Barang
# #         2. Kembali ke Menu Utama

# #         Masukkan angka Menu yang ingin dijalankan : ''')

# #         if (menu4=="1"):  
# #             kodebarang = input('\tMasukkan Kode Barang : ')
# #             if kodebarang in nama.keys(): 
# #                 print("\tKode : ",kodebarang," Nama : ",nama.get(kodebarang)," Stok : ",stok.get(kodebarang)," Harga : ",harga.get(kodebarang))
# #             if kodebarang not in nama.keys():     
# #                 print("\t****Barang tidak ada di daftar****")
# #                 continue
# #             while True:
#                 checkerdelete = input('\n\tHapus data? (y/n) = ')
#                 if (checkerdelete=='y'or checkerdelete=='Y'):
#                     del nama[kodebarang]
#                     del stok[kodebarang]
#                     del harga[kodebarang]
#                     print("\t****Data telah dihapus****") 
#                     break
#                 elif (checkerdelete=='n'or checkerdelete=='N'):
#                     print("\t****Data tidak jadi dihapus****") 
#                     break
#                 else:
#                     print("\tMenu yang anda masukkan salah")  
#                     continue 
#             continue
#         if (menu4=="2"): 
#             break
#         else:
#             print("\t****Menu yang anda masukkan salah****")     

# while True :
#     MenuUtama = input('''
#         Gudang Karya Stock System

#         List Menu :
#         1. Daftar Inventori Barang
#         2. Tambah Barang Baru
#         3. Edit Daftar Barang
#         4. Hapus Daftar Barang
#         5. Exit Program

#         Masukkan angka Menu yang ingin dijalankan : ''')

#     if(MenuUtama == '1') :
#         tampilListBarang()
#     elif(MenuUtama=='2'):
#         tambahBarang()    
#     elif(MenuUtama=='3'):
#         editBarang()
#     # elif(MenuUtama=='4'):
#     #     hapusBarang()
#     elif(MenuUtama=='5'):
#         print('\n\tTerima kasih. Sampai jumpa')
#         break
#     else:
#         print("\n\t****Menu yang Anda masukkan tidak tersedia****") 


# nama={'A01':'Kain A1','A02':'Kain A2','A03':'Kain A3'}
# stok={'A01': 20,'A02': 15,'A03':25}
# harga={'A01': 20000,'A02': 15000,'A03':25000}

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
#             print('\t===============')
#             print('\tDaftar Barang')
#             print('\t===============')
#             print('\tKode Barang : {}'.format(list(nama.keys())))  
#             print('\tNama Barang : {}'.format(nama))
#             print('\tStok Barang (Unit) : {}'.format(stok))
#             print('\tHarga Barang (Rp) : {}'.format(harga))
#         elif (menu1=="2"):    
#            kodeinput = input('\tMasukkan Kode Barang : ')
#            if(kodeinput in nama):
#                print("\tKode : ",kodeinput," Nama : ",nama.get(kodeinput)," Stok : ",stok.get(kodeinput)," Harga : ",harga.get(kodeinput))
#            elif not(kodeinput in nama):
#                print("\t****Barang tidak tersedia****")
#                continue
#         elif (menu1=='3'):
#             break
#         else:
#             print("\t****Menu yang anda masukkan salah****")        

# def tambahBarang() :
#     while True :
#         menu2 = input('''
#         Tambah Daftar Barang

#         List Menu :
#         1. Menambah Daftar Barang Baru
#         2. Kembali ke Menu Utama

#         Masukkan angka Menu yang ingin dijalankan : ''')

#         if (menu2=="1"):
#             kodebarang = input('\tMasukkan Kode Barang : ')
#             if kodebarang in nama.keys():
#                 print("\t****Barang sudah ada di daftar****")
#                 continue
#             if (len(kodebarang))<3:
#                 print("\t****Kode tidak valid****")
#                 continue
#             namabarang = input('\tMasukkan Nama Barang : ')
#             if namabarang in nama.values():
#                 print("\t****Barang sudah ada di daftar****")
#                 continue
#             try:            
#                 stockbarang = int(input('\tMasukkan Stock Barang : '))
#                 if stockbarang<0:
#                     print("\t****Data tidak valid. Stok tidak mungkin negatif****")
#                     continue
#                 hargabarang = int(input('\tMasukkan Harga Barang : '))
#                 if hargabarang<0:
#                     print("\t****Data tidak valid. Harga tidak mungkin negatif****")
#                     continue   
#                 nama.update({kodebarang:namabarang})
#                 stok.update({kodebarang:stockbarang})
#                 harga.update({kodebarang:hargabarang})
#                 print("\n\tKode : ",kodebarang," Nama : ",nama.get(kodebarang)," Stok : ",stok.get(kodebarang)," Harga : ",harga.get(kodebarang))
#                 while True:
#                     checker = input('\tSimpan data? (y/n) = ')
#                     if(checker == 'n'or checker=='N') :
#                         del nama[kodebarang]
#                         del stok[kodebarang]
#                         del harga[kodebarang]
#                         print('\t****Data tidak tersimpan****')
#                         break
#                     if(checker == 'y'or checker=='Y') :
#                         print ("\t****Data Tersimpan****")
#                         break
#                 continue
#             except ValueError:
#                 print("\t****Data tidak valid****") 
#                 continue 

#         if (menu2=="2"): 
#             break

#         else:
#             print("\t****Menu yang anda masukkan salah****")    

# def editBarang() :
#     while True :
#         menu3 = input('''
#         Edit Daftar Barang

#         List Menu :
#         1. Update Daftar Barang
#         2. Kembali ke Menu Utama

#         Masukkan angka Menu yang ingin dijalankan : ''')

#         if (menu3=="1"):            
#             kodebarang = input('\tMasukkan Kode Barang : ')
#             if kodebarang not in nama.keys():
#                 print("\t****Barang tidak ada di daftar****")
#                 continue
#             print("\tKode : ",kodebarang," Nama : ",nama.get(kodebarang)," Stok : ",stok.get(kodebarang)," Harga : ",harga.get(kodebarang))  

#             while True:
#                 varinput=input("\tMasukkan variabel yang akan diubah (nama/stok/harga) : ")
                
#                 if (varinput=='stok'):
#                     checkerstok = input('\n\tUpdate data stok? (y/n) = ')    
#                     if(checkerstok =='y'or checkerstok=='Y') :
#                         try:
#                             stockbarang = int(input('\tMasukkan stok barang : '))
#                             checker1 = input('\n\tSimpan data stok? (y/n) = ')
#                             if(checker1 =='y'or checker1=='Y') :
#                                 stok.update({kodebarang:stockbarang})
#                                 print ("\t****Data tersimpan****")
#                                 break
#                             elif(checker1 == 'n'or checker1 == 'N') :
#                                 print('\t****Data tidak tersimpan****')
#                                 break
#                             elif stockbarang<0:
#                                 print("\n\t****Data tidak valid. Stok tidak mungkin negatif****")   
#                         except ValueError:
#                             print("\t****Data tidak valid****") 
#                             continue        
#                     elif(checkerstok =='n' or checkerstok =='N') :
#                         print("\t****Data stok tidak diupdate****")
#                         break
#                     else:
#                         print("\t****Menu yang anda masukkan salah****")  
#                         continue                  

#                 if (varinput=='harga'):
#                     checkerharga = input('\n\tUpdate data harga? (y/n) = ') 
#                     if(checkerharga =='y'or checkerharga =='Y') :  
#                         try:                 
#                             hargabarang = int(input('\tMasukkan harga barang : '))
#                             checker2 = input('\n\tSimpan data harga? (y/n) = ')
#                             if(checker2 =='y'or checker2 =='Y') :
#                                 harga.update({kodebarang:hargabarang})
#                                 print ("\t****Data tersimpan****")
#                                 break
#                             elif(checker2 == 'n'or checker2 == 'N') :
#                                 print('\t****Data tidak tersimpan****')
#                                 break
#                             elif hargabarang<0:
#                                 print("\n\t****Data tidak valid. Harga tidak mungkin negatif****") 
#                         except ValueError:
#                             print("\t****Data tidak valid****") 
#                             continue          
#                     elif(checkerharga =='n'or checkerharga =='N') :
#                         print("\t****Data harga tidak diupdate****")
#                         break
#                     else:
#                         print("\t****Menu yang anda masukkan salah****")  
#                         continue  
                         
#                 if (varinput=='nama'):
#                     checkernama = input('\n\tUpdate nama barang? (y/n) = ') 
#                     if(checkernama =='y'or checkernama =='Y') :                   
#                         namabarang = (input('\tMasukkan nama barang : '))
#                         checker3 = input('\n\tSimpan nama barang? (y/n) = ')
#                         if(checker3 =='y'or checker3 =='Y') :
#                             nama.update({kodebarang:namabarang})
#                             print ("\t****Data tersimpan****")
#                             break
#                         elif(checker3 == 'n'or checker3 == 'N') :
#                             print('\t****Data tidak tersimpan****')
#                             break
#                         else:
#                             print("\t****Menu yang anda masukkan salah****")  
#                             continue 
#                     elif(checkernama =='n'or checkernama =='N') :
#                         print("\t****Nama barang tidak diupdate****")
#                         break
#                     else:
#                         print("\t****Menu yang anda masukkan salah****")  
#                         continue 

#                 else:
#                     print("\t****Menu yang anda masukkan salah****")  
#                     continue         
                
#             continue 

#         if (menu3=="2"): 
#             break
#         else:
#             print("\t****Menu yang anda masukkan salah****")
#             continue    

# def hapusBarang() :
#     while True :
#         menu4 = input('''
#         Hapus Daftar Barang

#         List Menu :
#         1. Hapus Daftar Barang
#         2. Kembali ke Menu Utama

#         Masukkan angka Menu yang ingin dijalankan : ''')

#         if (menu4=="1"):  
#             kodebarang = input('\tMasukkan Kode Barang : ')
#             if kodebarang in nama.keys(): 
#                 print("\tKode : ",kodebarang," Nama : ",nama.get(kodebarang)," Stok : ",stok.get(kodebarang)," Harga : ",harga.get(kodebarang))
#             if kodebarang not in nama.keys():     
#                 print("\t****Barang tidak ada di daftar****")
#                 continue
#             while True:
#                 checkerdelete = input('\n\tHapus data? (y/n) = ')
#                 if (checkerdelete=='y'or checkerdelete=='Y'):
#                     del nama[kodebarang]
#                     del stok[kodebarang]
#                     del harga[kodebarang]
#                     print("\t****Data telah dihapus****") 
#                     break
#                 elif (checkerdelete=='n'or checkerdelete=='N'):
#                     print("\t****Data tidak jadi dihapus****") 
#                     break
#                 else:
#                     print("\tMenu yang anda masukkan salah")  
#                     continue 
#             continue
#         if (menu4=="2"): 
#             break
#         else:
#             print("\t****Menu yang anda masukkan salah****")     

# while True :
#     MenuUtama = input('''
#         Gudang Karya Stock System

#         List Menu :
#         1. Daftar Inventori Barang
#         2. Tambah Barang Baru
#         3. Edit Daftar Barang
#         4. Hapus Daftar Barang
#         5. Exit Program

#         Masukkan angka Menu yang ingin dijalankan : ''')

#     if(MenuUtama == '1') :
#         tampilListBarang()
#     elif(MenuUtama=='2'):
#         tambahBarang()    
#     elif(MenuUtama=='3'):
#         editBarang()
#     elif(MenuUtama=='4'):
#         hapusBarang()
#     elif(MenuUtama=='5'):
#         print('\n\tTerima kasih. Sampai jumpa')
#         break
#     else:
#         print("\n\t****Menu yang Anda masukkan tidak tersedia****") 

a=int(input("Cek:"))
print(a)