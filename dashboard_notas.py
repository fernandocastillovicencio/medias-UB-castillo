import streamlit as st
import pandas as pd

# Carregar o CSV diretamente do GitHub
url = "https://raw.githubusercontent.com/fernandocastillovicencio/medias-UB-castillo/main/modelo_notas.csv"
df = pd.read_csv(url)

# Interface do Streamlit
st.title("Consulta de Notas")

# Criação da lista suspensa de RAs
rAs = df['RA'].astype(str).tolist()  # Converte os RAs para string para exibir na lista
ra_selecionado = st.selectbox("Escolha seu RA:", rAs)

if ra_selecionado:
    # Filtra os dados do aluno com base no RA selecionado
    aluno = df[df['RA'] == int(ra_selecionado)]

    if not aluno.empty:
        st.write("Notas do aluno:")
        st.write(aluno)
    else:
        st.write("RA não encontrado.")
