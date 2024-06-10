import streamlit as st

opcoes_ferramentas = [
    "Exploração de dados",
    "Série temporal",
]


def render_sidebar():
    st.sidebar.title("Ferramentas")
    opcao_selecionada = st.sidebar.selectbox("Selecione uma opção:", opcoes_ferramentas)
    return opcao_selecionada
