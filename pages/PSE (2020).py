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

    with open("dados/Relatório PSE2020 v_0_1_3.pdf", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="Baixe aqui o relatório completo", data=PDFbyte, file_name="Relatório PSE2020.pdf",
                        mime='application/octet-stream', use_container_width=True)
with cols_intro[1]:
    st.image("images/pse-img01-passos-magicos.png")

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

    st.markdown("")
    cols_destaque_contexto = st.columns(2)
    with cols_destaque_contexto[0]:
        st.markdown("<p class='font-text-destaques'>Principais contextos Socioeconômicos de Embu-Guaçu</p>", unsafe_allow_html=True)
    with cols_destaque_contexto[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> O <font color='red'><b> IDHM</b></font> em Embu-Guaçu atingiu, em 2010, o patamar de <b>0,749 (alto)</b> 
                             correspondente aos países em desenvolvimento. Grande parte do avanço é creditado a melhora do indicador 
                             de <b>Educação</b>, partindo do muito baixo em 1990 ao nível alto em 2010. Embora há muito espaço para melhoras.
                        </li>
                        <li> Em relação à <font color='red'><b>condição de vida</b></font>, Embu-Guaçu possui indicadores de pobreza
                             e vulnerabilidade abaixo do Brasil como um todo (<b>36,99%</b> contra <b>54,38%</b>), porém extremamente 
                             elevado em relação à <b>RMSP</b> e o <b>Estado de São Paulo</b> (<b>22,8%</b> e <b>21,95%</b>). 
                             Praticamente <b>60%</b> das crianças em Embu-Guaçu estão nessas condições adversas.
                        </li>
                        <li> Em relação à <font color='red'><b>renda</b></font>, segundo dados de 2021 do IBGE, o salário médio dos trabalhadores
                             formais é de <b>2,5 salários mínimos</b>, com apenas <b>13,3%</b> da população ocupada, sendo esta uma das menores taxas
                             entre os municípios do Estado de São Paulo (543º lugar dentre 645 municípios). 
                        </li>
                    </ul>''', unsafe_allow_html=True)

    st.markdown('#')
    st.markdown('#')

    cols_local = st.columns(2)
    with cols_local[0]:
        st.image("images/contexto-img01-localizacao_embu-guacu.png")
    with cols_local[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> O município de <font color='red'><b> Embu-Guaçu</b></font>, está localizado na porção Sudoeste da Região
                             Metropolitanda de São Paulo (RMSP)
                        </li>
                        <li> A <font color='red'><b>população no censo de 2022</b></font> foi de <b>66.970 pessoas</b>, ocupando a 489ª posição no Brasil, com a densidade
                             demográfica de aproximadamente <b>430 habitantes</b> por quilômetro quadrado.
                        </li>
                        <li> Em <font color='red'><b>níveis educacionais</b></font>, o município possui uma taxa de <b>97%</b> de escolarização de 6 a 14 anos de idade, com
                             com mais de <b>13.000 matrículas</b> no Ensino Fundamental (EF) e Médio (EM). O IDEB da rede pública de ensino em 2021
                             foi de <b>5,8</b> no EFAI (Anos Iniciais) e <b>5,2</b> no EFAF (Anos Finais). 
                        </li>
                    </ul>''', unsafe_allow_html=True)

    st.markdown('#')
    st.markdown('#')

    cols_perfil_se = st.columns(2)
    with cols_perfil_se[0]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> Cerca de <font color='red'><b>22% dos habitantes</b></font> de Embu-Guaçu, aproximadamente 14.500 pessoas,
                             são crianças e jovens com idades entre 5 e 19 anos.
                        </li>
                        <li> Considerando que <font color='red'><b>60% da parcela da população</b></font> vive em condição de vulnerabilidade,
                             pobreza ou extrema pobreza, estamos falando de cerca de <b>8.700 crianças e jovens</b>.
                        </li>
                        <li> A <font color='red'><b>mortalidade infantil</b></font> caiu para <b>9,27</b> a cada 1.000 nascidos em 2022, 
                             abaixo da média nacional (<b>12,59</b>). A porcentagem de crianças que vivem em domicílios em que ninguém completou
                            o EF é de <b>16,4%</b> e <b>3%</b> das crianças em idade escolar ainda não frequentam a escola (PNUD, 2020).  
                        </li>
                    </ul>''', unsafe_allow_html=True)
    with cols_perfil_se[1]:
        st.image("images/contexto-img02-piramide-etaria_embu-guacu.png")

    st.markdown('#')
    st.markdown('#')

    cols_perfil_se_estudantes = st.columns(2)
    with cols_perfil_se_estudantes[0]:
        st.image("images/contexto-img03-pop-criancas-jovens_embu-guacu.png")

    with cols_perfil_se_estudantes[1]:
        st.markdown('''<ul class="font-text-destaques">
                <li> Entre os <font color='red'><b>indivíduos em idade escolar</b></font>, quanto à raça declarada, estão distribuídos
                    <b>54,4%</b> de Brancos, <b>44,8%</b> de Pretos e Pardos, <b>0,7%</b> de Amarelos e <b>0,1%</b> de Indígenas.
                </li>
                <li> A <font color='red'><b>escolaridade do município</b></font> é bem desafiante, sendo que apenas <b>60%</b> dos maiores
                     de 18 anos concluíram o Ensino Fundamental e <b>40%</b> da mesma faixa etária concluíram o Ensino Médio.
                </li>
            </ul>''', unsafe_allow_html=True)
        
    st.markdown('#')
    st.markdown('#') 
with tabs[1]:
    st.header('Plot')

with tabs[2]:
    st.markdown("- Testando...")
    st.header('Chart')
 
with tabs[3]:
    st.header('Input')
    st.text_input('Enter some text')
    st.number_input('Enter a number')


## Rodapé
st.markdown("---")

st.markdown('''<div class="center">
                    <a target="_self" href="#b1732366">
                        <button class="back-to-top">
                            Voltar ao topo
                        </button>
                    </a>
                </div>''', unsafe_allow_html=True)

# estilização dos parâmetros dos textos e elementos da página
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
    /*Texto do princiapl destaque de cada aba*/
    p.font-text-destaques {
    font-size:40px;
    font-weight:bold;
    color:#0367b0;
    padding: 200px 0 200px;
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
st.markdown(css, unsafe_allow_html=True)