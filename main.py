from flask import Flask, render_template, request, redirect, flash
import controllerCRUD

app=Flask(__name__)

#rutas
@app.route("/formulario_agregar_cliente")
def formulario_agregar_cliente():
    return render_template("agregar_cliente.html")


@app.route("/guardar_cliente", methods=["POST"])
def guardar_juego():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controllerCRUD.insertar_juego(nombre, descripcion, precio)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/clientes")

@app.route("/")
@app.route("/clientes")
def clientes():
    clientes = controllerCRUD.get_clients()
    return render_template("listar_cliente.html", clientes=clientes)

@app.route("/eliminar_cliente", methods=["POST"])
def eliminar_cliente():
    controllerCRUD.eliminar_juego(request.form["id"])
    return redirect("/clientes")

@app.route("/formulario_editar_cliente/<int:id>")
def actualizar_cliente(id):
    # Obtener el juego por ID
    juego = controllerCRUD.obtener_juego_por_id(id)
    return render_template("editar_cliente.html", juego=juego)

@app.route("/actualizar_cliente", methods=["POST"])
def actualizar_juego():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controllerCRUD.actualizar_juego(nombre, descripcion, precio, id)
    return redirect("/clientes")


    #servidor
if __name__=="__main__":
    app.run(port=8000, debug=True)