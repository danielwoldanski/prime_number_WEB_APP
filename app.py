from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/echo", methods=['POST'])
def echo():
    y = int(request.form['prime_number'])
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
    x = ""
    for cyfra in lista:
        x = x + str(cyfra) + ", "
    return render_template("home.html", prime_numbers=x, your_number=your_number)

if __name__=="__main__":
    app.run(debug=True)

