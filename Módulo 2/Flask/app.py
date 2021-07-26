from flask import Flask, render_template, request, redirect

app = Flask(__name__)

itens = []


@app.route('/')
def index():
    nomelista = "Lista de coisas a fazer!"
    listapronta = True
    return render_template('index.html',
                           itens=itens, nomelista=nomelista)


@app.route('/nova', methods=['GET', 'POST'])
def nova():
    if request.method == 'POST':
        item = request.form['item']
        itens.append(item)
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
