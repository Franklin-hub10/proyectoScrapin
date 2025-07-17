# src/fetch_scoreboard.py

import requests
import pandas as pd

def fetch_scoreboard():
    # Acá elegimos la liga (esp.1 es la Primera División de España)
    liga = "esp.1"
    # Endpoint de ESPN para obtener el marcador de la liga
    url = f"https://site.api.espn.com/apis/site/v2/sports/soccer/{liga}/scoreboard"
    
    # Hacemos la petición a la API
    resp = requests.get(url)
    # Si algo anda mal, aquí explota y nos enteramos
    resp.raise_for_status()
    
    # Convertimos la respuesta a JSON
    data = resp.json()

    registros = []
    # Recorremos cada partido en el JSON
    for evento in data["events"]:
        comp = evento["competitions"][0]
        fecha = pd.to_datetime(evento["date"])
        
        # Distinguimos quién juega de local y quién de visitante
        home = next(c for c in comp["competitors"] if c["homeAway"] == "home")
        away = next(c for c in comp["competitors"] if c["homeAway"] == "away")
        
        # Metemos todo en un diccionario
        registros.append({
            "date":       fecha,
            "home_team":  home["team"]["displayName"],
            "home_score": int(home["score"] or 0),   # si no hay score, ponemos 0
            "away_team":  away["team"]["displayName"],
            "away_score": int(away["score"] or 0),
            "status":     comp["status"]["type"]["description"]
        })

    # Armamos el DataFrame con pandas
    df = pd.DataFrame(registros)
    # Guardamos a CSV para tener un respaldo fácil de revisar
    df.to_csv("data/scoreboard.csv", index=False)
    return df

if __name__ == "__main__":
    fetch_scoreboard()
