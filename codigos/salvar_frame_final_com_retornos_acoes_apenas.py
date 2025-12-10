#12 Salvar dataframe final com os retornos logaritmos

output_file_name = 'final_merged_dfs_with_log_returns.csv'
final_merged_df_with_returns.to_csv(output_file_name, index=False)

print(f"\nDataset final salvo localmente como: {output_file_name}")

files.download(output_file_name)