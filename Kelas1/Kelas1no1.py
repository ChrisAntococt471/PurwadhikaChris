# nomor=int(input("Insert a number : "))
# iptlist=input("Insert your list of number: ")
# nomorlist=iptlist.split(",")
# for i in range (len(nomorlist)):
#     if nomor == int(nomorlist[i]): 
#         print("Your number is in the {} position!".format(i+1))
#         break
      
# def carikata(kata):
#     x={}
#     for i in kata:
#         if i in list(x.keys()):
#             x[i]=x[i]+1
#         else:
#             x[i]=1  
#     return(x)          
# kata=input("Masukkan kata : ")
# hasil=carikata(kata)
# for k,v in hasil.items():
#     print("Huruf {} muncul {} kali".format(k,v))

# spare_parts = { 'RAM': { 'Corsair': {'8GB': 400000, '16GB': 700000}, 'Kingston': {'8GB': 300000, '16GB': 600000}, 'v-Gen': {'8GB': 200000, '16GB': 500000}, }, 'SSD': { 'Patriot': {'128GB': 600000}, 'Samsung': {'256GB': 650000}, 'Toshiba': {'64GB': 320000, '128GB': 650000, '256GB': 800000}, } }
# BrandRAM=list(spare_parts["RAM"].keys())
# print(BrandRAM)
# ssdtosiba=spare_parts["SSD"]["Toshiba"]["128GB"]
# print(ssdtosiba)
# SSD=spare_parts["SSD"]
# print(SSD)
# kingston=spare_parts["RAM"]["Kingston"]["32GB"]
# if kingston == KeyError:
#     print ("Tidak Tersedia")
# print(kingston)

# phone_cases = {'Samsung': [('Capdase', 100000), ('Nillkin', 75000), ('RhinoShield', 150000)], 'OnePlus': [('Imak', 70000), ('Capdase', 90000)], 'Oppo': [('Spigen', 90000), ('Nillkin', 50000)], 'Apple': [('Elementcase', 4000000), ('Spigen', 130000)]}
# # print(list(phone_cases.keys()))





















# kata=input("Masukkan kata : ")
# if len(list(kata)) == len(set(kata)):
#     print("Yes")
# else:
#     print("No")    

# kata=input("Masukkan kata : ")
# splitkata=kata.split(" ")
# listkata=0
# kata_terpanjang=""
# for i in splitkata:
#     if len(i)>listkata:
#         listkata=len(i)
#         kata_terpanjang=i
# print(kata_terpanjang)


















# x="lontong"
# print("\n".join(x[::-1]))