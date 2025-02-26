import streamlit as st
import pandas as pd

# 🔗 URL do CSV no GitHub
SHEET_URL = "https://raw.githubusercontent.com/fernandocastillovicencio/medias-UB-castillo/main/modelo_notas.csv"

# 📥 Função para carregar os dados
@st.cache_data
def carregar_dados():
    df = pd.read_csv(SHEET_URL)
    return df

df = carregar_dados()

# 🏆 Interface do Dashboard
st.title("📊 Dashboard de Notas")
st.write("Selecione seu RA para visualizar suas notas.")

# 🎯 Barra lateral para escolher o RA do aluno
st.sidebar.title("Consulta de Notas")
ra = st.sidebar.selectbox("Selecione seu RA", df["RA"].unique())

# 🔍 Filtrar os dados do aluno selecionado
aluno = df[df["RA"] == ra]

# 📢 Verificar se o aluno existe na base de dados
if aluno.empty:
    st.error("❌ Nenhuma nota encontrada para este RA.")
else:
    aluno = aluno.iloc[0]  # Pega a primeira linha correspondente ao RA

    # 🏆 Exibir informações do aluno
    st.title(f"📌 Notas de {aluno['Nome']}")
    st.write(f"**📚 Módulo:** {aluno['Módulo']}")

    # 📝 Obter a Nota Final e garantir que seja um número válido
    media = aluno["Nota Final (10,0)"]
    
    if pd.isna(media):  # Se media for NaN
        st.error("❌ Erro: Nota final não encontrada para este aluno.")
    else:
        st.write(f"📝 **Nota Final Calculada:** {media}")

        # 📊 Barra de progresso (garantindo que esteja entre 0 e 1)
        st.progress(min(max(media / 10, 0), 1))

        # ✅ Definir a situação do aluno
        if media >= 6:
            status = "✅ Aprovado"
            cor = "green"
        else:
            status = "⚠️ Precisa melhorar"
            cor = "red"

        st.markdown(f"### 🎯 **Situação:** <span style='color:{cor}'>{status}</span>", unsafe_allow_html=True)

        # 📊 Exibição detalhada das notas
        st.write("### 📊 **Detalhamento das Notas**")
        st.write(f"- 🏫 **Média Atividades em Sala:** {aluno['Média Atividades (3,5)']} (3,5 pontos)")
        st.write(f"- 📄 **Média Listas de Exercícios:** {aluno['Média Listas (1,0)']} (1,0 ponto)")
        st.write(f"- 📝 **Média Artigo:** {aluno['Média Artigo (2,0)']} (2,0 pontos)")
        st.write(f"- ✍️ **Nota Prova:** {aluno['Nota Prova (3,5)']} (3,5 pontos)")
        st.write(f"🎯 **Nota Final:** {media}/10")

        # 📢 Feedback ao aluno
        if media < 6:
            st.warning("⚠️ Revise os conteúdos e tente melhorar nas próximas avaliações.")
