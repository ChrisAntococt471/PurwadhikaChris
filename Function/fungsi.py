# def coba(nama):
#     print("Selamat datang {}".format(nama))
#     while (True):
#         mau=input("Mau coba kue ini? : ")
#         if (mau=="yes"):
#             print("Silahkan, ini kuenya")
#             return "Kue coklat"
#         elif (mau=="no"):
#             break 
#         print("Anda yakin?")   
#     print("Sampai jumpa")
# kue=coba("andi")
# print(kue,type(kue))

# def coba():
#     x=5
#     print(x+2)
#     return x+3      
# x=8
# print(coba(),x)

# def tambah(n1,n2):
#     return n1+n2
# def kurang(n1,n2):
#     return n1-n2
# def hitung (tes,n1,n2):
#     hasil=tes(n1,n2)        
#     return hasil
# print(hitung((kurang),1,2)    )

def angka(hitung):
    print(hitung)
    hitung-=1
    if(hitung>=0):
        angka(hitung)
angka(5)        