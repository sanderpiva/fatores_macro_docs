#8  Garantir que a coluna 'Date' no dataframe df_preco
# esteja no formato datatime e nomeada como 'Data',
# seguindo o padrão dos dataframes anteriores. 
# Proceder o merge entre os dataframes.

df_preco['Data'] = pd.to_datetime(df_preco['Date'])

df_preco_filtered = df_preco[df_preco['Data'].isin(merged_df_selic_cambio['Data'])].copy()

merged_df_selic_cambio_preco = pd.merge(
    merged_df_selic_cambio,
    df_preco_filtered[['Data', 'ITUB4', 'PETR4', 'VALE3']],
    on='Data',
    how='inner'
)

print("\nPrimeiras linhas do dataset final unido:")
display(merged_df_selic_cambio_preco.head())
print("\nInformações do dataset final unido:")
merged_df_selic_cambio_preco.info()
merged_df_selic_cambio_preco.tail()