cnt = 5

while True:
    print(cnt)
    cnt -=1
    if cnt ==0:
        print("countdown finished")
        break


print("-----------------------------------------------------------------------------------------------------------------------------")

for var in "elephant":
    if var == "e":
        continue
    print(var)

print("--------------------------------------------------------------------------------------------------------------")


for i in range(5):
    if i==3:
        pass
    else:
        print(i)