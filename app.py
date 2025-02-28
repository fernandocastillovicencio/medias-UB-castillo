# ---------------------------------------------------------------------------- #
#                                  BIBLIOTECAS                                 #
# ---------------------------------------------------------------------------- #
import streamlit as st
import pandas as pd
from functions import mostrar_modulo

# ---------------------------------------------------------------------------- #
#                           CARREGAR E CONFIGURAR CSV                          #
# ---------------------------------------------------------------------------- #
# Carregar o CSV diretamente do GitHub
url = "https://raw.githubusercontent.com/fernandocastillovicencio/medias-UB-castillo/main/modelo_notas.csv"
df = pd.read_csv(url)

# Converter a coluna RA para string
df['RA'] = df['RA'].astype(str)

# ---------------------------------------------------------------------------- #
#                             STREAM LIST INTERFACE                            #
# ---------------------------------------------------------------------------- #
# Título do aplicativo
st.title("Consulta de Notas")

# ---------------------------------------------------------------------------- #
#                                  CRIAR LISTA                                 #
# ---------------------------------------------------------------------------- #
# Ordenar a lista de RAs em ordem crescente
ra = ['---'] + sorted(df['RA'].astype(int).tolist())  # Converte para inteiro, ordena e depois volta para string


# Exibir a lista suspensa e definir "---" como a opção padrão
ra_selecionado = st.selectbox("Escolha seu RA:", ra, index=0)

# ---------------------------------------------------------------------------- #
#                                 MOSTRAR NOTAS                                #
# ---------------------------------------------------------------------------- #
# Exibir as notas apenas se um RA válido for selecionado
if str(ra_selecionado) != '---':  # Garante que o valor seja comparado como string
    aluno = df[df['RA'] == str(ra_selecionado)]  # Filtra os dados do aluno com base no RA selecionado

# ---------------------------------------------------------------------------- #
    if not aluno.empty:
        
        st.markdown("---")

        # ----------------{--------------- NOME ------------------------------- #
        nome = aluno['NC'].values[0]
        matricula = aluno['RA'].values[0]

        st.write(f"## ALUNO: {nome} -- RA: {matricula}")
        
        st.markdown("---")
        
        # -------------------------------------------------------------------- #
        #                               MÓDULO 1                               #
        # -------------------------------------------------------------------- #
        mostrar_modulo("1",aluno)
        # -------------------------------------------------------------------- #
        #                               MÓDULO 2                               #
        # -------------------------------------------------------------------- #
        mostrar_modulo("2",aluno)
        # -------------------------------------------------------------------- #
        #                               MÓDULO 3                               #
        # -------------------------------------------------------------------- #
        mostrar_modulo("3",aluno)
        # -------------------------------------------------------------------- #
        #                               MÓDULO 4                               #
        # -------------------------------------------------------------------- #
        mostrar_modulo("4",aluno)