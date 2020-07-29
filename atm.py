amount = int(input("How Much?"))
remainder = 0
twenties = 0
tens = 0
fives = 0
remainder = amount%20
twenties = (amount-remainder)/20
amount -= twenties * 20
remainder = remainder%10
tens = (amount-remainder)/10
amount -= tens * 10
remainder = remainder%5
fives = (amount-remainder)/5
print(f"{twenties} 20 dollar bills, {tens} 10 dollar bills, {fives} five dollar bills")

    