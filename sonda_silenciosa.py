from flask import Flask, jsonify, request

app = Flask(__name__)

# Datos simulados para la lectura del escáner (GET)
measurement_data = {
    "distance": 5.5,  # distancia en unidades astronómicas (UA)
    "time": 12.2,  # tiempo en horas
}


@app.route("/v1/s1/e1/resources/measurement", methods=["GET"])
def get_measurement():
    """
    Ruta GET que devuelve los datos de medición del escáner.
    """
    # Puedes agregar lógica adicional aquí si necesitas manipular los datos
    return jsonify(measurement_data)


@app.route("/v1/s1/e1/solution", methods=["POST"])
def post_solution():
    """
    Ruta POST para recibir la solución calculada (velocidad orbital).
    """
    # Recibimos la solución en formato JSON
    data = request.get_json()

    if "speed" not in data:
        return (
            jsonify({"error": "La velocidad orbital no está incluida en la solicitud"}),
            400,
        )

    speed = data["speed"]

    # Puedes procesar la solución aquí, por ejemplo, guardar la velocidad calculada
    # Pero en este caso, simplemente la devolvemos
    return jsonify({"message": "Solución recibida con éxito", "speed": speed})


if __name__ == "__main__":
    app.run(debug=True)
