names = ["John", "Jane", "Jordan", "Joe"]
names2 = ["Poe", "Jacob", "Johnathan"]

print(len(names))
# names.append("Kelvin")

names.insert(2, "Kelvin")
print(len(names))
print(names)

names.extend(names2)

print(names)