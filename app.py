import streamlit as st
import pandas as pd

def main():
    st.title("Gerenciador de Produtos")
    
    # Carregar a planilha
    uploaded_file = st.file_uploader("Escolha uma planilha", type=["csv", "xlsx"])
    if uploaded_file is not None:
        # Solicitar a linha do cabeçalho
        header_row = st.number_input("Qual é a linha do cabeçalho? (0 para primeira linha)", 
                                   min_value=0, 
                                   value=0, 
                                   help="Digite o número da linha que contém os nomes das colunas")
        
        # Carregar o arquivo com o cabeçalho especificado
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file, header=header_row)
        else:
            df = pd.read_excel(uploaded_file, header=header_row)
        
        # Exibir os produtos e as colunas disponíveis
        st.write("Colunas disponíveis:", df.columns.tolist())
        st.write("Produtos disponíveis:")
        st.dataframe(df)

        # Adicionar coluna 'Incluir' se não existir
        if 'Incluir' not in df.columns:
            df['Incluir'] = False

        # Verificar qual coluna contém o nome do produto
        nome_coluna_produto = df.columns[0]  # Usando a primeira coluna como exemplo
        
        # Adicionar lógica para seleção de produtos
        for index, row in df.iterrows():
            # Adicionando o índice ao ID do checkbox para torná-lo único
            checkbox_key = f"checkbox_{index}_{row[nome_coluna_produto]}"
            df.at[index, 'Incluir'] = st.checkbox(
                f"Incluir {row[nome_coluna_produto]}", 
                value=False,
                key=checkbox_key
            )

        # Botão para salvar as seleções
        if st.button("Salvar Seleções"):
            st.write("Seleções salvas!")

if __name__ == "__main__":
    main() 