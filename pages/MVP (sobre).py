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

###### Página Sobre o Streamlit ######
st.header(":bar_chart: Sobre o MVP")

st.markdown('''<ul class="font-text">
            <p style='font-size:20px;'> Desenvolvemos este aplicativo no Streamlit para ilustrar e quantificar o impacto que a ONG Passos Mágicos
            vem causando na comunidade de Embu-Guaçu na Região Metropolitana de São Paulo.
            <br><br>
            Criamos com todo carinho e cuidado um dashboard que:
            </p>
            <li> <b>Analisa os dados históricos e atuais</b> da ONG, buscando entender sua influência na educação de jovens e
            crianças da comunidade
            </li>
            <li> <b>Identifica fatores-chave de sucesso</b> para determinar o impacto positivo para os resultados de quem se 
            beneficia dos projetos da ONG.
            </li>
            <li> <b>Representa uma solução sustentável</b> que pode ser integrado e atualizado pela ONG, seja como ferramenta de pesquisa,
            como um relatório dinâmico para apresentação resumida da Passos Mágicos para possíveis voluntários e apoiadores
            </li>
            <li> <b>Visualiza e conta a história</b> da Passos Mágicos, destacando seus impactos de forma visual e instigante.
            </li>
            <p style='font-size:20px;'> Espero que gostem deste dashboard do Streamlit e que o mesmo possa gerar insights relevantes para a compreensão da grandeza 
            da Passos Mágicos para com a comunidade de Embu-Guaçu.
            <br><br>
            Sinta-se livre para explorar este ambiente! &#128187;
            </p>
            </ul>
            ''', unsafe_allow_html=True )


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
