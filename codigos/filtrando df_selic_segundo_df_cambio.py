#4 Filtrando df_selic para incluir apenas 
# as datas presentes em df_cambio | Renomeando a coluna da SELIC no dataframe filtrado

df_selic_filtered = df_selic[df_selic['Data'].isin(df_cambio['Data'])].copy()

df_selic_filtered = df_selic_filtered.rename(columns={'432 - Taxa de juros - Meta Selic definida pelo Copom - % a.a.': 'Taxa Selic - a.a.'})
