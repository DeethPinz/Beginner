text = "    heLLo WoRlD    "
print("original: ", text)
print("lowered: ", text.lower())
print("upper: ", text.upper())
print("stripped: ", text.strip())

text = "     hello hello world  "
print("original: ", text)
print("replaced: ", text.strip().replace("hello", "goodbye"))