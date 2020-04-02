numlist = []
for element in range(100):
    if element % 3 == 0 and element % 5 == 0:
        numlist.append("FizzBuzz")
    elif element % 3 == 0 and element % 5 != 0:
        numlist.append("Fizz")
    elif element % 3 != 0 and element % 5 == 0:
        numlist.append("Buzz")
    else:
        numlist.append(element)

for element in numlist:
    print(element)
