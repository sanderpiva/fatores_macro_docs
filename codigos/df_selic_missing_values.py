#1 Carregando Dataframe SELIC e verificando existencia de valores nulos ou missing

selic_file = '/content/STP-20251001161617503_selic.csv'

try:
    df_selic = pd.read_csv(selic_file, on_bad_lines='skip', sep=',')
    print(f"Dataset {selic_file} carregado com sucesso com utf-8 e separador ','.")
except UnicodeDecodeError:
    df_selic = pd.read_csv(selic_file, encoding='latin1', on_bad_lines='skip', sep=',')
    print(f"Dataset {selic_file} carregado com sucesso com latin1 e separador ','.")
except Exception as e:
    print(f"Erro ao carregar o dataset {selic_file}: {e}")

original_selic_col_name = df_selic.columns[1]
df_selic = df_selic.rename(columns={original_selic_col_name: 'Taxa Selic - a.a.'})

df_selic['Data'] = pd.to_datetime(df_selic['Data'], format='%d/%m/%Y', errors='coerce')

df_selic.dropna(subset=['Data'], inplace=True)

print(f"\nPrimeiras 5 linhas do dataset {selic_file} CORRIGIDO:")
display(df_selic.head())
print(f"\nInformações do dataset {selic_file} CORRIGIDO:")
df_selic.info()

     