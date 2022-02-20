# def tipeangka(list1):
#     if list1%2!=0:
#         return "Ganjil"
#     else:
#         return "Genap"    
# def ubahangka(listangka):
#     return list(map(tipeangka,listangka))  
# print(ubahangka([1,3,4,5]))

# def gaji(listgaji):
#     listgajifilter=[]
#     for i in listgaji:
#         if i>9000000:
#             listgajifilter.append(i)
#     return listgajifilter        
# print(gaji([9100000,8000000,10000000,8500000,9200000]))      
 
# gaji=[9100000,9800000,9500000,10300000,9300000]
# filtergaji=filter(lambda gaji:(gaji-(gaji*5/100))>9000000,gaji)
# print(list(filtergaji))



# x,y,z=["Hello","I am","John"]
# def say(word):
#     print(x)
# say("Python")   
# 
# a=200
# b=33
# if((b==a) and (1<10)) :
#     print("a and b are equal ")
# elif((a>b)or (2>4)):
#     print("a is smaller than b")
# else:
#     print("a is greater than b")        

# dict={'nama':'rony','kelas':'3b','nilai':80}
# dict.update({'keterangan':'lulus'})
# print(dict)

# a="Halo nama saya randy"
# b=[i.capitalize() for i in a.split()]
# print(b)

# a=33
# b=300
# if b>a:
#     print('b is greater than a')


# def greeting (x,y,z):
#     if z==True:
#         z='Married'
#     else:
#         z="Not Married"
#     print("hello my name is {}. next year i am {} and i am {} woman".format(x.capitalize(),y+1,z))        
# greeting("fita",26,True)  


# adj=["red","big","tasty"]
# fruits=["apple","banana","cherry"]
# for i in range (len(adj)):
#     print ("{} is {}".format(fruits[i],adj[i]))

# def encryptor(word):
#     abjad="abcdefghijklmnopqrstuvwxyz"
#     words=word.lower()
#     encrypt=''
#     for c in words:
#         if c!='':
#             index=(abjad.index(c)+2)%len(abjad)
#             encrypt+=abjad[index].upper()
#         else:
#             encrypt+=''
#     return encrypt
# print(encryptor('ridho'))
# 
# a_list=[]
# for i in range(1,6):
#     if i==4:
#         continue
#     else:
#         a_list.append(i)
# print(a_list)              

# y="good morning"
# def print_this(name):
#     y="good evening"
#     print("{a}{b}".format (a=y,b=name))
# print_this('ruben')

# y=30
# def my_func():
#     global x
#     x=10
#     print("value inside:",y)
# x=20
# my_func()
# print("value outside:",x)    


# def sum_all(numbers):
#     total=0
#     for x in numbers:
#         if x%2==0:
#             total+=x
#     print(total)
# sum_all([8,4,7,2,5])            

list1=['andi','budi','ceci','dedi']
print(list1.index('dedi'))















