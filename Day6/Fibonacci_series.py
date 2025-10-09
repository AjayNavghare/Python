num = int(input("Enter Number of terms : "))

a,b = 0,1


for i in range(num):
    print(a, end="  ")
    c = a + b
    a = b
    b = c

