from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/numbers", methods=['POST'])
def numbers():
    yy = (request.form['prime_number'])
    if yy.isdigit():
        y=int(yy)
        lista = list(range(2, y + 1))
        your_number=y
        i = y - 1
        while y > 1:
            while i > 1:
                wynik = y / i  # Or you can use: wynik = y % i     ##
                if wynik in lista:  # if wynik == 0:                    ##
                    lista.remove(y)
                    break
                i -= 1
            y -= 1
            i = y - 1
        xx = ""
        for cyfra in lista:
            xx = xx + str(cyfra) + ", "
        x=xx[0:-2]
        return render_template("prime_numbers.html", prime_numbers=x, your_number=your_number)
    else:
        return render_template('prime_wrong.html')

if __name__=="__main__":
    app.run(debug=True)

