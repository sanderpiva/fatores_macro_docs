#11 Carregar dataframe parcial (parcial_merged_dfs) e calcular o retorno 
# logaritmo das ações do itaú, Petrobras, Vale do Rio Doce

try:
    final_merged_df = pd.read_csv('/content/parcial_merged_dfs_cds.csv')
    final_merged_df['Data'] = pd.to_datetime(final_merged_df['Data'])
    final_merged_df = final_merged_df.sort_values('Data')
except FileNotFoundError:
    print("Certifique-se de que o arquivo final_merged_dataset.csv está disponível.")

acoes = ['Itau', 'Petrobras', 'Vale Rio Doce']

for acao in acoes:

    final_merged_df[f'RETORNO_LOG_{acao}'] = np.log(
        final_merged_df[acao] / final_merged_df[acao].shift(1)
    )

final_merged_df = final_merged_df.dropna(subset=[f'RETORNO_LOG_{acao}' for acao in acoes])

print("DataFrame com as novas colunas de Retorno Logarítmico:")
final_merged_df_with_returns = final_merged_df[[
    'Data', 'Taxa Selic - a.a.', 'Taxa Cambio u.m.c./US$', 'CDS', 'Itau', 'RETORNO_LOG_Itau',
    'Petrobras', 'RETORNO_LOG_Petrobras',
    'Vale Rio Doce', 'RETORNO_LOG_Vale Rio Doce']]

display(final_merged_df_with_returns.head())
final_merged_df_with_returns.info()
     

