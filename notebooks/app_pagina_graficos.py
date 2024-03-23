import streamlit as st 
from app_graficos import fig_1,fig_2,fig_3,fig_4,fig_5, df_medias,df_medias_1,df_virada

st.set_page_config(layout= 'wide')

st.markdown("### Indicadores Passos Mágicos")

st.markdown('''Os dados que serão mostrados abaixo tem a finalidade de demonstrar o impacto do sistema 
educacional da Passos Mágicos nos jovens da região de Embu-Guaçu''')

st.markdown("### Quantidade de alunos por ano")

st.markdown('''O gráfico abaixo demostra a quantidade de alunos e a evolução desse número 
no periodo de 2020 até 2022, podemos notar o crescimento expresivo entre o periodo de 2021 e 2022 que passou de 727 para 939 alunos''')


st.plotly_chart(fig_1, use_container_width=False, sharing="streamlit", theme="streamlit")
st.markdown("fonte: PEDE 2022-Passos Magicos")

st.markdown("### Dimenssão de indicadores INDE")

st.markdown("""O INDE (ÍNdice de deenvolvimento educacional ), como medida do presente processo avaliativo
, é composto por uma dimenssão acadêmica, uma dimenssão psicossocial e uma dimenssão psicopedagógica.
Essas dimensões são observadas por meio de resultado de 7 indicadores (IAN,IDA,IEG,IAA,IPS,IPP e IPV)
que aglutinados por ponderação formam o índice sintetico INDE.""")


st.dataframe(df_medias_1)

st.plotly_chart(fig_2, use_container_width=False, sharing="streamlit", theme="streamlit")
st.markdown("fonte: PEDE Dataset-FIAP-Passos Magicos")



st.markdown("### Comparativo de Notas Português e Matemática ")
st.markdown(""" O gráfico abaixo demostra a média de notas em Português e Matemática comparada com a média nacional que é de 4,41
contra 5,8 em matematica e 6,4 em português dos alunos da Passos.""")
st.markdown("""Segundo Ideb (https://qedu.org.br/brasil/ideb) 
Nota padronizada em português e matemática de acordo com a Prova Saeb/2021
é de 4,41  que é representada pela linha no gráfico .""")

st.plotly_chart(fig_3, use_container_width=False, sharing="streamlit", theme="streamlit")

st.markdown("""### Ponto de Virada """)

st.markdown(""" É um  indicador é um indicador psicopedagógico, os resultados são obtidos por meio de avaliação de professores e psicopedagogos da associação.
Ponto de virada é atingido quando o o estudante demostra de forma ativa por meio da trajetória dentro da associação, do valor de saber e a importancia de aprender.
No Ano de 2022 13% dos alunos atingiram o ponto de Virada.""")

st.dataframe(df_virada)


st.plotly_chart(fig_4, use_container_width=False, sharing="streamlit", theme="streamlit")


st.markdown("""### Percentual de Alunos na universidade na Ong Passos Mágicos""")

st.markdown("""Podemos notar que houve um crescimento de quase 3.3 pontos percentuais nos total de alunos estudando em uma universidade.""")

st.plotly_chart(fig_5, use_container_width=False, sharing="streamlit", theme="streamlit")
