import pandas as pd
import streamlit as st
from sidebar import render_sidebar

from plot.chart import *

st.set_page_config(layout="wide", page_title='DATASUS')
st.markdown("## DATASUS EXPLORER 💎")
st.write("DADOS DETALHADOS DAS AIH - BRASIL")


@st.cache_data
def load_data():
    df = pd.read_csv('../dataset/table_AIH_2009_2024_CLEAN.csv', sep=';')
    return df


def show_data():
    df = load_data()
    st.header(f'1000 linhas de {df.shape[0]} registros')
    st.dataframe(df[:1000].style.format(decimal='.', precision=1),
                 use_container_width=True,
                 hide_index=False,
                 width=600,
                 height=800)
    return df


def start():
    opcao_selecionada = render_sidebar()
    if opcao_selecionada == 'Exploração de dados':
        df = show_data()
        st.header('Contagem de nulos e não nulos')
        plot_nulos_e_nao_nulos(df)
        #st.header('Histograma')
        #opcao = st.selectbox(f"Selecione a variável", ['uf_nome', 'regiao_nome'], key='coluna1')
        #plot_histograma(df, opcao)
        #st.header('Gráfico de barras: quantidade de nascimentos por faixa populacional')
        categoria = st.selectbox(f"Selecione a categoria", ['populacao_faixa', 'regiao_nome', 'uf_nome'], key='coluna2')
        medida = st.selectbox(f"Selecione a medida", ['partos_e_nascimentos_qtd', 'diagnostico_ultrasonografia_qtd', 'cirurgias_obstetricas_qtd'], key='coluna3')
        plot_bar_horizontal(df, categoria, medida)
        st.header("Heatmaps")
        plot_heatmaps(df)


if __name__ == '__main__':
    start()
