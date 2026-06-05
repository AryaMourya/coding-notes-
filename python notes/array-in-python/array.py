import array as arr

val = arr.array('i',[1,2,3,4,5,6])

for i in range(0,6):
    print(val[i] , end=" ")

print('\n')

#method 2
for x in val:
    print(x , end=' , ')

print(val.typecode)

val.reverse()
for i in range(0,len(val)):
    print(val[i], end=" ")
    