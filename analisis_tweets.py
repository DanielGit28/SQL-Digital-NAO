import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob

# Carga los datos del archivo JSON
with open('tweets_extraction.json', 'r', encoding='utf-8') as file:
    tweets_data = json.load(file)

# Crea un DataFrame con los datos de los tweets
df_tweets = pd.DataFrame(tweets_data)

# Función para determinar el sentimiento de un comentario
def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positivo'
    elif analysis.sentiment.polarity < 0:
        return 'negativo'
    else:
        return 'neutral'

# Aplica la función a la columna de texto para obtener el sentimiento de cada comentario
df_tweets['sentimiento'] = df_tweets['texto'].apply(get_sentiment)

# Visualización de los resultados
sentimientos_counts = df_tweets['sentimiento'].value_counts()

# Gráfico de dona de sentimientos
plt.figure(figsize=(8, 6))
plt.pie(sentimientos_counts, labels=sentimientos_counts.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999', '#66b3ff', '#99ff99'])
plt.title('Distribución de Sentimientos en Tweets Analizados')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
