# src/clean_data.py

import pandas as pd

def clean_scoreboard():
    # leemos el CSV crudo
    df = pd.read_csv("data/scoreboard.csv", parse_dates=["date"])
    
    # quitamos espacios y ponemos cada palabra en mayúscula
    df["home_team"] = df["home_team"].str.strip().str.title()
    df["away_team"] = df["away_team"].str.strip().str.title()
    
    # borramos partidos repetidos y los que no tienen marcador
    df = df.drop_duplicates(subset=["date", "home_team", "away_team"])
    df = df.dropna(subset=["home_score", "away_score"])
    
    # calculamos goles totales
    df["total_goals"] = df["home_score"] + df["away_score"]
    
    # guardamos el CSV limpio
    df.to_csv("data/scoreboard_clean.csv", index=False)
    print("CSV limpio guardado en data/scoreboard_clean.csv")
    
    return df

if __name__ == "__main__":
    clean_scoreboard()
