m=int(input())
if m>=8 and m<=12 and m%2==0:
    print(31)
elif m>=1 and m<=7 and m%2!=0:
    print(31)
elif m==2:
    print(28)
else:
    print(30)
