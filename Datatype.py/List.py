list1=[0,1,2,3,4,5]
# list1[0]=7
# print(list1)
def tambah(list):
    satu=[]
    for i in list:
        satu.append(i+1)
    return satu
print(tambah(list1))        