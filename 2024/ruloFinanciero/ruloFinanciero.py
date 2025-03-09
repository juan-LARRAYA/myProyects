import requests

def obtener_dolar(tipo):
    """ Obtiene el precio del dólar según el tipo (blue o bolsa).   """
    url = f"https://dolarapi.com/v1/dolares/{tipo}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        raise Exception(f"Error al obtener datos de la API para {tipo}")

def obtener_precio_dolar():
    """Obtiene el precio del dólar blue y MEP (bolsa)."""
    try:
        dolar_blue = obtener_dolar("blue")["venta"]
        dolar_mep = obtener_dolar("bolsa")["compra"]
        return dolar_mep, dolar_blue
    except Exception as e:
        print(e)
        return None, None
        
def gentiRecursivo(veces: int, dineroInicial: float, factor: float) -> float:
    if veces == 0:
        return round(dineroInicial, 2)
    dineroInicial *= factor
    return gentiRecursivo(veces - 1, dineroInicial, factor)



# Obtener los precios del dólar˜˜
dolar_mep, dolar_blue = obtener_precio_dolar()

# Definir la tasa de interés 
rulo = dolar_blue/dolar_mep  #tasa real que ganas comprando mep y vendiendo blue
print("Dolar mep para la compra hoy: ", dolar_mep)
print("Dolar blue para la venta hoy: ", dolar_blue)
print("ganancia porcentual del rulo: ",100*(rulo-1))

# Impresión de resultados para diferentes valores de veces
print("hacelo 3 veces y ganas:", gentiRecursivo(3, 72000, rulo))
print("hacelo 4 veces y ganas:", gentiRecursivo(4, 72000, rulo))
print("hacelo 5 veces y ganas:", gentiRecursivo(5, 72000, rulo))
print("hacelo 6 veces y ganas:", gentiRecursivo(6, 72000, rulo))
print("hacelo 7 veces y ganas:", gentiRecursivo(7, 72000, rulo))
print("hacelo 8 veces y ganas:", gentiRecursivo(8, 72000, rulo))
print("hacelo 9 veces y ganas:", gentiRecursivo(9, 72000, rulo))

