#9.8 Ajustar escala da coluna Taxa Selic (Dividir por 100)

# Correção da escala da Selic
merged_dfs['Taxa Selic - a.a.'] = merged_dfs['Taxa Selic - a.a.'] / 100

# Verificação
display(merged_dfs['Taxa Selic - a.a.'].head())
merged_dfs.info()
display(merged_dfs)