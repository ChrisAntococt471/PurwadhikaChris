numbers=[41,5,1,3,89,32]
minval=numbers[0]
maxval=numbers[0]
for i in numbers:
    if i>maxval:
        maxval=i
    if i<minval:
        minval=i
print("Numbers = {}".format(numbers))
print("Minimum value = {}".format(minval))
print("Maximum value = {}".format(maxval))