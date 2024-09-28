# open file and read its content
file = open("Codingal.txt", "r")
print(file.read())
file.close()


# open file and read its beginning 8 characters
file = open("Codingal.txt", "r")
print(file.read(8))
file.close()


# append your name and age  in the file
file = open("Codingal.txt", "a")
file.write("\nHi ! I am Sudip and I am 25 years old")
file.close()