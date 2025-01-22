import requests
import time

def obtener_precio_cripto(cripto_id='WLD', moneda='USD'):
    """
    Obtiene el precio de una criptomoneda en una moneda específica utilizando la API de CryptoCompare sin necesidad de API key.

    Args:
    - cripto_id: El identificador de la criptomoneda (por ejemplo, 'worldcoin', 'bitcoin', 'ethereum', etc.).
    - moneda: La moneda en la que deseas obtener el precio (por ejemplo, 'USD', 'EUR', etc.).

    Returns:
    - El precio de la criptomoneda en la moneda especificada.
    """
    url = f'https://min-api.cryptocompare.com/data/price'

    params = {
        'fsym': cripto_id,  # Símbolo de la criptomoneda
        'tsyms': moneda     # Símbolo de la moneda
    }

    try:
        # Realizamos la solicitud a la API
        respuesta = requests.get(url, params=params)
        respuesta.raise_for_status()  # Si la respuesta tiene un error, lanza una excepción

        # Extraemos el precio de la respuesta JSON
        data = respuesta.json()

        # Verificamos si la criptomoneda está presente en la respuesta
        if moneda in data:
            precio = data[moneda]
            return precio
        else:
            print(f"No se encontró el precio para '{cripto_id}' en la respuesta.")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener los datos: {e}")
        return None

def mostrar_precio_continuo():
    """
    Muestra el precio de la criptomoneda en la terminal de forma continua.
    """
    while True:
        precio = obtener_precio_cripto()  # Obtiene el precio
        if precio is not None:
            print(f"El precio actual de Worldcoin (WLD) es: {precio} USD")
        else:
            print("No se pudo obtener el precio en tiempo real.")

        # Pausa de 10 segundos antes de obtener el precio de nuevo
        time.sleep(10)  # Puedes cambiar el tiempo si necesitas una frecuencia mayor o menor

# Iniciar la visualización del precio en la terminal
if __name__ == '__main__':
    mostrar_precio_continuo()
