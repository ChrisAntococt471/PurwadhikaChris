# stars=""
# size=5
# for i in range(size):
#     for j in range(size-i):
#         stars+="*"
#     stars+="\n"
# for i in range (1,size):
#     for j in range(1+i):
#         stars+="*"
#     stars+="\n"    
# print(stars)    


hargaapel=10000
hargajeruk=15000
hargaanggur=20000
stokapel=5
stokjeruk=7
stokanggur=6

while(True):
    apel=int(input("Masukkan Jumlah Apel : "))
    if apel>stokapel:
        print("Jumlah yang dimasukkan terlalu banyak \nStok Apel tinggal {}".format(stokapel))
    else:
        break    
while(True):
    jeruk=int(input("Masukkan Jumlah Jeruk : "))
    if jeruk>stokjeruk:
        print("Jumlah yang dimasukkan terlalu banyak \nStok Jeruk tinggal {}".format(stokjeruk))
    else:
        break    
while(True):
    anggur=int(input("Masukkan Jumlah Anggur : "))
    if anggur>stokanggur:
        print("Jumlah yang dimasukkan terlalu banyak \nStok Anggur tinggal {}".format(stokanggur))
    else:
        break 

totapel=apel*hargaapel
totjeruk=jeruk*hargajeruk
totanggur=anggur*hargaanggur
total=totapel+totjeruk+totanggur

print('''
Detail Belanja:

Apel : {} x {} = {}
Jeruk : {} x {} = {}
Anggur : {} x {} = {}

Total={}'''.format(apel,hargaapel,totapel,jeruk,hargajeruk,totjeruk,anggur,hargaanggur,totanggur,total))

while(True):
    uang=int(input("Masukkan jumlah uang : "))
    sisa=abs(uang-total)   
    if uang<total:        
        print("Uang anda kurang sebesar {}".format(sisa))
    elif uang>total:
        print("Terima kasih\nUang kembali anda : {}".format(sisa))
        break
    else:
        print("Terima kasih")    
        break


















