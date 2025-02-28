
import streamlit as st
import pandas as pd


# ---------------------------------------------------------------------------- #
#                           CALCULAR E MOSTRAR NOTAS                           #
# ---------------------------------------------------------------------------- #
def calcular_e_mostrar_notas(aluno, modulo, prefixo):
    # ------------------------------ selecionar ------------------------------ #
    categoria = f"{modulo}-{prefixo}"
    colunas = aluno.filter(regex=categoria)
    
    # ---------------------------- formatar tabela --------------------------- #
    colunas = colunas.applymap(lambda x: f"{x:.2f}" if pd.notna(x) else x)


    
    # --------------------------------- peso --------------------------------- #
    peso_dict = {
        'S': 3.5,
        'Q': 3.5,
        'L': 1.0,
        'A': 2.0
    }
    peso = peso_dict.get(prefixo, 0.0)
    # ----------------------------- média e nota ----------------------------- #
    nota = 0
    if colunas.notna().any().any():
        # média
        media = colunas.apply(pd.to_numeric,errors='coerce').mean(axis=1,skipna=True).mean()
        media = round(media,2)
        # nota
        if pd.notna(media):
            nota = media*peso
            nota = round(nota,2)
            # mostrar tabela
                # Exibe a tabela com a formatação de CSS para alterar o tamanho da fonte e ocultar o índice
            st.markdown(
            """
            <style>
            .streamlit-expanderHeader {
                font-size: 12px;  /* Tamanho da fonte reduzido para título */
            }
            .stDataFrame {
                font-size: 12px; /* Tamanho menor da fonte para o conteúdo da tabela */
            }
            .stDataFrame tbody td, .stDataFrame th {
                text-align: center;
                padding: 5px;
            }
            .stDataFrame thead {
                display: none; /* Ocultar cabeçalho */
            }
            </style>
            """, unsafe_allow_html=True)
            st.table(colunas)
            # mostrar média 
            st.markdown(f"\tMédia: **{media}** (máximo 1.0) -- Pontos: **{nota}** (máximo: {peso})")
        # -------------------------------------------------------------------- #
    return nota

# ---------------------------------------------------------------------------- #
#                                MOSTRAR MÓDULO                                #
# ---------------------------------------------------------------------------- #
def mostrar_modulo(index,aluno):
    # ------------------------------------------------------------------------ #
    #                                  MÓDULO                                  #
    # ------------------------------------------------------------------------ #
    st.markdown(f"### MÓDULO {str(index)}:")
    # -------------------------- atividades em sala -------------------------- #
    st.markdown(f"##### 1. Atividades em sala (35%):")
    nota_sala = calcular_e_mostrar_notas(aluno, index, 'S')
    # ------------------------- listas de exercícios ------------------------- #
    st.markdown(f"##### 2. Lista de Exercícios (10%):")
    nota_listas = calcular_e_mostrar_notas(aluno, index, 'L')
    # -------------------------------- artigo -------------------------------- #
    st.markdown(f"##### 3. Artigo da Disciplina (20%):")
    nota_artigo = calcular_e_mostrar_notas(aluno, index, 'A')
    # ----------------------------- prova escrita ---------------------------- #
    st.markdown(f"##### 4. Prova Escrita (35%):")
    nota_prova = calcular_e_mostrar_notas(aluno, index, 'Q')
    # ------------------------------ média total ----------------------------- #
    media_modulo = nota_sala + nota_listas + nota_artigo + nota_prova
    media_modulo = round(media_modulo,2)
    if media_modulo > 0.0:
        st.markdown(f"##### Média do Módulo: {media_modulo}")
    st.markdown("---")
    # ------------------------------------------------------------------------ #