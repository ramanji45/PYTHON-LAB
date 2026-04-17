# Input string
s = input("Enter a String: ")

# Split the string into words
words = s.split()

# Store in dictionary (index : word)
d = {}
for i in range(len(words)):
    d[i] = words[i]

# Join the words with '-'
joined_string = "-".join(words)

# Output
print("Dictionary after splitting")
print(d)

print("String after join with -")
print(joined_string)
