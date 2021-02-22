thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]


x = thisdict.keys()
print(x)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x) #before the change

car["year"] = 2020

print(x) #after the change


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  thisdict.update({"year": 2020})

  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  thisdict["color"] = "red"
  print(thisdict)

  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  thisdict.pop("model")
  print(thisdict)

  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  mydict = thisdict.copy()
  print(mydict)

  thisdict = {
      "brand": "Ford",
      "model": "Mustang",
      "year": 1964
  }
  mydict = dict(thisdict)
  print(mydict)