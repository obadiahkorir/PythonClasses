f = open("filetext.txt", "r")
print(f.read(5))

f = open("filetext.txt", "r")
print(f.readline())

f = open("filetext.txt", "r")
print(f.readline())
print(f.readline())

f = open("filetext.txt", "r")
for x in f:
  print(x)

  f = open("filetext.txt", "r")
  print(f.readline())
  f.close()

  f = open("filetext.txt", "a")
  f.write("Now the file has more content!")
  f.close()

  # open and read the file after the appending:
  f = open("filetext.txt", "r")
  print(f.read())