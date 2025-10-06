#set
a = {1,2,3,4,"Ajay"}
a.add(9)
print(a)
b = a.pop()
print(b)

a = {}
print(type(a))    #remember when you check type of empty set then it give you Dictionary type ------------

b = {1,2,3,4}    #REMEMBER  when you have values/element in set and check for type then its type is SET 
print(type(b)) 


# ----------   Remove  ---------
# x = {1,2,3,4,5}
# z = x.remove(1)
# print(x)


#pop
s = {10, 20, 30, 40}
x = s.pop()
print("Removed:", x)

#union
s1 = {1,2,3,4}
s2 = {2,3,4,7,9}

res = s1.union(s2)
print(res)



#intersection
s1 = {1,2,3,4}
s2 = {2,3,4,7,9}

res = s1.intersection(s2)
print(res)


#intersection_update       not mostely  ask but remember
a = {1, 2, 3, 4}
b = {3, 4, 5}
a.intersection_update(b)
print(a)



