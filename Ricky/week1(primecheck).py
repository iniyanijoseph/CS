a = int(input("What number do you want to check?"))
c = 2
while c < a:
    if a % c == 0:
        print(f"Not prime({c})")
        exit()
    c += 1
print("Prime")
