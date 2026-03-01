import base64
import json
import logging
from datetime import timedelta

from flask import Flask, jsonify, make_response, redirect, render_template, request, session, url_for
from flask_session import Session

app = Flask(__name__)

# Configuración base para sesiones en servidor.
app.config.update(
    SECRET_KEY="change-this-secret-in-production",
    SESSION_TYPE="filesystem",
    PERMANENT_SESSION_LIFETIME=timedelta(days=30),
)
Session(app)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)
logger = logging.getLogger(__name__)

PRODUCT_INFO = {
    "name": "Acceso a bots de trading Python + actualizaciones + soporte",
    "price_usd": "49",
    "price_usdc": "50",
}


def check_payment() -> bool:
    """Valida si el usuario tiene acceso premium activo en sesión.

    En producción, este método debería consultar una fuente de verdad:
    - base de datos con suscripciones activas,
    - proveedor de pago (Stripe, Coinbase Commerce, etc.),
    - o validación de prueba de pago on-chain (x402).
    """
    return bool(session.get("paid"))


def generate_402_response():
    """Retorna una respuesta 402 con metadata mock en formato x402.

    Para un flujo real x402, reemplaza el payload mock por uno firmado/emitido
    por tu backend de cobro y valida en el servidor la prueba de pago del cliente.
    Referencias:
    - https://docs.coinbase.com/x402
    - https://github.com/coinbase/x402
    """
    payment_request = {
        "amount": "5.00",
        "currency": "USDC",
        "recipient": "0xTuDireccion",
        "chain": "Base",
        "description": "Acceso premium 30 días",
    }
    encoded_payload = base64.b64encode(json.dumps(payment_request).encode("utf-8")).decode("utf-8")

    response = make_response(
        jsonify(
            {
                "error": "Payment Required",
                "message": "Necesitas pagar para acceder al contenido premium.",
                "hint": "Completa el checkout y vuelve a intentar.",
            }
        ),
        402,
    )
    response.headers["PAYMENT-REQUIRED"] = encoded_payload
    return response


@app.route("/")
def index():
    return render_template("index.html", product=PRODUCT_INFO)


@app.route("/buy", methods=["POST"])
def buy():
    """Mock de compra: marca la sesión como pagada.

    Aquí luego puedes integrar un checkout real y, al confirmar pago,
    persistir el acceso premium en DB antes de setear sesión/JWT.
    """
    email = request.form.get("email") or request.json.get("email") if request.is_json else None
    session["paid"] = True
    session["buyer_email"] = email or "cliente@demo.com"
    session.permanent = True

    logger.info("Compra mock registrada para %s", session["buyer_email"])

    if request.is_json:
        return jsonify({"ok": True, "message": "Pago simulado con éxito", "redirect": url_for("premium")})

    return redirect(url_for("premium", success=1))


@app.route("/premium")
def premium():
    if not check_payment():
        logger.warning("Intento de acceso premium sin pago desde IP %s", request.remote_addr)
        return generate_402_response()

    return render_template("premium.html", email=session.get("buyer_email"), product=PRODUCT_INFO)


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
