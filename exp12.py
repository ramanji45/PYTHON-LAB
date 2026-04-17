
s = input("Enter a String: ")
words = s.split()
d = {}
for i in range(len(words)):
    d[i] = words[i]
joined_string = "-".join(words)
print("Dictionary after splitting")
print(d)

print("String after join with -")
print(joined_string)
