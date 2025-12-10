#9.6 Renomear colunas para os nomes reais das companhias

merged_dfs = merged_dfs_columns_ordered.rename(columns={
    'ITUB4': 'Itau',
    'PETR4': 'Petrobras',
    'VALE3': 'Vale Rio Doce'
})

print("\nPrimeiras linhas do dataframe final com colunas de ações renomeadas:")
display(merged_dfs.head())
print("\nInformações do dataframe final com colunas de ações renomeadas:")
merged_dfs.info()
