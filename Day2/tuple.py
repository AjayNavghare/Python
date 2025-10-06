#Tuple
tup = (3,4,6,3,2,5)
# print(tup)

# we can add a number in tuple but first we need to convert it into list 
# a = (1,2,3)
# b = list(a)
# print(b)
# b[0] = 20
# print(b)


#using temp  we
a = (1, 2, 3,4,5,6,7)
temp = list(a)
temp[6] = 20
a = tuple(temp)
print(a)