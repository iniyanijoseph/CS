overall = 0
totdict = {}
stringthing = input("What is your string?")
stringthing = stringthing.lower()
for element in stringthing:
    if element == "a" or element == "e" or element == "i" or element == "o" or element == "u":
        overall += 1
        if element not in totdict:
            totdict[element] = 1
        else:
            totdict[element] += 1
print(overall)
print(totdict)