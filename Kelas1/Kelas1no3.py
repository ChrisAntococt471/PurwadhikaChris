# def urutkan(list,terbalik=False):
#     if terbalik== False:
#         for i in range (len(list)-1):
#             for j in range (i+1,len(list)):
#                 if list[i]>list[j]:
#                     list[i],list[j]=list[j],list[i]
#     else:
#         for i in range (len(list)-1):
#             for j in range (i+1,len(list)):
#                 if list[i]<list[j]:
#                     list[i],list[j]=list[i],list[j]  
#     return list                             
# list1=[1,2,3,4]
# print(urutkan(list1))


# list1=[1,2,3,4,5]
# def kali(list):
#     kali=[]
#     for i in list:        
#         if i%2==0:
#             kali.append(i*2)
#         else:
#             kali.append(i*3)
#     return kali        
# print(kali(list1))

# def kali(angka):
#     if angka%2==0:
#         return angka*2
#     else:
#         return angka*3
# def ubah(angka):
#     return list(map(kali,angka))
# print(ubah(list1))

# ubahlist=map(lambda angka:angka*2 if angka%2==0 else angka*3,list1)
# print(list(ubahlist))


# buah=['pisang','melon','mangga','jeruk','kiwi','kelapa']
# # def cari(y,kata):
# #     return (list(filter(lambda x:y in x,kata)))
# # print(cari("e",buah))


# def factor(angka):
#     if angka==1:
#         return 1
#     return angka*factor(angka-1)
# print(factor(4))              


# def jumlah(angka):
#     return sum(angka)
# def ave(angka):
#     return (sum(angka))/(len(angka))
# def med(angka):
#     angka.sort()
#     if (len(angka))%2!=0:
#         i=int((len(angka)+1)/2)
#         return angka[i-1]
#     else:
#         nilai1=(angka[len(angka)//2])
#         nilai2=(angka[len(angka)//2]-1)
#         return (nilai1+nilai2)/2     

# def kalkulator(x):
#     while True:
#         pilihanmenu=input('''
#         Menu:
#         \t1.Total
#         \t2.Rata-rata
#         \t3.Nilai tengah
#         \t4.Keluar
#         Masukkan nomor menu yang ingin kalian pilih:  ''')

#         if (pilihanmenu=="1"):
#             print("Total dari angka yang anda masukkan adalah {}".format(jumlah(x)))
#         elif (pilihanmenu=="2"):
#             print("Rata-rata dari angka yang anda masukkan adalah {}".format(ave(x)))
#         elif (pilihanmenu=="3"):
#             print("Nilai tengah dari angka yang anda masukkan adalah {}".format(med(x)))
#         elif (pilihanmenu=="4"):
#             break 
#         else:
#             print("Menu yang anda pilih tidak tersedia")

# kalkulator([1,2,3,4,5])            


# def timeconverter(detik):
#     if detik<0 or detik>359999 or type(detik)!=int:
#         print("Invalid Input")
#         return
#     HH=int((detik/3600))
#     sisasec=detik%3600
#     MM=(sisasec//60)
#     SS=sisasec%60
#     print("{}:{}:{}".format(HH,MM,SS))
# timeconverter(5000)