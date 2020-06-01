a = int(input("What number do you want to check?"))
c=2
while a/2 > c:
    if a%c == 0:
        print(f"Not prime({c})")
        exit()
    c=c+1
print("Prime")