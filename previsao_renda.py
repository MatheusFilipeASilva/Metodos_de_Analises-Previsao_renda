import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


pg_icon = """https://w7.pngwing.com/pngs/397/76/png-transparent-dollar-sign-illustration-dollar-sign-united-states-dollar-symbol-gold-dollar-text-gold-number.png"""
st.set_page_config(
    page_title="Renda - Previsão",
    page_icon=pg_icon,
    layout="wide",
)

renda = pd.read_csv(r'C:\Users\Matheus\Downloads\PROJETO PREVISAO DE RENDA\projeto 2\previsao_de_renda.csv')

st.sidebar.header('Exposisão - Previsão de Renda')
st.sidebar.write('- Panorama dos dados utilizados')
st.sidebar.write('- Bivariadas das variáveis utilizadas')
st.sidebar.write('- Conlusões sobre o modelo')
st.title('DataFrame de Origem:')
st.write(renda)

st.write("""Estes foram os dados que foram utilizados ao longo do 
        projeto. Isto é, um DataFrame constando diversos dados dos
        clientes, que podem ou não servir de indicadores para a renda
        dos mesmos. Nosso modelo foi construído através de um algoritmo
        'stepwise' que seleciona com autonomia as melhores variáveis
        explicativas para a variável dependente utilizando as
        informações disponíveis. Após isso, utilizamos um algoritmo
        de regressão Elastic Net para minimizar as possíveis
        colinearidades entre as variáveis utilizadas.''')
st.write('''As nossas variáveis utilizadas foram: 'tempo_emprego', 'sexo_M', 
        'tipo_renda_Empresário', 'idade', 'educacao_Superior_completo', 
        'posse_de_imovel', 'estado_civil_Solteiro',""")

st.write(f"""\n Vamos, a seguir, expor alguns gráficos que mostram a relação entre 
        as variáveis utilizadas e a renda média:""")


fig, ax = plt.subplots(8,1,figsize=(10,70))
sns.lineplot(x='data_ref',y='renda', hue='posse_de_imovel', data=renda, ax=ax[0])
ax[0].tick_params(axis='x', rotation=45)
sns.barplot(x='posse_de_veiculo', y='renda',data=renda, ax=ax[1])
ax[1].tick_params(axis='x', rotation=90)
sns.barplot(x='idade', y='renda', data=renda, ax=ax[2])
ax[2].tick_params(axis='x', rotation=90)
sns.lineplot(x='data_ref', y='renda', hue = 'tipo_renda', data=renda, ax=ax[3])
ax[3].tick_params(axis='x', rotation = 90)
ax[3].legend(loc = 'upper right')
sns.lineplot(x='data_ref', y='renda', hue='estado_civil', data=renda, ax=ax[4])
ax[4].tick_params(axis='x', rotation=90)
sns.lineplot(x='data_ref', y='renda', hue='educacao', data=renda, ax=ax[5])
ax[5].tick_params(axis='x', rotation=90)
sns.lineplot(x='data_ref', y='renda', hue='educacao', data=renda, ax=ax[6])
ax[6].tick_params(axis='x', rotation=90)
renda['cut_tempo_emprego'] = pd.cut(renda['tempo_emprego'], bins=30)
tempo_emprego_group = renda.groupby('cut_tempo_emprego')['renda'].mean().reset_index()
pd.DataFrame(tempo_emprego_group)
sns.barplot(x='cut_tempo_emprego', y='renda', data=tempo_emprego_group, ax=ax[7])
ax[7].tick_params(axis='x', rotation=90)
plt.tight_layout()
st.pyplot(plt)

st.header('Conclusões:')
st.write('''As variáveis selecionadas pelo modelo, via de regra, apresentam correlação explícita com a variável
        dependente, como pode-se visualizar nos gráficos. No entanto, uma das variáveis que mostram alta corre-
        lação com a renda ao se ver os gráficos, quando foi adicionada no nosso modelo, afetou negativamente os resul-
        tados, como indício, provavelmente, de esta variável ser em grande partelinearmente construtível
        por meio das demais variáveis selecionadas.''')