
#common tag from multiple course  ---           use intersection

s = "python"
rev = ""

for i in range(len(s)-1, -1, -1):
    rev += s[i]

print("Reversed string:", rev)