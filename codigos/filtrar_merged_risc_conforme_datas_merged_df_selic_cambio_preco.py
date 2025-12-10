#9.3 Filtrar o dataframe merged_risk de modo que sejam incluidas 
# apenas as datas do dataframe merged_df_selic_cambio_preco

merged_risc_filtered = df_risc[df_risc['Data'].isin(merged_df_selic_cambio_preco['Data'])].copy()
merged_risc_filtered.info()