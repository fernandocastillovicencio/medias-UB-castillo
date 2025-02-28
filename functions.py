
import streamlit as st
import pandas as pd

# ---------------------------------------------------------------------------- #
#                           CALCULAR E MOSTRAR NOTAS                           #
# ---------------------------------------------------------------------------- #
def calcular_e_mostrar_notas(aluno, modulo, prefixo):
    # ------------------------------ selecionar ------------------------------ #
    categoria = f"{modulo}-{prefixo}"
    colunas = aluno.filter(regex=categoria)
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
        # nota
        if pd.notna(media):
            nota = media*peso
            # mostrar tabela
            st.write(colunas.round(2))
            # mostrar média 
            st.write(f"\tMédia: {media.round(2)}, Contribuição: {nota.round(2)}")
        # -------------------------------------------------------------------- #
    return nota

# ---------------------------------------------------------------------------- #
#                                MOSTRAR MÓDULO                                #
# ---------------------------------------------------------------------------- #
def mostrar_modulo(index,aluno):
    # ------------------------------------------------------------------------ #
    #                                  MÓDULO                                  #
    # ------------------------------------------------------------------------ #
    st.markdown(f"### MÓDULO {index}:")
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
    if media_modulo > 0.0:
        st.markdown(f"##### Nota do Módulo: {media_modulo.round(2)}")
    st.markdown("---")
    # ------------------------------------------------------------------------ #