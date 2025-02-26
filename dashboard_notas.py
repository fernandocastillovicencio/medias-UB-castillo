import streamlit as st
import pandas as pd

# 🔗 Link do arquivo CSV no OneDrive/SharePoint (modifique com seu link real)
SHEET_URL = "https://unibrasilcombr-my.sharepoint.com/personal/978937_unibrasil_com_br/_layouts/15/download.aspx?SourceUrl=https://unibrasilcombr-my.sharepoint.com/:x:/g/personal/978937_unibrasil_com_br/EcBFFNYi-klPnnGcHqMRG9cBACEnVfHD_cr6vVx2XUsxTQ?e=huPRSL&format=csv"

@st.cache_data
def carregar_dados():
    df = pd.read_csv(SHEET_URL, delimiter=",")  # Ajuste o delimitador se necessário
    return df

df = carregar_dados()

# 🎯 Sidebar para selecionar o RA
st.sidebar.title("Consulta de Notas")
ra = st.sidebar.selectbox("Selecione seu RA", df["RA"])

# 🔍 Filtrar os dados do aluno
aluno = df[df["RA"] == ra].iloc[0]

# 🏆 Exibir Informações do Aluno
st.title(f"📌 Notas de {aluno['Nome']}")
st.write(f"**📚 Módulo:** {aluno['Módulo']}")

# 📊 Barra de progresso da Nota Final
media = aluno["Nota Final (10,0)"]
st.progress(media / 10)

# 🏁 Definir situação do aluno
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
