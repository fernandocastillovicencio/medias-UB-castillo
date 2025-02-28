# ---------------------------------------------------------------------------- #
#                                  BIBLIOTECAS                                 #
# ---------------------------------------------------------------------------- #
import streamlit as st
import pandas as pd

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
        st.markdown(f"### MÓDULO 1:")

        # ------------------------ ATIVIDADES EM SALA ------------------------ #
        st.markdown(f"##### 1. Atividades em sala (35%):")
        # ------------------------------ tabela ------------------------------ #
        # Seleciona as colunas que começam com "M1-S"
        colunas = aluno.filter(regex='^M1-S')
        # --------------------------- média e nota --------------------------- #
        if colunas.notna().any().any():
            # média e nota
            media = colunas.apply(pd.to_numeric, errors='coerce').mean(axis=1, skipna=True).mean()
            nota_sala = media * 1.0
            st.write(colunas.round(2))
            if pd.notna(media):
                st.write(f"\tMédia: {media.round(2)}, Contribuição: {nota_sala.round(2)}")

        # ----------------------- LISTAS DE EXERCÍCIOS ----------------------- #
        st.markdown(f"##### 2. Lista de Exercícios (10%):")
        # ------------------------------ tabela ------------------------------ #
        # Seleciona as colunas que começam com "M1-S"
        colunas = aluno.filter(regex='^M1-L')
        # --------------------------- média e nota --------------------------- #
        if colunas.notna().any().any():
            # média e nota
            media = colunas.apply(pd.to_numeric, errors='coerce').mean(axis=1, skipna=True).mean()
            nota_listas = media * 1.0
            st.write(colunas.round(2))
            if pd.notna(media):
                st.write(f"\tMédia: {media.round(2)}, Contribuição: {nota_listas.round(2)}")

        # ------------------------------ artigo ------------------------------ #

        st.markdown(f"##### 3. Artigo da Disciplina (20%):")
        # ------------------------------ tabela ------------------------------ #
        # Seleciona as colunas que começam com "M1-A"
        colunas = aluno.filter(regex='^M1-A')    
        # --------------------------- média e nota --------------------------- #
        if colunas.notna().any().any():
            # média e nota
            media = colunas.apply(pd.to_numeric, errors='coerce').mean(axis=1, skipna=True).mean()
            nota_artigo = media * 1.0
            st.write(colunas.round(2))
            if pd.notna(media):
                st.write(f"\tMédia: {media.round(2)}, Contribuição: {nota_artigo.round(2)}")


        # --------------------------- prova escrita -------------------------- #
        st.markdown(f"##### 4. Prova Escrita (35%):")
        # ------------------------------ tabela ------------------------------ #
        # Seleciona as colunas que começam com "M1-A"
        colunas = aluno.filter(regex='^M1-Q')
        # -------------------------- média e nota --------------------------- #
        if colunas.notna().any().any():
            # média e nota
            media = colunas.apply(pd.to_numeric, errors='coerce').mean(axis=1, skipna=True).mean()
            nota_prova = media * 1.0
            st.write(colunas.round(2))
            if pd.notna(media):
                st.write(f"\tMédia: {media.round(2)}, Contribuição: {nota_prova.round(2)}")
        # -------------------------------------------------------------------- #
        st.markdown("---") 
