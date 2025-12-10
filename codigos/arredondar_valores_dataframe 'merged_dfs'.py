#9.9 Arredondar valores do dataframe 'merged_dfs'

merged_dfs['Taxa Cambio u.m.c./US$'] = merged_dfs['Taxa Cambio u.m.c./US$'].round(4)
merged_dfs['Itau'] = merged_dfs['Itau'].round(2)
merged_dfs['Petrobras'] = merged_dfs['Petrobras'].round(2)
merged_dfs['Vale Rio Doce'] = merged_dfs['Vale Rio Doce'].round(2)

print("DataFrame 'merged_dfs' com colunas arredondadas para 2 casas decimais:")
display(merged_dfs.head())
