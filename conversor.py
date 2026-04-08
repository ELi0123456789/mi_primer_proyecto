import requests

def convertir_moneda():
    print("--- Conversor de Monedas Express ---")
    
    # Configuración de la API (Uso de una clave gratuita de ejemplo)
    api_key = "b0b85b07058c4c6a20bb0570" # Esta es una key de prueba
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"

    try:
        # Obtenemos los datos
        respuesta = requests.get(url)
        datos = respuesta.json()

        if respuesta.status_code != 200:
            print("Error al conectar con la API.")
            return

        # Pedir datos al usuario
        monto = float(input("Ingresa la cantidad en USD: "))
        moneda_destino = input("Ingresa la moneda de destino (ej: MXN, EUR, ARS): ").upper()

        # Lógica de conversión
        if moneda_destino in datos['conversion_rates']:
            tasa = datos['conversion_rates'][moneda_destino]
            resultado = monto * tasa
            print(f"\n{monto} USD equivalen a {resultado:.2f} {moneda_destino}")
            print(f"Tasa de cambio actual: {tasa}")
        else:
            print("Esa moneda no está disponible.")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    convertir_moneda()