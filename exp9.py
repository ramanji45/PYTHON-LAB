str1=input("Enter String1: ")
str2=input("Enter string2: ")
print("Checking both are equal or not")
a=""
if len(str1)==len(str2):
    print("YES,both strings of same length")
    for i in range(len(str2)):
        a=a+str1[i]+str2[i];
else:
    print("Both strings are not equal and exit")
print(a)
    
    
