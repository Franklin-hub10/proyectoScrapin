

import pandas as pd

def compute_stats():
    # leemos el CSV limpio y convertimos la columna date a datetime
    df = pd.read_csv("data/scoreboard_clean.csv", parse_dates=["date"])
    
    # calculamos las métricas básicas
    stats = {
        "goles_promedio": df["total_goals"].mean(), 
        "goles_max":      df["total_goals"].max(),  
        "goles_min":      df["total_goals"].min(), 
        "partidos_tot":   df.shape[0]               
    }
    
    # armamos la serie temporal: suma de goles por día
    trend = (
        df.groupby(df["date"].dt.date)["total_goals"]
          .sum()
          .reset_index()
          .rename(columns={"total_goals": "goles_totales"})
    )
    
    return df, stats, trend

if __name__ == "__main__":
    df, stats, trend = compute_stats()
    print("Estadísticas:")
    for clave, valor in stats.items():
        print(f"{clave}: {valor}")
