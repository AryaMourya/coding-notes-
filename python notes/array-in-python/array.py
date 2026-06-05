import array

val = array.array('i',[1,2,3,4,5,6])

for i in range(0,6):
    print(val[i] , end=" ")

print('\n')

#method 2
for x in val:
    print(x , end=' , ')