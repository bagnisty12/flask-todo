from flask import Flask, render_template, request, redirect
name = "Andrzej"
age = 0

def change_name(new):
    global name
    name = new
def change_age(new):
    global age
    age = new
    
app = Flask(__name__)
#dekorator -> funkcja, która wywołuje inną funkcję w środku, POŚREDNIK
@app.route("/")
def indexa():
    
    return render_template("index.html", zmienna=name, wiek=age)

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

if __name__ == "__main__":
    # localhost -> 0.0.0.0 -> TWÓJ ADRES IP, TWÓJ KOMPUTER
    app.run(host="0.0.0.0", port=5000, debug=True)