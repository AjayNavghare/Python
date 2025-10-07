# Reverse a String

string1 = "Trinity"

rev = string1[::-1]

# print(rev)

# Reverse a String (without built-in)

str1 = "abcd"
rev = ""

for i in range(len(str1)-1, -1, -1):
    rev += str1[i]

print(rev)


