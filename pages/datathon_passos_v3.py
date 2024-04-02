import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 
import plotly.graph_objects as go
import numpy as np

df = pd.read_csv("dados/PEDE_PASSOS_DATASET_FIAP-empilhados.csv", sep=",", encoding="utf-8",engine="python", decimal=".")
df.fillna(0,inplace=True)


# Alunos po ano fonte : PEDE2022
alunos_por_ano = pd.DataFrame({"Ano":["2020","2021","2022"],"Alunos":[727,737,929]})

#grafico 1
fig_1 = px.bar(alunos_por_ano, x='Ano', y='Alunos',
             hover_data=["Alunos"],color=pd.Series('Alunos', index=range(len(alunos_por_ano))),
             labels={'Alunos':'Quantidade de Alunos '}, height=500,width=700)

fig_1.update_layout(
    title="Quantidade de Alunos por Ano ",
    xaxis_title="Ano",
    yaxis_title="Alunos ",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"))

df_media = df.iloc[:,[1,2,3,4,5,6,7,8,9]]

df_2020 = df_media.query("Ano == 2020").query("IAA !=0 ").mean()
df_2021 = df_media.query("Ano == 2021").query("IAA !=0 ").mean()
df_2022 = df_media.query("Ano == 2022").query("IAA !=0 ").mean()

df_2020 = pd.DataFrame(df_2020).T
df_2021 = pd.DataFrame(df_2021).T
df_2022 = pd.DataFrame(df_2022).T


df_medias_1 = pd.concat([df_2020,df_2021,df_2022])
df_medias_1['Ano'] = ["2020","2021","2022"]



fig_2 = go.Figure()
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IAA, name="IAA",
                    ))
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IEG, name="IEG",
                    ))
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IPS, name="IPS",
                    ))
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IDA, name="IDA",
                    ))
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IPP, name="IPP",
                    ))
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IPV, name="IPV",
                    ))
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IAN, name="IAN",
                    ))
#grafico 2 
fig_2.update_layout(
    title="Valores médios dos indicadores",
    xaxis_title="Ano",
    yaxis_title="Média",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"))
fig_2.show()


df_2 = pd.read_csv("dados/PEDE_PASSOS_DATASET_FIAP-original.csv", sep=",", decimal=".", encoding="latin-1")
df_2.fillna(0, inplace=True)


df_notas = df_2.iloc[:,[55,56,57]]
df_notas = df_notas.query("NOTA_PORT_2022 !=0 and NOTA_MAT_2022 !=0")
df_medias = pd.DataFrame(df_notas.mean())
df_medias.reset_index(inplace=True)
df_medias.rename(columns={"index":"notas",0:"media"}, inplace=True)




#grafico 3
fig_3 = px.bar(df_medias, x='notas', y='media',color=pd.Series('notas', index=range(len(df_medias))),
             labels={'media':'Médias'}, height=500, width=700)

fig_3.add_hline(4.41,annotation_text="Média Nacional de Português e Matematica ")

fig_3.update_layout(
    title=" Médias Portugues e Matematica ",
    xaxis_title="Materias",
    yaxis_title="Médias",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"))
fig_3.show()


df_virada = df_2[["NOME","PONTO_VIRADA_2022"]]
df_virada = df_virada.query("PONTO_VIRADA_2022 !=0")
df_virada = pd.DataFrame(df_virada.groupby("PONTO_VIRADA_2022")["PONTO_VIRADA_2022"].count())
df_virada.rename(columns={"PONTO_VIRADA_2022":"valores"}, inplace=True)
df_virada.reset_index(inplace=True)
df_virada["%"] = [(749/(749+113))*100,(113/(749+113))*100]



#grafico4
fig_4 = px.bar(df_virada, x =df_virada["PONTO_VIRADA_2022"],y = df_virada["%"],color="PONTO_VIRADA_2022", height=500, width=700)

fig_4.update_layout(
    title="Ponto de Virada ",
    xaxis_title="Sim ou Não ",
    yaxis_title="Quantidade ",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"))
fig_4.show()


df_est_univer = pd.DataFrame({"Ano":["2020","2021","2022"],"alunos_unv":[24,49,59],"total_alunos":[727,737,929]})
df_est_univer["%_univer"] =(df_est_univer["alunos_unv"]/df_est_univer["total_alunos"])*100



fig_5 = px.line(df_est_univer, x='Ano', y='%_univer',color=pd.Series('Ano', index=range(len(df_medias))),
             labels={'%_univer':'Percentual de alunos na universidade'},markers= True, width=700)


#Grafico_5
fig_5.update_layout(
    title=" Percentual de alunos universitários ",
    xaxis_title="Ano",
    yaxis_title="Percentual %",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"))
fig_5.show()


import streamlit as st

st.set_page_config(layout= 'wide')
tabs_titles_2= ["Como funciona a Passos","Alunos impactados pela Passos","Indicadores"]
tabs_2 = st.tabs(tabs_titles_2)

with tabs_2[0]: 
    st.markdown("")
    colunas_1 = st.columns(2, gap="large")
    with colunas_1 [0]:

            st.markdown("""A Passos Mágicos tem como objetivo acelerar a ascensão social de crianças e jovens do município de Embu Guaçu através da educação. 
            Fornecendo aulas de português, matemática e inglês três vezes na semana, 
            atividades extracurriculares de finais de semana e bolsas de estudos no colégio particular, em cursos técnicos e de graduação..""")

    with colunas_1 [1]:
            st.image("images/Ong-Passos-Magicos.jpeg",width= 250)
            
    st.markdown("""A Passos Mágicos baseia-se na meritocracia, por isso engajamos nossas crianças para que acreditem que estudar é bom e pode transformar a vida delas.
            Avaliamos a participação, desempenho e presença para decidir quem participará das atividades de finais de semana e quem pode concorrer a bolsas de estudos na escola particular sendo apadrinhado por uma pessoa que se dispõe a financiar seu estudo. 
            As aulas são dadas fora do horário de aula escolar em locais fixos cedidos pela comunidade (em 4 núcleos diferentes), ou seja, 
            não temos uma sede construída, pois acreditamos que todo o valor de arrecadação do projeto deve ir para a melhora da qualidade de entrega e investimento em novas oportunidades para as crianças.""")
    st.image("images/metodologia.jpg",caption="Fonte:Relatório de atividades Passos Mágicos 2022")



    st.markdown("""A Passos conta  com um corpo docente composto por 7 professores, uma psicóloga e uma psicopedagoga, 
            todos eles contratados e remunerados para garantir a qualidade do ensino. 
            A ong conta com inumeras atividades de final de semana podem ser culturais como visita a museus e teatros ou educacionais como oficinas,
             cursos e workshops, todas realizadas com a ajuda de voluntários que acompanham e participam com nossas crianças.""")

    st.markdown( """A tabela a baixo demostra 
            o número de alunos impactados pelo sistema de aceleração de aprendizado 
            da Passos Mágicos""")

    st.image("images/pac-passos.png",caption="Fonte:Relatório de atividades Passos Mágicos 2022")


        
with tabs_2[2]: 
    st.markdown("")
    colunas_3 = st.columns(2)


    with colunas_3 [0]:
        st.markdown("### Indicadores Passos Mágicos")

        st.markdown('''Os dados que serão mostrados abaixo tem a finalidade de demonstrar o impacto do sistema 
educacional da Passos Mágicos nos jovens da região de Embu-Guaçu''')
        st.markdown(
                '''   
                  
                  O gráfico abaixo demostra a quantidade de alunos e a evolução desse número no periodo de 2020 até 2022.    
  Podemos notar o crescimento expresivo entre o periodo de 2021 e 2022 que passou de 727 para 939 alunos.''')

    with colunas_3 [1]:

        st.plotly_chart(fig_1, use_container_width=True)
        st.markdown("fonte: PEDE 2022-Passos Magicos")



    st.markdown("### Dimenssão de indicadores INDE")


    st.markdown("""O INDE (ÍNdice de deenvolvimento educacional ),como medida do presente processo avaliativo,  é composto por uma dimenssão acadêmica, uma dimenssão psicossocial e uma dimenssão psicopedagógica.    
                  Essas dimensões são observadas por meio de resultado de 7 indicadores (IAN,IDA,IEG,IAA,IPS,IPP e IPV) que aglutinados por ponderação formam o índice sintetico INDE.""")
    
    st.image("images/indicadores-INDE.png",caption="Fonte:PEDE 2022 Passos Mágicos")


    
    
    st.dataframe(df_medias_1)


          
    st.plotly_chart(fig_2, use_container_width=False)
    st.markdown("fonte: PEDE Dataset-FIAP-Passos Magicos")


    st.markdown("### Comparativo de Notas Português e Matemática ")
    st.markdown("")

    cols_perfil_4 = st.columns(2)
    with cols_perfil_4[0]:
              st.markdown(""" O gráfico abaixo demostra a média de notas em Português e Matemática comparada com a média nacional que é de 4,41
              contra 5,8 em matematica e 6,4 em português dos alunos da Passos.""")
              st.markdown("""Segundo Ideb (https://qedu.org.br/brasil/ideb) 
Nota padronizada em português e matemática de acordo com a Prova Saeb/2021
é de 4,41  que é representada pela linha no gráfico .""")

    with cols_perfil_4[1]:
            st.plotly_chart(fig_3, use_container_width=False)

    st.markdown("""### Ponto de Virada """)

    st.markdown(""" É um  indicador é um indicador psicopedagógico, os resultados são obtidos por meio de avaliação de professores e psicopedagogos da associação.
Ponto de virada é atingido quando o o estudante demostra de forma ativa por meio da trajetória dentro da associação, do valor de saber e a importancia de aprender.
No Ano de 2022 13% dos alunos atingiram o ponto de Virada.""")

    st.markdown("")
 
    st.dataframe(df_virada)

  
    st.plotly_chart(fig_4, use_container_width=False)


    
    st.markdown("""### Percentual de Alunos na universidade na Ong Passos Mágicos""")

    st.markdown("""Podemos notar que houve um crescimento de quase 3.3 pontos percentuais nos total de alunos estudando em uma universidade.""")

    st.plotly_chart(fig_5, use_container_width=False, sharing="streamlit", theme="streamlit")


  
