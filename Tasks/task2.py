#Reverse a String (without built-in)

arr = [20,10,30,44,88,89]

max_num = arr[0]
for num in arr:
    if num > max_num:
        max_num = num 


min_num = arr[0]
for num in arr:
    if num < min_num:
        min_num = num
    
print("Max Number : ",max_num)
print("Min Number : ",min_num)