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
    st.image("images\Passos-magicos-icon-cor.png")
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


cols_intro = st.columns(2)
with cols_intro[0]:
    st.markdown("### :mag_right: Pesquisa Sócio Econômica (2020)")
    st.markdown('''Aqui compilamos os dados da Pesquisa Socioeconômica 2020 organizada e produzida pela [Associação Passos Mágicos](https://passosmagicos.org.br/).
                   Essa pesquisa, visa conhecer melhor o contexto das famílias atendidas pelo projeto e seuas condições reais de vida.
                   Como a própria ONG prega, a Educação não está desvinculada das condições materiais de vida, da organização familiar,
                   do acesso às capacidades e aos funcionamentos sociais, e da saúde física, mental e emocional dos estudantes e seus familiares.''')

    st.markdown('''A pesquisa foi realizada por meio de entrevistas no segundo trimestre do ano de 2020, sendo todas elas feitas respeitando
                   as regras de distanciamento social e de proteção, no contexto da pandemia COVID-19. Todas as informações foram cedidas pelas
                   famílias de forma voluntária e os principais resultados divulgados no relatório abaixo, que você poderá baixar em PDF.''')

    with open("dados\Relatório PSE2020 v_0_1_3.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="Baixe aqui o relatório completo", data=PDFbyte, file_name="Relatório PSE2020.pdf",
                        mime='application/octet-stream', use_container_width=True)
with cols_intro[1]:
    st.image("images\pse-img01-passos-magicos.png")

with st.container(border=True):
    st.markdown("### Sobre a edição de 2020")
    st.markdown('''Esta é a 1ª edição da Pesquisa Socioeconômica. A coleta dos dados foi realizada por meio da aplicação de um questionário seguindo
                   os moldes dos questionário da Pesqueisa Nacional por Amostras de Domicílios Contínua do IBGE (PNAD), para possibilitar a comparação
                   dos resultados desta Pesquisa com as estatísticas públicas nos âmbitos municipal, regional, estadual e nacional.''')

    st.markdown('''O questionários possuía 53 perguntas, divididas em cinco seções: Demografia, Passo Mágicos, Relações de Trabalho, Rendas do Trabalho
                    e de outras fontes e Condições de Moradia.''')
    
    cols_container = st.columns(3, gap="small")
    with cols_container[0]:
        quadro_1 = cols_container[0].container(height = 140, border=True)
        quadro_1.markdown("### 2.673")
        quadro_1.markdown("\nindivíduos responderam a pesquisa")
    with cols_container[1]:
        quadro_2 = cols_container[1].container(height = 140, border=True)
        quadro_2.markdown("### 654")
        quadro_2.markdown("\ndomicílios diferentes. Todos localizados no município de Embu-Guaçu-SP")
    with cols_container[2]:
        quadro_2 = cols_container[2].container(height = 140, border=True)
        quadro_2.markdown("### 141.669")
        quadro_2.markdown("\nquestões respondidas no total")


# Criando as tabs da pesquisa
tab_titles = ["Contexto", "Demografia", "Passos Mágicos", "Trabalho", "Renda", "Moradia"]
tabs = st.tabs(tab_titles)
 
# Add content to each tab
with tabs[0]:
    st.header('Metrics')
    st.metric('Metric 1', 123)
    st.metric('Metric 2', 456)
 
with tabs[1]:
    st.header('Plot')

with tabs[2]:
    st.markdown("- Testando...")
    st.header('Chart')
 
with tabs[3]:
    st.header('Input')
    st.text_input('Enter some text')
    st.number_input('Enter a number')




# Ajustando parâmetros dos textos
css = '''
<style>
    /* Ajusta topicalização*/
    [data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
    }
    /* Botões das páginas*/
    div.stButton > button:first-child {
    color:#ed3237;
    }
    div.stButton > button:hover {
    border-color: #f58334;
    color:#f58334;
    }
    /*Botão do dowload do relatório*/
    div.stDownloadButton > button:first-child {
    background-color: #2c5381;
    color:#ffffff;
    }
    div.stDownloadButton > button:hover {
    background-color: #ffffff;
    color:#000000;
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
    div.stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size:1.2rem;
    font-weight:bold;
    margin-left: 2rem;
    }

</style>
'''
st.markdown(css, unsafe_allow_html=True)