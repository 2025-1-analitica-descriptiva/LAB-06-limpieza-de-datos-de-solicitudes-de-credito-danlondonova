import pandas as pd

def main():
    # Cargar el archivo limpio
    df = pd.read_csv("files/output/solicitudes_de_credito.csv", sep=';')

    # Verificar si la columna existe
    if "sexo" not in df.columns:
        print("La columna 'sexo' no existe en el archivo.")
        return

    # Mostrar valores únicos
    print("Valores únicos en 'sexo':\n")
    for valor in sorted(df["sexo"].dropna().unique()):
        print(f"- {valor}")

if __name__ == "__main__":
    main()