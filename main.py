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

if __name__ == '__main__':
    app.run(debug=True,port=3000)    