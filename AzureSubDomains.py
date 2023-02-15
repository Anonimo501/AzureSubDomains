import requests
from tabulate import tabulate

# Dominio ingresado por el usuario
dominio = input("Ingrese el dominio: ")

# Lista de extensiones
extensiones = [".azurewebsites.net", ".scm.azurewebsites.net", ".p.azurewebsites.net", ".cloudapp.net", ".file.core.windows.net", ".blob.core.windows.net", ".queue.core.windows.net", ".table.core.windows.net", ".redis.cache.windows.net", ".documents.azure.com", ".database.windows.net", ".vault.azure.net", ".onmicrosoft.com", ".mail.protection.outlook.com", ".sharepoint.com", ".azureedge.net", ".search.windows.net", ".azure-api.net"]

# Tabla de resultados
resultados = []

# Verificar cada subdominio
for extension in extensiones:
    subdominio = dominio + extension
    try:
        # Realizar solicitud GET
        response = requests.get("https://" + subdominio, timeout=3)
        # Almacenar el resultado en la tabla
        resultados.append([subdominio, response.status_code == 200])
    except requests.exceptions.Timeout:
        # Si se agota el tiempo de conexión, almacenar False en la tabla
        resultados.append([subdominio, False])
    except requests.exceptions.RequestException:
        # Si hay un error de conexión, almacenar False en la tabla
        resultados.append([subdominio, False])

# Imprimir la tabla de resultados con tabulate
encabezado = ["Subdominio", "Éxito"]
tabla = tabulate(resultados, headers=encabezado, tablefmt="grid")
print(tabla)
