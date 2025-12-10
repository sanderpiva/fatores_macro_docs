#9.2 Realizar ajustes no frame Risco Brasil - CDS

df_risc[['Data', 'CDS']] = df_risc['Data,CDS'].str.split(',', n=1, expand=True)

df_risc['Data'] = pd.to_datetime(df_risc['Data'], format='%d.%m.%Y', errors='coerce')

df_risc['CDS'] = df_risc['CDS'].str.replace('"', '', regex=False)
df_risc['CDS'] = df_risc['CDS'].str.replace(',', '.', regex=False)
df_risc['CDS'] = pd.to_numeric(df_risc['CDS'], errors='coerce')

df_risc.drop(columns=['Data,CDS'], inplace=True)
df_risc.dropna(subset=['Data', 'CDS'], inplace=True)

print("\nPrimeiras linhas do dataset df_risc com as colunas 'Data' e 'CDS' corrigidas:")
display(df_risc.head())
print("\nInformações do dataset df_risc com as colunas 'Data' e 'CDS' corrigidas:")
df_risc.info()

