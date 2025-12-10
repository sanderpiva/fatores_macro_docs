#6 Realizando merge dos dataframes df_selic, df_cambio, 
# tendo como referencia/índice a coluna 'Data'


merged_df_selic_cambio = pd.merge(
    df_selic_filtered[['Data', 'Taxa Selic - a.a.']],
    df_cambio[['Data', 'Taxa Cambio u.m.c./US$']],
    on='Data',
    how='inner'
)

print("\nPrimeiras linhas do dataset unido corretamente:")
display(merged_df_selic_cambio.head())
print("\nInformações do dataset unido corretamente:")
merged_df_selic_cambio.info()