from flask import Flask, render_template, request, redirect, flash
import controllerCRUD

app=Flask(__name__)

#rutas
@app.route("/formulario_agregar_cliente")
def formulario_agregar_cliente():
    return render_template("agregar_cliente.html")


@app.route("/guardar_cliente", methods=["POST"])
def guardar_cliente():
    nom = request.form["nombres"]
    ape = request.form["apellidos"]
    dni = request.form["dni"]
    dir = request.form["direccion"]
    ema = request.form["email"]
    controllerCRUD.create_client(nom,ape,dni,dir,ema)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/clientes")

@app.route("/")
@app.route("/clientes")
def clientes():
    clientes = controllerCRUD.get_clients()
    return render_template("listar_cliente.html", clientes=clientes)

@app.route("/eliminar_cliente", methods=["POST"])
def eliminar_cliente():
    controllerCRUD.delete_client(request.form["id"])
    return redirect("/clientes")

@app.route("/formulario_editar_cliente/<int:id>")
def actualizar_cliente_id(id):
    # Obtener el juego por ID
    cliente = controllerCRUD.get_by_id(id)
    return render_template("editar_cliente.html", cliente=cliente)

@app.route("/actualizar_cliente", methods=["POST"])
def actualizar_cliente():
    id = request.form["id"]
    nom = request.form["nombres"]
    ape = request.form["apellidos"]
    dni = request.form["dni"]
    dir = request.form["direccion"]
    ema = request.form["email"]
    controllerCRUD.update_client(nom,ape,dni,dir,ema,id)
    return redirect("/clientes")


    #servidor
if __name__=="__main__":
    app.run(port=8000, debug=True)