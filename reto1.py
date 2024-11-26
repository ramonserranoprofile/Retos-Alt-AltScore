import requests
import math

# URLs proporcionadas
get_url = "https://example.com/v1/s1/e1/resources/measurement"
post_url = "https://example.com/v1/s1/e1/solution"

def get_measurement():
    response = requests.get(get_url)
    data = response.json()
    return data

def calculate_speed(distance, time):
    if time == 0:
        return None  # Evitar divisiones por cero
    speed = distance / time
    return round(speed)

def send_solution(speed):
    payload = {"speed": speed}
    response = requests.post(post_url, json=payload)
    return response.status_code, response.text

def main():
    data = get_measurement()
    
    # Verificar si los datos del escáner son válidos
    if not data.get("success", False):
        print("Error en la lectura del escáner. Interferencia cósmica detectada.")
        return

    # Obtener valores de distancia y tiempo
    distance = data.get("distance")
    time = data.get("time")
    
    if distance is None or time is None:
        print("Datos incompletos recibidos.")
        return
    
    # Calcular la velocidad orbital
    speed = calculate_speed(distance, time)
    if speed is None:
        print("No se puede calcular la velocidad debido a un tiempo igual a cero.")
        return
    
    # Enviar la solución
    status_code, response_text = send_solution(speed)
    if status_code == 200:
        print("Respuesta enviada exitosamente:", response_text)
    else:
        print(f"Error al enviar la respuesta. Código de estado: {status_code}, Respuesta: {response_text}")

if __name__ == "__main__":
    main()
