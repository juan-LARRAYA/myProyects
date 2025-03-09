import requests
import time



def get_coordinates_osm(address):
    url = f"https://nominatim.openstreetmap.org/search?q={address}&format=json&limit=1"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (compatible; OpenStreetMap Python Script)'})
    if response.status_code == 200:
        data = response.json()
        if data:
            lat = float(data[0]['lat'])
            lon = float(data[0]['lon'])
            return lat, lon
        else:
            print(f"No se encontraron resultados para la dirección: {address}")
            return None
    else:
        print(f"Error en la solicitud a Nominatim. Código de estado: {response.status_code}")
        return None

def calculate_center_of_mass(coordinates):
    lat_sum = sum(lat for lat, lon in coordinates)
    lon_sum = sum(lon for lat, lon in coordinates)
    
    center_lat = lat_sum / len(coordinates)
    center_lon = lon_sum / len(coordinates)
    
    return center_lat, center_lon

# Lista de direcciones de tus amigos
addresses = [
    "Vicente Lopez 2227, recoleta, Buenos Aires, Argentina",
    "Federico Lacroze 2344, Buenos Aires, Argentina",
    #"Gurruchaga 690, villa crespo, Buenos Aires, Argentina",
    #"Manuela Pedraza 5983, villa urquiza, Buenos Aires, Argentina",
    #yerson no viene "soldado de independencia 979, palermo, Buenos Aires, Argentina",
    #"amenabar 2445, nuñez, Buenos Aires, Argentina",
    #"Hernan Cortes 440, Sarandi",
    #"Somellera 678, Adrogué",
    #pessi no viene "Francisco Acuña de Figueroa 719, Buenos Aires, Argentina"

    #"Dirección, barrio, Ciudad, País",
    # Añade más direcciones aquí
]

# Convertir direcciones a coordenadas
coordinates = []
for address in addresses:
    coords = get_coordinates_osm(address)
    if coords != None:
        coordinates.append(coords)
    # Añade un pequeño retardo para no sobrecargar el servicio
    time.sleep(1)

# Calcular el centro de masa si se obtuvieron todas las coordenadas
if coordinates:
    center_of_mass = calculate_center_of_mass(coordinates)
    print(f"Centro de masa (Latitud, Longitud): {center_of_mass}")
else:
    print("No se pudieron obtener suficientes coordenadas para calcular el centro de masa.")


