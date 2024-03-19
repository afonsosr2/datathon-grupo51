import streamlit as st

###### Páginal de Referências do Streamlit ######
st.set_page_config(layout= 'wide')

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

st.header(":books: Referências")

st.markdown('''<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}</style>''', 
unsafe_allow_html=True)

st.markdown('''
            - PANDAS. Documentação da biblioteca Pandas [Internet]. [acessado 2023 Jan].  
             Disponível em: https://pandas.pydata.org/docs/reference/
            - STREAMLIT. Documentação da biblioteca Streamlit [Internet]. [acessado 2023 Jan].  
            Disponível em: https://docs.streamlit.io/
            - PLOTLY. Documentação da biblioteca Plotly [Internet]. [acessado 2023 Jan].  
            Disponível em: https://plotly.com/python/
            - JOEL, Grus. Data Science do Zero: Noções Fundamentais com Python [Livro físico]
            - KNAFLIC, Cole Nussbaumer. Storytelling com dados: uma guia sobre visualização de dados para profissionais de negócio [Livro físico]
            - REF_1, Desc Ref. [acessado 2023 Mar].  
            Disponível em: link_ref
            - REF_2, Desc Ref. [acessado 2023 Mar].  
            Disponível em: link_ref
            - REF_3, Desc Ref. [acessado 2023 Mar].  
            Disponível em: link_ref             
            ''')
