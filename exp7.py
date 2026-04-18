a=int(input("Enter First value:"))
print(a)
b=int(input("Enter Second value:"))
print(b)
dif=abs(b-a)
if dif<=0.001:
    print("close")
else:
        print("Not close")
