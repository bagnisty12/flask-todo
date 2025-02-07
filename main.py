from flask import Flask, render_template, request, redirect, session, jsonify

#cookies -> przez 3 miesiące trzymaj te informacje: 35insdksdfjksdfj 
#session -> traktuj jako dict

chat = []
def add_message(new):
    # z sesji wyciągnij imie użytkownika
    name = session.get("name","Anon")

    # text: janusz: jazda jazda
    text = f"{name} - {new}"
    chat.append(text)

def change_name(new):
    session['name'] = new

def change_age(new):
    session["age"] = new
    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'haslo'
#dekorator -> funkcja, która wywołuje inną funkcję w środku, POŚREDNIK
@app.route("/")
def index():
#to chcemy wziac z sesji \/       \/ -- dostaniemy, jeśli tego nie ma
    name = session.get("name", "Anon")
    age = session.get("age","0")
    # po nazwie pliku html, możesz dać dowolne zmienne
    return render_template("index.html", zmienna=name, wiek=age, chat=chat)

@app.route("/test", methods=["POST"])
def test():
    form = request.form

    for name, value in form.items():
        print(name, value)
        if name == "imie":
            change_name(value)
        elif name == "wiek":
            change_age(value)
            
        else:
            print("NIE OBSLUGUJEMY:", name )
        

    return redirect("/")

@app.route("/send", methods = ["POST"])
def send():
    form = request.form

    for name, value in form.items():
        if name =="wiadomosc":
            add_message(value)

    return redirect("/")

@app.route("/wiadomosci")
def messages():
    return jsonify(chat)

if __name__ == "__main__":
    # localhost -> 0.0.0.0 -> TWÓJ ADRES IP, TWÓJ KOMPUTER
    app.run(host="0.0.0.0", port=5000, debug=True)