cambio_file = '/content/STP-20251001162317444_tx_cambio.csv'

metadados_cambio = {}
data_list = []
original_cambio_col_name = None

try:
    with open(cambio_file, 'r', encoding='latin1') as file:
        reader = csv.reader(file, delimiter=',')

        linha1 = next(reader)

        if len(linha1) > 1:
            original_cambio_col_name = linha1[1].strip()
        else:
            original_cambio_col_name = 'CAMBIO_DEFAULT'

        metadados_cambio = {
            'nome_original': original_cambio_col_name,
            'unidade': 'N/A'
        }

        for row in reader:
            if not row:
                continue

            if row[0].strip().lower().startswith('fonte'):
                break

            if len(row) >= 2:
                data_list.append([row[0].strip(), row[1].strip()])


    df_cambio = pd.DataFrame(data_list, columns=['Data', original_cambio_col_name])

except Exception as e:
    print(f"Erro ao carregar e processar o dataset {cambio_file}: {e}")
    df_cambio = pd.DataFrame(columns=['Data', 'CAMBIO_ERROR']) # Define a default empty df
    original_cambio_col_name = 'CAMBIO_ERROR' # Update col name for error state

if not df_cambio.empty:
    df_cambio['Data'] = pd.to_datetime(df_cambio['Data'], format='%d/%m/%Y', errors='coerce')
    df_cambio.dropna(subset=['Data'], inplace=True)

    if original_cambio_col_name in df_cambio.columns:
        df_cambio[original_cambio_col_name] = df_cambio[original_cambio_col_name].str.replace(',', '.', regex=False)
        df_cambio[original_cambio_col_name] = pd.to_numeric(df_cambio[original_cambio_col_name], errors='coerce')
        df_cambio.dropna(subset=[original_cambio_col_name], inplace=True)
    else:
        print(f"A coluna '{original_cambio_col_name}' não foi encontrada no DataFrame. Verifique o cabeçalho do arquivo.")
        df_cambio = pd.DataFrame(columns=['Data', original_cambio_col_name]) # Empty df if col not found
else:
    print("DataFrame df_cambio está vazio após o carregamento inicial.")

print("\n--- Metadados Documentados ---")
print(f"Nome da Série Original: {metadados_cambio.get('nome_original', original_cambio_col_name)}")
print(f"Unidade de Medida: {metadados_cambio.get('unidade', 'N/A')}")
print("------------------------------")

print(f"\nPrimeiras 5 linhas do dataframe {cambio_file} CORRIGIDO:")
display(df_cambio.head())

print(f"\nInformações do dataframe {cambio_file} CORRIGIDO:")
df_cambio.info()
     