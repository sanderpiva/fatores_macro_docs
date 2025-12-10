# --- 3 Carregando dataframe de preços de ações e checando valores missing ---
df_preco = pd.read_csv('/content/precos_acoes_5anos.csv')
display(df_preco.head())
df_preco.info()
