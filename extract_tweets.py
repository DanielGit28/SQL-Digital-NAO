import json

# Carga los datos del archivo JSON
with open('tweets_extraction.json', 'r', encoding='utf-8') as file:
    tweets_data = json.load(file)

# Extrae información de cada tweet
for tweet in tweets_data[:10]:
    tweet_id = tweet['id']
    tweet_text = tweet['texto']
    tweet_user = tweet['usuario']
    tweet_hashtags = tweet['hashtags']
    tweet_date = tweet['fecha']
    tweet_retweets = tweet['retweets']
    tweet_favorites = tweet['favoritos']

    # Verifica tipos de datos
    print(f"ID: {tweet_id}, Tipo: {type(tweet_id)}")
    print(f"Texto: {tweet_text}, Tipo: {type(tweet_text)}")
    print(f"Usuario: {tweet_user}, Tipo: {type(tweet_user)}")
    print(f"Hashtags: {tweet_hashtags}, Tipo: {type(tweet_hashtags)}")
    print(f"Fecha: {tweet_date}, Tipo: {type(tweet_date)}")
    print(f"Retweets: {tweet_retweets}, Tipo: {type(tweet_retweets)}")
    print(f"Favoritos: {tweet_favorites}, Tipo: {type(tweet_favorites)}")
    print()

# Verifica estructura de datos
print(f"Número de tweets: {len(tweets_data)}")

#Imprime la estructura de cada objeto del json de tweets
print("Estructura de un tweet: ")
for key in tweets_data[0].keys():
    print (key)
