import streamlit as st
from app_graficos import fig_1,fig_2,fig_3,fig_4,fig_5, df_medias,df_medias_1,df_virada


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
            st.image("/content/Ong-Passos-Magicos.jpeg",width= 250,use_column_width=True)
            
    st.markdown("""A Passos Mágicos baseia-se na meritocracia, por isso engajamos nossas crianças para que acreditem que estudar é bom e pode transformar a vida delas.
            Avaliamos a participação, desempenho e presença para decidir quem participará das atividades de finais de semana e quem pode concorrer a bolsas de estudos na escola particular sendo apadrinhado por uma pessoa que se dispõe a financiar seu estudo. 
            As aulas são dadas fora do horário de aula escolar em locais fixos cedidos pela comunidade (em 4 núcleos diferentes), ou seja, 
            não temos uma sede construída, pois acreditamos que todo o valor de arrecadação do projeto deve ir para a melhora da qualidade de entrega e investimento em novas oportunidades para as crianças.""")
    st.image("images/metodologia.jpg")



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

        st.plotly_chart(fig_1, use_container_width=True, sharing="streamlit")
        st.markdown("fonte: PEDE 2022-Passos Magicos")



    st.markdown("### Dimenssão de indicadores INDE")


    st.markdown("""O INDE (ÍNdice de deenvolvimento educacional ),como medida do presente processo avaliativo,  é composto por uma dimenssão acadêmica, uma dimenssão psicossocial e uma dimenssão psicopedagógica.    
                  Essas dimensões são observadas por meio de resultado de 7 indicadores (IAN,IDA,IEG,IAA,IPS,IPP e IPV) que aglutinados por ponderação formam o índice sintetico INDE.""")
    
    st.image("images/indicadores-INDE.png",caption="Fonte:PEDE 2022 Passos Mágicos")


    
    
    st.dataframe(df_medias_1)


          
    st.plotly_chart(fig_2, use_container_width=False, sharing="streamlit")
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
            st.plotly_chart(fig_3, use_container_width=False, sharing="streamlit")

    st.markdown("""### Ponto de Virada """)

    st.markdown(""" É um  indicador é um indicador psicopedagógico, os resultados são obtidos por meio de avaliação de professores e psicopedagogos da associação.
Ponto de virada é atingido quando o o estudante demostra de forma ativa por meio da trajetória dentro da associação, do valor de saber e a importancia de aprender.
No Ano de 2022 13% dos alunos atingiram o ponto de Virada.""")

    st.markdown("")
 
    st.dataframe(df_virada)

  
    st.plotly_chart(fig_4, use_container_width=False, sharing="streamlit", theme="streamlit")


    
    st.markdown("""### Percentual de Alunos na universidade na Ong Passos Mágicos""")

    st.markdown("""Podemos notar que houve um crescimento de quase 3.3 pontos percentuais nos total de alunos estudando em uma universidade.""")

    st.plotly_chart(fig_5, use_container_width=False, sharing="streamlit", theme="streamlit")


  
