 

import streamlit as st


colunas_1 = st.columns(2, gap="large")
with colunas_1 [0]:

            st.markdown("""A Associação Passos Mágicos tem uma trajetória de 31 anos de atuação, 
                trabalhando na transformação da vida de crianças e jovens baixa renda os levando a melhores oportunidades de vida.
                A transformação, idealizada por Michelle Flues e Dimetri Ivanoff, começou em 1992, 
                atuando dentro de orfanatos, no município de Embu-Guaçu.""")

            st.markdown("""Em 2016, depois de anos de atuação, decidem ampliar o programa para que mais jovens tivessem acesso a essa fórmula mágica para transformação que inclui: 
                educação de qualidade, auxílio psicológico/psicopedagógico, ampliação de sua visão de mundo e protagonismo. 
                Passaram então a atuar como um projeto social e educacional, criando assim a Associação Passos Mágicos.""")

with colunas_1 [1]:
            st.image("images/Ong-Passos-Magicos.jpeg",width= 250,use_column_width=True)




tab_titles_2 = ["Como funciona a Passos","Alunos impactados pela Passos" "Indicadores"]
tabs_2 = st.tabs(tab_titles_2)


with tabs_2[0]: 
    st.markdown("")
    cols_destaque_passos = st.columns(2)
    with cols_destaque_passos[0]:
        st.markdown(""" A Passos Mágicos baseia-se na meritocracia, por isso engajamos nossas crianças para que acreditem que estudar é bom e pode transformar a vida delas.
            Avaliamos a participação, desempenho e presença para decidir quem participará das atividades de finais de semana e quem pode concorrer a bolsas de estudos na escola particular sendo apadrinhado 
            por uma pessoa que se dispõe a financiar seu estudo. 
            As aulas são dadas fora do horário de aula escolar em locais fixos cedidos pela comunidade (em 4 núcleos diferentes), ou seja, 
            não temos uma sede construída, 
            pois acreditamos que todo o valor de arrecadação do projeto deve ir para a melhora da qualidade de entrega e investimento em novas oportunidades para as crianças. """, )



    with cols_destaque_passos[1]:
            st.markdown(""" A Passos conta  com um corpo docente composto por 7 professores, uma psicóloga e uma psicopedagoga, 
            todos eles contratados e remunerados para garantir a qualidade do ensino. 
            A ong conta com inumeras atividades de final de semana podem ser culturais como visita a museus e teatros ou educacionais como oficinas,
             cursos e workshops, todas realizadas com a ajuda de voluntários que acompanham e participam com nossas crianças. """)



    colunas_3 = st.columns(2)
    with colunas_3 [0]:
        
            st.markdown("<p class='font-text-destaques'> Alunos participantes do Processo de Aceleração </p>", unsafe_allow_html=True)
    
            
    with colunas_3 [1]:
            st.image("images/pac-passos.png",width= 400)





  
