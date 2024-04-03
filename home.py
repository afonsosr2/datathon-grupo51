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

###### Configuração Inicial ######
@st.cache_data
def config_inicial():
    df = pd.read_csv("dados/PEDE_PASSOS_DATASET_FIAP-empilhados.csv", sep=",", encoding="utf-8",engine="python", decimal=".")
    df.fillna(0,inplace=True)
    return df


# Alunos por ano fonte : PEDE2022
# Gráfico 1
alunos_por_ano = pd.DataFrame({"Ano":["2020","2021","2022"],"Alunos":[727,737,929]})

fig_1 = px.bar(alunos_por_ano, x='Ano', y='Alunos', hover_data=["Alunos"], color=pd.Series('Alunos', index=range(len(alunos_por_ano))),
             labels={'Alunos':'Quantidade de Alunos'}, text_auto=True, color_discrete_sequence=["#0367b0"])
fig_1.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>%{y}</b>', cliponaxis=False)
fig_1.update_xaxes(tickmode='array', tickvals=np.arange(2020,2023))

fig_1.update_layout(
    width=700, height=400, font_family = 'Open Sans', title_font_color= "black", title_font_size=24, 
    showlegend=False, plot_bgcolor= "#f8f9fa", xaxis_tickfont_size=14, yaxis_tickfont_size=14,
    title="Quantidade de Alunos por Ano ",
    xaxis_title="Ano",
    yaxis_range = [0, 950],
    yaxis_title="Alunos",
    font=dict(
        family="Open Sans",
        size=15,
        color="black"
        ))

df = config_inicial()
df_media = df.iloc[:,[1,2,3,4,5,6,7,8,9]]

df_2020 = df_media.query("Ano == 2020").query("IAA !=0 ").mean()
df_2021 = df_media.query("Ano == 2021").query("IAA !=0 ").mean()
df_2022 = df_media.query("Ano == 2022").query("IAA !=0 ").mean()

df_2020 = pd.DataFrame(df_2020).T
df_2021 = pd.DataFrame(df_2021).T
df_2022 = pd.DataFrame(df_2022).T


df_medias_1 = pd.concat([df_2020,df_2021,df_2022])
df_medias_1['Ano'] = ["2020","2021","2022"]

# Gráfico 2
fig_2 = go.Figure()
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IAA, name="IAA"))
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IEG, name="IEG"))
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IPS, name="IPS"))
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IDA, name="IDA"))
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IPP, name="IPP"))
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IPV, name="IPV"))
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IAN, name="IAN"))
fig_2.update_layout(
    width=1200, height=400, font_family = 'Open Sans',
    plot_bgcolor= "#f8f9fa", xaxis_tickfont_size=14, yaxis_tickfont_size=14,
    title="Valores médios dos indicadores",
    xaxis_title="Ano",
    yaxis_title="Média",
    yaxis_range = [5, 9],
    font=dict(
        family="Open Sans",
        size=15,
        ))

df_2 = pd.read_csv("dados/PEDE_PASSOS_DATASET_FIAP-original.csv", sep=",", decimal=".", encoding="latin-1")
df_2.fillna(0, inplace=True)


# Gráfico 3
df_notas = df_2.iloc[:,[55,56,57]]
df_notas = df_notas.query("NOTA_PORT_2022 !=0 and NOTA_MAT_2022 !=0")
df_medias = pd.DataFrame(df_notas.mean())
df_medias.reset_index(inplace=True)
df_medias.rename(columns={"index":"notas",0:"media"}, inplace=True)

fig_3 = px.bar(df_medias, x='notas', y='media',color=pd.Series('notas', index=range(len(df_medias))),
             labels={'media':'Médias'}, text_auto=True, color_discrete_sequence=["#0367b0"])
fig_3.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>%{y:.2f}</b>', cliponaxis=False)

fig_3.update_xaxes(tickmode='array', tickvals=np.arange(0,3), ticktext = ["Português - 2022", "Matemática - 2022", "Inglês - 2022"])

fig_3.add_hline(4.41, annotation_text="Média Nacional de PORT e MAT")

fig_3.update_layout(
    width=700, height=400, font_family = 'Open Sans', showlegend=False, 
    plot_bgcolor= "#f8f9fa", xaxis_tickfont_size=14, yaxis_tickfont_size=14,
    title=" Médias de Português (PORT), Matemática (MAT) e Inglês (ING)",
    xaxis_title="Matérias",
    yaxis_title="Médias",
    font=dict(
        family="Open Sans",
        size=15,
        ))


# Gráfico 4
df_virada = df_2[["NOME","PONTO_VIRADA_2022"]]
df_virada = df_virada.query("PONTO_VIRADA_2022 !=0")
df_virada = pd.DataFrame(df_virada.groupby("PONTO_VIRADA_2022")["PONTO_VIRADA_2022"].count())
df_virada.rename(columns={"PONTO_VIRADA_2022":"valores"}, inplace=True)
df_virada.reset_index(inplace=True)
df_virada["%"] = [(749/(749+113))*100,(113/(749+113))*100]

fig_4 = px.bar(df_virada, x =df_virada["PONTO_VIRADA_2022"],y = df_virada["%"],color="PONTO_VIRADA_2022", text_auto=True, 
               color_discrete_sequence=["#be282c", "#0367b0"])
fig_4.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>%{y:.2f}%</b>', cliponaxis=False)

fig_4.update_layout(
    width=700, height=400, font_family = 'Open Sans', showlegend=False, 
    plot_bgcolor= "#f8f9fa", xaxis_tickfont_size=14, yaxis_tickfont_size=14,
    title="",
    xaxis_title="Atingiu o Ponto de Virada?",
    yaxis_title="% dos Alunos",
    font=dict(
        family="Open Sans",
        size=15,
        color = "black"
        ))


# Gráfico 5
df_est_univer = pd.DataFrame({"Ano":["2020","2021","2022"],"alunos_unv":[24,49,59],"total_alunos":[727,737,929]})
df_est_univer["%_univer"] =(df_est_univer["alunos_unv"]/df_est_univer["total_alunos"])*100

fig_5 = px.line(df_est_univer, x='Ano', y='%_univer',color=pd.Series('Ano', index=range(len(df_medias))),
             labels={'%_univer':'Percentual de alunos na universidade'}, markers= True, color_discrete_sequence=["#0367b0"])

fig_5.update_xaxes(tickmode='array', tickvals=np.arange(2020,2023))

fig_5.update_layout(
    width=700, height=400, font_family = 'Open Sans', showlegend=False, 
    plot_bgcolor= "#f8f9fa", xaxis_tickfont_size=14, yaxis_tickfont_size=14,
    title=" Percentual de alunos universitários ",
    xaxis_title="Ano",
    yaxis_title="Percentual %",
    yaxis_range = [0, 10],
    font=dict(
        family="Open Sans",
        size=15))


# Gráfico 6
df_pac  = pd.DataFrame({"Ano":["2016","2017","2018","2019","2020","2021","2022"],"Alunos":[70,300,550,812,841,824,1000]})

fig_6 = px.line(df_pac, x='Ano', y='Alunos',color=pd.Series('Alunos', index=range(len(df_pac))),
             labels={'Alunos':'Evolução do número de alunos no Pac por ano'},markers= True, color_discrete_sequence=["#0367b0"])

fig_6.update_layout(
    width=700, height=400, font_family = 'Open Sans', showlegend=False, 
    plot_bgcolor= "#f8f9fa", xaxis_tickfont_size=14, yaxis_tickfont_size=14,
    title=" Quantidade de alunos no PAC por ano ",
    xaxis_title="Ano",
    yaxis_title="Alunos",
    font=dict(
        family="Open Sans",
        size=15, color = "black")
        )


# Gráfico 7
df_idade = pd.DataFrame({"Faixa etaria":["5 a 9 anos","10 a 14 anos","15 a 19 anos ","20 a 24 anos"],"%alunos":[15.8,59.9,23.8,0.4]})

fig_7 = px.bar(df_idade, x='Faixa etaria', y='%alunos',
             hover_data=["%alunos"],color=pd.Series('%alunos', index=range(len(df_idade))),
             labels={'%alunos':'Percentual de Alunos '}, text_auto=True, color_discrete_sequence=["#0367b0"])
fig_7.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>%{y}%</b>', cliponaxis=False)

fig_7.update_layout(
    width=700, height=400, font_family = 'Open Sans', showlegend=False, 
    plot_bgcolor= "#f8f9fa", xaxis_tickfont_size=14, yaxis_tickfont_size=14,
    title="Percentual por faixa etária de alunos na Passos ",
    xaxis_title="Faixa Etária",
    yaxis_title="% Alunos ",
    font=dict(
        family="Open Sans",
        size=15, color = "black")
        )


# Gráfico 8
df_etnia = pd.DataFrame({"Etnia":["Amarelos","Brancos ","Pardos","Pretos"],"Percentual%":[1,47,43,9]})

fig_8 = px.bar(df_etnia, x='Etnia', y='Percentual%',
             hover_data=["Percentual%"],color=pd.Series('Percentual%', index=range(len(df_etnia))),
             labels={'Percentual%':'Percentual de Alunos '}, text_auto=True, color_discrete_sequence=["#0367b0"])
fig_8.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>%{y}%</b>', cliponaxis=False)

fig_8.update_layout(
    width=700, height=400, font_family = 'Open Sans', showlegend=False, 
    plot_bgcolor= "#f8f9fa", xaxis_tickfont_size=14, yaxis_tickfont_size=14,
    title="Percentual de alunos da Passos por Etnia ",
    xaxis_title="Etnia",
    yaxis_title="Percentual % ",
    font=dict(
        family="Open Sans",
        size=15, color="black")
        )


# Gráfico 9
labels = ["Feminino","Masculino"]
values = [54,46]

fig_9 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.5,marker_colors=["#0367b0","#fec52b"],textinfo='label+percent')])
fig_9.update_layout( width=400, height=500, font_family = 'Open Sans', showlegend=False, plot_bgcolor= "#f8f9fa", 
                    xaxis_tickfont_size=14, yaxis_tickfont_size=14, title_font_color= "black", title_text="")

### Título da Página Inicial
st.header(":footprints: ONG Passos Mágicos e seus principais indicadores")
st.markdown("#")

### Tabs da página inicial
tabs_titles_2= ["Como funciona a Passos","Alunos impactados pela Passos","Indicadores"]
tabs_2 = st.tabs(tabs_titles_2)

# Tab Como funciona a Passos
with tabs_2[0]: 
    st.markdown("")
    colunas_1 = st.columns(2)
    with colunas_1 [0]:

        with st.container(border=True):
            st.markdown("""
                        <p style='font-size:20px;'>A Passos Mágicos tem como objetivo acelerar a ascensão social de crianças e jovens do município de Embu Guaçu através da educação.   
                        <br><br>
                        Fornecendo aulas de português, matemática e inglês três vezes na semana, atividades extracurriculares de finais de semana e bolsas de estudos no colégio particular, em cursos técnicos
                        e de graduação.</p>""", unsafe_allow_html=True)

    with colunas_1 [1]:
                st.image("images/Ong-Passos-Magicos.jpeg",width=300)
                  
    st.markdown('''<p style='font-size:20px;'>
                A Passos baseia-se na meritocracia, por isso engajamos nossas crianças para que acreditem que estudar é bom e pode transformar a vida delas.
                <br><br>
                Avaliamos a participação, desempenho e presença para decidir quem participará das atividades de finais de semana e quem pode concorrer a bolsas de estudos na escola particular
                sendo apadrinhado por uma pessoa que se dispõe a financiar seu estudo.
                <br><br>
                As aulas são dadas fora do horário de aula escolar em locais fixos cedidos pela comunidade (em 4 núcleos diferentes), ou seja, não temos uma sede construída, pois acreditamos que
                todo o valor de arrecadação do projeto deve ir para a melhora da qualidade de entrega e investimento em novas oportunidades para as crianças.
                </p>
                <br>
                ''', unsafe_allow_html=True)
    
    st.markdown("")

    colunas_2 = st.columns(2, gap="large")

    with colunas_2 [0]:

        st.image("images/metodologia.jpg",caption="Fonte:Relatório de atividades Passos Mágicos 2022", width=600)

    with colunas_2 [1]:

        st.markdown("#")
        with st.container(border=True):

            st.markdown("""
                        <p style='font-size:20px;'>A Passos conta com um corpo docente composto por 7 professores, uma psicóloga e uma psicopedagoga, todos eles contratados e remunerados para
                        garantir a qualidade do ensino. 
                        <br><br>
                        A ONG conta com inúmeras atividades de final de semana podem ser culturais como visita a museus e teatros ou educacionais como oficinas, cursos e workshops, todas realizadas
                        com a ajuda de voluntários que acompanham e participam com nossas crianças.</p>""", unsafe_allow_html=True)
    
    st.markdown("#")
    st.markdown( """## Organograma da estrutura hierárquica da Passos Mágicos""")
    st.markdown("#")

    st.image("images/Estrutura passos.jpg")

# TAB Alunos Impactados
with tabs_2[1]: 
    st.header("Alunos Impactados pela Passos Mágicos")

    st.markdown("""
                <p style='font-size:20px;'>A Passos Mágicos, no decorrer de sua trajetória, já impactou mais de 4.400 pessoas( considerando familiares). Vamos demostrar, logo abaixo, a quantidade de alunos
                 que fizeram parte do PAC (Programa de Aceleração de Conhecimento), o percentual de alunos por sexo e etnia e a sua faixa etária.
                <br><br>
                </p>""", unsafe_allow_html=True)

    colunas_3 = st.columns(2, gap="large")
    
    with colunas_3 [0]:
        st.markdown( """         
            <ul class="font-text-destaques">
                <br><br>
                <li> O gráfico ao lado demonstra a evolução do número de alunos impactados pelo sistema de aceleração de aprendizado da Passos Mágicos.
                </li>
                <li> Podemos notar que houve um crescimento exponencial chegando ao número de <b> 1.000 </b> alunos impactados pelo PAC da Passos no ano de 2022.
                </li>
            </ul>""",unsafe_allow_html=True)
    
    with colunas_3 [1]:    
        st.plotly_chart(fig_6, use_container_width=True)

    st.markdown("""### Percentual de alunos por Faixa Etária""")
    colunas_4 = st.columns(2, gap="large") 
    with colunas_4 [0]:
        st.plotly_chart(fig_7, use_container_width=True)
    with colunas_4 [1]:      
       st.markdown("""<ul class="font-text-destaques">
                   <br><br>
                   <li> A Passos possui alunos na entre <b> 5 e 24 anos</b> a faixa etária com maior percentual de alunos é entre <b> 10 e 14 anos </b> com <b> 59.9 % </b> do total de alunos.
                    Em segundo lugar, fica a faixa entre 15 e 19 anos com 23.8 %.
                   </li>
                   </ul>""", unsafe_allow_html=True)

    st.markdown("""### Percentual de alunos por Etnia""")
    colunas_5 = st.columns(2, gap="large")

    with colunas_5 [0]:
        st.markdown("""<ul class="font-text-destaques">
                    <br><br>
                    <li> O gráfico ao lado demonstra a distribuição de alunos por etnia:  Brancos com <b> 47 % </b>, Pardos com <b> 43 % </b> e Pretos com <b> 9% </b>
                    </li>
                    </ul>""", unsafe_allow_html=True) 
    with colunas_5 [1]:
        st.plotly_chart(fig_8, use_container_width=True)

    st.markdown("""### Percentual de alunos por Gênero""")
    colunas_6 = st.columns(2, gap="large")

    with colunas_6 [0]:
      st.plotly_chart(fig_9, use_container_width=True)

    with colunas_6 [1]:
      st.markdown('''<ul class="font-text-destaques">
                  <li> <b>54%</b> dos alunos são do sexo feminino e <b>46%</b> do sexo masculino.</li>
                  </ul>''', unsafe_allow_html=True)

# TAB de Indicadores      
with tabs_2[2]: 
    st.header("Indicadores Passos Mágicos")
    st.markdown('''<p style='font-size:20px;'>Os dados que serão mostrados abaixo tem a finalidade de demonstrar o impacto da Passos Mágicos no sistema educacional e nos jovens da região de Embu-Guaçu.
                <br><br>
                </p>''',unsafe_allow_html=True)
    colunas_3 = st.columns(2)
    with colunas_3 [0]:
        st.markdown(''' <ul class="font-text-destaques">
                    <br><br>
                    <li> O gráfico abaixo demonstra a quantidade de alunos e a evolução desse número no período de 2020 até 2022. Podemos notar o crescimento expressivo entre o período de 2021 e 2022.
                    que passou de <b> 727 <b> para <b> 939 <b> alunos.
                    </li>
                    </ul>''',unsafe_allow_html=True)

    with colunas_3 [1]:
        st.plotly_chart(fig_1, use_container_width=True)

    st.markdown("### Dimensões e indicadores INDE")
    st.markdown("#")

    colunas_9 = st.columns(2)
    with colunas_9 [1]:

       st.markdown("""<ul class="font-text-destaques">
                   <br><br>
                    <li> O INDE (Índice de Desenvolvimento Educacional), como medida do presente processo avaliativo, é composto por uma dimensão acadêmica, uma dimensão psicossocial e uma dimensão
                    psicopedagógica.
                    </li>   
                    <li> Essas dimensões são observadas por meio do resultado de 7 indicadores (IAN, IDA, IEG, IAA, IPS, IPP e IPV) que aglutinados por ponderação formam o índice sintético INDE.
                    </li>
                    </ul>""",unsafe_allow_html=True)
       with colunas_9 [0]:    
        st.image("images/indicadores-INDE.png",caption="Fonte: PEDE 2022 Passos Mágicos")
 
    colunas_10 = st.columns(2)

    with colunas_10[0]: 
        st.markdown('''<ul class="font-text-destaques">
                    <br><br>
                    <li> A tabela ao lado demonstra a evolução dos indicadores de desenvolvimento educacional.
                    </li>
                    </ul>''', unsafe_allow_html=True)
        st.markdown('''<ul class="font-text-destaques">
                    <li> Podemos notar que o indicador IDA (Indicador de desempenho acadêmico) e IEG(Indicador de engajamento) teve uma queda em 2021 referente ao ano de 2020 possivelmente impactado 
                    pela pandemia.
                    </li>
                    </ul>''', unsafe_allow_html=True)
    with colunas_10[1]: 
        
        st.dataframe(df_medias_1)

    st.markdown("#")
    st.markdown("### Gráfico com a evolução dos Indicadores de Desempenho entre o período de 2020 até 2022")
          
    st.plotly_chart(fig_2, use_container_width=True)


    st.markdown("### Comparativo de Notas - Português e Matemática ")
    st.markdown("#")

    cols_perfil_4 = st.columns(2)
    with cols_perfil_4[0]:
              st.markdown("""<ul class="font-text-destaques">
                          <br><br>
                          <li> O gráfico abaixo demostra a média de notas em Português e Matemática comparada com a média nacional que é de 4,41 contra 5,8 em matematica e 6,4 em português
                          dos alunos da Passos.
                          </li>
                          </ul>""",unsafe_allow_html=True)
              st.markdown("""<ul class="font-text-destaques">
                          <li> Segundo <a href="https://qedu.org.br/brasil/ideb">IDEB</a> a nota padronizada em português e matemática na Prova Saeb/2021 é de 4,41, representada pela linha no gráfico.
                          </li>
                          </ul>""",unsafe_allow_html=True)

    with cols_perfil_4[1]:
            st.plotly_chart(fig_3, use_container_width=False)

       
    st.markdown("""### Ponto de Virada """)
    st.markdown("#")

    colunas_11 = st.columns(2)
    with colunas_11[1]:
        st.markdown("""<ul class="font-text-destaques">
                    <li> É um  indicador é um indicador psicopedagógico, os resultados são obtidos por meio de avaliação de professores e psicopedagogos da associação.
                    </li>
                    <li> Ponto de virada é atingido quando o estudante demonstra de forma ativa por meio da trajetória dentro da associação, do valor de saber e a importância de aprender.
                     No ano de 2022, 13% dos alunos atingiram o Ponto de Virada.
                     </li>
                     </ul>
                    <br><br>""",unsafe_allow_html=True)
        st.dataframe(df_virada)

    with colunas_11[0]:
         st.plotly_chart(fig_4, use_container_width=200)


    
    st.markdown("""### Percentual de Alunos da ONG nas universidades""")
    st.markdown("#")

    colunas_12 = st.columns(2)
    with colunas_12[0]:
          st.markdown("""<ul class="font-text-destaques">
                    <li> Podemos notar que houve um crescimento de quase <b>3.3 pontos percentuais</b> no total de alunos estudando em uma universidade.
                    </li>
                    </ul>""",unsafe_allow_html=True)

    with colunas_12[1]:
          st.plotly_chart(fig_5, use_container_width=False, sharing="streamlit", theme="streamlit")


## Rodapé
st.markdown("---")

st.markdown('''<div class="center">
                    <a target="_self" href="#ea054864">
                        <button class="back-to-top">
                            Voltar ao topo
                        </button>
                    </a>
                </div>''', unsafe_allow_html=True)

css_2 = '''
<style>
    /* Ajusta topicalização*/
    [data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
    }
    /*Container de pesquisa*/
    [class="st-emotion-cache-r421ms e1f1d6gn0"]{
    background-color: #0367b0;
    border-radius: 30px;
    }
    /*Títulos do Container de pesquisa*/
    [class="st-emotion-cache-r421ms e1f1d6gn0"] h3{
    color: #ffffff;
    font-weight:bold;    
    }
    /*Títulos do Container de pesquisa*/
    [class="st-emotion-cache-r421ms e1f1d6gn0"] p{
    color: #ffffff; 
    }
    /*Cards do container de pesquisa*/
    [class="st-emotion-cache-r421ms e1f1d6gn0"] [data-testid="stHorizontalBlock"] [data-testid="stVerticalBlockBorderWrapper"]{
    background-color: #68a4d0;    
    border-radius: 30px;
    }
    /*Tabs da Pesquisa*/    
    [class="st-emotion-cache-l9bjmx e1nzilvr5"] p {
    font-size:1.2rem;
    font-weight:bold;
    margin-left: 2rem;
    }
    /*Texto do principal destaque de cada aba*/
    p.font-text-destaques {
    font-size:40px;
    font-weight:bold;
    color:#0367b0;
    padding: 150px 0 150px;
    }
    /*Texto dos destaques de cada aba*/
    ul.font-text-destaques li{
    font-size:20px;
    }
    /*Botão de retorno ao topo do relatório*/
    .center {
    position: absolute;
    left: 50%;
    -ms-transform: translateX(-50%);
    transform: translateX(-50%);
    }
    button.back-to-top{
    background-color: #2c5381;
    color:#ffffff;
    border-radius: 8px;
    }
    button.back-to-top:hover{
    background-color: #ffffff;
    color:#000000;
    }
</style>
'''
st.markdown(css_2, unsafe_allow_html=True)


