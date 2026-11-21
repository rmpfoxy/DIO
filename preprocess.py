import os
import pandas as pd

df = pd.read_csv('data/sales.csv')

print("--- Diagnóstico Inicial ---")
print(df.head())
print(df.shape)
print(df.dtypes)
print("-" * 30)

df["data"] = pd.to_datetime(df["data"], errors='coerce')

df["mes"] = df["data"].dt.to_period("M").astype(str)

df["status"] = df["status"].str.strip().str.lower()

df = df.drop_duplicates()

df["receita"] = df["quantidade"] * df["preco_unitario"]

os.makedirs("data_processed/sales_clean.csv", Index=False, decimal=",", sep=",")
print("\n[Sucesso] O dado limpo foi salvo em 'data_processed/sales_clean.csv")