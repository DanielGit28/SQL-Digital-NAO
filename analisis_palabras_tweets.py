import json
import pandas as pd
import matplotlib.pyplot as plt

# Carga los datos del archivo JSON
with open('tweets_extraction.json', 'r', encoding='utf-8') as file:
    tweets_data = json.load(file)

# Crea un DataFrame con los datos de los tweets
df_tweets = pd.DataFrame(tweets_data)

# Palabras clave a buscar en los comentarios
palabras_clave = ['bugs', 'diseño', 'documentos', 'facilidad de uso', 'características', 'otros', 'pdf', 'precio', 'propuestas', 'calidad', 'menciones', 'servicio', 'ui']

# Función para evaluar la presencia de palabras clave en un comentario
def evaluar_palabras_clave(texto):
    palabras_encontradas = [palabra for palabra in palabras_clave if palabra in texto.lower()]
    return palabras_encontradas

# Aplica la función a la columna de texto para obtener las palabras clave encontradas en cada comentario
df_tweets['palabras_clave'] = df_tweets['texto'].apply(evaluar_palabras_clave)

# Cuenta la frecuencia de cada palabra clave y crea un DataFrame con los resultados
df_palabras_clave = pd.DataFrame(df_tweets['palabras_clave'].explode().value_counts()).reset_index()
df_palabras_clave.columns = ['palabra_clave', 'cantidad']

# Grafico de barras de la frecuencia de palabras clave
plt.figure(figsize=(10, 6))
plt.bar(df_palabras_clave['palabra_clave'], df_palabras_clave['cantidad'], color='skyblue')
plt.xlabel('Palabra Clave')
plt.ylabel('Cantidad de Tweets Relacionados')
plt.title('Frecuencia de Palabras Clave en Tweets Analizados')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
