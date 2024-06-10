import streamlit as st
from sidebar import render_sidebar


st.set_page_config(layout="wide", page_title='DATASUS')
st.markdown("### DATASUS EXPLORER 💎")
st.write("DADOS DETALHADOS DAS AIH - BRASIL")


def start():
    opcao_selecionada = render_sidebar()
    print(opcao_selecionada)


if __name__ == '__main__':
    start()
