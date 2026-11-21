import pandas as pd

df = pd.read_csv("creditcard.csv") 

fraudes = df[df["Class"] == 1]
normais = df[df["Class"] == 0].sample(len(fraudes), random_state=42)

df_under = pd.concat([fraudes, normais])
print(df_under["Class"].value_counts())