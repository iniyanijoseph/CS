a = int(input("Please give a number"))
c = 2
while a > c:
    if a%c == 0:
        print("Not Prime", c)
        exit()
    c = c + 1
print("Prime")