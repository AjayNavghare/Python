try:
    file = open("example.txt","r")
    content = file.read()

except FileNotFoundError:
    print("File not found")     #if file is not present then this block will execute 

finally:
    print("This will run no matter what.")
    file.close()