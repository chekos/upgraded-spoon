import requests
import json

# URL de la API
api_url = "https://my.api.mockaroo.com/users.json"
payload = {"key": "03ee11f0}

# Hacer la petición a la API
response = requests.get(api_url, params=payload)

# Verificar que la petición fue exitosa
if response.status_code == 200:
    # Convertir la respuesta en JSON
    data = response.json()
    
    # Guardar los datos en un archivo JSON
    with open('users_data.json', 'w') as file:
        json.dump(data, file)
    
    print("Datos extraídos y guardados en 'users_data.json'.")
else:
    print("Error al hacer la petición a la API:", response.status_code)
