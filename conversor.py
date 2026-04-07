import requests

def convertir_momneda():
        print("Conversor de monedas")
        api_key = "602d33405781a539b52479e0" # Esta es una key de prueba
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
        
    try:
        respuesta = requests.get(url)
        datos = respuesta.json()

        if respuesta.status_code != 200:
            print("error al conectar a la api")    
            return
        
        monto = float(input("ingresa la cantidad en USD: "))
        moneda_destino = input("ingresa la moneda destino: ")

        if moneda_destino in datos['conversion_rates']:
               tasa = datos['conversion_rates'][moneda_destino]
               resultado = monto * tasa
               print("f\n{monto} USD equivalen a {resultado:.2f}{moneda_destino}")
               print("tasa de cambio actual: {tasa}")
        else:
               print("esa moneda no esta disponible")
    except Exception as e:
       print(f"ocurrio un problema {e}")

if  __name__ == "__main__":
       convertir_momneda()


