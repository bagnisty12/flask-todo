from flask import Flask, render_template
    
app = Flask(__name__)

#dekorator -> funkcja, która wywołuje inną funkcję w środku, POŚREDNIK
@app.route("/")
def index():
    name = "Andrzej"
    return render_template("index.html", zmienna=name)

@app.route("/test")
def test():
    return "test"
if __name__ == "__main__":
    # localhost -> 0.0.0.0 -> TWÓJ ADRES IP, TWÓJ KOMPUTER
    app.run(host="0.0.0.0", port=5000, debug=True)