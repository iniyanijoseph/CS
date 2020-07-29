from flask import Flask, render_template, request
import json
import mysql.connector

app=Flask(__name__)

def linEq(readfile):
    matrix = []
    
    for row in readfile.split(";"):
        matrix.append(row.split(","))
    lenrow = len(matrix) + 1
    lencol = len(matrix)
    for element in range(lencol):
        for num in range(lenrow):
            matrix[element][num] = int(matrix[element][num])


    # Clears Bottom
    for element in range(lencol):
        divisor = matrix[element][element]
        if divisor == 0:
            return [0]
        for num in range(lenrow):
            matrix[element][num] = matrix[element][num] / divisor
        for num in range(element + 1, lencol):
            start = matrix[num][element]
            for n in range(lenrow):
                matrix[num][n] = matrix[num][n] - (matrix[element][n] * start)
    for element in range(lencol):
        if matrix[element][element] == 0:
            return [0]

    # Calculates X and Y values and clears top
    n = lencol - 1
    while n > 0:
        for element in range(n):
            start = matrix[element][n]
            for num in range(lenrow):
                matrix[element][num] = matrix[element][num] - (matrix[n][num] * start)
        n -= 1
    ans = []
    for element in range(lencol):
        ans.append(matrix[element][lencol])
    return ans
def isprime(a):
    c=2
    while a/2 >= c:
        if a%c == 0:
            return False
        c=c+1
    return True    

def Prime(strnum):
    num = int(strnum)
    nnum = num
    numcount = 0
    retlist = []
    for counter in range(num-1):
        if nnum < counter:
            break
        numcount = 0
        if isprime(counter):
            if counter != 0 and counter != 1:
                while nnum%counter == 0:
                    nnum = nnum/counter
                    numcount += 1
                if numcount != 0:
                    retlist.append(str(counter)+"^" + str(numcount))

    return json.dumps(retlist)

def gcf(enter):
    enter = enter.split(",")
    big = int(enter[0])
    small = int(enter[1])
    swaphold = 0
    hold = 0
    if big<small:
        swaphold = small
        small = big
        big = swaphold
    while big%small != 0:
        hold = big%small
        big = small
        small = hold
    return small
    
def encryptceaser(input):
    finput = input.split(",")
    push = int(finput[0])
    mes = finput[1]
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alphabetdic = {"a":0, "b":1, "c":2, "d":3, "e":4, "f":5, "g":6, "h":7, "i":8, "j":9, "k":10, "l":11, "m":12, "n":13, "o":14, "p":15, "q":16, "r":17, "s":18, "t":19, "u":20, "v":21, "w":22, "x":23, "y":24, "z":25}
    newmes = []
    for num in range(push):
        moved = alphabet.pop(0)
        alphabet.insert(len(alphabet), moved)
    def splitter(word):
        return [char for char in word]
    splitmes = splitter(mes)
    if " " in splitmes:
        while " " in splitmes:
            splitmes.remove(" ")
    for element in splitmes:
        key = alphabetdic.get(element)
        element = alphabet[key]
        newmes.append(element)
    finmes = ""
    for element in newmes:
        finmes = finmes+element
    return finmes
    
def books(titlename):
    title='%' + titlename + '%'
    mydb = mysql.connector.connect(
        host="192.168.1.4",
        user="iniyan",
        passwd="iniyangc",
        database="checkouts"
    )
    mycursor = mydb.cursor()
    tuptitle=(title,)
    sqlr = "SELECT * FROM books WHERE title like %s;"
    mycursor.execute(sqlr, tuptitle)
    base = "["
    for x in mycursor:
        base += '"' + x[2]+","+ str(x[0]) + '",'
    base = base[0:len(base)-1] + ']'
    if len(base)>0:
        return base
    else:
        return "No Entries"

def entries(titlename):
    reslist = []
    sep = titlename.split(",")
    title = sep[0]
    url = sep[1]
    mydb = mysql.connector.connect(
        host="192.168.1.4",
        user="iniyan",
        passwd="iniyangc",
        database="checkouts"
    )
    mycursor = mydb.cursor()
    tuptitle=(title,url)
    sqlr = "INSERT INTO books(title,url) VALUES(%s,%s);"
    mycursor.execute(sqlr, tuptitle)
    id=mycursor.lastrowid
    mydb.commit()
    mycursor.close()
    mydb.close()
    return str(id)

def entries_delete(id):
    reslist = []
    mydb = mysql.connector.connect(
        host="192.168.1.4",
        user="iniyan",
        passwd="iniyangc",
        database="checkouts"
    )
    mycursor = mydb.cursor()
    tuptitle=(id,)
    sqlr = "DELETE FROM books WHERE idbooks = %s;"
    mycursor.execute(sqlr, tuptitle)
    mydb.commit()
    mycursor.close()
    mydb.close()
    return '"Success +^.^+"'    

@app.route("/ceaser_code")
def CeaserCode():
    return render_template("ceaser.html")
@app.route("/prime")
def prime():
    return render_template("prime.html")
@app.route("/gcf")
def gcff():
    return render_template("gcf.html")
@app.route("/linear")
def linear():
    return render_template("oth.html")
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/onlinelibrary")
def libra():
    return render_template("lib.html")
@app.route("/bookentry")
def inp():
    return render_template("enterr.html")




@app.route("/calc",methods=['POST'])
def calc():
    linere = request.get_json()['a']
    return str(linEq(linere))
@app.route("/primes",methods=['POST'])
def primes():
    primee = request.get_json()['a']
    return str(Prime(primee))
@app.route("/gcf",methods=['POST'])
def gcfs():
    gcff = request.get_json()['a']
    return str(gcf(gcff))
@app.route("/ceasercode", methods=['POST'])
def encrypt():
    ceasercode = request.get_json()['a']
    return "\"" + encryptceaser(ceasercode) + "\""
@app.route("/sqllibra",methods=['POST'])
def libre():
    libr = request.get_json()['a']
    return books(libr)
@app.route("/input",methods=['POST'])
def librentry():
    ent = request.get_json()['a']
    return str(entries(ent))
@app.route("/delete",methods=['POST'])
def libdel():
    dele = request.get_json()['a']
    return str(entries_delete(int(dele)))
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)

