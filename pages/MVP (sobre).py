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

st.markdown('''<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}</style>''', 
unsafe_allow_html=True)

st.markdown('''
            Desenvolvemos este aplicativo no Streamlit para ilustrar e quantificar o impacto que a ONG Passos Mágicos
            vem causando na comunidade de Embu-Guaçu na Região Metropolitana de São Paulo.

            Criamos com todo carinho e cuidado um dashboard que:
            - **Analisa os dados históricos e atuais** da ONG, buscando entender sua influência na educação de jovens e
            crianças da comunidade
            - **Identifica fatores-chave de sucesso** para determinar o impacto positivo para os resultados de quem se 
            beneficia dos projetos da ONG.
            - **Representa uma solução sustentável** que pode ser integrado e atualizado pela ONG, seja como ferramenta de pesquisa,
            como um relatório dinâmico para apresentação resumida da Passos Mágicos para possíveis voluntários e apoiadores
            - **Visualiza e conta a história** da Passos Mágicos, destacando seus impactos de forma visual e instigante.
            
            Espero que gostem deste dashboard do Streamlit e que o mesmo possa gerar insights relevantes para a compreensão da grandeza 
            da Passos Mágicos para com a comunidade de Embu-Guaçu.
            
            Sinta-se livre para explorar este ambiente! :computer:
            ''')



