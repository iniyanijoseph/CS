import pyperclip
while True:
    words = input("What is your sentence? ")
    words = words.split(" ")
    for ele in range(len(words)):
        word = words[ele]
        ogword = words[ele]
        firstletter = word[0]
        word = word[1::]
        word = word + f"{firstletter}ay"
        words.remove(ogword)
        words.insert(ele, word)
    finstr = ""
    for element in words:
        finstr += f"{element} "
    print(finstr)
    pyperclip.copy(finstr)