# ---------------------------------------------------------------------------- #
#                                  BIBLIOTECAS                                 #
# ---------------------------------------------------------------------------- #
import pandas as pd
import streamlit as st

from functions import carregar_dados, mostrar_modulo

# Título do aplicativo
st.image("logoub.png", width=300)
st.markdown("#### Escola Politécnica")
st.markdown("##### Prof. Fernando Castillo Vicencio")
st.markdown("##### Médias 2025/1")

# ---------------------------------------------------------------------------- #
#                                CARREGAR TURMA                                #
# ---------------------------------------------------------------------------- #
# Defina as opções de disciplinas com a chave sendo o código e o valor o nome da disciplina
disciplinas = {
    "RAA": "Refrigeração e Ar-Condicionado",
    "MaF": "Máquinas de Fluxo",
    "FdT": "Fenômenos de Transporte",
    "HiP": "Hidráulica e Pneumática",
}

# Exibe o selectbox para o usuário escolher a disciplina
disciplina_selecionada = st.selectbox(
    "Escolha a Disciplina:", ["---"] + sorted(disciplinas.values())
)

# Inicializa o dataframe
df = None

# Reseta o RA toda vez que a disciplina mudar
if (
    "ra_selecionado" in st.session_state
    and disciplina_selecionada != st.session_state.disciplina_selecionada_anterior
):
    st.session_state.ra_selecionado = "---"  # Reseta o RA

# Salva a disciplina selecionada
st.session_state.disciplina_selecionada_anterior = disciplina_selecionada

# Exibe o nome da disciplina antes do título "Consulta de Notas"
if disciplina_selecionada != "---":
    st.write(f"## {disciplina_selecionada}")

# Carrega o arquivo CSV de acordo com a disciplina selecionada usando a função de cache
if disciplina_selecionada != "---":
    df = carregar_dados(disciplina_selecionada)

# ---------------------------------------------------------------------------- #
#                                    MOSTRAR                                   #
# ---------------------------------------------------------------------------- #

# Verifique se o dataframe foi carregado corretamente
if df is not None:
    # Ordenar a lista de RAs em ordem crescente
    df["RA"] = df["RA"].astype(str)
    ra = ["---"] + sorted(
        df["RA"].astype(int).tolist()
    )  # Converte para inteiro, ordena e depois volta para string

    # Exibir a lista suspensa e definir "---" como a opção padrão
    ra_selecionado = st.selectbox("Escolha seu RA:", ra, index=0)

    # Salvar a seleção de RA no session_state (sem precisar verificar se já existe ou não)
    st.session_state.ra_selecionado = ra_selecionado

    # Exibir as notas apenas se um RA válido for selecionado
    if str(ra_selecionado) != "---":  # Garante que o valor seja comparado como string
        aluno = df[
            df["RA"] == str(ra_selecionado)
        ]  # Filtra os dados do aluno com base no RA selecionado

        if not aluno.empty:
            # ----------------{--------------- NOME ------------------------------- #
            nome = aluno["NC"].values[0]
            matricula = aluno["RA"].values[0]

            st.write(f"#### Aluno(a): {nome}")
            st.write(f"#### RA: {matricula}")

            st.markdown("---")

            # Exibindo os módulos de forma dinâmica (loop para módulos 1 a 4)
            for i in range(1, 5):
                mostrar_modulo(i, aluno)
