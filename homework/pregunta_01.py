"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import os
from datetime import datetime



def corregir_fecha(fecha):
        partes = fecha.split('/')
        p1, p2, p3 = partes[0], partes[1], partes[2]
        if len(p1) == 4:
            date = '/'.join(reversed(partes))
        else:
            date = '/'.join(partes)
        return date



def pregunta_01():

    df = pd.read_csv("files/input/solicitudes_de_credito.csv", sep=";")
    df = df.dropna() 
    df['sexo'] = df.sexo.str.lower()
    df['tipo_de_emprendimiento'] = df.tipo_de_emprendimiento.str.lower()


    df['idea_negocio'] = df.idea_negocio.str.lower()

    caracteres1 = ['_', '-']
    for c in caracteres1:
     df["idea_negocio"] = df["idea_negocio"].str.replace(c, ' ', regex=False)


    df['barrio'] = df.barrio.str.lower()
    for c in caracteres1:
        df["barrio"] = df["barrio"].str.replace(c, ' ', regex=False)


    df['línea_credito'] = df.línea_credito.str.lower()
    for c in caracteres1:
     df["línea_credito"] = df["línea_credito"].str.replace(c, ' ', regex=False)


    df["fecha_de_beneficio"] = df["fecha_de_beneficio"].apply(corregir_fecha)

    caracteres2 = [' ', '$', ',']
    for c in caracteres2:
     df["monto_del_credito"] = df["monto_del_credito"].str.replace(c, '', regex=False)
    df.monto_del_credito = df.monto_del_credito.astype(float)

    df = df.drop_duplicates(subset=[
    "sexo", "tipo_de_emprendimiento", "idea_negocio", "barrio", "estrato",
    "comuna_ciudadano", "fecha_de_beneficio", "monto_del_credito", "línea_credito"
]).dropna()


    df.to_csv("files/output/solicitudes_de_credito.csv", sep=";", index=False)

