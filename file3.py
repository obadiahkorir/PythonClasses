f = open("filetext.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("filetext.txt", "r")
print(f.read())

f = open("myfile.txt", "x")

import os
os.remove("myfile.txt")