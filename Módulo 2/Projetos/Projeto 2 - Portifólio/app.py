# Página criada junto ao professor durante a aula

from flask import Flask, render_template, redirect, request
from flask_mail import Mail, Message
app = Flask(__name__)

mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": 'testeblue1995@gmail.com',
    "MAIL_PASSWORD": 'Joaovitor199527'
}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formcontato = Contato(
            request.form['nome'],
            request.form['email'],
            request.form['mensagem']
        )

        msg = Message(
            subject='Contato do Portifólio',
            sender=app.config.get("MAIL_USERNAME"),
            recipients=[app.config.get("MAIL_USERNAME")],
            body=f'''{formcontato.nome} enviou a seguinte mensagem: 
            
            {formcontato.mensagem}'''
        )
        mail.send(msg)
    return render_template('send.html', formcontato=formcontato)


app.config.update(mail_settings)
mail = Mail(app)


class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem


if __name__ == '__main__':
    app.run(debug=True)
