# src/app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from analysis import compute_stats

# cargamos datos y estadísticas
df, stats, trend = compute_stats()

# configuración inicial de la página
st.set_page_config(page_title="Marcadores ESPN EC", layout="wide")
st.title("Marcadores Diario – ESPN Ecuador")

# mostramos los KPIs más importantes
k1, k2, k3, k4 = st.columns(4)
k1.metric("Partidos totales", stats["partidos_tot"])
k2.metric("Goles promedio", f"{stats['goles_promedio']:.2f}")
k3.metric("Goles máximo", int(stats["goles_max"]))
k4.metric("Goles mínimo", int(stats["goles_min"]))

st.markdown("---")

# tabla resumida con todos los partidos
st.subheader("Tabla de partidos")
st.dataframe(df, use_container_width=True)

st.markdown("---")

# histograma de goles totales usando matplotlib
st.subheader("Histograma de goles totales")
fig1, ax1 = plt.subplots()
ax1.hist(df["total_goals"], bins=range(int(df["total_goals"].max()) + 2))
ax1.set_xlabel("Goles totales")
ax1.set_ylabel("Frecuencia")
st.pyplot(fig1)

# boxplot local vs visitante usando seaborn
st.subheader("Boxplot de goles locales vs visitantes")
fig2, ax2 = plt.subplots()
sns.boxplot(data=df[["home_score", "away_score"]], ax=ax2)
ax2.set_xlabel("Tipo de equipo")
ax2.set_xticklabels(["Local", "Visitante"])
ax2.set_ylabel("Goles")
st.pyplot(fig2)

# gráfico de línea de la tendencia de goles por fecha usando plotly
st.subheader("Tendencia de goles por fecha")
fig3 = px.line(
    trend,
    x="date",
    y="goles_totales",
    labels={"date": "Fecha", "goles_totales": "Goles totales"},
    title="Goles totales por día"
)
st.plotly_chart(fig3, use_container_width=True)
