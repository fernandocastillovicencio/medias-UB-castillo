import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------------- #
#                           CALCULAR E MOSTRAR NOTAS                           #
# ---------------------------------------------------------------------------- #


# @st.cache_data
# ---------------------------------------------------------------------------- #


def carregar_dados(disciplina):
    """
    Função para carregar os dados de acordo com a disciplina selecionada
    """
    if disciplina == "Refrigeração e Ar-Condicionado":
        #     # return pd.read_csv(
        #     #     #     "https://raw.githubusercontent.com/fernandocastillovicencio/medias-UB-castillo/main/ref2.csv"
        #     # )
        return pd.read_csv("db-RAC-2e.csv")
    elif disciplina == "Máquinas de Fluxo":
        return pd.read_csv("db-MaF-2e.csv")
    elif disciplina == "Fenômenos de Transporte":
        return pd.read_csv("db-FdT-2b.csv")
    elif disciplina == "Hidráulica e Pneumática":
        return pd.read_csv("db-HiP-2b.csv")


# ---------------------------------------------------------------------------- #


def calcular_media(colunas):
    """
    Função para calcular a média, ignorando NaN e valores ausentes
    """
    media = (
        colunas.apply(pd.to_numeric, errors="coerce").mean(axis=1, skipna=True).mean()
    )
    return round(media, 2) if pd.notna(media) else 0.0


def calcular_e_mostrar_notas(aluno, modulo, prefixo):
    """
    Função para calcular e mostrar as notas do aluno
    """
    categoria = f"{modulo}-{prefixo}"
    colunas = aluno.filter(regex=categoria)

    # ---------------------------- formatar tabela --------------------------- #
    colunas = colunas.applymap(
        lambda x: f"{x:.2f}".rstrip("0").rstrip(".") if pd.notna(x) else x
    )

    # --------------------------------- peso --------------------------------- #
    peso_dict = {"S": 3.5, "Q": 3.5, "L": 1.0, "A": 2.0}
    peso = peso_dict.get(prefixo, 0.0)

    # ----------------------------- média e nota ----------------------------- #
    nota = 0
    if colunas.notna().any().any():
        # média
        media = calcular_media(colunas)
        # nota
        if pd.notna(media):
            nota = media * peso
            # mostrar tabela
            st.table(colunas)
            # mostrar média
            st.markdown(
                f"\tMédia: **{media:.2f}** (máx. 1.0) -- Pontos: **{nota:.2f}** (máx. {peso})"
            )

    return nota


# ---------------------------------------------------------------------------- #
#                                MOSTRAR MÓDULO                                #
# ---------------------------------------------------------------------------- #
def mostrar_modulo(index, aluno):
    """
    Função para exibir as notas do módulo, passando as respectivas informações
    """
    st.markdown(f"### MÓDULO {str(index)}:")
    # -------------------------- atividades em sala -------------------------- #
    st.markdown(f"##### 1. Atividades em sala (35%):")
    nota_sala = calcular_e_mostrar_notas(aluno, index, "S")
    # ------------------------- listas de exercícios ------------------------- #
    st.markdown(f"##### 2. Lista de Exercícios (10%):")
    nota_listas = calcular_e_mostrar_notas(aluno, index, "L")
    # -------------------------------- artigo -------------------------------- #
    st.markdown(f"##### 3. Artigo da Disciplina (20%):")
    nota_artigo = calcular_e_mostrar_notas(aluno, index, "A")
    # ----------------------------- prova escrita ---------------------------- #
    st.markdown(f"##### 4. Prova Escrita (35%):")
    nota_prova = calcular_e_mostrar_notas(aluno, index, "Q")
    # ------------------------------ média total ----------------------------- #
    media_modulo = nota_sala + nota_listas + nota_artigo + nota_prova
    # media_modulo = round(media_modulo, 2)
    if media_modulo > 0.0:
        st.markdown(f"##### Média do Módulo (Total de Pontos): {media_modulo:.2f}")
    st.markdown("---")
