a = [1,2,3,4,5]
a.insert(1,6)
print(a)

a.append("apple")
print(a)


#extend  --  you can add more than one values
a = [1,2,3,4,5]
a.extend([6,7,8,9])
print(a)


#another type to insert more that one values ---- we join two list
a = [1,2,3,4,5]
result = a + [6,7,8,9]
print(result)



#pop === remove last values in list                        List part
a = [1,2,3,4,5]
a.pop()
print(a)


#remove === remove particular value in list              List part
a = [1,2,3,4,5]
a.remove(4)
print(a)

# find Average 

marks = [90,85,70,60,80]
result = sum(marks) / len(marks)

print(result)


#sort the list
a = [1,5,4,7,6,3]
a.sort(4)
print(a)


#reverse
a = [1,5,4,7,6,3]
a.reverse()
print(a)

