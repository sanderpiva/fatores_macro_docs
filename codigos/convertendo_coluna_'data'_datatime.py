#3 Convertendo as colunas 'Data', do df_cambio, para datetime

df_cambio['Data'] = pd.to_datetime(df_cambio['Data'], format='%d/%m/%Y', errors='coerce')