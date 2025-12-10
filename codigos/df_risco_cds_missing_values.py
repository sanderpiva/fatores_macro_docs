#3 Carregar dataframe Risco Brasil - CDS e checar valores missing
df_risc = pd.read_csv('/content/Brasil_CDS_5anos_final.csv', sep=';')
print("Primeiras linhas do dataframe carregado corretamente:")
display(df_risc.head())
print("\nInformações do dataframe carregado corretamente:")
df_risc.info()
df_risc.isnull().sum()



