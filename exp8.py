word=input("Enter name: ")
vowels=["a","e","i","o","u","A","E","I","O","U"]
for i in word:
    if i in vowels:
        print("word contain vowels")
        break;
else:
    print("word  not contain vowels")
            
