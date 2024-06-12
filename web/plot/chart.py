import plotly.express as px
import pandas as pd
import streamlit as st


def plot_nulos_e_nao_nulos(df):
    # Determine the null values:
    df_null_vals = df.isnull().sum().to_frame()
    df_null_vals = df_null_vals.rename(columns={0: 'Nulo'})
    # Determine the not null values:
    df_not_null_vals = df.notna().sum().to_frame()
    df_not_null_vals = df_not_null_vals.rename(columns={0: 'Não Nulo'})
    # Combine the dataframes:
    df_null_count = pd.concat([df_null_vals, df_not_null_vals], ignore_index=False, axis=1).reset_index()

    df_null_count = df_null_count.rename(columns={'index': 'Variavel'})

    # df_g = df_null_count.groupby(['Nulo', 'Não Nulo']).size().reset_index()
    # df_g = df_g.rename(columns={0: 'total'})

    # Generate Plot
    fig = px.bar(df_null_count, x="Variavel", y=['Não Nulo', 'Nulo'],
                 color_discrete_map={'Não Nulo': 'blue', 'Nulo': 'red'})
    fig.update_xaxes(categoryorder='total descending')
    fig.update_layout(
        title={'text': "Contagem de nulos e não nulos",
               'xanchor': 'center',
               'yanchor': 'top',
               'x': 0.5},
        xaxis_title="Variável",
        yaxis_title="Total")
    fig.update_layout(legend_title_text='Categoria')
    st.plotly_chart(fig, use_container_width=True)


def plot_histograma(df, coluna):
    fig = px.histogram(df, x=coluna, nbins=100)
    fig.update_layout(xaxis_title=coluna, yaxis_title="Total").update_xaxes(categoryorder='total descending')
    st.plotly_chart(fig, use_container_width=True)


def plot_bar_horizontal(df, categoria, medida):
    df_agrupado = df.groupby([categoria]).agg({medida: 'sum'}).reset_index()
    fig = px.bar(df_agrupado, x=medida, y=categoria, orientation='h', width=800, height=800)
    fig.update_layout(xaxis_title=f'Total de {medida}', yaxis_title=f'{categoria}').update_yaxes(
        categoryorder='total ascending')
    st.plotly_chart(fig, use_container_width=True)


def plot_heatmaps(df):
    df = df.filter(regex='_qtd$|_val$|numero_habitantes')
    df = df.corr(method='pearson').round(2)
    fig = px.imshow(df, text_auto=True, width=800, height=800, aspect='auto', color_continuous_scale='blues')
    st.plotly_chart(fig, use_container_width=True)


