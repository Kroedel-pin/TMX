import streamlit as st
import pandas as pd

def main():
    st.title("Gerenciador de Produtos")
    
    # Carregar a planilha
    uploaded_file = st.file_uploader("Escolha uma planilha", type=["csv", "xlsx"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        # Exibir os produtos
        st.write("Produtos disponíveis:")
        st.dataframe(df)

        # Adicionar lógica para seleção de produtos
        for index, row in df.iterrows():
            df.at[index, 'Incluir'] = st.checkbox(f"Incluir {row['Nome do Produto']}", value=False)

        # Botão para salvar as seleções
        if st.button("Salvar Seleções"):
            st.write("Seleções salvas!")

if __name__ == "__main__":
    main()
