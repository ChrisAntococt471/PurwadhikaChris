bin=""
size=5
for i in range(size):
    for j in range (size-i):
        bin+=" "
    for k in range (i*2+1):
        bin+="*"    
    bin+="\n"
for i in range(1,size):
    for j in range (i+1):
        bin+=" "
    for k in range ((size*2)-(i*2)-1):
        bin+="*"    
    bin+="\n"
print(bin)    