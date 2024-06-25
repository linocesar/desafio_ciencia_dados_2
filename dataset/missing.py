import pandas as pd

df = pd.read_csv('table_AIH_2009_2024_SUBGRUPO_PROC.csv', sep='')


# grupoby por ano e municipio
df = df.groupby(['ano', 'Nome_Municipio'])['qtd_0310'].sum()

print(df)
