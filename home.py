import streamlit as st
import pandas as pd
import numpy as np
from plotly import express as px
from plotly import graph_objs as go

###### Páginal Inicial do Streamlit ######
st.set_page_config(layout= 'wide')

#### Páginas
cols = st.columns(6, gap="large")
with cols[0]:
    st.image("images/Passos-magicos-icon-cor.png")
with cols[1]:
    if st.button("Home"):
        st.switch_page("home.py")
with cols[2]:
    if st.button("PSE (2020)"):
        st.switch_page("pages/PSE (2020).py")
with cols[3]:
    if st.button("Sobre"):
        st.switch_page("pages/MVP (sobre).py")
with cols[4]:
    if st.button("Referências"):
        st.switch_page("pages/Referências.py")

st.header("", divider="gray")

st.header(":footprints: Análise dos dados da ONG Passos Mágicos")




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

df_pac  = pd.DataFrame({"Ano":["2016","2017","2018","2019","2020","2021","2022"],"Alunos":[70,300,550,812,841,824,1000]})

fig_6 = px.line(df_pac, x='Ano', y='Alunos',color=pd.Series('Alunos', index=range(len(df_pac))),
             labels={'Alunos':'Evolução do número de alunos no Pac por ano'},markers= True, width=700)

fig_6.update_layout(
    title=" Quantidade de alunos no PAC por ano ",
    xaxis_title="Ano",
    yaxis_title="Alunos",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"))
fig_6.show()

df_idade = pd.DataFrame({"Faixa etaria":["5 a 9 anos","10 a 14 anos","15 a 19 anos ","20 a 24 anos"],"%alunos":[15.8,59.9,23.8,0.4]})

fig_7 = px.bar(df_idade, x='Faixa etaria', y='%alunos',
             hover_data=["%alunos"],color=pd.Series('%alunos', index=range(len(df_idade))),
             labels={'%alunos':'Percentual de Alunos '}, height=500,width=700)

fig_7.update_layout(
    title="Percentual por faixa etária de alunos na Passos ",
    xaxis_title="Faixa Etária",
    yaxis_title="% Alunos ",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"))
fig_7.show()

df_etnia = pd.DataFrame({"Etnia":["Amarelos","Brancos ","Pardos","Pretos"],"Percentual%":[1,47,43,9]})

fig_8 = px.bar(df_etnia, x='Etnia', y='Percentual%',
             hover_data=["Percentual%"],color=pd.Series('Percentual%', index=range(len(df_etnia))),
             labels={'Percentual%':'Percentual de Alunos '}, height=500,width=700)

fig_8.update_layout(
    title="Percentual de alunos da Passos por Etnia ",
    xaxis_title="Etnia",
    yaxis_title="Percentual % ",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"))
fig_8.show()




labels = ["Feminino","Masculino"]
values = [54,46]

fig_9 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.5,marker_colors=["#0367b0","#fec52b"],textinfo='label+percent')])
fig_9.update_layout(width=500, height=500, font_family = 'Open Sans', font_color= "white", title_font_color= "black", 
                        title_font_size=24, title_text="Percentual de Alunos por genero")
fig_9.show()




tabs_titles_2= ["Como funciona a Passos","Alunos impactados pela Passos","Indicadores"]
tabs_2 = st.tabs(tabs_titles_2)

with tabs_2[0]: 
    st.markdown("")
    colunas_1 = st.columns(2)
    with colunas_1 [0]:

        with st.container(border=True):

            st.markdown("""A Passos Mágicos tem como objetivo acelerar a ascensão social de crianças e jovens do município de Embu Guaçu através da educação. 
            Fornecendo aulas de português, matemática e inglês três vezes na semana, 
            atividades extracurriculares de finais de semana e bolsas de estudos no colégio particular, em cursos técnicos e de graduação.""")

    with colunas_1 [1]:

                st.image("images/Ong-Passos-Magicos.jpeg",width=300)
                  
    st.markdown("""A Passos Mágicos baseia-se na meritocracia, por isso engajamos nossas crianças para que acreditem que estudar é bom e pode transformar a vida delas.
            Avaliamos a participação, desempenho e presença para decidir quem participará das atividades de finais de semana e quem pode concorrer a bolsas de estudos na escola particular sendo apadrinhado por uma pessoa que se dispõe a financiar seu estudo. 
            As aulas são dadas fora do horário de aula escolar em locais fixos cedidos pela comunidade (em 4 núcleos diferentes), ou seja, 
            não temos uma sede construída, pois acreditamos que todo o valor de arrecadação do projeto deve ir para a melhora da qualidade de entrega e investimento em novas oportunidades para as crianças.""")
    
    st.markdown("")

    colunas_2 = st.columns(2, gap="large")

    with colunas_2 [0]:

        st.image("images/metodologia.jpg",caption="Fonte:Relatório de atividades Passos Mágicos 2022", width=600)

    with colunas_2 [1]:

        st.markdown("")
        st.markdown("")
        with st.container(border=True):

            st.markdown("")
            st.markdown("""A Passos conta  com um corpo docente composto por 7 professores, uma psicóloga e uma psicopedagoga, 
            todos eles contratados e remunerados para garantir a qualidade do ensino. 
            A ong conta com inumeras atividades de final de semana podem ser culturais como visita a museus e teatros ou educacionais como oficinas,
             cursos e workshops, todas realizadas com a ajuda de voluntários que acompanham e participam com nossas crianças.""")
    

    st.markdown( """Organograma abaixo demostra a estrutura hiherraquica da Passo Mágicos""")
    st.markdown("")

    st.image("images/Estrutura passos.jpg", width=800)







with tabs_2[1]: 



    st.header("Alunos impactados pela Passo màgicos")
    st.markdown("")

    st.markdown("""A Passo Mágicos no decorrer de sua tragetória já impactou mais de 4.400 pessoas considerando familiares, vamos demostrar a quantidade de alunos que fizeram parte do PAC, 
    percentual de alunos por sexo e etnia e faixa etária """)

    colunas_3 = st.columns(2, gap="large")
    
    with colunas_3 [0]:


        st.markdown("")
        st.markdown("")

        st.markdown( """ 
        
            <ul class="font-text-destaques"> <li> O gráfico ao lado demostra a evolução de 
            o número de alunos impactados pelo sistema de aceleração de aprendizado 
            da Passos Mágicos .""",unsafe_allow_html=True)

        st.markdown(""" <ul class="font-text-destaques"> <li> Podemos notar que houve um crescimento exponencial chegando ao número de <b> 1.000 </b> alunos impactados 
        pelo PAC da Passo no ano de 2022.  """,unsafe_allow_html=True)

    
    with colunas_3 [1]:
    
        st.plotly_chart(fig_6, use_container_width=True)


    colunas_4 = st.columns(2, gap="large")

    with colunas_4 [0]:
        st.plotly_chart(fig_7, use_container_width=True)

    with colunas_4 [1]:
      
       st.markdown("""### Percentual de alunos por Faixa Etária""")
       st.markdown("     ")
       st.markdown("""<ul class="font-text-destaques"> <li> A passos possui alunos na entre <b> 5 e 24 anos</b> a faixa etária com maior percentual de alunos é entre <b> 10 e 14 anos </b> com <font color='red'><b> 59.9 % </b></font> do total de alunos 
       Em segundo lugar fica a faixa entre 15 e 19 anos com 23.8 %  """, unsafe_allow_html=True)


    colunas_5 = st.columns(2, gap="large")

    with colunas_5 [0]:
        st.markdown("""### Percentual de alunos por Etnia""")
        st.markdown("     ")
        st.markdown("     ")
        st.markdown("     ")
        st.markdown("""<ul class="font-text-destaques"> <li> O Gráfico ao lado demonstra a distribução de alunos por Etnia  Brancos<b> 47 % </b>, Pardos <b> 43 % </b> e Pretos com <b> 9% </b>  """, unsafe_allow_html=True) 

       

    with colunas_5 [1]:

        st.plotly_chart(fig_8, use_container_width=True)
        
    colunas_6 = st.columns(2, gap="large")

    with colunas_6 [0]:

      st.plotly_chart(fig_9, use_container_width=True)

    with colunas_6 [1]:

      st.markdown("<p class='font-text-destaques'><br> 54 % dos alunos são do sexo feminino e 46 % do sexo masculino </p>", unsafe_allow_html=True)
        
with tabs_2[2]: 
    st.markdown("")
    colunas_3 = st.columns(2)


    with colunas_3 [0]:
        st.markdown("### Indicadores Passos Mágicos")

        st.markdown('''   <li> Os dados que serão mostrados abaixo tem a finalidade de demonstrar o impacto do sistema 
educacional da Passos Mágicos nos jovens da região de Embu-Guaçu.''',unsafe_allow_html=True)
        st.markdown("")
        st.markdown(
                ''' 
                 <li> O gráfico abaixo demostra a quantidade de alunos e a evolução desse número no periodo de 2020 até 2022.    
  Podemos notar o crescimento expresivo entre o periodo de 2021 e 2022 que passou de <b> 727 <b> para <b> 939 <b> alunos.''',unsafe_allow_html=True)

    with colunas_3 [1]:

        st.plotly_chart(fig_1, use_container_width=True)
       


    st.markdown("### Dimenssão de indicadores INDE")


    st.markdown("""O INDE (ÍNdice de deenvolvimento educacional ),como medida do presente processo avaliativo,  é composto por uma dimenssão acadêmica, uma dimenssão psicossocial e uma dimenssão psicopedagógica.    
                  Essas dimensões são observadas por meio de resultado de 7 indicadores (IAN,IDA,IEG,IAA,IPS,IPP e IPV) que aglutinados por ponderação formam o índice sintetico INDE.""")
    st.markdown("")
    st.markdown("O quaro abaixo explica o significado de cada indicador :")
    st.image("images/indicadores-INDE.png",caption="Fonte:PEDE 2022 Passos Mágicos")


    
    
    st.dataframe(df_medias_1)


          
    st.plotly_chart(fig_2, use_container_width=False)


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


