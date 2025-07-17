#!/usr/bin/env python3
import subprocess
import sys

def run(cmd):
    print(f"\n🔄 Ejecutando: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    if result.returncode != 0:
        sys.exit(f"⚠️ El comando {' '.join(cmd)} falló con código {result.returncode}")

def main():
    # 1) Obtener datos
    run([sys.executable, "src/fetch_scoreboard.py"])
    # 2) Limpiar y organizar
    run([sys.executable, "src/clean_data.py"])
    # 3) Análisis estadístico
    run([sys.executable, "src/analysis.py"])
    # 4) Lanzar la app Streamlit (bloqueará aquí hasta que detengas Ctrl+C)
    run(["streamlit", "run", "src/app.py"])

if __name__ == "__main__":
    main()
