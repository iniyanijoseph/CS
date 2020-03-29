from flask import Flask, request
app = Flask(__name__)


def add(a):
    sum = 0
    for element in a:
        try:
            element = int(element)
            sum += element
        except:
            element = 0
            element = int(element)
            sum += element
    return sum


def listranger(li, comp):
    for element in li:
        if element[1] > comp > element[0]:
            if li.index(element) == 0:
                return " Much Less Than Others"
            if li.index(element) == 1:
                return " Less Than Others"
            if li.index(element) == 2:
                return " Like the Majority of Others"
            if li.index(element) == 3:
                return " More Than Others"
            if li.index(element) == 4:
                return " Much More Than Others"


retstr = """"""
for item in range(1, 87):
    retstr += str(item) + """<input type="number" name=""" + str(item) + """ value="0"><br>"""


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == "POST":
        aud = []
        for element in range(1, 9):
            aud.append(request.form.get(str(element)))
        vis = []
        for element in range(9, 16):
            vis.append(request.form.get(str(element)))
        tou = []
        for element in range(16, 27):
            tou.append(request.form.get(str(element)))
        mov = []
        for element in range(27, 35):
            mov.append(request.form.get(str(element)))
        bopo = []
        for element in range(35, 43):
            bopo.append(request.form.get(str(element)))
        orse = []
        for element in range(43, 53):
            orse.append(request.form.get(str(element)))
        con = []
        for element in range(53, 62):
            con.append(request.form.get(str(element)))
        soem = []
        for element in range(62, 76):
            soem.append(request.form.get(str(element)))
        att = []
        for element in range(76, 87):
            att.append(request.form.get(str(element)))
        seeking = [
            request.form.get("14"),
            request.form.get("21"),
            request.form.get("22"),
            request.form.get("25"),
            request.form.get("27"),
            request.form.get("28"),
            request.form.get("30"),
            request.form.get("31"),
            request.form.get("32"),
            request.form.get("41"),
            request.form.get("48"),
            request.form.get("49"),
            request.form.get("50"),
            request.form.get("51"),
            request.form.get("55"),
            request.form.get("56"),
            request.form.get("60"),
            request.form.get("82"),
            request.form.get("83")]

        avoiding = [
            request.form.get("1"),
            request.form.get("2"),
            request.form.get("5"),
            request.form.get("15"),
            request.form.get("18"),
            request.form.get("58"),
            request.form.get("59"),
            request.form.get("61"),
            request.form.get("63"),
            request.form.get("64"),
            request.form.get("65"),
            request.form.get("66"),
            request.form.get("67"),
            request.form.get("68"),
            request.form.get("70"),
            request.form.get("71"),
            request.form.get("72"),
            request.form.get("74"),
            request.form.get("75"),
            request.form.get("81")]

        sensitivity = [
            request.form.get("3"),
            request.form.get("4"),
            request.form.get("6"),
            request.form.get("7"),
            request.form.get("9"),
            request.form.get("13"),
            request.form.get("16"),
            request.form.get("19"),
            request.form.get("20"),
            request.form.get("44"),
            request.form.get("45"),
            request.form.get("46"),
            request.form.get("47"),
            request.form.get("52"),
            request.form.get("69"),
            request.form.get("73"),
            request.form.get("77"),
            request.form.get("78"),
            request.form.get("84")]

        registration = [
            request.form.get("8"),
            request.form.get("12"),
            request.form.get("23"),
            request.form.get("24"),
            request.form.get("26"),
            request.form.get("33"),
            request.form.get("34"),
            request.form.get("35"),
            request.form.get("36"),
            request.form.get("37"),
            request.form.get("38"),
            request.form.get("39"),
            request.form.get("40"),
            request.form.get("53"),
            request.form.get("54"),
            request.form.get("57"),
            request.form.get("62"),
            request.form.get("76"),
            request.form.get("79"),
            request.form.get("80"),
            request.form.get("85"),
            request.form.get("86")]
        aud = add(aud)
        vis = add(vis)
        tou = add(tou)
        mov = add(mov)
        bopo = add(bopo)
        orse = add(orse)
        con = add(con)
        soem = add(soem)
        att = add(att)
        seeking = add(seeking)
        avoiding = add(avoiding)
        sensitivity = add(sensitivity)
        registration = add(registration)
        seklist = [(0, 6), (7, 19), (20, 47), (48, 60), (61, 95)]
        avolist = [(0, 7), (8, 20), (21, 46), (47, 59), (60, 100)]
        senlist = [(0, 6), (7, 17), (18, 42), (43, 53), (54, 95)]
        reglist = [(0, 6), (7, 18), (19, 43), (44, 55), (56, 110)]
        audlist = [(0, 2), (3, 9), (10, 24), (25, 31), (32, 40)]
        vislist = [(0, 4), (5, 8), (9, 17), (18, 21), (22, 30)]
        toulist = [(0, 0), (1, 7), (8, 21), (22, 28), (29, 55)]
        movlist = [(0, 1), (2, 6), (7, 18), (19, 24), (25, 40)]
        bopolist = [(0, 0), (1, 4), (5, 15), (16, 18), (20, 40)]
        orlist = [(-1, -1), (0, 7), (8, 24), (25, 32), (33, 50)]
        conlist = [(0, 1), (2, 8), (9, 22), (23, 29), (30, 45)]
        soemlist = [(0, 2), (3, 12), (13, 31), (32, 41), (42, 70)]
        attlist = [(0, 0), (1, 8), (9, 24), (25, 31), (32, 50)]
        sekl = listranger(seklist, seeking)
        avol = listranger(avolist, avoiding)
        senl = listranger(senlist, sensitivity)
        regl = listranger(reglist, registration)
        audl = listranger(audlist, aud)
        visl = listranger(vislist, vis)
        toul = listranger(toulist, tou)
        movl = listranger(movlist, mov)
        bopol = listranger(bopolist, bopo)
        orl = listranger(orlist, orse)
        conl = listranger(conlist, con)
        soeml = listranger(soemlist, soem)
        attl = listranger(attlist, att)
        try:
            return '''<html lang="en">
            <head>
            <meta charset="UTF-8">
            <title>Scores Calculator</title>
            </head>
            <body bgcolor="#3dccc2">
            <center>
            <h2>Auditory Processing is {}<h2>
            <h2>Visual Processing is {}<h2>
            <h2>Touch Processing is {}<h2>
            <h2>Movement Processing is {}<h2>
            <h2>Body Position Processing is {}<h2>
            <h2>Oral Sensory Processing is {}<h2>
            <h2>Conduct Processing is {}<h2>
            <h2>Social Emotional Processing is {}<h2>
            <h2>Attention Processing is {}<h2>
            <h2>Seeking Score(Orange) is {}<h2>
            <h2>Avoiding Score(Blue) is {}<h2>
            <h2>Sensitivity Score(Green) is {}<h2>
            <h2>Registration Score(Magenta) is {}<h2>
            <h2>Seeking Score Tabular{}</h2>
            <h2>Avoiding Score Tabular{}</h2>
            <h2>Sensitivity Score Tabular{}</h2>
            <h2>Registration Score Tabular{}</h2>
            <h2>Auditory Score Tabular{}</h2>
            <h2>Visual Score Tabular{}</h2>
            <h2>Touch Score Tabular{}</h2>
            <h2>Movement Score Tabular{}</h2>
            <h2>Body Postition Score Tabular{}</h2>
            <h2>Oral Score Tabular{}</h2>
            <h2>Conduct Score Tabular{}</h2>
            <h2>Social Emotional Score Tabular{}</h2>
            <h2>Attentional Score Tabular{}</h2>
            </center>
            </body>
            </html>'''.format(aud, vis, tou, mov, bopo, orse, con, soem, att, seeking, avoiding, sensitivity, registration, sekl, avol, senl, regl, audl, visl, toul, movl, bopol, orl, conl, soeml, attl)
        except:
            pass
    return """<html lang="en">
        <head>
        <meta charset="UTF-8">
        <title>Scores Calculator</title>
        </head>
        <body bgcolor="#3dccc2">
        <center>
        <h1 style="color:blue;">Calculate</h1>
        <form method="POST">
        <ol> """ + retstr + """
        </ol>

        <input type="submit" value="Calculate">
        </form>
        </center>
        </body>
        </html>"""


if __name__ == '__main__':
    app.run(debug=True, port=5000)
