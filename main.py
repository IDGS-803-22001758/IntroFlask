from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():    
    grupo="IDGS803"
    lista=["Juan","Pedro","Mario"]
    return render_template("index.html", grupo=grupo, lista=lista)

@app.route('/OperasBas')
def operas():
    return render_template("OperasBas.html", resulta=None)

@app.route('/resultado', methods=["GET","POST"])
def resultado():    
    if request.method == "POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        resulta= int(num1)+int(num2)
        return render_template("OperasBas.html", resulta=resulta)

@app.route('/ejemplo1')
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route('/ejemplo2')
def ejemplo2():
    return render_template("ejemplo2.html")    

@app.route('/hola')
def hola():
    return "Hola!!!"     

@app.route('/user/<string:user>')     
def user(user):
    return f"Hola {user}!!!"

@app.route('/numero/<int:n>')
def numero(n):
    return "Numero:{}".format(n) 

@app.route('/user/<string:user>/<int:id>')     
def username(user,id):
    return f"Nombre: {user} ID:{id}!!!" 

@app.route('/suma/<float:n1>/<float:n2>')     
def suma(n1,n2):
    return "La suma es: {}!!!".format(n1+n2)

@app.route('/default')  
@app.route('/default/<string:nom>')     
def func(nom='Viviana'):
    return "El nombre de Nom es: "+nom     

@app.route("/form1")
def form1():
    return '''
        <form><label>Nombre:</label>
        <input type="text" name="nombre" placeolder="Nombre">
        </form>    
    '''     

@app.route('/cine')
def cine():
    return render_template("cinepolis.html", total=None)

@app.route('/procesa', methods=["POST"])
def procesa():
    if request.method == "POST":
        try:
            nombre = request.form.get("nombre")
            cantCompra = int(request.form.get("cantCompra", 0))
            cantBoletos = int(request.form.get("cantBoletos", 0))
            tarjetaCineco = request.form.get("tarjetaCineco")
            precio_unitario = 12

            max_boletos = cantCompra * 7
            if cantBoletos > max_boletos:
                return render_template("cinepolis.html", total="Error: Excede la cantidad permitida")

            total = cantBoletos * precio_unitario

            if cantBoletos > 5:
                total *= 0.85 
            elif 3 <= cantBoletos <= 5:
                total *= 0.90  

            if tarjetaCineco == "si":
                total *= 0.90  

            return render_template("cinepolis.html", total=round(total, 2))  

        except ValueError:
            return render_template("cinepolis.html", total="Error: Datos inválidos")       

if __name__ == '__main__':
    app.run(debug=True,port=3000)    