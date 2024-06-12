import pandas as pd
import numpy as np
import streamlit as st


class Clean:
    def __init__(self, input_filename: str,
                 colunas_escolhidas: list,
                 dicionario: dict,
                 output_filename: str):
        self.input_filename = input_filename
        self.colunas_escolhidas = colunas_escolhidas
        self.dicionario = dicionario
        self.df = self.load_data()
        self.output_filename = output_filename

    def load_data(self):
        st.write('Carregando dados...')
        df = pd.read_csv(self.input_filename, sep=';', usecols=self.colunas_escolhidas)
        return df

    def rename_columns(self):
        st.write('Renomeando colunas...')
        self.df.rename(columns=self.dicionario, inplace=True)
        return self.df

    def get_nome_mes(self):
        st.write('Transformando código dos meses em nomes...')
        mes = {1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr', 5: 'Mai', 6: 'Jun',
               7: 'Jul', 8: 'Ago', 9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'}
        self.df['mes'] = self.df['mes'].apply(lambda x: mes.get(x))
        return self.df

    def retira_espacos_em_branco(self):
        st.write('Retirando espaços em branco...')
        self.df = self.df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

    def substituir_ponto_por_nulo(self):
        st.write('Substituindo ponto por nulo...')
        self.df['partos_e_nascimentos_qtd'] = self.df['partos_e_nascimentos_qtd'].replace('.', np.nan)
        self.df['diagnostico_ultrasonografia_qtd'] = self.df['diagnostico_ultrasonografia_qtd'].replace('.', np.nan)
        self.df['cirurgias_obstetricas_qtd'] = self.df['cirurgias_obstetricas_qtd'].replace('.', np.nan)
        self.df['cirurgias_obstetricas_val'] = self.df['cirurgias_obstetricas_val'].replace('.', np.nan)
        self.df['partos_e_nascimentos_val'] = self.df['partos_e_nascimentos_val'].replace('.', np.nan)
        self.df['diagnostico_ultrasonografia_val'] = self.df['diagnostico_ultrasonografia_val'].replace('.', np.nan)

    def substituir_virgula_por_ponto(self):
        st.write('Substituindo vírgula por ponto...')
        self.df['partos_e_nascimentos_val'] = self.df['partos_e_nascimentos_val'].str.replace(',', '.')
        self.df['diagnostico_ultrasonografia_val'] = self.df['diagnostico_ultrasonografia_val'].str.replace(',', '.')
        self.df['cirurgias_obstetricas_val'] = self.df['cirurgias_obstetricas_val'].str.replace(',', '.')
        self.df['longitude'] = self.df['longitude'].str.replace(',', '.')
        self.df['latitude'] = self.df['latitude'].str.replace(',', '.')

    def formatar_capital(self):
        st.write('Formatando valores para capital...')
        self.df['capital'] = self.df['capital'].apply(lambda x: x if x == 'Sim' else 'Não')

    def set_categoria_colunas(self):
        st.write('Definindo categorias nas colunas...')
        self.df['mes'] = self.df['mes'].astype('category')
        self.df['municipio'] = self.df['municipio'].astype('category')
        self.df['regiao_codigo'] = self.df['regiao_codigo'].astype('category')
        self.df['regiao_nome'] = self.df['regiao_nome'].astype('category')
        self.df['capital'] = self.df['capital'].astype('category')
        self.df['uf'] = self.df['uf'].astype('category')
        self.df['uf_nome'] = self.df['uf_nome'].astype('category')
        self.df['uf_codigo'] = self.df['uf_codigo'].astype('category')
        self.df['populacao_faixa'] = self.df['populacao_faixa'].astype('category')
        self.df['latitude'] = self.df['latitude'].astype('float64')
        self.df['longitude'] = self.df['longitude'].astype('float64')
        for col in self.df.filter(regex='_qtd'):
            self.df[col] = self.df[col].astype('Int64')
        for col in self.df.filter(regex='_val'):
            self.df[col] = self.df[col].astype('float64')

    def save_data(self):
        st.write('Salvando dados...')
        self.df.to_csv(self.output_filename, sep=';', index=False)

    def start(self):
        self.load_data()
        self.rename_columns()
        #self.get_nome_mes()
        self.retira_espacos_em_branco()
        self.substituir_ponto_por_nulo()
        self.substituir_virgula_por_ponto()
        self.formatar_capital()
        self.set_categoria_colunas()
        self.save_data()


if __name__ == '__main__':
    input_filename = r'../../dataset/table_AIH_2009_2024_SUBGRUPO_PROC.csv'
    output_filename = r'../../dataset/table_AIH_2009_2024_CLEAN.csv'
    colunas = ['ano',
               'mes',
               'Faixa_Populacao',
               # 'Faixa_Populacao_FPM',
               'LATITUDE',
               'LONGITUDE',
               'Municipio_Capital',
               'Nome_Municipio',
               'Numero_Habitantes_Censo_2022',
               'qtd_0310',
               'VL_0310',
               'qtd_0411',
               'VL_0411',
               'qtd_0205',
               'VL_0205',
               'Regiao_Codigo',
               'Regiao_Nome',
               'UF',
               'UF_Codigo',
               'UF_Nome']
    dicionario = {'Nome_Municipio': 'municipio',
                  'Regiao_Codigo': 'regiao_codigo',
                  'Regiao_Nome': 'regiao_nome',
                  'UF_Codigo': 'uf_codigo',
                  'UF': 'uf',
                  'UF_Nome': 'uf_nome',
                  'Municipio_Capital': 'capital',
                  'Numero_Habitantes_Censo_2022': 'numero_habitantes',
                  'Faixa_Populacao': 'populacao_faixa',
                  # 'Faixa_Populacao_FPM': 'populacao_faixa_fpm',
                  'qtd_0205': 'diagnostico_ultrasonografia_qtd',
                  'VL_0205': 'diagnostico_ultrasonografia_val',
                  'qtd_0411': 'cirurgias_obstetricas_qtd',
                  'VL_0411': 'cirurgias_obstetricas_val',
                  'qtd_0310': 'partos_e_nascimentos_qtd',
                  'VL_0310': 'partos_e_nascimentos_val',
                  'LATITUDE': 'latitude',
                  'LONGITUDE': 'longitude'}

    clean = Clean(input_filename=input_filename,
                  colunas_escolhidas=colunas,
                  dicionario=dicionario,
                  output_filename=output_filename)
    clean.start()
