import streamlit as st

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

###### Página de Referências do Streamlit ######
st.header(":books: Referências")

st.markdown('''<ul class="font-text">
            <li>
            PASSOS MÁGICOS, Website da ONG Passos Mágicos. [acessado 2023 Mar].<br>  
            Disponível em: <a href="https://passosmagicos.org.br/">https://passosmagicos.org.br/</a>
            </li>
            <li> 
            PANDAS. Documentação da biblioteca Pandas [Internet]. [acessado 2023 Jan].<br>   
             Disponível em: <a href="https://pandas.pydata.org/docs/reference/">https://pandas.pydata.org/docs/reference/</a>
            </li>
            <li>
            STREAMLIT. Documentação da biblioteca Streamlit [Internet]. [acessado 2023 Jan].<br>   
            Disponível em: <a href="https://docs.streamlit.io/">https://docs.streamlit.io/</a>
            </li>
            <li>
            PLOTLY. Documentação da biblioteca Plotly [Internet]. [acessado 2023 Jan]. <br>  
            Disponível em: <a href="https://plotly.com/python/">https://plotly.com/python/</a>
            </li>
            <li>
            JOEL, Grus. Data Science do Zero: Noções Fundamentais com Python [Livro físico]
            </li>
            <li>
            KNAFLIC, Cole Nussbaumer. Storytelling com dados: uma guia sobre visualização de dados para profissionais de negócio [Livro físico]
            </li>
            <li>
            IBGE, Panorama de Embu-Guaçu. [acessado 2023 Mar].  <br> 
            Disponível em: <a href="https://cidades.ibge.gov.br/brasil/sp/embu-guacu/panorama">https://cidades.ibge.gov.br/brasil/sp/embu-guacu/panorama</a>
            </li>
            <li>
            SEADE, Dashboard dos dados dos Municípios. [acessado 2023 Mar]. <br>  
            Disponível em: <a href="https://municipios.seade.gov.br/">https://municipios.seade.gov.br/</a>
            </li>
            <li>
            IMP, Informações dos Municípios Paulistas. [acessado 2023 Mar].  <br> 
            Disponível em: <a href="http://www.imp.seade.gov.br/frontend/#/tabelas">http://www.imp.seade.gov.br/frontend/#/tabelas</a>.
            </li>       
            </ul>''', unsafe_allow_html=True)


css = '''
<style>
    /* Ajusta topicalização*/
    [data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
    }
    /*Texto dos destaques de cada aba*/
    ul.font-text li{
    font-size:20px;
    }
</style>'''

st.markdown(css, unsafe_allow_html=True)