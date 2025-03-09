import mysql.connector
import pandas as pd
from datetime import datetime
#from openai import OpenAI 
import anthropic
from textblob import TextBlob
import matplotlib.pyplot as plt
from fpdf import FPDF
from dotenv import load_dotenv
import os


# Configuración de Claude (otra IA que si es gratuita)
load_dotenv('api_key.env')  # Carga las variables de entorno desde el archivo .env

api_key_anthropic = os.getenv('API_KEY')

client = anthropic.Anthropic(api_key = api_key_anthropic)
client

def clasificar_comentarios(comentarios):
    clasificaciones = []
    for comentario in comentarios:
        client.messages.create(
            model= 'claude-3-sonnet-20240229',
            max_tokens=10,
            n=1,
            messages = [{"role": "user","content": "Por favor clasifica el siguiente comentario como satisfactorio, insatisfactorio o neutro: Estuve mas de seis meses tratando de que me reembolsaran los primeros gastos de servicio de luz, agua y gas. Clasificación:"}],
            
        )
        clasificacion = completion.choices[0].message.content.strip().lower()

        clasificacion = response.choices[0].text
        clasificaciones.append(clasificacion)
    return clasificaciones




"""
# Configuración de OpenAI
openai = OpenAI(
    api_key = os.getenv('API_KEY'),
)

"""

# Conexión a la base de datos
db_config = {
    'user': 'postulante',
    'password': 'HB<tba!Sp6U2j5CN',
    'host': '54.219.2.160',
    'database': 'prueba_postulantes'
}


conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()


# Lectura de la tabla MySQL con los datos de la encuesta
query = "SELECT * FROM encuesta"
cursor.execute(query)
rows = cursor.fetchall()
columns = cursor.column_names
df = pd.DataFrame(rows, columns=columns)


# Cálculo de valores solicitados

#sng de satisfaccion general
total_respuestas = len(df)
satisfaccion = df[(df['satisfeccion_general'] >= 6) & (df['satisfeccion_general'] <= 7)].shape[0]
insatisfaccion = df[(df['satisfeccion_general'] >= 1) & (df['satisfeccion_general'] <= 4)].shape[0]
sng = round((satisfaccion * 100) / total_respuestas) - round((insatisfaccion * 100) / total_respuestas)

#Total de personas que conocian la empresa
total_conocia_empresa = df[df['conocia_empresa'] == 'si'].shape[0]

#sng de recomendacion
satisfaccion_recomendacion = df[(df['recomendacion'] >= 6) & (df['recomendacion'] <= 7)].shape[0]
insatisfaccion_recomendacion = df[(df['recomendacion'] >= 1) & (df['recomendacion'] <= 4)].shape[0]
sng_recomendacion = round((satisfaccion_recomendacion * 100) / total_respuestas) - round((insatisfaccion_recomendacion * 100) / total_respuestas)

#nota promedio de recomendacion
nota_promedio_recomendacion = df['recomendacion'].mean()

#Total de personas que hicieron un comentario
total_hicieron_comentario = df[df['recomendacion_abierta'].notnull() & (df['recomendacion_abierta'] != '')].shape[0]

#Dias y meses que llevo la encuesta
fecha_inicio = pd.to_datetime(df['fecha']).min()
fecha_fin = pd.to_datetime(df['fecha']).max()



dias_encuesta = (fecha_fin - fecha_inicio).days
meses_encuesta = dias_encuesta // 30





####################################################################################
#           Análisis de sentimiento con Claude            
####################################################################################

#comentarios = df['recomendacion_abierta'].dropna().tolist()

client.messages.create(
    model = 'claude-3-sonnet-20240229',
    max_tokens = 10,
    messages = [{"role": "user","content": "Por favor clasifica el siguiente comentario como satisfactorio, insatisfactorio o neutro: Estuve mas de seis meses tratando de que me reembolsaran los primeros gastos de servicio de luz, agua y gas. Clasificación:"}]        
)

#print(messages)

"""
def generar_conclusion(comentarios):
    prompt = "A continuación se presentan algunos comentarios sobre una empresa. Por favor, proporciona un análisis de los problemas principales y una conclusión general basada en estos comentarios:\n\n"
    for comentario in comentarios:
        prompt += f"- {comentario}\n"
    prompt += "\nProblemas principales y conclusión:"

    client.messages.create(
        model= 'claude-3-sonnet-20240229',
        max_tokens=100,
        n=1,
        messages=[{"role": "user", "content": prompt}],
    )

    conclusion = response.choices[0].text.strip()
    return conclusion


# Clasificación de los comentarios
clasificaciones = clasificar_comentarios(comentarios)
print("Clasificaciones de los comentarios:")
print(df_clasificaciones)



# Obtención de la conclusión y análisis de problemas principales
conclusion = generar_conclusion(comentarios)

print("\nConclusión y análisis de problemas principales:")
print(conclusion)

"""






"""

####################################################################################
#           Análisis de sentimiento con textBlob            
####################################################################################

comentarios = df['recomendacion_abierta'].dropna().tolist()
sentimientos = []



for comentario in comentarios:
    analysis = TextBlob(comentario)
    sentimientos.append(analysis.sentiment.polarity)

df_sentimientos = pd.DataFrame({
    'comentario': comentarios,
    'sentimiento': sentimientos
})




"""




"""
####################################################################################
#               Creación de gráficos de            
####################################################################################

plt.figure(figsize=(10, 5))
df['satisfeccion_general'].hist()
plt.title('Distribución de Satisfacción General')
plt.xlabel('Satisfacción General')
plt.ylabel('Frecuencia')
plt.savefig('satisfeccion_general.png')

plt.figure(figsize=(10, 5))
df_sentimientos['sentimiento'].hist()
plt.title('Distribución de Sentimientos')
plt.xlabel('Sentimiento')
plt.ylabel('Frecuencia')
plt.savefig('sentimientos.png')



# Cierre de la conexión
cursor.close()
conn.close()

"""



"""
####################################################################################
#                     Análisis de sentimiento CON CHAT GPT
####################################################################################

# Función para clasificar los comentarios utilizando ChatGPT
def clasificar_comentarios(comentarios):
    clasificaciones = []
    for comentario in comentarios:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            #messages=[{"role": "user","content": "Por favor clasifica el siguiente comentario como satisfactorio, insatisfactorio o neutro:\n\n{comentario}\n\nClasificación:"}],
            messages=[{"role": "user","content": "Por favor clasifica el siguiente comentario como satisfactorio, insatisfactorio o neutro: Estuve mas de seis meses tratando de que me reembolsaran los primeros gastos de servicio de luz, agua y gas. Clasificación:"}],
             
            max_tokens=10,
            n=1,
        )
        clasificacion = completion.choices[0].message.content.strip().lower()

        #clasificacion = response.choices[0].text
        clasificaciones.append(clasificacion)
    return clasificaciones



def generar_conclusion(comentarios):
    prompt = "A continuación se presentan algunos comentarios sobre una empresa. Por favor, proporciona un análisis de los problemas principales y una conclusión general basada en estos comentarios:\n\n"
    for comentario in comentarios:
        prompt += f"- {comentario}\n"
    prompt += "\nProblemas principales y conclusión:"

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",        
        messages=[{"role": "user", "content": prompt}],
    )

    conclusion = response.choices[0].text.strip()
    return conclusion

# Clasificación de los comentarios
clasificaciones = clasificar_comentarios(comentarios)
print("Clasificaciones de los comentarios:")
print(df_clasificaciones)

# Obtención de la conclusión y análisis de problemas principales
conclusion = generar_conclusion(comentarios)

print("\nConclusión y análisis de problemas principales:")
print(conclusion)
"""

