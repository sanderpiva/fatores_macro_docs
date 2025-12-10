#9.5 Verificar a ordem das colunas do dataframe
# merged_df_selic_cambio_preco_cds e proceder reorganização

current_cols = merged_df_selic_cambio_preco_cds.columns.tolist()
display(current_cols)

desired_order = [
    'Data',
    'Taxa Selic - a.a.',
    'Taxa Cambio u.m.c./US$',
    'CDS',
    'ITUB4',
    'PETR4',
    'VALE3'
]

merged_dfs_columns_ordered = merged_df_selic_cambio_preco_cds.reindex(columns=desired_order)

print("\nPrimeiras linhas do dataset final com colunas reordenadas:")
display(merged_dfs_columns_ordered.head())
print("\nInformações do dataset final com colunas reordenadas:")
merged_dfs_columns_o