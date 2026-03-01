from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["SECRET_KEY"] = "cambia-esta-clave-secreta"


@app.route("/")
def index():
    """Renderiza la landing principal con variables de producto."""
    product = {
        "name": "CryptoBots Pro Suite",
        "price": 199,
        "currency": "USD",
        "description": "Paquete de 10 bots de trading en Python para criptomonedas con estrategias probadas, documentación paso a paso y soporte técnico durante 6 meses.",
        "offer_end": "2026-12-31T23:59:59",
    }
    return render_template("index.html", product=product)


@app.route("/contacto", methods=["POST"])
def contacto():
    """Procesa un formulario simple de pre-venta y muestra mensaje flash."""
    nombre = request.form.get("nombre", "")
    email = request.form.get("email", "")
    mensaje = request.form.get("mensaje", "")

    if not nombre or not email:
        flash("Por favor completa nombre y email para recibir la oferta.", "danger")
        return redirect(url_for("index") + "#contacto")

    # Aquí podrías integrar envío real por email/CRM.
    flash(
        f"¡Gracias, {nombre}! Recibimos tu mensaje y te contactaremos en menos de 24h.",
        "success",
    )

    if mensaje:
        app.logger.info("Lead recibido: %s - %s - %s", nombre, email, mensaje)

    return redirect(url_for("index") + "#contacto")


if __name__ == "__main__":
    app.run(debug=True)
