# for i in range(1,51):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")
#     else:
#         print(i) 
 
# inputsuhu=input("Input Temperature (Example: 50C,125F) : ")
# suhu=int(inputsuhu[:-1])
# if inputsuhu[-1:] == "C":
#     F=int(((suhu*9/5)+32))
#     print("{} is {} in Fahrenheit".format(inputsuhu,F))
# elif inputsuhu[-1:] == "F":  
#     C=int(((suhu-32)*5/9))
#     print("{} is {} in Celcius".format(inputsuhu,C))

nums=[1,3,5,6]
target=5
for i,d in enumerate(nums):
    if target<=d:
        print(i)
        break

# for i in range (1500,2700):
#     if i%7==0 and i%5==0:
#         print(i)

# def balik(kata):
#     hasil=kata[::-1]
#     return hasil
# print(balik("nice"))

# numbers=[1,2,3,4,5,6,7,8,9]
# count_odd=0
# count_even=0
# for i in numbers:
#     if i%2!=0:
#         count_odd+=1
#     else:
#         count_even+=1   
# print(count_odd)
# print(count_even)

# for i in range (0,101):
#     if i%3==0 or i%6==0:
#         continue
#     print(i)

# def fib(n):
#     if n<=1:
#         return n
#     return (n-1)+(n-2)
# x=0
# count=0
# while (x<=50):
#     x=fib(count)
#     print(x)
#     count+=1

# x=3
# y=4
# for i in range (0,x):
#     for j in range (0,y):
#         print (i*j, end=" ")
#     print ("")    











































