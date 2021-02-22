thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

  thistuple = ("apple", "banana", "cherry")
  for i in range(len(thistuple)):
      print(thistuple[i])

      thistuple = ("apple", "banana", "cherry")
      i = 0
      while i < len(thistuple):
          print(thistuple[i])
          i = i + 1

  tuple1 = ("a", "b", "c")
  tuple2 = (1, 2, 3)

  tuple3 = tuple1 + tuple2
  print(tuple3)

  fruits = ("apple", "banana", "cherry")
  mytuple = fruits * 2
  print(mytuple)

  thisset = {"apple", "banana", "cherry"}
  print(thisset)

  thisset = {"apple", "banana", "cherry", "apple"}
  print(thisset)

  myset = {"apple", "banana", "cherry"}
  print(type(myset))

  thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
  print(thisset)