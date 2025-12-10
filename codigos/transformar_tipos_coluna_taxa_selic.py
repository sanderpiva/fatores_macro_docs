#9.7 Transformar tipo de dados da Taxa Selic em numero

col = merged_dfs[
    'Taxa Selic - a.a.'
].astype(str)

# limpar espaço
col = col.str.strip()

# remover símbolo %
col = col.str.replace('%', '', regex=False)

# trocar vírgula por ponto
col = col.str.replace(',', '.', regex=False)

# remover strings vazias
col = col.replace('', None)

# converter
merged_dfs[
    'Taxa Selic - a.a.'
] = pd.to_numeric(col, errors='coerce')

#display resultado
merged_dfs.info()
display(merged_dfs)
