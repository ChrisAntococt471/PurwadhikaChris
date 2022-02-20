# list1 = [1,3,4,5]
# list2 = [22,17,19,20,14]
# list3 = [1,3,5]
# list4 = [2,4,6]
# def ubahlist(listangka):
#     if listangka%2!=0:
#         return "Ganjil"
#     else:
#         return "Genap"
# def ubahangka(listangka):
#     return list(map(ubahlist,listangka))

# print(ubahangka(list2))

# def angkagenap(angka):
#     return angka%2==0
# hasilfilter=filter(angkagenap,list1)
# # print(list(hasilfilter))

# hasilfilter=(filter(lambda angka:angka%2==0,list1))
# print(list(hasilfilter))


# gaji=[9100000,9800000,9500000,10300000,9300000]
# # # def gaji1(listgaji):
# # #     return (listgaji-(listgaji*5/100)>9000000)
# # # gajifilter=filter(gaji1,gaji)
# # # print(list(gajifilter))

# hasilfilter=(filter(lambda angka:(angka-(angka*5/100)>9000000),gaji))
# print(list(hasilfilter))    

list1 = [1,3,4,5]
for i in range (len(list1)):
    if i%2!=0:
        list1[i]="Angka Ganjil"
    else:
        list1[i]="Angka Genap"
print(list1)          
                