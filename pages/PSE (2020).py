import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pywaffle import Waffle
from plotly import express as px
from plotly import graph_objs as go
from plotly.subplots import make_subplots
from PIL import Image


###### Configuração Inicial ######
@st.cache_data
def config_inicial():
    df = pd.read_excel("dados/PSE2020_domicílios.xlsx", sheet_name = "PSE2020_domicílios")
    # Retirando as colunas do ano (todos são 2020) e entrevistador(a)
    cols_a_retirar = ["V100_first", "V101_first", "V106_first", "filter_$"]
    dados = df.drop(columns=cols_a_retirar)
    return dados

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

#### Página dos modelos de previsão do petróleo Brent ####
# Função que roda as configurações iniciais
# Leitura dos dados do IPEA, treino e retreino de modelos 
dados = config_inicial()

cols_intro = st.columns(2)
with cols_intro[0]:
    st.markdown("## :mag_right: Pesquisa Sócio Econômica (2020)")
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
with tabs[0]: # TAB de Contexto
    st.markdown("")
    cols_destaque_contexto = st.columns(2)
    with cols_destaque_contexto[0]:
        st.markdown("<p class='font-text-destaques'>Principais contextos Socioeconômicos de Embu-Guaçu</p>", unsafe_allow_html=True)
    with cols_destaque_contexto[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> O <font color='red'><b> IDHM</b></font> em Embu-Guaçu atingiu, em 2010, o patamar de <b>0,749 (alto)</b> 
                             correspondente aos países em desenvolvimento. Parte do avanço é creditado ao indicador <b>Educação</b>, 
                             partindo do muito baixo em 1990 ao nível alto em 2010.
                        </li>
                    <br>
                        <li> Em relação à <font color='red'><b>condição de vida</b></font>, Embu-Guaçu possui indicadores de pobreza
                             e vulnerabilidade abaixo do Brasil (<b>36,99%</b> contra <b>54,38%</b>), porém extremamente 
                             elevado em relação à <b>RMSP</b> e o <b>Estado de São Paulo</b> (<b>22,8%</b> e <b>21,95%</b>). 
                             Praticamente <b>60%</b> das crianças em Embu-Guaçu estão nessas condições adversas.
                        </li>
                    <br>
                        <li> Em relação à <font color='red'><b>renda</b></font>, o salário médio dos trabalhadores formais é de <b>2,5 
                             salários mínimos</b>, com apenas <b>13,3%</b> da população ocupada, uma das menores taxas
                             entre os municípios do Estado de São Paulo (543º lugar dentre 645 municípios) (IGBE, 2021). 
                        </li>
                    </ul>''', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('#')

    cols_local = st.columns(2)
    with cols_local[0]:
        st.image("images/contexto-img01-localizacao_embu-guacu.png")
    with cols_local[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> O município de <font color='red'><b> Embu-Guaçu</b></font>, está localizado na porção Sudoeste da Região
                             Metropolitanda de São Paulo (RMSP)
                        </li>
                    <br>
                        <li> A <font color='red'><b>população no censo de 2022</b></font> foi de <b>66.970 pessoas</b>, ocupando a 489ª posição no Brasil, com a densidade
                             demográfica de aproximadamente <b>430 habitantes</b> por quilômetro quadrado.
                        </li>
                    <br>
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
                    <br>
                        <li> Considerando que <font color='red'><b>60% da parcela da população</b></font> vive em condição de vulnerabilidade,
                             pobreza ou extrema pobreza, estamos falando de cerca de <b>8.700 crianças e jovens</b>.
                        </li>
                    <br>
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
                    <br><br>
                        <li> Entre os <font color='red'><b>indivíduos em idade escolar</b></font>, quanto à raça declarada, estão distribuídos
                            <b>54,4%</b> de Brancos, <b>44,8%</b> de Pretos e Pardos, <b>0,7%</b> de Amarelos e <b>0,1%</b> de Indígenas.
                        </li>
                    <br>                    
                        <li> A <font color='red'><b>escolaridade do município</b></font> é bem desafiante, sendo que apenas <b>60%</b> dos maiores
                            de 18 anos concluíram o Ensino Fundamental e <b>40%</b> da mesma faixa etária concluíram o Ensino Médio.
                        </li>
                    </ul>''', unsafe_allow_html=True)
        
    st.markdown('#')
    st.markdown('#') 
with tabs[1]: # TAB de Demografia
    st.markdown("")
    cols_destaque_demografia = st.columns(2)
    with cols_destaque_demografia[0]:
        st.markdown("<p class='font-text-destaques'><br>Principais destaques sobre Demografia</p>", unsafe_allow_html=True)
    with cols_destaque_demografia[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> A <font color='red'><b>PSE 2020</b></font> trouxe dados de <b>784</b> alunos da <b>Associação Passos Mágicos</b>.
                             Considerando a população de <b>68.053</b> habitantes em 2020 (SEADE, 2020), a pesquisa representa <b>4% da 
                             população</b> do município.
                        </li>
                    <br>
                        <li> <font color='red'><b>Na faixa entre 5 a 19 anos de idade</b></font> na pesquisa temos <b>1.137</b> crianças e
                             jovens. Considerando os dados apenas nos domicílios entrevistados, <b>353</b> jovens ainda não foram atendidos
                             pela APM. 
                        </li>
                    <br>
                        <li> Extrapolando a população dessa faixa etária para <b>42,5%</b> e uma população de <b>68.053</b> habitantes,
                             <b>28.923</b> seriam de crianças e jovens. <font color='red'><b>Aproximadamente 17.350 crianças e jovens</b></font>
                             como público potencial da APM (<b>60%</b> da população socialmente vulnerável).
                        </li>
                    <br>
                        <li> Foi possível observar uma <font color='red'><b>preponderância do gênero feminino</b></font> em diversas 
                             categorias, bem como de Pardos e Pretos. Em domicílios monoparentais, mais de <b>90%</b> dos casos são de 
                             mulheres responsáveis, com <b>60%</b> de Pretas ou Pardas e <b>71%</b> do total
                             de domicílios monoparentais com 1 a 2 filhos e/ou enteados.
                        </li>
                    </ul>''', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('#')

    st.markdown('## Indivíduos')
    
    cols_pop_sexo = st.columns(2)
    with cols_pop_sexo[0]:
        mulheres = dados.D1702_sum.sum()
        homens = dados.D1701_sum.sum()
        total = mulheres + homens
        pct_mulheres = (100 *mulheres/total)
        pct_homens = (100 * homens/total)

        data = {'Mulheres': pct_mulheres, 'Homens': pct_homens}
        fig = plt.figure(FigureClass=Waffle, rows=5, values=data, colors=["#f58334", "#0367b0"],
                        title={'label': 'População total por sexo', 'loc': 'left', 'size':10},
                        labels=[f"{k} ({v:.1f}%)" for k, v in data.items()],
                        legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0},
                        starting_location='NW', block_arranging_style='snake')
        st.pyplot(fig)
    with cols_pop_sexo[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> O recorte da pesquisa engloba <font color='red'><b>4% do total da população</b></font> de Embu-Guaçu, uma amostra considerável.
                        </li>
                    <br>
                        <li> Da população pesquisada, <font color='red'><b>1.452 são mulheres</b></font>, representando aproximadamente <b>54.3%</b>
                             do total, e <font color='red'><b>1.221 moradores são homens</b></font>, representando <b>45.7%</b> do total.
                        </li>
                    <br>
                        <li> A <font color='red'><b>proporção entre homens e mulheres</b></font> em Embu-Guaçu em 2020 é de <b>50,5%</b> de mulheres
                     e <b>49,5%</b> de homens. O ligeiro afastamento em relação a pesquisa pode ser explicado pelo recorte socioeconômico.  
                        </li>
                    </ul>''', unsafe_allow_html=True)

    st.markdown('#')
    st.markdown('#')    

    cols_pop_cor_raca = st.columns(2)
    with cols_pop_cor_raca[0]:
        st.markdown('''<ul class="font-text-destaques">
                    <br><br>
                        <li> Com relação à <font color='red'><b>distribuição da população por raça e cor</b></font>, as proporções da 
                             população total do Brasil se assemelham ao de Embu-Guaçu, que podemos observar na imagem ao lado
                        </li>
                    <br>
                        <li> Os declarados <font color='red'><b>Pretos e Pardos</b></font> somam cerca de <b>54,8%</b>, próximo dos <b>54%</b> do Brasil e
                             os declarados <font color='red'><b>Brancos, Amarelos e Indígenas</b></font> juntos somam <b>45,2%</b> próximo dos 
                             <b>46%</b> do Brasil.
                        </li>
                    </ul>''', unsafe_allow_html=True)
    with cols_pop_cor_raca[1]:
        pop_cor_raca = dados.copy()
        pop_cor_raca["pop"] =  dados["D1701_sum"] + dados["D1702_sum"]
        pop_cor_raca = pop_cor_raca.groupby("V109_first")[["pop"]].sum().reset_index()
        pop_cor_raca.columns = ["cor_raca", "qtd"]

        fig = px.bar(pop_cor_raca, x="qtd", y="cor_raca", color = "cor_raca", text_auto=True,
                    color_discrete_sequence=["#fec52b","#00b050","#f58334", "#ed3237", "#0367b0"],
                    category_orders={'cor_raca':["Parda", "Preta", "Branca", "Amarela","Indígena"]})

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=350, font_family = 'Open Sans', font_color= "black", 
                          title_font_color= "black", title_font_size=24, title_text='População por Cor ou Raça' + 
                          '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', xaxis_title='', yaxis_title='',
                          xaxis_tickfont_size=14, yaxis_tickfont_size=14, xaxis_range = [0,1350], 
                          plot_bgcolor= "#f8f9fa", showlegend=False)

        fig.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>%{x}</b>', cliponaxis=False)
 
        st.plotly_chart(fig)

    st.markdown('## Domicílios')

    cols_dom_sexo = st.columns(2)
    with cols_dom_sexo[0]:
        domicilio_sexo_resp = dados.V107_first.value_counts()
        domicilio_sexo_resp.index = ["Mulheres", "Homens"]
        total = domicilio_sexo_resp.sum()
        pct_mulheres = (100 * domicilio_sexo_resp.loc["Mulheres"]/total)
        pct_homens = (100 * domicilio_sexo_resp.loc["Homens"]/total)

        data = {'Mulheres': pct_mulheres, 'Homens': pct_homens}
        fig = plt.figure(FigureClass=Waffle, rows=5, values=data, colors=["#f58334", "#0367b0"],
                title={'label': 'Total de domicílios por sexo do responsável', 'loc': 'left', 'size':10},
                labels=[f"{k} ({v:.1f}%)" for k, v in data.items()],
                legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0},
                starting_location='NW', block_arranging_style='snake')
        
        st.pyplot(fig)
    with cols_dom_sexo[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> Embu-Guaçu tem um total projetado de <b>22.112</b> domicílios em 2020 (SEADE, 2020). Este recorte da pesquisa 
                             engloba <font color='red'><b>3% do total de domicílios</b></font> do município.
                        </li>
                    <br>
                        <li> Dos responsáveis pelo domicílio, <font color='red'><b>354 são mulheres</b></font>, representando aproximadamente <b>54.1%</b>
                             do total, e <font color='red'><b>300 moradores são homens</b></font>, representando <b>45.9%</b> do total.
                        </li>
                    <br>
                        <li> A <font color='red'><b>vantagem numérica dos domicílios chefiados por mulheres</b></font> foi destacado nos dados 
                             demográficos dos domicílios entrevistados de Embu-Guaçu, principalmente pelos arranjos familiares.
                        </li>
                    </ul>''', unsafe_allow_html=True)

    st.markdown('#')
    st.markdown('#')

    cols_dom_cor_raca = st.columns(2)
    with cols_dom_cor_raca[0]:
        st.markdown('''<ul class="font-text-destaques">
                    <br>
                        <li> A <font color='red'><b>distribuição por cor e raça dos responsáveis dos domicílios</b></font>, tem relação
                             direta com os dados da população da amostra e, consequentemente, com a proporção da população total do Brasil.
                             Isso evidencia uma homogeneidade dos domicílios quanto a característica dos indivíduos, em que a frequência de
                             domicílios heterogêneos são pouco significativos.
                        </li>
                    <br>
                        <li> Os responsáveis declarados <font color='red'><b>Pretos e Pardos</b></font> somam cerca de <b>54,9%</b>, próximo dos <b>54%</b> do Brasil e
                             os declarados <font color='red'><b>Brancos, Amarelos e Indígenas</b></font> juntos somam <b>45,1%</b> próximo dos 
                             <b>46%</b> do Brasil.
                        </li>
                    </ul>''', unsafe_allow_html=True)
    with cols_dom_cor_raca[1]:
        pop_cor_raca = dados.V109_first.value_counts().to_frame().reset_index()
        pop_cor_raca.columns = ["cor_raca", "qtd"]

        fig = px.bar(pop_cor_raca, x="qtd", y="cor_raca", color = "cor_raca", text_auto=True,
                    color_discrete_sequence=["#fec52b","#00b050","#f58334", "#ed3237", "#0367b0"],
                    category_orders={'cor_raca':["Parda", "Preta", "Branca", "Amarela","Indígena"]})

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=350, font_family = 'Open Sans', font_size=15, font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='População por Cor ou Raça do responsável' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', xaxis_title='', yaxis_title='',
                        xaxis_tickfont_size=14, yaxis_tickfont_size=14, xaxis_range = [0,350], 
                        plot_bgcolor= "#f8f9fa", showlegend=False)

        fig.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>%{x}</b>', cliponaxis=False)
        st.plotly_chart(fig)

    cols_dom_n_moradores = st.columns(2)
    with cols_dom_n_moradores[0]:
        domicilio_n_moradores = dados.V104_max.value_counts().to_frame()
        domicilio_n_moradores.loc["1"], domicilio_n_moradores.loc["9"] = 0, 0
        domicilio_n_moradores = domicilio_n_moradores.reset_index()
        domicilio_n_moradores.columns = ["Nº de Moradores", "Nº de Domicílios"]

        fig = px.histogram(domicilio_n_moradores, x="Nº de Moradores", y="Nº de Domicílios", 
                        text_auto=True, color_discrete_sequence=["#68a4d0"], nbins= 10)

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=500, font_family = 'Open Sans', font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Distribuição dos domicílios por nº de moradores' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', 
                        xaxis_title='Nº de Moradores', yaxis_title='Nº de Domicílios',
                        xaxis_tickfont_size=14, yaxis_tickfont_size=14, yaxis_range = [0,270], 
                        plot_bgcolor= "#f8f9fa", showlegend=False, bargap=0.1)

        fig.update_xaxes(tickmode='array', tickvals=np.arange(1,11))
        fig.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>%{y}</b>', cliponaxis=False)
        st.plotly_chart(fig)
    with cols_dom_n_moradores[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> Segundo as projeções da Fundação SEADE, no município em 2020, os <font color='red'><b>68.503 habitantes se dividem em 22.112
                             domicílios</b></font>, o que resultaria numa média de pouco mais de <b>3</b> moradores por domicílio.
                        </li>
                    <br>
                        <li> Observando o gráfico ao lado, com a distribuição dos domicílios na pesquisa, podemos notar <font color='red'><b>uma concentração
                             maior dos domicílios entrevistados com 4 moradores</b></font> tanto na média, quanto na moda e mediana.
                        </li>
                    <br>
                        <li> Extrapolando para a faixa <font color='red'><b>entre 3 e 5 moradores, são somados 538 domicílios,</b></font> ou seja, mais de <b>82%</b> do total
                             de domicílios entrevistados. É importante focar em moradias com um número <b>acima de 5 filhos</b> verificando o impacto
                             de acordo com a condição de moradia desses locais.
                        </li>
                    </ul>''', unsafe_allow_html=True)

    st.markdown('#')
    st.markdown('#')

    cols_dom_arranjo = st.columns(2)
    with cols_dom_arranjo[0]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> Podemos notar no gráfico ao lado, que o <font color='red'><b>arranjo familiar de união e casamento entre indivíduos de sexo diferente</b></font>,
                             é amplamente representado com mais de <b>75%</b> dos arranjos familiares. Outro fator relevantes é de que mais de <b>23%</b> dos 
                             arranjos familiares são <b>monoparentais</b> (apenas mulher ou homem), que é <b>muito</b> superior à média nacional de <b>13%</b>.
                        </li>
                    <br>
                        <li> Dos <font color='red'><b>arranjos monoparentais, mais de 90% são de mulheres</b></font>, acima dos <b>83,3%</b> de Embu-Guaçu dada pelo Censo do IBGE em 2010.
                             Dos <font color='red'><b>arranjos de união ou casamento, em 38,6% dos casos a mulher é a responsável pelo domicílio</b></font>.
                        </li>
                    <br>
                        <li> Dos <font color='red'><b>138 domicílios monoparentais chefiados por mulheres, a proporção de Pardas e Pretas representam 61,6% do total</b></font>,
                             e temos uma média de <b>41</b> anos de idade para a responsável.
                        </li>
                    </ul>''', unsafe_allow_html=True)
    with cols_dom_arranjo[1]:
        domicilio_arranjo_familiar = dados.D1606D.value_counts().to_frame().reset_index()
        domicilio_arranjo_familiar.columns = ["arranjo", "qtd"]

        fig = px.bar(domicilio_arranjo_familiar, x="qtd", y="arranjo", color = "arranjo", text_auto=True,
                    color_discrete_sequence=["#fec52b","#00b050", "#ed3237", "#0367b0"])

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=500, font_family = 'Open Sans', font_size=15, font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Distribuição dos domicílios pelos arranjos familiares' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', xaxis_title='', yaxis_title='',
                        xaxis_tickfont_size=14, yaxis_tickfont_size=14, xaxis_range = [0,550], 
                        plot_bgcolor= "#f8f9fa", showlegend=False)

        fig.update_yaxes(tickmode='array', tickvals=np.arange(0,4), 
                         ticktext = ["União ou casamento<br>(indivíduos de sexo<br>diferente)", "Monoparental", "Consanguíneo",
                                     "União ou casamento<br>(indivíduos do<br>mesmo sexo)"])
        fig.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>%{x}</b>', cliponaxis=False)
        st.plotly_chart(fig)
with tabs[2]: # TAB dos Alunos Passos Mágicos
    cols_destaque_passos_magicos = st.columns(2)
    with cols_destaque_passos_magicos[0]:
        st.markdown("<p class='font-text-destaques'><br>Principais destaques sobre os<br>Alunos Passos Mágicos</p>", unsafe_allow_html=True)
    with cols_destaque_passos_magicos[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> A <font color='red'><b>PSE 2020</b></font> trouxe dados de <b>784</b> alunos da <b>Associação Passos Mágicos</b> 
                             ativos. Esse número é estatisticamente censitário do universos de alunos atendidos, ou seja, é uma contagem completa 
                             dos <b>Alunos Passos Mágicos</b>.
                        </li>
                        <br>
                        <li> A <font color='red'><b>distribuição geral dos indivíduos e domicílios</b></font>, é bastante homogênea às 
                             características dos <b>Alunos Passos Mágicos</b>, especialmente quanto a cor ou raça e ao sexo. Conforme outros 
                             recortes, a uma <font color='red'><b>prevalência feminina e parda e preta</b></font>, em pequena vantagem acima dos demais. 
                        </li>
                        <br>
                        <li> Quanto à idade, a <font color='red'><b>concentração dos Alunos Passos Mágicos se encontra nos ciclos correspondentes
                             ao EFAF (Ensino Fundamental Anos Finais)</b></font>. O que pode levantar a hipótese do porquê baseado na 
                             pirâmide etária dos habitantes de Embu-Guaçu.
                        </li>
                        <br>
                        <li> Abaixo, trazemos algumas <font color='red'><b>características demográficas dos Alunos Passos Mágicos</b></font>, 
                            como sexo biológico, etnia, condição no domicílio e distribuição por núcleo da <b>Associação Passos Mágicos</b>.
                        </li>
                    </ul>''', unsafe_allow_html=True)

    st.markdown("---") 
    st.markdown('## Alunos Passos Mágicos')

    cols_alunos_totais = st.columns(2)
    with cols_alunos_totais[0]:
        total_individuos = dados.V104_max.sum()
        total_alunos_ativos = dados.D201_sum.sum() - 1  # Um aluno inativo na lista
        total_demais_indivíduos = total_individuos - total_alunos_ativos

        labels = ["Alunos Passos Mágicos", "Demais Indivíduos"]
        values = [total_alunos_ativos, total_demais_indivíduos]

        fig = go.Figure(
            data=[
                go.Pie(labels = labels, values = values, textinfo='label+percent',
                    marker_colors=["#0367b0","#68a4d0"], rotation = 90 )
                ]
            )

        # Ajustando o layout do gráfico
        fig.update_layout(width=500, height=500, font_family = 'Open Sans', font_color= "white", title_font_color= "black", 
                        title_font_size=24, title_text='Proporção dos Alunos Passos Mágicos<br>Ativos na amostra da pesquisa' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', showlegend=False)

        fig.update_traces(textfont_size=12, texttemplate='<b>%{label}<br>%{value} (%{percent})<br></b>')

        st.plotly_chart(fig)
    with cols_alunos_totais[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <br><br><br><br><br>                    
                        <li> Em relação a amostra da população entrevistada pela PSE 2020, o <font color='red'><b> total de 783 indivíduos</b></font> 
                             representam <b>29,3%</b> dos moradores pesquisados, como podemos notar no gráfico ao lado.
                        </li>
                        <br>
                        <li> Os demais moradores, responsáveis, pessoas da família e com alguma relação com o aluno, somam <font color='red'><b>1.890 pessoas,
                             o equivalente a 70,7% da população total</b></font> pesquisada.
                        </li>
                    </ul>''', unsafe_allow_html=True)
        
    cols_aluno_sexo = st.columns(2)
    with cols_aluno_sexo[0]:
        st.markdown('''<ul class="font-text-destaques">
                        <br><br>
                        <li> Da população pesquisada, foram registradas <font color='red'><b>783 crianças e jovens</b></font>. Desses,
                             <b>442</b> estudantes, ou <b>56,4%</b>, são meninas e <b>341</b>, ou <b>43,6%</b> são meninos.
                        </li>
                        <br>
                        <li> Mais detalhes sobre o perfil dos alunos veremos logo abaixo.  
                        </li>
                    </ul>''', unsafe_allow_html=True)        
    with cols_aluno_sexo[1]:
        pct_meninas = (100 * 442/783)
        pct_meninos = (100 * 341/783)
        data = {'Meninas': pct_meninas, 'Meninos': pct_meninos}
        fig = plt.figure(FigureClass=Waffle, rows=5, values=data, colors=["#f58334", "#0367b0"],
                        title={'label': 'Total de Alunos Passos Mágicos por sexo', 'loc': 'left', 'size':14, 'weight':'bold', 'family': 'Open Sans'},
                        labels=[f"{k} ({v:.1f}%)" for k, v in data.items()],
                        legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0},
                        starting_location='NW', block_arranging_style='snake')
        st.pyplot(fig)

    st.markdown('#')
    st.markdown('## Perfil dos Alunos Passos Mágicos')
    st.markdown('#')
  
    cols_aluno_cor_raca = st.columns(2)
    with cols_aluno_cor_raca[0]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> Com relação à <font color='red'><b>distribuição dos alunos por raça e cor</b></font>, temos bastante similariedades
                             com a população da PSE 2020. Esse dado reforça a homogeneidade observada em toda pesquisa da composição dos arranjos
                             familiares neste quesito
                        </li>
                        <br>
                        <li> Os declarados <font color='red'><b>Brancos, Amarelos e Indígenas</b></font> somam cerca de <b>47,5%</b>, 
                             próximo dos <b>46%</b> do Brasil e os declarados <font color='red'><b>Pardos e Pretos</b></font> juntos 
                             somam <b>52,5%</b> próximo dos <b>54%</b> do Brasil.
                        </li>
                    </ul>''', unsafe_allow_html=True)
    with cols_aluno_cor_raca[1]:
        aluno_cor_raca = pd.DataFrame({
            "cor_raca": ["Branca", "Parda", "Preta", "Amarela", "Indígena","Ignorada"],
            "qtd": [368, 358, 51, 4, 1, 1]
        })

        fig = px.bar(aluno_cor_raca, x="qtd", y="cor_raca", color = "cor_raca", text_auto=True,
                    color_discrete_sequence=["#f58334", "#fec52b","#00b050", "#ed3237", "#0367b0", "#cccccc"],
                    category_orders={'cor_raca':["Branca", "Parda", "Preta", "Amarela","Indígena", "Ignorada"]})

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=300, font_family = 'Open Sans', font_size=15, font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='População por Cor ou Raça' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', xaxis_title='', yaxis_title='',
                        xaxis_tickfont_size=14, yaxis_tickfont_size=14, xaxis_range = [0,400], 
                        plot_bgcolor= "#f8f9fa", showlegend=False)

        fig.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>%{x}</b>', cliponaxis=False)
 
        st.plotly_chart(fig)

    st.markdown('#')
    st.markdown('#')  
   
    cols_aluno_condicao_dom = st.columns(2)
    with cols_aluno_condicao_dom[0]:
        condicao_domicilio = dados.loc[dados.index.repeat(dados.D201_sum)].V201_first.value_counts()
        condicao_domicilio = condicao_domicilio.to_frame().reset_index()
        condicao_domicilio.columns = ["condicao", "qtd"]
        condicao_domicilio = condicao_domicilio.head(4) # retirando o aluno desistente

        condicao = {'Pai ou mãe de aluno(a) ativo (atualmente cursando)': "Filho(a) do responsável e/ou do cônjuge",
                    'Responsável por aluno(a) ativo (atualmente cursando)': "Outra relação com o responsável",
                    'Avô(ó) de aluno(a) ativo (atualmente cursando)': "Neto(a) do responsável",
                    'Sem relação': "Sem relação com o responsável"}

        condicao_domicilio.condicao = condicao_domicilio.condicao.map(condicao)

        fig = px.bar(condicao_domicilio, x="qtd", y="condicao", color = "condicao", text_auto=True,
                    color_discrete_sequence=["#fec52b","#00b050", "#ed3237", "#0367b0"])

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=400, font_family = 'Open Sans', font_size=15, font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Distribuição dos alunos por sua condição no domicílio' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', xaxis_title='', yaxis_title='',
                        xaxis_tickfont_size=14, yaxis_tickfont_size=14, xaxis_range = [0,850], 
                        plot_bgcolor= "#f8f9fa", showlegend=False, yaxis_categoryorder='total descending')

        fig.update_yaxes(tickmode='array', tickvals=np.arange(0,4), ticktext = ["Filho(a) do responsável<br>e/ou do cônjuge",
                                                                        "Outra relação com<br>o responsável",
                                                                        "Neto(a) do<br>responsável",
                                                                        "Sem relação com<br>o responsável"])

        fig.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>%{x}</b>', cliponaxis=False)
        
        st.plotly_chart(fig)
    with cols_aluno_condicao_dom[1]:        
        st.markdown('''<ul class="font-text-destaques">
                    <br><br>
                        <li> Investigando a condição das crianças e jovens, considerando a relação destas com o indivíduo responsável 
                             pelo município, notamos que em <font color='red'><b>aproximadamente 94% dos casos os Alunos Passos Mágicos
                             possui em seu arranjo familiar a presença da figura paterna e/ou materna</b></font>.                          
                        </li>
                        <br>
                        <li> Isso demonstra que <font color='red'><b>o vínculo afetivo da criança ou jovem na condição de vida auxilia na capacidade de 
                             atuação no processo educacional de forma plena</b></font>. Essa carcaterística suporta o <b>planejamento e direcionamento
                             das ações de suporte psicológico e psicopedagágico</b>, individual e familiar, que são rotina da Associação 
                             Passos Mágicos.
                        </li>
                    </ul>''', unsafe_allow_html=True)

    st.markdown('#')
    st.markdown('#')

    cols_alunos_idade = st.columns(2)
    with cols_alunos_idade[0]:
        st.markdown('''<ul class="font-text-destaques">
                        <br><br><br>
                        <li> A <font color='red'><b>distribuição por idade dos Alunos Passos Mágicos</b></font>, mostra uma alta 
                             concentração de alunos na etapa do <b>EFAF (sexto ao nono ano do ensino regular)</b>. Essa etapa, idealmente
                             com crianças na faixa entre <b>10 a 14 anos</b>, soma <b>466 alunos</b>, ou <b>59,5%</b> do total.
                        </li>
                        <br>
                        <li> Nas faixas equivalentes a <font color='red'><b>EFAI (7 a 9 anos) tem-se 118 crianças</b></font>, <b>15%</b> do total de alunos, equanto os jovens
                             que frequentam o <font color='red'><b>Ensino Médio (15 a 17 anos) somam 171 alunos</b></font>, o equivalente a <b>21,8%</b> do total. Por fim,
                             os <font color='red'><b>alunos em idade universitária, 18 ou mais, somam 28 jovens (3,6% do total)</b></font>.
                        </li>
                    </ul>''', unsafe_allow_html=True)
    with cols_alunos_idade[1]:
        aluno_idade = pd.DataFrame({
            "Idade": [7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
            "Nº de Alunos": [11, 45, 62, 107, 107, 84, 84, 84, 52, 62, 57, 20, 6, 1, 1]
        })

        fig = px.histogram(aluno_idade, x="Idade", y="Nº de Alunos", text_auto=True, color_discrete_sequence=["#68a4d0"], nbins= 8)

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=500, font_family = 'Open Sans', font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Distribuição dos alunos por idade' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', 
                        xaxis_title='Idade', yaxis_title='Nº de Alunos',
                        xaxis_tickfont_size=14, yaxis_tickfont_size=14, yaxis_range = [0,240], 
                        plot_bgcolor= "#f8f9fa", showlegend=False, bargap=0.1)

        fig.update_xaxes(tickmode='array', tickvals=np.arange(6.5,22.5,2), ticktext = ["6 - 7", "8 - 9", "10 - 11", "12 - 13", 
                                                                                    "14 - 15", "16 - 17", "18 - 19", "20 - 21"])
        fig.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>%{y}</b>', cliponaxis=False)
        st.plotly_chart(fig)

    cols_dom_n_alunos = st.columns(2)
    with cols_dom_n_alunos[0]:
        domicilio_n_alunos = dados.D201_sum.value_counts().to_frame().reset_index()
        domicilio_n_alunos.columns = ["Nº de Alunos Passos Mágicos", "Nº de Domicílios"]

        fig = px.histogram(domicilio_n_alunos, x="Nº de Alunos Passos Mágicos", y="Nº de Domicílios", 
                        text_auto=True, color_discrete_sequence=["#68a4d0"], nbins= 5)

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=400, font_family = 'Open Sans', font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Distribuição dos domicílios por nº de alunos' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', 
                        xaxis_title='Nº de Alunos Passos Mágicos', yaxis_title='Nº de Domicílios',
                        xaxis_tickfont_size=14, yaxis_tickfont_size=14, yaxis_range = [0,580], 
                        plot_bgcolor= "#f8f9fa", showlegend=False, bargap=0.1)

        fig.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>%{y}</b>', cliponaxis=False)
        st.plotly_chart(fig)
    with cols_dom_n_alunos[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <br><br><br>
                        <li> Dos 654 domicílios entrevistados, com os dados dos Alunos Passos Mágicos, cerca de <font color='red'><b>530 domicílios, ou 81% dos
                             domicílios, temos apenas um Aluno Passos Mágicos</b></font>.
                        </li>
                        <br>
                        <li> <font color='red'><b>Cerca de 18%, 118 domicílios, possuimos 2 ou mais alunos</b></font>. Por fim, temos em nossa pesquisa, <font color='red'><b>6 domicílios
                             com nenhum aluno ativo</b></font>.
                        </li>
                    </ul>''', unsafe_allow_html=True)

    st.markdown('#')
    st.markdown('#')  

    cols_nucleo = st.columns([1,3,4])
    with cols_nucleo[1]:
        st.image("images/alunos-passos-magicos-img01-nucleos.png",width=400)
    with cols_nucleo[2]:
        st.markdown('''<ul class="font-text-destaques">
                        <br><br><br>
                        <li> A  <font color='red'><b> Associação Passos Mágicos possui 4 núcleos em Embu-Guaçu</b></font> sendo eles <b>Filipinho, 
                             Centro, Granjinha e Cipó</b>. Dentro desses núcleos são desenvolvidas as ações educacionais no município.
                        </li>
                        <br>
                        <li> <font color='red'><b>O maior dos núcleos de ensino da APM é o núcleo Centro</b></font>, que recebe
                             crianças e jovens de diversos bairros por ser de fácil acesso, oferencendo aulas de Português, Matemática
                             e Inglês, como os demais Núcleos de ensino.
                        </li>
                    </ul>''', unsafe_allow_html=True)

    st.markdown('#')
    st.markdown('#')

    cols_dom_arranjo = st.columns(2)
    with cols_dom_arranjo[0]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> Como falamos anteriormente, <font color='red'><b>o núcleo Centro atende mais crianças e jovens</b></font>,
                             cerca de <b>329 alunos</b>, representando por volta de <b>42%</b> dos estudantes atendidos pela Passos Mágicos. 
                        </li>
                        <br>
                        <li> Em seguida, temos <font color='red'><b>o núcleo localizado no bairo Filipinho, com 240 alunos,</b></font>
                             em que <b>135 são meninas</b> e <b>105 meninos</b>. Em Filipinho notamos a presença de um público maior de
                             alunos de raça ou cor <font color='red'><b>Parda e Preta</b></font>, com 60% do público contra 40% de Brancos. 
                        </li>
                        <br>
                        <li> Os <font color='red'><b>núcleos subsequentes, Cipó e Granjinha, juntos atendem 214 crianças e jovens</b></font>,
                             representando <b>28%</b> dos estudantes atendidos pela APM. No núcleo Granjinha, observamos um desvio levemente
                             maior entre os alunos do sexo feminino, com <b>60%</b> contra <b>40%</b> do sexo masculino.
                        </li>
                    </ul>''', unsafe_allow_html=True)
    with cols_dom_arranjo[1]:
        alunos_nucleo = dados.loc[dados.index.repeat(dados.D201_sum)].V102_first.value_counts(normalize=True)
        data = (alunos_nucleo * 100)

        fig = plt.figure(FigureClass=Waffle, rows=5, values=data, colors=["#f58334", "#fec52b", "#ed3237", "#0367b0"],
                        title={'label': 'Total de Alunos Passos Mágicos por núcleo', 'loc': 'left', 'size':14, 'weight':'bold', 'family': 'Open Sans'},
                        labels=[f"{k} ({v:.0f}%)" for k, v in data.items()],
                        legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': 2, 'framealpha': 0},
                        starting_location='NW', block_arranging_style='snake')
        st.pyplot(fig)
with tabs[3]: # TAB das Relações de Trabalho
    st.markdown("")
    cols_destaque_trabalho = st.columns(2)
    with cols_destaque_trabalho[0]:
        st.markdown("<p class='font-text-destaques'><br>Principais destaques sobre as<br>Relações de Trabalho</p>", unsafe_allow_html=True)
    with cols_destaque_trabalho[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> A <font color='red'><b>PSE 2020 trouxe dados sobre as relações de trabalho</b></font>, permitindo uma avaliação mais
                             ampla e detalhada sobre as condições de trabalho da população estudada. Houve uma <font color='red'><b>prevalência da 
                             precariedade nas relações de trabalho em relação ao gênero</b></font>, em que a mulher tem maior parcela fora da força
                             de trabalho (<b>62,8%</b>), maior população desocupada (<b>62%</b>), menor taxa de ocupação (<b>80,3%</b>), maior taxa
                             de desemprego (<b>24,5%</b>), entre outros.
                        </li>
                        <br>
                        <li> A <font color='red'><b>população em idade de trabalho</b></font> segue uma distribuição próxima a pirâmide etária da
                             população total, em que a força de trabalho (FT) está mais concentrada nas faixas entre <b>30 e 49 anos</b>, com <b>71,8%</b>
                             do total desse indicador. A <font color='red'><b>faixa etária com maior atenção da Associação Passos Mágicos é a de 15 aos 19 anos
                             </b></font>, pois inclui indivíduos ainda em formação escolar ou acadêmica. Nessa faixa, temos <b>37 indivíduos</b>, ou <b>3,6%</b> do 
                             total da FT, em que apenas <b>19</b> desses (<b>51,4%</b>) encontram-se ocupados. 
                        </li>
                        <br>
                        <li> A <font color='red'><b>população estudada não apresenta nenhum indicador de trabalho com resultados melhores que as 
                             estatísticas públicas</b></font>. A população tem hoje um baixo nível de trabalho infanto-juvenil (<b>1,6%</b>)
                             , mas altas taxas de desemprego geral e segmentado, com <font color='red'><b>destaque para o desemprego entre as mulheres
                             e uma altíssima taxa de informalidade</b></font>. Há uma prevalência de desemprego de longo prazo (<b>57,2%</b> dos 
                             desocupados) e uma taxa significativa de desemprego oculto pelo desalento.
                        </li>
                    </ul>''', unsafe_allow_html=True)

    st.markdown("---")
    
    st.markdown('## Relações de Trabalho')

    cols_conceitos = st.columns(1)
    with cols_conceitos[0]:
        with st.columns([1,3,1])[1]:
            st.markdown("<h3 style='text-align: center;'>Conceitos Analíticos das Relações de Trabalho</h3>", unsafe_allow_html=True)
            st.image("images/trabalho-img01-conceitos-analiticos.png")
    
        st.markdown(''' <p style='font-size:20px;'>
                        <b>PTo - População Total</b>: corresponde ao número total de indivíduos pesquisados
                        <br> 
                        <b>PIT - População em Idade de Trabalho</b>: corresponde ao primeiro grupo da População Total (PTo) cuja idade esteja entre
                        15 e 65 anos.
                        <br> 
                        <b>PFIT - População fora da Idade de Trabalho</b>: correponde a diferença entre a PTo e a PIT, ou seja, todos os indivíduos
                        menores de 15 anos ou maiores de 65 anos, idade não laborial.
                        <br>
                        <b>FT - Força de Trabalho</b>: corresponde aos indivíduos que se inserem no mundo do trabalho por meio de uma atividade
                        regular de trabalho remunerado, ou que estabelecem relação por meio do ato da busca por uma vaga para exercer uma atividade
                        regular de trabalho remunerado. Ou seja, parcela de individuos que está trabalhando, disponível para trabalho buscando 
                        ativamente.
                        <br>
                        <b>FFT - Fora da Força de Trabalho</b>: corresponde aos indivíduos que não trabalham ou não estão em busca de trabalho 
                        (estudantes, aposentados precoces, dependentes, ou desocupados afetados pelo desalento). É calculado por meio da diferença 
                        entre PIT e FT. 
                        <br>
                        <b>PO - População Ocupada</b>: corresponde a parcela de indivíduos da FT que estão atualmente trabalhando em trabalho
                        remunerado.
                        <br>
                        <b>PD - População Desocupada</b>: corresponde a parcela de indivíduos da FT que mesmo não exercendo atividade laborial, está
                        engajada na busca por uma nova vaga de trabalho.
                        </p> 
                        ''', unsafe_allow_html=True)
        
    cols_relacao_trabalho = st.columns(2)
    with cols_relacao_trabalho[0]:
        # PTo, PIT e PFIT
        PTo = dados.D1702_sum.sum() + dados.D1701_sum.sum()
        PIT = dados.D301_sum.sum()
        PFIT = PTo - PIT

        pct_PIT = (100 * PIT/PTo)
        pct_PFIT = (100 * PFIT/PTo)
        data = {'PIT': pct_PIT, 'PFIT': pct_PFIT}
        fig = plt.figure(FigureClass=Waffle, rows=5, values=data, colors=["#f58334", "#fec52b"],
                        title={'label': 'População Total dentro e fora da Idade de Trabalho', 'loc': 'left', 'size':14, 'weight':'bold', 'family': 'Open Sans'},
                        labels=[f"{k} ({v:.1f}%)" for k, v in data.items()],
                        legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0},
                        starting_location='NW', block_arranging_style='snake')
        st.pyplot(fig)

        # PIT, FT e FFT
        PIT = dados.D301_sum.sum()
        FT = dados.D306_sum.sum()
        FFT = dados.D305_sum.sum()

        pct_FT = (100 * FT/PIT)
        pct_FFT = (100 * FFT/PIT)
        data = {'FT': pct_FT, 'FFT': pct_FFT}
        fig2 = plt.figure(FigureClass=Waffle, rows=5, values=data, colors=["#0367b0", "#68a4d0"],
                        title={'label': 'População em Idade de Trabalho dentro e fora da Força de Trabalho', 'loc': 'left', 'size':14, 'weight':'bold', 'family': 'Open Sans'},
                        labels=[f"{k} ({v:.1f}%)" for k, v in data.items()],
                        legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0},
                        starting_location='NW', block_arranging_style='snake')
        st.pyplot(fig2)

        # FT, PO e PD
        FT = dados.D306_sum.sum()
        PO = dados.D302_sum.sum()
        PD = dados.D303_sum.sum()

        pct_PO = (100 * PO/FT)
        pct_PD = (100 * PD/FT)
        data = {'PO': pct_PO, 'PD': pct_PD}
        fig3 = plt.figure(FigureClass=Waffle, rows=5, values=data, colors=["#7030a0", "#ff3399"],
                        title={'label': 'População Ocupada e Desocupada da Força de Trabalho ', 'loc': 'left', 'size':14, 'weight':'bold', 'family': 'Open Sans'},
                        labels=[f"{k} ({v:.1f}%)" for k, v in data.items()],
                        legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0},
                        starting_location='NW', block_arranging_style='snake')
        st.pyplot(fig3)
    with cols_relacao_trabalho[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <br><br>
                        <li> Na PSE 2020, <font color='red'><b>a População Total (PTo) é de 2.673 indivíduos</b></font>. O nº de indivíduos entre
                        <b>15 e 65 anos</b> (a População em Idade de Trabalho - PIT) é de <b>1.674 indivíduos</b>, ou <b>62,6%</b> da PTo. 
                        Consequentemente, a População Fora da Idade de Trabalho (PFIT), soma 999 indivíduos, ou seja 37,4% do total de 
                        indivíduos pesquisados.
                        </li>
                        <br><br><br>
                        <li> Partindo agora para divisão da PIT, temos <font color='red'><b>a parcela de pessoas trabalhando ou em busca por trabalho 
                        (Força de Trabalho - FT) correspondente à 1.018 indivíduos</b></font> e a parcela dos indivíduos Fora da Força de Trabalho 
                        (FFT) de <b>656</b> indivíduos. Uma proporção próxima de 2/3 entre quem está na FFT em relação a FT.                    
                        </li>
                        <br><br><br>
                        <li> Por fim, <font color='red'><b>divindo a Força de Trabalho em dois grupos, aqueles que estão ocupados em atividades remuneradas População
                        Ocupada - PO) e aqueles desocupados dessas atividades, mas engajados na busca de um novo trabalho (População Desocupada - PD)</b></font>,
                        temos: PO com <b>853</b> índivíduos e PD com <b>165</b> pessoas. Ou seja, aproximadamente <b>5 vezes</b> mais pessoas 
                        ocupadas que desocupadas na FT.  
                        </li>
                    </ul>''', unsafe_allow_html=True) 

    cols_conceitos_2 = st.columns(1)
    with cols_conceitos_2[0]:
        with st.columns([1,3,1])[1]:
            st.markdown("<h3 style='text-align: center;'>Conceitos das Relações de Trabalho da PSE 2020</h3>", unsafe_allow_html=True)
            st.image("images/trabalho-img02-conceitos-analiticos.png")
    
        st.markdown(''' <p style='font-size:20px;'>
                        Podemos notar no diagrama acima a <font color='red'><b>divisão de cada relação de trabalho com os valores apresentados na interpretação
                        da pesquisa</b></font> e compilados nos gráficos anteriores. A demonstração dos dados dessa maneira são de grande
                        relevância para o entendimento dos <font color='red'><b>indicadores das relações de trabalho</b></font> que veremos logo
                        no tópico a seguir.
                        </p> 
                        ''', unsafe_allow_html=True)
  
    st.markdown('## Indicadores das Relações de Trabalho')
    st.markdown('#')
   
    cols_taxa_participacao = st.columns(2)
    with cols_taxa_participacao[0]:
        FT = dados.D306_sum.sum()
        PIT = dados.D301_sum.sum()
        TP = FT/PIT

        labels = ["Taxa de Participação", "Complementar da Taxa de Participação"]
        values = [TP, 1 - TP]

        fig = go.Figure( data=[ go.Pie(labels=labels, values = values, marker_colors=["#0367b0","#cce2f2"], hole = 0.6) ] )

        # Ajustando o layout do gráfico
        fig.update_layout(width=500, height=500, font_family = 'Open Sans', font_color= "black", title_font_color= "black",
                        title_font_size=24, title_text='Taxa de Participação Geral' + '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>',
                        showlegend=False, annotations=[dict(text=f'<b>Taxa de<br>Participação<br>{TP*100:.1f}%</b>', x=0.5, y=0.5, font_size=28, 
                                                            showarrow=False)])

        fig.update_traces(hoverinfo='label+percent', textinfo='none')       
        st.plotly_chart(fig)
    with cols_taxa_participacao[1]:        
        st.markdown('''<ul class="font-text-destaques">
                    <br><br>
                        <li> Investigando a <font color='red'><b>disposição da FT em participar das relações de produção</b></font> é o que define
                        a <b>Taxa de Participação</b>. Ela nada mais é que a razão entre a Força de Trabalho e a População em Idade de Trabalho.                          
                        </li>
                        <br>
                        <li> A <font color='red'><b>Taxa de Participação (Tp) observada na pesquisa foi de 60,8%</b></font>, o que significa que
                        essa é a parcela da população em idade de trabalhar que participa efetivamente da estrutura produtiva e é a parcela 
                        efetivamente envolvida com a geração de renda por meio do trabalho. Esse valor é bem próximo ao da RMSP (<b>61%</b>).
                        </li>
                    </ul>''', unsafe_allow_html=True)

    cols_taxa_ocupacao = st.columns(2)
    with cols_taxa_ocupacao[0]:
        st.markdown('''<ul class="font-text-destaques">
                        <br><br><br>
                        <li> Calculando a <font color='red'><b>razão entre a População Ocupada (PO) e a Força de Trabalho (FT) </b></font> 
                        definimos a <b>Taxa de Ocupação</b>. Essa taxa é a proporção dos indivíduos ocupados em relação a FT, expressando
                        o quanto o fator de produção está efetivamente sendo utilizado.                          
                        </li>
                        <br>
                        <li> Temos ao lado,a <font color='red'><b>Taxa de Ocupação (To) geral e por gênero</b></font>. Destaque para uma <b>menor
                        To de mulheres</b>, aproximadamente <b>7</b> pontos percentuais menor que os homens. Essa diferença de gênero será presente
                        em outros indicadores da pesquisa.
                        </li>
                    </ul>''', unsafe_allow_html=True)
    with cols_taxa_ocupacao[1]:
        # Taxa de Ocupação Geral
        FT = dados.D306_sum.sum()
        PO = dados.D302_sum.sum()
        TO = PO/FT
        labels = ["TO", "Complementar da TO"]
        values = [TO, 1 - TO]

        # Taxa de Ocupação Homens
        TO_H = 0.874
        values_2 = [TO_H, 1 - TO_H]

        # Taxa de Ocupação Mulheres
        TO_M = 0.803
        values_3 = [TO_M, 1 - TO_M]

        fig = make_subplots(1, 3, specs=[[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}]])
        fig.add_trace(go.Pie(labels=labels, values=values, marker_colors=["#203864","#d2d7e0"], hole = 0.6), 1, 1)
        fig.add_trace(go.Pie(labels=labels, values=values_2, marker_colors=["#203864","#d2d7e0"], hole = 0.6), 1, 2)
        fig.add_trace(go.Pie(labels=labels, values=values_3, marker_colors=["#203864","#d2d7e0"], hole = 0.6), 1, 3)

        #Ajustando o layout do gráfico
        fig.update_layout(width=700, height=500, font_family = 'Open Sans', font_color= "black", title_font_color= "black",
                        title_font_size=24, title_text='Taxa de Ocupação geral e por gênero' + '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>',
                        showlegend=False, 
                        annotations=[dict(text=f'<b>Taxa de<br>Ocupação<br>GERAL<br>{TO*100:.1f}%</b>', x=0.08, y=0.5, font_size=18, showarrow=False),
                                    dict(text=f'<b>Taxa de<br>Ocupação<br>HOMENS<br>{TO_H*100:.1f}%</b>', x=0.5, y=0.5, font_size=18, showarrow=False),
                                    dict(text=f'<b>Taxa de<br>Ocupação<br>MULHERES<br>{TO_M*100:.1f}%</b>', x=0.93, y=0.5, font_size=18, showarrow=False)]
                                    )

        fig.update_traces(hoverinfo='label+percent', textinfo='none')
        st.plotly_chart(fig)

    cols_ocupacao_sexo = st.columns(1)
    with cols_ocupacao_sexo[0]:
        dados_ocupacao = pd.DataFrame(
            {
                "Ocupação":["Conta Própria", "Conta Própria", "Doméstico", "Doméstico", "Empregado c/ carteira", "Empregado c/ carteira",
                            "Empregado s/ carteira", "Empregado s/ carteira", "Empregador", "Empregador", "Funcionário público",
                            "Funcionário público", "Militar", "Militar", "Não Caracterizado", "Não Caracterizado"],
                "Gênero": ['Homens', 'Mulheres', 'Homens', 'Mulheres', 'Homens', 'Mulheres', 'Homens', 'Mulheres', 'Homens', 'Mulheres',
                            'Homens', 'Mulheres', 'Homens', 'Mulheres', 'Homens', 'Mulheres'],
                "Qtd": [158, 127, 5, 45, 169, 125, 39, 31, 17, 21, 28, 55, 2, 2, 18, 11]
            }
        )

        fig = px.bar(dados_ocupacao, x="Qtd", y="Ocupação", color = "Gênero", text_auto=True,
                    color_discrete_sequence=["#0367b0","#f58334"])

        # Ajustando o layout do gráfico
        fig.update_layout(width=1200, height=400, font_family = 'Open Sans', font_size=15, font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Caracteríticas das Ocupações com distribuição por gênero' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', xaxis_title='', yaxis_title='',
                        xaxis_tickfont_size=14, yaxis_tickfont_size=14, xaxis_range = [0,305], 
                        plot_bgcolor= "#f8f9fa", yaxis_categoryorder='total ascending', legend=dict(x=0.82, y=0.1, bgcolor="#f8f9fa", title=None))

        fig.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>%{x}</b>', cliponaxis=False)
        st.plotly_chart(fig)
 
        st.markdown('''<ul class="font-text-destaques">
                        <li> Observamos no gráfico acima, <font color='red'><b>a distribuição da População Ocupada (PO) pelas características declaradas de suas 
                        ocupações</b></font>, detalhadas por gênero. É possível notar uma grande relevância dos empregos de carteira assinada e 
                        trabalhadores por conta própria. Vamos investigar as diferenças entre informalidade e assalariamento mais a frente.
                        </li>
                    </ul>''', unsafe_allow_html=True)

    st.markdown('#')
    st.markdown('#')  

    cols_taxa_desemprego = st.columns(2)
    with cols_taxa_desemprego[0]:
        st.markdown('<br><br>', unsafe_allow_html=True) 
        # Taxa de Desemprego Geral
        PD = dados.D303_sum.sum()
        PO = dados.D302_sum.sum()
        TD = PD/PO
        labels = ["TD", "Complementar da TD"]
        values = [TD, 1 - TD]

        # Taxa de Desemprego Homens
        TD_H = 0.144
        values_2 = [TD_H, 1 - TD_H]

        # Taxa de Desemprego Mulheres
        TD_M = 0.245
        values_3 = [TD_M, 1 - TD_M]

        fig = make_subplots(1, 3, specs=[[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}]])
        fig.add_trace(go.Pie(labels=labels, values=values, marker_colors=["#be282c","#fac2c3"], hole = 0.6, rotation = 90), 1, 1)
        fig.add_trace(go.Pie(labels=labels, values=values_2, marker_colors=["#be282c","#fac2c3"], hole = 0.6, rotation = 90), 1, 2)
        fig.add_trace(go.Pie(labels=labels, values=values_3, marker_colors=["#be282c","#fac2c3"], hole = 0.6, rotation = 90), 1, 3)

        #Ajustando o layout do gráfico
        fig.update_layout(width=700, height=500, font_family = 'Open Sans', font_color= "black", title_font_color= "black",
                        title_font_size=24, title_text='Taxa de Desemprego geral e por gênero' + '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>',
                        showlegend=False, 
                        annotations=[dict(text=f'<b>Taxa de<br>Desemprego<br>GERAL<br>{TD*100:.1f}%</b>', x=0.06, y=0.5, font_size=18, showarrow=False),
                                    dict(text=f'<b>Taxa de<br>Desemprego<br>HOMENS<br>{TD_H*100:.1f}%</b>', x=0.5, y=0.5, font_size=18, showarrow=False),
                                    dict(text=f'<b>Taxa de<br>Desemprego<br>MULHERES<br>{TD_M*100:.1f}%</b>', x=0.94, y=0.5, font_size=18, showarrow=False)])

        fig.update_traces(hoverinfo='label+percent', textinfo='none')
        st.plotly_chart(fig)
    with cols_taxa_desemprego[1]:        
        st.markdown('''<ul class="font-text-destaques">
                        <li> O <font color='red'><b>indicador da condição das relações de trabalho e das condições sociais de vida em uma 
                        dada sociedade é a Taxa de Desemprego (Td)</b></font>. Esta taxa mede a porporção entre a <b>População Ocupada (PO)</b> e a
                        <b>População Desocupada (PD)</b>, ambas culminando na <b>Força de Trabalho (FT)</b>. É a relação entre quem busca emprego
                        e quem está efetivamente trabalhando.                  
                        </li>
                        <br>
                        <li> Na PSE 2020, <font color='red'><b>a taxa de desemprego geral é de 19,3%, algo em torno de 43% maior que a taxa 
                        apurada para RMSP (13,5%)</b></font>. Ao decompormos para <b>critérios de cor ou raça</b>, podemos perceber uma <b>baixa 
                        sensibilidade entre as diferenças de raça ou cor</b>, apontando que na prática, Brancos, Pardos e Pretos tem as mesmas 
                        dificuldades de acesso às formas de ocupação, formais e/ou informais.
                        <li> Entretanto, <font color='red'><b>no recorte do gênero, notamos uma maior sensibilidade (de 70% - 14,4% contra 
                        24,5%)</b></font> apontando que as mulheres possuem uma <b>maior vulnerabilidade ao acesso ao trabalho</b>. Para a 
                        população estudada do PSE 2020, <b>o gênero foi o principal elemento</b> diferenciador da vulnerabilidade no acesso ao trabalho.
                        </li>
                    </ul>''', unsafe_allow_html=True)

    cols_taxa_info_salario = st.columns(2)
    with cols_taxa_info_salario[0]:
        st.markdown('''<ul class="font-text-destaques">
                    <br><br>
                        <li> Outro aspecto importante das relações de trabalho é <font color='red'><b>a diferenciação entre as ocupações formais e 
                        informais</b></font>. Na PSE 2020, os vínculos considerados formais foram: Militar, empregado com carteira assinada, 
                        estatutário do setor público e empregador. Os vínculos considerados informais foram: trabalhador doméstico, empregado
                        sem carteira assinada e trabalhador por conta própria.             
                        </li>
                        <br>
                        <li> Na PSE 2020, <font color='red'><b>a taxa de informalidade geral é foi de 47,5%, acima do Brasil, Sudeste e RMSP</b></font>. 
                        Sendo oposta a taxa de informalidade, a <b>taxa de assalariamento foi de 52,5%</b>, como podemos notar no gráfico ao lado.
                        Podemos observar, novamente pelo gênero, uma <font color='red'><b>maior informalidade entre as mulheres, por serem a 
                        maioria em quase todas as modalidades ditas de ocupação informal</b></font>. A característica do trabalho formal ou
                        informal não possui um desvio significativo da distribuição geral de cor ou raça.
                        </li>
                    </ul>''', unsafe_allow_html=True)
    with cols_taxa_info_salario[1]:
        formal = ["Militar", "Empregado c/ carteira", "Funcionário público", "Empregador", "Não Caracterizado"]
        informal = ["Doméstico", "Empregado s/ carteira", "Conta Própria"]
        trabalhadores_formais = dados_ocupacao.query("Ocupação in @formal ").Qtd.sum()
        trabalhadores_informais = dados_ocupacao.query("Ocupação in @informal ").Qtd.sum()
        PO = dados_ocupacao.Qtd.sum()
        TI = trabalhadores_informais/PO
        TA = trabalhadores_formais/PO

        # Taxa de Informalidade
        labels = ["TI", "Complementar da TI"]
        values = [TI, 1 - TI]

        # Taxa de Assalariamento
        labels = ["TA", "Complementar da TA"]
        values_2 = [TA, 1 - TA]

        from plotly.subplots import make_subplots

        fig = make_subplots(1, 2, specs=[[{'type':'domain'}, {'type':'domain'}]])
        fig.add_trace(go.Pie(labels=labels, values=values, marker_colors=["#00b050","#99dfb9"], hole = 0.6, rotation = 180), 1, 1)
        fig.add_trace(go.Pie(labels=labels, values=values_2, marker_colors=["#fec52b","#ffe8aa"], hole = 0.6, rotation = 0), 1, 2)

        #Ajustando o layout do gráfico
        fig.update_layout(width=700, height=500, font_family = 'Open Sans', font_color= "black", title_font_color= "black",
                        title_font_size=24, title_text='Taxa de Informalidade x assalariamento geral' + '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>',
                        showlegend=False, 
                        annotations=[dict(text=f'<b>Taxa de<br>Informalidade<br>{TI*100:.1f}%</b>', x=0.11, y=0.5, font_size=21, showarrow=False),
                                    dict(text=f'<b>Taxa de<br>Assalariamento<br>{TA*100:.1f}%</b>', x=0.9, y=0.5, font_size=21, showarrow=False)]
                        )

        fig.update_traces(hoverinfo='label+percent', textinfo='none')
        st.plotly_chart(fig)

    cols_taxa_participacao = st.columns(2)
    with cols_taxa_participacao[0]:
        sem_formais = dados.query("D316A_sum == 0").shape[0]
        sem_trabalhadores = formais_e_informais = dados.query("D316B_sum == 0 and D316A_sum == 0").shape[0]
        apenas_formais = dados.query("D316B_sum == 0 and D316A_sum > 0").shape[0]
        com_formais_e_informais = dados.shape[0] - (sem_formais + sem_trabalhadores + apenas_formais)


        labels = ["SEM Formais", "APENAS Formais", "COM Formais<br>e Informais", "SEM<br>Trabalhadores"]
        values = [sem_formais, apenas_formais, com_formais_e_informais, sem_trabalhadores]

        fig = go.Figure(
            data=[
                go.Pie(labels = labels, values = values, textinfo='label+percent',
                    marker_colors=["#00b050", "#fec52b", "#0367b0","#be282c"])
                ]
            )

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=700, font_family = 'Open Sans', font_color= "white", title_font_color= "black", 
                        title_font_size=24, title_text='Domicílios pelas relações de trabalho' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', showlegend=False)

        fig.update_traces(textfont_size=14, texttemplate='<b>%{label}<br>%{value} (%{percent})<br></b>')   
        st.plotly_chart(fig)
    with cols_taxa_participacao[1]:        
        st.markdown('''<ul class="font-text-destaques">
                    <br><br>
                        <li> Se contarmos os <font color='red'><b>654 domicílios que compõem a PSE 2020, aqueles com ao menos um trabalhador com trabalho
                        informal é de aproximadamente 370 domicílios, ou 56% do total</b></font>. A distribuição por gênero do total de informais dos 
                        responsáveis pelos domicílios é levemente superior para os homens em relação às mulheres (<b>188</b> contra <b>182</b>). 
                        Entretanto quando contamos os domicílios sem um indivíduo fazendo trabalho formal, chegamos a <b>283 domicílios</b>, 
                        ou seja <b>43,3%</b> de todos os domicílios da pesquisa.            
                        </li>
                        <br>
                        <li> Dos <font color='red'><b>370 domicílios com algum trabalhador informal, apenas 85 possuem também pelo menos um trabalhador
                        formal</b></font>. Por fim, <b>225</b> domicílios possuem todos os trabalhadores com acesso ao emprego formal, finalizando 
                        com <b>61</b> domicílios sem registros de trabalhadores.
                        </li>
                        <br>
                        <li>
                        A distribuição por gênero da pesquisa com apenas trabalhadores informais, aponta que <font color='red'><b>a condição de 
                        informalidade é majoritariamente encontrada em domicílios chefiados por mulheres</b></font>. Entretanto em domicílios com
                        apenas trabalhadores formais chefiados por mulheres, também temos uma maior quantidade de casos.
                        </li>
                    </ul>''', unsafe_allow_html=True)
with tabs[4]: # TAB da Renda
    cols_destaque_renda = st.columns(2)
    with cols_destaque_renda[0]:
        st.markdown("<p class='font-text-destaques'><br>Principais destaques sobre Renda</p>", unsafe_allow_html=True)
    with cols_destaque_renda[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> A <font color='red'><b>renda média domiciliar, na PSE 2020, abaixo de 4 salários mínimos abrange 83,5% das famílias 
                        pesquisadas</b></font>. A renda per capita  é de <b>R$ 659,00</b>, equivalente a um <b>1/3 da renda per capita</b> do Estado de
                        São Paulo e <b>menos da metade</b> de Embu-Guaçu. 
                        </li>
                        <br>
                        <li> Tratando os núcleos separadamente, <font color='red'><b>dois deles possuem uma renda per capita abaixo da média da PSE 2020
                        </b></font>: o núcleo <b>Filipinho com R$ 586,00</b> (2º maior em estudantes da Passos Mágicos) seguido do núcleo <b>Granjinha 
                        com apenas R$ 518,00</b> (menor de todos os núcleos). 
                        </li>
                        <br>
                        <li> Não encontramos, nos indicadores pesquisados, <font color='red'><b>qualquer evidência de distribução significativamente 
                        desigual quando observamos os domícilios por cor e raça</b></font>. Infelizmente pelo recorte de gênero a <font color='red'><b>
                        condição feminina predispõe a um nível maior de precariedade</b></font>, com renda média domiciliar <b>10% menores</b> em domicílios
                        liderado por mulheres.
                        </li>
                        <br>
                        <li> Quanto a <font color='red'><b>origem da renda, 91,3% advém de rendas do trabalho, sendo exlusiva em 47,7% deles</b></font>. 
                        Os <font color='red'><b>programas sociais correspondem a 12,4% de renda para os domicílios que possuem</b></font>, com <b>35</b>
                        domícilios pesquisados cujos <b>programas sociais são responsáveis por toda renda disponível</b>. A aposentadoria  é o programa
                        mais importante com <b>43%</> da renda.
                        </li>
                    </ul>''', unsafe_allow_html=True)

    st.markdown("---") 
    st.markdown('## Renda média e per capita dos domicílios')

    cols_dom_faixa_renda = st.columns(2)
    with cols_dom_faixa_renda[0]:
        domicilios_por_faixa_renda = dados.D425.value_counts().to_frame()
        domicilios_por_faixa_renda.index = ["2-3 SM", "1-1.5 SM", "3-4 SM", "1.5-2 SM", "5-7 SM", "0.5-1 SM",
                                            "4-5 SM", "0-0.5 SM", "7-10 SM", "0", "acima de 10 SM"]
        domicilios_por_faixa_renda = domicilios_por_faixa_renda.sort_index().reset_index()
        domicilios_por_faixa_renda.columns = ["faixa_renda", "qtd"]

        fig = px.histogram(domicilios_por_faixa_renda, x="faixa_renda", y="qtd", text_auto=True, color_discrete_sequence=["#68a4d0"])

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=500, font_family = 'Open Sans', font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Domicílios por faixas de renda total' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', 
                        xaxis_title='Faixas de Renda Total', yaxis_title='Nº de Domicílios',
                        xaxis_tickfont_size=14, yaxis_tickfont_size=14, yaxis_range = [0,150], 
                        plot_bgcolor= "#f8f9fa", showlegend=False, bargap=0.1)

        fig.update_xaxes(tickmode='array', tickvals=np.arange(0,12,1), ticktext = ['0', '0 - 0.5<br>SM', '0.5 - 1<br>SM', '1 - 1.5<br>SM',
                                                                                '1.5 - 2<br>SM', '2 - 3<br>SM', '3 - 4<br>SM', '4 - 5<br>SM',
                                                                                '5 - 7<br>SM', '7 - 10<br>SM', 'acima de<br>10 SM'])
        fig.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>%{y}</b>', cliponaxis=False)
        st.plotly_chart(fig)
    with cols_dom_faixa_renda[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <br><br><br><br>                  
                        <li> Em relação a amostra da população entrevistada pela PSE 2020, a <font color='red'><b>renda média dos 654 domicílios foi de
                        R$ 2.694.54</b></font>. Observando a <b>distribuição domiciliar por faixa de renda</b> no gráfico ao lado, temos uma maior 
                        quantidade de domicílios <b>entre 1 a 4 salários mínimos</b>.
                        </li>
                        <br>
                        <li> Observamos aqui que <font color='red'><b>8 domicílios sequer possuem acesso a renda</b></font> e o domicílio com maior renda 
                        entre os pesquisados tinha renda de 10 salários mínimos (R$ 10.648,00, em fev/2020). Notamos também que <b>546 domicílios (83,5%)
                        </b> recebem o equivalente a <b>4 salários mínimos ou menos</b>.
                        </li>
                    </ul>''', unsafe_allow_html=True)
        
    cols_renda_per_capita = st.columns(2)
    with cols_renda_per_capita[0]:
        st.markdown('''<ul class="font-text-destaques">
                        <br><br>
                        <li> Da população pesquisada, a <font color='red'><b>renda per capita ficou em apenas R$ 659,00</b></font>, sendo <b>44,7%</b>
                        do mesmo valor em Embu-Guaçu, <b>33,8%</b> do valor do estado de SP e <b>45,8%</b> no Brasil. O gráfico ao lado ilustra essa
                        comparação em valores monetários.
                        </li>
                        <br>
                        <li> Esse nível de disparidade corrobora a hipótese de <font color='red'><b>vulnerabilidade social e de precariedade das condições
                        de vida da população atendida pela Associação</b></font>. Pela PSE 2020 este grupo está entre a <b>parcela mais carente</b> de renda
                        da população de Embu-Guaçu.
                        </li>
                    <br>
                        <li> O <font color='red'><b>total de indivíduos com renda inferior ao da renda per capita geral do município é de 2.523</b></font>,
                        ou seja <b>94,4%</b> da população estudada.
                        </li>
                    </ul>''', unsafe_allow_html=True)        
    with cols_renda_per_capita[1]:
        total_moradores, renda_total = dados.V104_max.sum(), dados.D420_sum.sum()
        renda_per_capita_pse = (renda_total/total_moradores).round(0)

        rendas_per_capita = pd.DataFrame({
            "local": ["Brasil", "SP", "Embu-Guaçu", "PSE 2020"],
            "renda_per_capita": [1439, 1946, 1391, renda_per_capita_pse] })

        fig = px.bar(rendas_per_capita, x="local", y="renda_per_capita",  color="local",
                    color_discrete_sequence=["#f58334", "#fec52b", "#00b050","#be282c"], text_auto=True,)

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=500, font_family = 'Open Sans', font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Renda <i>per capita</i> PSE 2020 em comparação' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', 
                        yaxis_title='Valor da Renda <i>per capita</i>',
                        xaxis_tickfont_size=14, yaxis_tickfont_size=14, yaxis_range = [0,2100], 
                        plot_bgcolor= "#f8f9fa", showlegend=False, bargap=0.1)

        fig.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>R$ %{y:,.2f}</b>', cliponaxis=False)
        fig.update_yaxes(tickprefix = 'R$ ', tickformat = ',.0f')
        st.plotly_chart(fig)

    st.markdown('## Renda per capita por núcleo da Passos Mágicos')
    st.markdown('#')

    cols_dom_faixa_renda_per_capita = st.columns(1)
    with cols_dom_faixa_renda_per_capita[0]:
        domicilios_por_faixa_renda_per_capita = dados.D423.value_counts().to_frame()

        faixas = ['R$ 0,00 a R$ 278,00','R$ 278,01 a R$ 557,00', 'R$ 557,01 a R$ 836,00', 'R$ 836,01 a R$ 1.115,00',
                'R$ 1.115,01 a R$ 1.394,00', 'R$ 1.394,01 a R$ 1.673,00', 'R$ 1.673,01 a R$ 1.952,00',
                'R$ 1.952,01 a R$ 2.231,00', 'R$ 2.231,01 a R$ 2.510,00', 'R$ 2.510,01 acima']

        domicilios_por_faixa_renda_per_capita = domicilios_por_faixa_renda_per_capita.reindex(faixas).reset_index()
        domicilios_por_faixa_renda_per_capita.columns = ["faixa_renda_per_capita", "qtd"]

        fig = px.histogram(domicilios_por_faixa_renda_per_capita, x="faixa_renda_per_capita", y="qtd", text_auto=True, color_discrete_sequence=["#68a4d0"])

        # Ajustando o layout do gráfico
        fig.update_layout(width=1200, height=500, font_family = 'Open Sans', font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Domicílios por faixas de renda per capita' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', 
                        xaxis_title='Faixas de Renda <i>per capita</i>', yaxis_title='Nº de Domicílios',
                        xaxis_tickfont_size=12, yaxis_tickfont_size=14, yaxis_range = [0,220], 
                        plot_bgcolor= "#f8f9fa", showlegend=False, bargap=0.1)

        fig.update_xaxes(tickmode='array', tickvals=np.arange(0,12,1), 
                        ticktext = ['R$ 0,00<br>a<br>R$ 278,00','R$ 278,01<br>a<br>R$ 557,00', 'R$ 557,01<br>a<br>R$ 836,00', 
                                    'R$ 836,01<br>a<br>R$ 1.115,00', 'R$ 1.115,01<br>a<br>R$ 1.394,00', 'R$ 1.394,01<br>a<br>R$ 1.673,00', 
                                    'R$ 1.673,01<br>a<br>R$ 1.952,00', 'R$ 1.952,01<br>a<br>R$ 2.231,00', 
                                    'R$ 2.231,01<br>a<br>R$ 2.510,00', 'acima de<br>R$ 2.510,01'])
        fig.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>%{y}</b>', cliponaxis=False)
        st.plotly_chart(fig)

        st.markdown('''<ul class="font-text-destaques">
                <li> A <font color='red'><b>cidade de Embu-Guaçu está listada na posição 562ª (IBGE 2020) entre os 13% municipíos mais pobres do estado de SP
                </b></font>. Que ilustra a vulnerabilidade da população pesquisada pelo PSE 2020, que tem renda per capita de apenas <b>50% da renda</b>
                deste município. Se dividirmos do ponto de vista geográfico por núcleo, apenas um deles (<b>Centro</b>) possui uma renda per capita acima
                do valor da PSE como um todo. <br>Vamos observar pontos de destaque em cada uma delas:
                    <ul><li>
                    O <font color='red'><b>Núcleo Centro</b></font> é o maior de todos, atendendo <b>329 alunos (42% do total) de 288 domicílios 
                    diferentes</b>. A maioria dos domicílios se encontram na 2ª e 3 ª faixas de renda, com <b>151 domicílios (52,4% do grupo) com renda 
                    entre R$ 278,01 e 836,00</b>. A renda per capita média desses domicílios é de <b>R$ 818,78</b>.
                    </li></ul>
                    <br>
                    <ul><li>
                    O segundo maior núcleo é o <font color='red'><b>Filipinho</b></font>, que atende <b>239 alunos (30,5% do total) de 180 domicílios 
                    diferentes</b>. A maioria dos domicílios se encontram na 2ª faixa de renda, com <b>70 domicílios (39% do grupo) com renda 
                    entre R$ 278,01 e R$ 557,00</b>. A renda per capita média desses domicílios é de <b>R$ 586,51</b>.
                    </li></ul>
                    <br>
                    <ul><li>
                    O núcleo <font color='red'><b>Cipó</b></font> é o terceiro com mais atendimentos, <b>132 alunos (17% do total) de 119 domicílios 
                    diferentes</b>. A maioria dos domicílios se encontram na 2ª faixa de renda, com <b>72 domicílios (61% do grupo) com renda 
                    entre R$ 278,01 e R$ 836,00</b>. A renda per capita média desses domicílios é de <b>R$ 678,99</b>.
                    </li></ul>
                    <br>
                    <ul><li>
                    Por fim, temos o núcleo <font color='red'><b>Granjinha</b></font> com apenas <b>84 alunos (10,5% do total) de 67 domicílios 
                    diferentes</b>. Aqui, a maioria dos domicílios se encontram entre a 1ª e 3ª faixa de renda, com <b>48 domicílios (72% do grupo) com renda 
                    entre R$ 0 e R$ 836,00</b>. A renda per capita média desses domicílios é de apenas <b>R$ 518,88</b>, ou seja 37,3% da renda per capita
                    do município.
                    </li></ul>   
                </li>
                    <br>
                <li>
                    O gráfico abaixo ilustra as rendas per capita dos núcleos da Passos Mágicos comparados com esferas geográficas acima deles:
                </li>
            </ul>''', unsafe_allow_html=True)
        
        st.markdown('#')
        
        # Agrupamento por renda per capita
        renda_per_capita_brasil, renda_per_capita_SP, renda_per_capita_embu_guacu = 1439, 1946, 1391
        renda_per_capita_pse = dados.D422.sum() / dados.shape[0]
        renda_per_capita_centro = dados.query("V102_first =='Centro'").D422.sum() / dados.query("V102_first =='Centro'").shape[0]
        renda_per_capita_filipinho = dados.query("V102_first =='Filipinho'").D422.sum() / dados.query("V102_first =='Filipinho'").shape[0]
        renda_per_capita_cipo = dados.query("V102_first =='Cipó'").D422.sum() / dados.query("V102_first =='Cipó'").shape[0]
        renda_per_capita_granjinha = dados.query("V102_first =='Granjinha'").D422.sum() / dados.query("V102_first =='Granjinha'").shape[0]

        rendas_per_capita = pd.DataFrame({
        "local": ["Brasil", "SP", "Embu-Guaçu", "PSE 2020", "Centro", "Filipinho", "Cipó", "Granjinha"],
        "renda_per_capita": [renda_per_capita_brasil, renda_per_capita_SP, renda_per_capita_embu_guacu, renda_per_capita_pse,
                            renda_per_capita_centro, renda_per_capita_filipinho, renda_per_capita_cipo, renda_per_capita_granjinha] })

        fig = px.bar(rendas_per_capita, x="local", y="renda_per_capita",  color="local",
                    color_discrete_sequence=["#f58334", "#333333", "#cccccc","#be282c", "#fac2c3", "#fac2c3", "#fac2c3","#fac2c3"], text_auto=True)

        # Ajustando o layout do gráfico
        fig.update_layout(width=1200, height=500, font_family = 'Open Sans', font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Agrupamento por Renda <i>per capita</i>' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', xaxis_title = '', yaxis_title='',
                        xaxis_tickfont_size=14, yaxis_tickfont_size=14, yaxis_range = [0,2100], 
                        plot_bgcolor= "#f8f9fa", showlegend=False)

        fig.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>R$ %{y:,.2f}</b>', cliponaxis=False)
        fig.update_yaxes(tickprefix = 'R$ ', tickformat = ',.0f')
        st.plotly_chart(fig)
    
    st.markdown('## Renda per capita por gênero e por cor ou raça')
    st.markdown('#')
   
    cols_renda_sexo = st.columns(2)
    with cols_renda_sexo[0]:
        renda_per_capita_homens = dados.query("V107_first == 'Homem'").D420_sum.sum() / dados.query("V107_first == 'Homem'").V104_max.sum()
        renda_per_capita_mulheres = dados.query("V107_first == 'Mulher'").D420_sum.sum() / dados.query("V107_first == 'Mulher'").V104_max.sum()

        rendas_per_capita = pd.DataFrame({
            "genero": ["Homens", "Mulheres"],
            "renda_per_capita": [renda_per_capita_homens, renda_per_capita_mulheres] })

        fig = px.bar(rendas_per_capita, x="genero", y="renda_per_capita",  color="genero",
                    color_discrete_sequence=["#0367b0", "#f58334"], text_auto=True)

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=500, font_family = 'Open Sans', font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Renda <i>per capita</i> por gênero' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', 
                        yaxis_title='', xaxis_title='', xaxis_tickfont_size=14, yaxis_tickfont_size=14, 
                        yaxis_range = [0,770], plot_bgcolor= "#f8f9fa", showlegend=False)

        fig.update_traces(textfont_size=20, textposition="outside", texttemplate='<b>R$ %{y:,.2f}</b>', cliponaxis=False)
        fig.update_yaxes(tickprefix = 'R$ ', tickformat = ',.2f')
        st.plotly_chart(fig)
    with cols_renda_sexo[1]:        
        st.markdown('''<ul class="font-text-destaques">
                    <br><br><br><br>
                        <li> Investigando a renda dos responsáveis pelo domicílio, encontramos uma <font color='red'><b>renda total dos domicílios cujo 
                        responsável é um  homem, em média 11% acima do que a média dos domicílios chefiados por mulheres</b></font>.                
                        </li>
                        <br>
                        <li> A renda per capita evidenciou algo semelhante, com <font color='red'><b>8,8 pontos percentuais acima do caso dos domicílios 
                        chefiados por homens em relação a mulher</b></font>.
                        </li>
                    </ul>''', unsafe_allow_html=True)

    cols_renda_cor_raca = st.columns(2)
    with cols_renda_cor_raca[0]:
        st.markdown('''<ul class="font-text-destaques">
                        <br><br><br><br>
                        <li> Ao avaliarmos a renda dos responsáveis pelo domicílio em relação a cor ou raça, <font color='red'><b>não encontramos qualquer
                        diferença significativa</b></font>. As dificuldades de acesso à renda dessa população é a mesma para brancos, pretos, pardos,
                        amarelos e indígenas.                
                        </li>
                        <br>
                        <li> Logo abaixo, vamos explorar a origem das rendas da população investigada na PSE 2020.
                        </li>
                    </ul>''', unsafe_allow_html=True)
    with cols_renda_cor_raca[1]:
        renda_per_capita_resp_brancos = dados.query("V109_first == 'Branca'").D420_sum.sum() / dados.query("V109_first == 'Branca'").V104_max.sum()
        condicao_preto_pardo = "V109_first == 'Parda' or V109_first == 'Preta'"
        condicao_amarelo_indigena = "V109_first == 'Indígena' or V109_first == 'Amarela'"
        renda_per_capita_resp_pretos_pardos = dados.query(condicao_preto_pardo).D420_sum.sum() / dados.query(condicao_preto_pardo).V104_max.sum()
        renda_per_capita_resp_amarelo_indigena = dados.query(condicao_amarelo_indigena).D420_sum.sum() / dados.query(condicao_amarelo_indigena).V104_max.sum()

        rendas_per_capita = pd.DataFrame({
            "cor_raca": ["Brancos", "Pretos e Pardos", "Amarelos e Indígenas"],
            "renda_per_capita": [renda_per_capita_resp_brancos, renda_per_capita_resp_pretos_pardos, renda_per_capita_resp_amarelo_indigena] })

        fig = px.bar(rendas_per_capita, x="cor_raca", y="renda_per_capita",  color="cor_raca",
                    color_discrete_sequence=["#f58334", "#fec52b", "#0367b0"], text_auto=True)

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=500, font_family = 'Open Sans', font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Renda <i>per capita</i> por gênero' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', 
                        yaxis_title='', xaxis_title='', xaxis_tickfont_size=14, yaxis_tickfont_size=14, 
                        yaxis_range = [0,770], plot_bgcolor= "#f8f9fa", showlegend=False)

        fig.update_traces(textfont_size=20, textposition="outside", texttemplate='<b>R$ %{y:,.2f}</b>', cliponaxis=False)
        fig.update_yaxes(tickprefix = 'R$ ', tickformat = ',.2f')
        st.plotly_chart(fig)

    st.markdown('## Origens da Renda dos Domicílios')
    st.markdown('#')

    cols_origem_renda = st.columns(2)
    with cols_origem_renda[0]:
        origem_renda_domicilio = dados.D421.value_counts().to_frame().reset_index()
        origem_renda_domicilio.columns = ["origem_renda", "qtd"]

        fig = px.bar(origem_renda_domicilio, x="qtd", y="origem_renda", color = "origem_renda", text_auto=True,
                    color_discrete_sequence=["#0367b0", "#0367b0", "#0367b0", "#fec52b","#0367b0", "#be282c", "#fec52b", "#00b050"])

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=600, font_family = 'Open Sans', font_size=15, font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Distribuição dos alunos por sua condição no domicílio' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', xaxis_title='', yaxis_title='',
                        xaxis_tickfont_size=14, yaxis_tickfont_size=14, xaxis_range = [0,350], 
                        plot_bgcolor= "#f8f9fa", showlegend=False)

        fig.update_yaxes(tickmode='array', tickvals=np.arange(0,8,1), ticktext = ["Outras Rendas", "Programas Sociais e<br>Outras Rendas", 
                                                                                "Sem Renda", "Trabalho,<br>Programas Sociais e<br>Outras Rendas",
                                                                                "Programa Sociais", "Trabalho e<br>Outras Rendas", 
                                                                                "Trabalho e<br>Programas Sociais", "Apenas Trabalho"])

        fig.update_traces(textfont_size=15, textposition="outside", texttemplate='<b>%{x}</b>', cliponaxis=False)
        st.plotly_chart(fig)
    with cols_origem_renda[1]:        
        st.markdown('''<ul class="font-text-destaques">
                    <br><br><br><br>
                        <li> Investigando a origem da renda dos domicílios, foi possível perceber que <font color='red'><b>a renda advinda exclusivamente 
                        do trabalho representa quase a metade dos domicílios</b></font> (<b>47,4% ou 310 domicílios</b>), seguida das rendas de trabalho 
                        combinadas as rendas de programas sociais que representa quase um terço (<b>31,7% ou 207 domicílios</b>).            
                        </li>
                        <br>
                        <li> Analisando os pesos de cada parcela da renda, a partir de sua origem, em relação à renda total dos domicílios notamos que
                        <font color='red'><b>84,5% advém do trabalho, seguida por 12,4% da renda oriunda dos programas sociais</b></font> e a parcela 
                        restante (3,1%) vem de outras rendas.
                        </li>
                    </ul>''', unsafe_allow_html=True)

    cols_renda_por_domicilio = st.columns(2)
    with cols_renda_por_domicilio[0]:
        st.markdown('''<ul class="font-text-destaques">
                        <br><br><br><br>
                        <li> Partindo para a <font color='red'><b>análise da renda média por domicílio pela origem da renda</b></font>, observamos que 
                        as 4 primeiras posições evidenciam a força do trabalho na geração de renda das famílias no PSE 2020. <b>Todas as médias estão acima
                        de 2 salários mínimos</b> para esta situação.                
                        </li>
                        <br>
                        <li> Excluindo as famílias que estavam, no momento da pesquisa, em total privação de acesso à renda, <font color='red'><b>aquelas com 
                        renda exclusivamente advindas de programas sociais tinham o menor nível de renda domiciliar</b></font> observado.
                        </li>
                    </ul>''', unsafe_allow_html=True)
    with cols_renda_por_domicilio[1]:
        renda_media_domicilio = dados.groupby("D421")["D420_sum"].mean().round(2)
        ordem = ["renda do trabalho", "trabalho e programas sociais", "trabaho e outras rendas", "programas sociais", 
                "trabalho e programas sociais e outras rendas", "sem renda", "programas sociais e outras rendas", "outras rendas"]

        renda_media_domicilio = renda_media_domicilio.reindex(ordem).reset_index()
        renda_media_domicilio.columns = ["origem_renda", "renda_media"]

        fig = px.bar(renda_media_domicilio, x="renda_media", y="origem_renda", text_auto=True, color_discrete_sequence=["#0367b0"])

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=600, font_family = 'Open Sans', font_size=15, font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Renda Média por domicílio e origem da renda' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', xaxis_title='', yaxis_title='',
                        xaxis_tickfont_size=14, yaxis_tickfont_size=14, xaxis_range = [0, 5000], 
                        plot_bgcolor= "#f8f9fa", showlegend=False, yaxis_categoryorder='total ascending')

        fig.update_xaxes(tickprefix = 'R$ ', tickformat = ',.0f')
        fig.update_yaxes(tickmode='array', tickvals=np.arange(0,8), ticktext = ["Sem Renda", "Programa Sociais", "Outras Rendas", 
                                                                                "Programas Sociais e<br>Outras Rendas", "Trabalho e<br>Programas Sociais", 
                                                                                "Trabalho e<br>Outras Rendas", "Apenas Trabalho",
                                                                                "Trabalho,<br>Programas Sociais e<br>Outras Rendas"])

        fig.update_traces(textfont_size=15, textposition="outside", texttemplate='R$ <b>%{x:,.2f}</b>', cliponaxis=False)
        st.plotly_chart(fig)
 
    st.markdown('## Renda do Trabalho')
    st.markdown('#')

    cols_renda_trabalho = st.columns(2)
    with cols_renda_trabalho[0]:
        formal_ou_informal = dados.query("D421 == 'renda do trabalho' and (D316A_sum > 0 or D316B_sum > 0)")
        um_ou_mais_formal = dados.query("D421 == 'renda do trabalho' and D316A_sum > 0")
        somente_informal = dados.query("D421 == 'renda do trabalho' and (D316A_sum == 0 and D316B_sum > 0)")

        qtd_formal_ou_informal = formal_ou_informal.shape[0]
        qtd_um_ou_mais_formal = um_ou_mais_formal.shape[0]
        qtd_somente_informal = somente_informal.shape[0]

        renda_per_capita_formal_ou_informal = (formal_ou_informal.D420_sum.sum() / formal_ou_informal.V104_max.sum()).round(2)
        renda_per_capita_um_ou_mais_formal = (um_ou_mais_formal.D420_sum.sum() / um_ou_mais_formal.V104_max.sum()).round(2)
        renda_per_capita_somente_informal = (somente_informal.D420_sum.sum() / somente_informal.V104_max.sum()).round(2)

        rendas_per_capita = pd.DataFrame({
            "relacao_trabalho": ["formais ou informais", "Ao menos um formal", "somente informais"],
            "renda_per_capita": [renda_per_capita_formal_ou_informal, renda_per_capita_um_ou_mais_formal, renda_per_capita_somente_informal],
            "qtd_domicilios": [qtd_formal_ou_informal, qtd_um_ou_mais_formal, qtd_somente_informal]})

        fig = go.Figure(
            [go.Bar(x=rendas_per_capita["relacao_trabalho"], y=rendas_per_capita["renda_per_capita"], name ='Renda per capita (R$)',
                    marker_color = ["#f58334", "#00b050", "#0367b0"], text=rendas_per_capita["renda_per_capita"], yaxis='y1',
                    textfont_size=14, textposition="inside", texttemplate='<b>R$ %{y:,.2f}</b>', cliponaxis=False),
            go.Scatter(x=rendas_per_capita["relacao_trabalho"], y=rendas_per_capita["qtd_domicilios"], marker={'color':"#fec52b"}, name ='Nº de domicílios', 
                        text=rendas_per_capita["qtd_domicilios"], yaxis='y2', textfont_size=14, textposition="top right", mode="text+lines",
                        texttemplate='<b>%{y}</b>')])

        fig.update_layout(width=700, height=500, font_family = 'Open Sans', font_color= "black", hovermode='x', bargap=.3,
                            title={'text': 'Renda <i>per capita</i> domicílios com renda exclusiva do trabalho' + 
                                    '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', 
                                'font_color': "black", 
                                'font_size': 22}, 
                            yaxis={'title': "Renda per capita (R$)", 
                                'range':[0,1000],
                                'tickfont_size':14},
                            yaxis2={'rangemode': "tozero", 'overlaying': 'y',
                                    'position': 1, 'side': 'right',
                                    'title': 'Nº de domicílios',
                                    'range':[0,350],
                                    'tickfont_size':14},
                            xaxis={'tickfont_size':14},
                            showlegend=False, plot_bgcolor= "#f8f9fa")
        st.plotly_chart(fig)
    with cols_renda_trabalho[1]:        
        st.markdown('''<ul class="font-text-destaques">
                        <br><br>
                        <li> Vamos tratar neste tópico sobre a renda do trabalho. Neste recorte, temos <font color='red'><b>310 domicílios (47% da população
                        investigada) com renda exclusivamente do trabalho</b></font>, cujos domicílos são habitados por <b>1.220 com 358 alunos Passos Mágicos.
                        </b> A <b>renda total média desses domicílios é de R$ 2.910,87</b> e a <b>renda per capita de R$ 739,65</b>.                
                        </li>
                        <br>
                        <li> No recorte, <b>235 domicílios</b> possuem ao menos um trabalhador formal com <b>renda total média de R$ 3.171,27 e R$ 805,67 
                        per capita</b>. Representando <font color='red'><b>um valor 8,9% acima dos domicílios com renda exclusiva do trabalho em 
                        geral</b></font>. Temos também, <b>75 domicílios</b> com apenas trabalhadores informais com renda <b>34% inferior</b> àqueles dos
                        domicílios com ao menos um trabalhador formal. 
                        </li>
                    </ul>''', unsafe_allow_html=True)

    cols_renda_trabalho_PS = st.columns(2)
    with cols_renda_trabalho_PS[0]:
        st.markdown('''<ul class="font-text-destaques">
                        <br><br>
                        <li> Em <font color='red'><b>207 domicílios (32% do total de domicílios), a renda é composta pela combinação das rendos do trabalho
                        e de programas sociais</b></font>. Nesses domicílios possuímos <b>263 alunos Passos Mágicos</b>, <font color='red'><b>mais de um terço
                        dos alunos atendidos pela Associação</b></font>.           
                        </li>
                        <br>
                        <li> A renda média desses domicílios é de <b>R$ 2.626,86</b>, e a renda per capita de <b>R$ 600,18</b>. Podemos notar no gráfico ao
                        lado que <font color='red'><b>75% da renda do domicílio é advindo do trabalho enquanto, quase 25%, vem dos programas sociais</b></font>.                    
                        </li>
                        <br>
                        <li> Logo abaixo, vamos explorar a participação dos programas sociais tanto desses domicílios quanto dos domicílios em que os
                        programas sociais são rendas exclusivas.
                        </li>
                    </ul>''', unsafe_allow_html=True)
    with cols_renda_trabalho_PS[1]:
        renda_trabalho_TPS = dados.query("D421 == 'trabalho e programas sociais'").D319_sum.sum()
        renda_programas_sociais_TPS = dados.query("D421 == 'trabalho e programas sociais'").D415_sum.sum()

        labels = ["Trabalho", "Programas<br>Sociais"]
        values = [renda_trabalho_TPS, renda_programas_sociais_TPS]

        fig = go.Figure(
            data=[
                go.Pie(labels = labels, values = values, textinfo='label+percent',
                    marker_colors=["#0367b0","#fec52b"], hole=.4)
                ]
            )

        # Ajustando o layout do gráfico
        fig.update_layout(width=500, height=500, font_family = 'Open Sans', font_color= "white", title_font_color= "black", 
                        title_font_size=24, title_text='Renda dos domicílios por<br>trabalho e programas sociais' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', showlegend=False)

        fig.update_traces(textfont_size=14, texttemplate='<b>%{label}<br>%{percent}</b>')
        st.plotly_chart(fig)

    st.markdown('## Participação dos Programas Sociais')
    st.markdown('#')

    cols_programas_sociais = st.columns(2)
    with cols_programas_sociais[0]:
        part_aposentadoria_TPS = dados.query("D421 == 'trabalho e programas sociais'").V408_sum.sum()
        part_outros_TPS = dados.query("D421 == 'trabalho e programas sociais'").V406_sum.sum()
        part_bolsa_familia_TPS = dados.query("D421 == 'trabalho e programas sociais'").V404_sum.sum()
        part_seguro_desemprego_TPS = dados.query("D421 == 'trabalho e programas sociais'").V410_sum.sum()
        part_bpc_loas_TPS = dados.query("D421 == 'trabalho e programas sociais'").V402_sum.sum()
        renda_programas_sociais_TPS = dados.query("D421 == 'trabalho e programas sociais'").D415_sum.sum()

        pct_aposentadoria_TPS = (100 * part_aposentadoria_TPS/renda_programas_sociais_TPS)
        pct_outros_TPS = (100 * part_outros_TPS/renda_programas_sociais_TPS)
        pct_bolsa_familia_TPS = (100 * part_bolsa_familia_TPS/renda_programas_sociais_TPS)
        pct_seguro_desemprego_TPS = (100 * part_seguro_desemprego_TPS/renda_programas_sociais_TPS)
        pct_bpc_loas_TPS = (100 * part_bpc_loas_TPS/renda_programas_sociais_TPS)

        data = {'Aposentadoria': pct_aposentadoria_TPS, 'Outros Programas': pct_outros_TPS, 'Bolsa Família': pct_bolsa_familia_TPS,
                'Seguro Desemprego': pct_seguro_desemprego_TPS, 'BPC/LOAS': pct_bpc_loas_TPS}
        fig = plt.figure(FigureClass=Waffle, rows=5, values=data, colors=["#fec52b", "#00b050", "#be282c", "#f58334", "#0367b0"],
                        title={'label': 'Participação dos Programas Sociais', 'loc': 'left', 'size':14, 
                            'weight':'bold', 'family': 'Open Sans'},
                        labels=[f"{k} ({v:.1f}%)" for k, v in data.items()],
                        legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.5), 'ncol': 2, 'framealpha': 0},
                        starting_location='NW', block_arranging_style='snake', figsize=(8,8))
        st.pyplot(fig)

        part_aposentadoria_PS = dados.query("D421 == 'programas sociais'").V408_sum.sum()
        part_outros_PS = dados.query("D421 == 'programas sociais'").V406_sum.sum()
        part_bolsa_familia_PS = dados.query("D421 == 'programas sociais'").V404_sum.sum()
        part_seguro_desemprego_PS = dados.query("D421 == 'programas sociais'").V410_sum.sum()
        part_bpc_loas_PS = dados.query("D421 == 'programas sociais'").V402_sum.sum()
        renda_programas_sociais_PS = dados.query("D421 == 'programas sociais'").D415_sum.sum()

        pct_aposentadoria_PS = (100 * part_aposentadoria_PS/renda_programas_sociais_PS)
        pct_outros_PS = (100 * part_outros_PS/renda_programas_sociais_PS)
        pct_bolsa_familia_PS = (100 * part_bolsa_familia_PS/renda_programas_sociais_PS)
        pct_seguro_desemprego_PS = (100 * part_seguro_desemprego_PS/renda_programas_sociais_PS)
        pct_bpc_loas_PS = (100 * part_bpc_loas_PS/renda_programas_sociais_PS)

        data = {'Aposentadoria': pct_aposentadoria_PS, 'Outros Programas': pct_outros_PS, 'Bolsa Família': pct_bolsa_familia_PS,
                'Seguro Desemprego': pct_seguro_desemprego_PS, 'BPC/LOAS': pct_bpc_loas_PS}
        fig2 = plt.figure(FigureClass=Waffle, rows=5, values=data, colors=["#fec52b", "#00b050", "#be282c", "#f58334", "#0367b0"],
                        title={'label': 'Renda dos domicílios somente de Programas Sociais', 'loc': 'left', 'size':14, 
                            'weight':'bold', 'family': 'Open Sans'},
                        labels=[f"{k} ({v:.1f}%)" for k, v in data.items()],
                        legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.5), 'ncol': 2, 'framealpha': 0},
                        starting_location='NW', block_arranging_style='snake', figsize=(8,8))
        st.pyplot(fig2)
    with cols_programas_sociais[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <br>
                        <li> Os programas sociais estão presentes <b>207 domicílios com 906 moradores</b> ao todo. Na PSE 2020, <font color='red'><b>a 
                        Aposentadoria é o programa social mais importante com 36,1% de participação na renda</b></font>, seguido de outros programas
                        (<b>22,5%></b>) e o Bolsa Família (<b>21,5%</b>)  
                        </li>
                        <br><br><br><br><br>
                        <li> Nos domicílios com renda somente de programas sociais (<b>35 domicílios ou 5,4% do total</b>) com <b>42 alunos Passos Mágicos</b>,
                        notamos novamente a <font color='red'><b>ampla participação da Aposentadoria como programa social mais importante (43%)</b></font>, 
                        seguido do BPC/LOAS (Benefício Assistencial à Pessoa com Deficiência, com <b>29%</b>) e do Bolsa Família (<b>13%</b>).                   
                        </li>
                    </ul>''', unsafe_allow_html=True) 
with tabs[5]: # TAB de Moradia
    st.markdown("")
    cols_destaque_demografia = st.columns(2)
    with cols_destaque_demografia[0]:
        st.markdown("<p class='font-text-destaques'><br>Principais destaques sobre Moradia</p>", unsafe_allow_html=True)
    with cols_destaque_demografia[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> A <font color='red'><b>pesquisa de moradia da PSE 2020 nos propicia acesso aos aspectos de vulnerabilidade social e precariedade
                        nas condições de vida</b></font> da população. Mais de <b>89% dos domicílios são casas e 68 domicílios (10,4%)</b>
                        de apartamentos de conjuntos habitacionais de programas de auxílio.
                        </li>
                    <br>
                        <li> Observamos apenas <font color='red'><b>41% das moradias como próprias e quitadas</b></font>, abaixo da média nacional (<b>66%</b>),
                        as financiadas em andamento de <b>13%</b>, mais que o dobro da nacional (<b>6,1%</b>) e <b>45%</b>, acima da taxa
                        nacional (<b>33,6%</b>).
                        </li>
                    <br>
                        <li> Dentro das características das moradias não obtivemos grandes destaques, com a <font color='red'><b>disponibilidade de banheiro para
                        uso exclusivo, energia elétrica e uso de combustível para a preparação de alimentos próximos da média nacional</b></font>. Exceto o fato
                        de <b>14,2% dos domicílios não ter acesso à água encanada</b>, muito superior ao <b>2,4%</b> nacional, e apenas <b>59% das moradias</b>,
                         contra <b>90,2%</b> da RMSP, ter uma rede geral de coleta de esgoto.
                        </li>
                    <br>
                        <li> Como destaque, pela PSE 2020, <font color='red'><b>a presença de ao menos um telefone celular foi superior a média da região Sudeste
                         (99,5% contra 94,5%), a posse quase universalizada de geladeira/freezer (99,8%) e a posse de 58,7% dos domicílios de ao menos um
                         automóvel</b></font>. A média é bastante superior à nacional que em 2019 era de <b>49,2%</b>.
                        </li>
                    </ul>''', unsafe_allow_html=True)

    st.markdown("---")
    st.markdown('#')

    st.markdown('## Tipos de Moradia e Condição de Ocupação')
    
    cols_tipo_moradia = st.columns(2)
    with cols_tipo_moradia[0]:
        tipos_moradia = dados.V501_first.value_counts().to_frame().reset_index()
        tipos_moradia.columns = ["moradia", "qtd"]

        fig = px.bar(tipos_moradia, x="moradia", y="qtd",  color="moradia", text_auto=True,
                    color_discrete_sequence=["#0367b0", "#f58334", "#ed3237"])

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=500, font_family = 'Open Sans', font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Tipos de Moradia' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', 
                        yaxis_title='', xaxis_title='', xaxis_tickfont_size=14, yaxis_tickfont_size=14, 
                        yaxis_range = [0,650], plot_bgcolor= "#f8f9fa", showlegend=False)

        fig.update_traces(textfont_size=20, textposition="outside", texttemplate='<b>%{y}</b>', cliponaxis=False)
        fig.update_xaxes(tickmode='array', tickvals=np.arange(0,3), ticktext = ["Casa", "Apartamento", "Cortiço"])
        st.plotly_chart(fig)
    with cols_tipo_moradia[1]:
        st.markdown('''<ul class="font-text-destaques">
                    <br><br>
                        <li> O recorte da pesquisa aponta que <font color='red'><b>89,3% dos domicílio são de casas</b></font>, valor acima da média nacional
                        (<b>85,6%</b>) e da Região Sudeste (<b>80,3%</b>). 
                        </li>
                    <br>
                        <li> Da população pesquisada, <font color='red'><b>10,4% do total vive em apartamentos</b></font> próprios ou alugados. O restante, 
                        <b>0,3%</b> dos casos, moram em habitações de cômodos ou cortiços como podemos observar no gráfico ao lado.
                        </li>
                    <br>
                        <li> Mais abaixo, vamos observar à condição e modalidade dessas ocupações para a população pesquisada na PSE 2020.  
                        </li>
                    </ul>''', unsafe_allow_html=True)

    cols_cond_moradia = st.columns(2)
    with cols_cond_moradia[0]:
        st.markdown('''<ul class="font-text-destaques">
                    <br><br><br>
                        <li> A <font color='red'><b>moradia própria e quitada corresponde a 41% dos casos</b></font>, muito aquém da média nacional de <b>66,4%
                        </b> e da Região Sudeste de <b>62,3%</b>. Essa  baixa quantidade de moradias quitadas é um forte indicador de <b>vulnerabilidade social</b>.
                        </li>
                    <br>
                        <li> Da modalidade de <font color='red'><b>moradia própria com quitação em andamento temos 13,3% dos casos</b></font>, mais que o dobro
                        da médial nacional de <b>6,1%</b>. As modalidades não proprietárias tem um peso de <b>47,5%</b> nos domicílios da PSE 2020, bastante 
                        superior aos <b>33,6%</b> da média nacional e <b>37,4%</b> da média da Região Sudeste.
                        </li>
                    <br>
                        <li> Segundo a pesquisa, <font color='red'><b>a formatação prevalente de moradia é de uma casa com 4 cômodos e 2 dormitórios, com 191 
                        domicílios neste arranjo, quase 30% dos casos</b></font>. A configuração de 4 moradores pelos 4 cômodos é presente em <b>78 domicílios
                        </b> dentro dos <b>220</b> que possuem 4 cômodos, ou seja <b>12%</b> de todos os casos observados. Apesar de algumas condições vulneráveis
                        não foi possível perceber uma distribuição desproporcional entre o nº de moradores e o nº de moradias.
                        </li>
                    </ul>''', unsafe_allow_html=True)
    with cols_cond_moradia[1]:
        cond_moradia = dados.V511_first.value_counts().to_frame().reset_index()
        cond_moradia.columns = ["condicao", "qtd"]

        fig = px.bar(cond_moradia, x="condicao", y="qtd",  color="condicao", 
                    color_discrete_sequence=px.colors.qualitative.D3, text_auto=True)

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=500, font_family = 'Open Sans', font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Condição de ocupação das moradias' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', 
                        yaxis_title='', xaxis_title='', xaxis_tickfont_size=14, yaxis_tickfont_size=14, 
                        yaxis_range = [0,320], plot_bgcolor= "#f8f9fa", showlegend=False)

        fig.update_traces(textfont_size=20, textposition="outside", texttemplate='<b>%{y}</b>', cliponaxis=False)
        fig.update_xaxes(tickmode='array', tickvals=np.arange(0,7), ticktext = ["Próprio<br>Já Pago", "Cedido por<br>familiar", "Alugado",
                                                                                "Próprio<br>Pagando", "Cedido de<br>outra forma", 
                                                                                "Cedido por<br>empregador", "Outra<br>condição"])
        st.plotly_chart(fig)

    st.markdown('## Características das moradias')
    st.markdown(''' <p style='font-size:20px;'>
                        A descrição das condições físicas das moradias e do acesso de seus moradores a bens de consumo e serviços são elementos fundamentais
                        na análise das suas condições de vida.
                    </p>
                    <br>
                    ''', unsafe_allow_html=True)
    
    cols_dom_agua = st.columns(2)
    with cols_dom_agua[0]:
        dom_agua_encanada = dados.V505_first.value_counts().to_frame().reset_index()
        dom_agua_encanada.columns = ["tipo", "qtd"]

        fig = px.bar(dom_agua_encanada, x="tipo", y="qtd",  color="tipo", text_auto=True,
                    color_discrete_sequence=["#0367b0", "#f58334", "#ed3237"])

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=400, font_family = 'Open Sans', font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Domicílios pela disponibilidade de água encanada' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', 
                        yaxis_title='', xaxis_title='', xaxis_tickfont_size=14, yaxis_tickfont_size=14, 
                        yaxis_range = [0,650], plot_bgcolor= "#f8f9fa", showlegend=False)

        fig.update_traces(textfont_size=20, textposition="outside", texttemplate='<b>%{y}</b>', cliponaxis=False)
        fig.update_xaxes(tickmode='array', tickvals=np.arange(0,3), ticktext = ["Canalizada em pelo<br>menos um cômodo", 
                                                                                "Canalizada só na<br>propriedade ou terreno	", 
                                                                                "Não canalizada"])
        # Adicionando imagens
        img_1 = Image.open("images/moradia-img01-chuveiro.png")
        img_2 = Image.open("images/moradia-img02-torneira.png")
        fig.add_layout_image(dict(source=img_1, x=0.75, y=0.65))
        fig.add_layout_image(dict(source=img_2, x=0.90, y=0.65))
        fig.update_layout_images(dict(xref="paper", yref="paper", sizex=0.2, sizey=0.2, xanchor="right", yanchor="bottom"))

        fig.add_annotation(text='Fonte: <a href="https://www.flaticon.com/br/icones-gratis/torneira">Torneira ícones criados por Octopocto - Flaticon</a>'
                                '<br>Fonte: <a href="https://www.flaticon.com/br/icones-gratis/chuveiro">Chuveiro ícones criados por Freepik - Flaticon</a>',
                        align="left", xref="paper", yref = "paper", x=1, y=-0.3, showarrow=False, font_size=10)
        st.plotly_chart(fig)
    with cols_dom_agua[1]:
        st.markdown('''<ul class="font-text-destaques">
                    <br>
                        <li> Do ponto de vista <font color='red'><b>do material do piso dos domicílios, quase 92% possuem 
                        cerâmica, lajota ou pedra</b></font>, sendo superior a média nacional (<b>78,3%</b>) e da região Sudeste (<b>86,6%</b>). 
                        </li>
                    <br>
                        <li> Sobre a água encanada, que podemos observar no gráfico ao lado, <font color='red'><b>561 domicílios, ou 85,8% do total, tem acesso
                         à água encanada no interior do domicílio</b></font>. Abaixo da média nacional de <b>97,6%</b> e da RMSP de <b>99,9%</b> dos domicílios. 
                        </li>
                    <br>
                        <li> Outros <font color='red'><b>87 domicílios, ou 13,3%, só tem esse acesso nos limites do terreno</b></font>, enquanto 6 domicílios, 
                        <b>0,9%</b>, do total não possui acesso algum.
                        </li>
                    </ul>''', unsafe_allow_html=True)

    cols_dom_banheiro = st.columns(2)
    with cols_dom_banheiro[0]:
        st.markdown('''<ul class="font-text-destaques">
                    <br><br><br>
                        <li> A <font color='red'><b>proporção dos domicílios pesquisados na PSE 2020 com banheiro exclusivo para uso de moradores foi de 99,8%
                        </b></font>, compatível com a média nacional de 97,8% e com a RMSP de 99,9%.
                        </li>
                    <br>
                        <li> <font color='red'><b>Apenas 1 domicílio dos 654 pesquisados não possui um banheiro exclusivo</b></font>, compartilhando com outro
                        domicílio. 
                        </li>
                    </ul>''', unsafe_allow_html=True)
    with cols_dom_banheiro[1]:
        dom_banheiro_exc = dados.V506_first.value_counts().to_frame().reset_index()
        dom_banheiro_exc.columns = ["n_banheiros", "qtd"]

        fig = px.histogram(dom_banheiro_exc, x="n_banheiros", y="qtd",  color="n_banheiros", text_auto=True, 
                        color_discrete_sequence=["#68a4d0"], nbins=5)

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=400, font_family = 'Open Sans', font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Domicílios pelo nº de banheiros de uso exclusivo' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', 
                        yaxis_title='Nº de Domicílios', xaxis_title='Nº de Banheiros Exclusivos', xaxis_tickfont_size=14, yaxis_tickfont_size=14, 
                        yaxis_range = [0,580], plot_bgcolor= "#f8f9fa", showlegend=False, bargap=0.1)

        fig.update_traces(textfont_size=20, textposition="outside", texttemplate='<b>%{y}</b>', cliponaxis=False)

        # Adicionando imagens
        img_3 = Image.open("images/moradia-img03-sanitario.png")
        fig.add_layout_image(dict(source=img_3, x=0.85, y=0.55))
        fig.update_layout_images(dict(xref="paper", yref="paper", sizex=0.3, sizey=0.3, xanchor="right", yanchor="bottom"))

        fig.add_annotation(text='Fonte: <a href="https://www.flaticon.com/br/icones-gratis/banheiro">Banheiro ícones criados por Creaticca Creative Agency - Flaticon</a>',
                        align="left", xref="paper", yref = "paper", x=1, y=-0.3, showarrow=False, font_size=10)
        st.plotly_chart(fig)

    cols_dom_esgoto = st.columns(2)
    with cols_dom_esgoto[0]:
        dom_esgoto = dados.V508_first.value_counts().to_frame().reset_index()
        dom_esgoto.columns = ["tipo", "qtd"]

        fig = px.bar(dom_esgoto, x="tipo", y="qtd",  color="tipo", text_auto=True,
                    color_discrete_sequence=["#f58334", "#fec52b", "#0367b0", "#ed3237", "#cccccc"])

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=400, font_family = 'Open Sans', font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Domicílios pela forma de escoamento do esgoto' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', 
                        yaxis_title='', xaxis_title='', xaxis_tickfont_size=14, yaxis_tickfont_size=14, 
                        yaxis_range = [0,440], plot_bgcolor= "#f8f9fa", showlegend=False)

        fig.update_traces(textfont_size=20, textposition="outside", texttemplate='<b>%{y}</b>', cliponaxis=False)
        fig.update_xaxes(tickmode='array', tickvals=np.arange(0,5), ticktext = ["Rede geral", "Fossa não<br>ligada à rede", "Rio, lago ou<br> mar",
                                                                                "Vala", "Outra forma"])
        # Adicionando imagens
        img_4 = Image.open("images/moradia-img04-esgoto.png")
        fig.add_layout_image(dict(source=img_4, x=0.75, y=0.55))
        fig.update_layout_images(dict(xref="paper", yref="paper", sizex=0.3, sizey=0.3, xanchor="right", yanchor="bottom"))

        fig.add_annotation(text='Fonte: <a href="https://www.flaticon.com/br/icones-gratis/esgoto">Esgoto ícones criados por Freepik - Flaticon</a>',
                        align="left", xref="paper", yref = "paper", x=1, y=-0.3, showarrow=False, font_size=10)
        st.plotly_chart(fig)
    with cols_dom_esgoto[1]:
        st.markdown('''<ul class="font-text-destaques">
                    <br>
                        <li> Sobre as formas de escoamento do esgoto, <font color='red'><b>59% dos domicílios pesquisados possuem esgotamento pela rede geral
                        </b></font>, menos que a média nacional de <b>62,7%</b> e de <b>90,2%</b> da RMSP. 
                        </li>
                    <br>
                        <li> Observando o gráfico ao lado, com a distribuição dos domicílios na pesquisa sobre esgoto, podemos notar <font color='red'><b>
                        uma concentração de 39,6% dos domicílios com fossa asséptica (não ligada à rede)</b></font>. Muito acima da taxa nacional de 
                        <b>5,6%</b> e <b>2,5%</b> da RMSP. 
                        </li>
                    </ul>''', unsafe_allow_html=True)

    cols_dom_energia = st.columns(2)
    with cols_dom_energia[0]:
        st.markdown('''<ul class="font-text-destaques">
                    <br><br>
                        <li> Como podemos notar no gráfico de pizza ao lado, <font color='red'><b> a disponibilidade de energia elétrica dos domicílios
                        pesquisados é muito semelhante à nacional (99,5%)</b></font>. Apenas 4 domicílios entre os 654 pesquisados não tinha acesso à energia
                         elétrica.
                        </li>
                    <br>
                        <li> Outro indicador interessante sobre a condição de vida das famílias é do <font color='red'><b>tipo de combustível utilizado para
                        a preparação dos alimentos</b></font>. Na PSE 2020, <b>todos os domicílios</b> utilizam meios adequados para essa preparação, onde 
                        <b>99,7%</b> utilizam gás de botijão e <b>0,3%</b> utilizam energia elétrica.
                        </li>
                    </ul>''', unsafe_allow_html=True)
    with cols_dom_energia[1]:
        tem_energia = dados.query("V509_first == 'Utiliza ao menos uma fonte de energia elétrica'").shape[0]
        total = dados.V509_first.shape[0]
        acesso_energia = tem_energia/total

        labels = ["Tem energia elétrica", "Não tem energia elétrica"]
        values = [acesso_energia, 1 - acesso_energia]

        fig = go.Figure( data=[ go.Pie(labels=labels, values = values, marker_colors=["#fec52b","#ffe8aa"], hole = 0.6) ] )

        # Ajustando o layout do gráfico
        fig.update_layout(width=500, height=400, font_family = 'Open Sans', font_color= "black", title_font_color= "black",
                        title_font_size=24, title_text='Domicílios pelo acesso à energia elétrica' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>',
                        showlegend=False, annotations=[dict(text=f'<b>{acesso_energia*100:.1f}%</b>', x=0.5, y=0.4, font_size=28, 
                                                            showarrow=False)])

        # Adicionando imagens
        img_5 = Image.open("images/moradia-img05-lampada.png")
        fig.add_layout_image(dict(source=img_5, x=0.5, y=0.62))
        fig.update_layout_images(dict(xref="paper", yref="paper", sizex=0.3, sizey=0.3, xanchor="center", yanchor="middle"))

        fig.update_traces(hoverinfo='label+percent', textinfo='none')
        fig.add_annotation(text='Fonte: <a href="https://www.flaticon.com/br/icones-gratis/lampada">Lampada ícones criados por Freepik - Flaticon</a>',
                        align="left", xref="paper", yref = "paper", x=1, y=-0.2, showarrow=False, font_size=10)
        st.plotly_chart(fig)

    st.markdown('## Acesso à bens e serviços')
    st.markdown(''' <p style='font-size:20px;'>
                    A descrição do acesso a bens de consumo e serviços é um aspecto relevante na análise das condições de vida das moradias e população.
                    O acesso a consumo de bens duráveis, tem relação com a capacidade de operar funcionamentos importantes para a realização social de
                    uma população ou grupo.
                    </p>
                    <br>
                    ''', unsafe_allow_html=True)

    cols_dom_celular = st.columns(2)
    with cols_dom_celular[0]:
        dom_celular = dados.V512_first.value_counts().to_frame().reset_index()
        dom_celular.columns = ["n_celulares", "qtd"]

        fig = px.histogram(dom_celular, x="n_celulares", y="qtd",  color="n_celulares", text_auto=True, 
                        color_discrete_sequence=["#001932"], nbins=8)

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=400, font_family = 'Open Sans', font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Domicílios pelo nº de moradores que possuem celular' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', 
                        yaxis_title='Nº de Domicílios', xaxis_title='Nº de Moradores que possuem celular', xaxis_tickfont_size=14, 
                        yaxis_tickfont_size=14, yaxis_range = [0,260], plot_bgcolor= "#f8f9fa", showlegend=False, bargap=0.1)

        fig.update_traces(textfont_size=20, textposition="outside", texttemplate='<b>%{y}</b>', cliponaxis=False)
        fig.update_xaxes(tickmode='array', tickvals=np.arange(0,8))

        # Adicionando imagens
        img_6 = Image.open("images/moradia-img06-celular.png")
        fig.add_layout_image(dict(source=img_6, x=0.9, y=0.55))
        fig.update_layout_images(dict(xref="paper", yref="paper", sizex=0.4, sizey=0.4, xanchor="right", yanchor="bottom"))

        fig.add_annotation(text='Fonte: <a href="https://www.flaticon.com/br/icones-gratis/telefone">Telefone ícones criados por prettycons - Flaticon</a>',
                        align="left", xref="paper", yref = "paper", x=1, y=-0.3, showarrow=False, font_size=10)
        st.plotly_chart(fig)
    with cols_dom_celular[1]:
        st.markdown('''<ul class="font-text-destaques">
                    <br><br>
                        <li> Na PSE 2020, podemos notar que <font color='red'><b>apenas 3 domicílios não possuem sequer um morador com o porte de telefone 
                        celular</b></font>, ou seja, em <b>99,5%</b> dos domicílios esse bem é presente, com maior concentração entre 2 ou 3 moradores por domicílio. 
                        </li>
                    <br>
                        <li> Já, <font color='red'><b>a telefonia fixa convencional está em apenas 29,7% dos domicílios</b></font>. A presença desse serviço é de 
                        <b>26,8%</b> nacionalmente e <b>38,9%</b> na região Sudeste. 
                        </li>
                    </ul>''', unsafe_allow_html=True)

    cols_dom_tv = st.columns(2)
    with cols_dom_tv[0]:
        st.markdown('''<ul class="font-text-destaques">
                    <br><br>
                        <li> Segundo a pesquisa, em <font color='red'><b>639 dos 654 domicílios existe ao menos um aparelho de televisão</b></font>, ou seja, 
                        apenas 15 não declaram a existência desse bem. A prevalência da existência desse bem é praticamente a mesma da observada na região
                        Sudeste (<b>97,7% contra 97,8%</b>) e um pouco acima da nacional com <b>96,4%</b>.
                        </li>
                    <br>
                        <li> Outro bem praticamente universal nas casas é a <font color='red'><b>presença de geladeira ou freezer, em 99,8% dos domicílios 
                        pesquisados</b></font>. Outro ponto curioso é que os 4 domicílios sem energia elétrica possuíam esse bem, provavelmente acionados por gás
                        de cozinha, ou seja, o único domicílio sem esse bem possui acesso à energia elétrica.
                        </li>
                    </ul>''', unsafe_allow_html=True)
    with cols_dom_tv[1]:
        dom_tv = dados.V515_first.value_counts().to_frame().reset_index()
        dom_tv.columns = ["tipo", "qtd"]

        fig = px.bar(dom_tv, x="tipo", y="qtd",  color="tipo", text_auto=True,
                    color_discrete_sequence=["#f58334", "#fec52b", "#0367b0", "#ed3237"])

        # Ajustando o layout do gráfico
        fig.update_layout(width=700, height=400, font_family = 'Open Sans', font_color= "black", 
                        title_font_color= "black", title_font_size=24, title_text='Domicílios com aparelhos de TV' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>', 
                        yaxis_title='', xaxis_title='', xaxis_tickfont_size=14, yaxis_tickfont_size=14, 
                        yaxis_range = [0,590], plot_bgcolor= "#f8f9fa", showlegend=False)

        fig.update_traces(textfont_size=20, textposition="outside", texttemplate='<b>%{y}</b>', cliponaxis=False)
        fig.update_xaxes(tickmode='array', tickvals=np.arange(0,4), ticktext = ["Sim, somente<br>de tela fina (LED,<br>LCD ou plasma)", 
                                                                                "Sim, somente<br>de tubo", "Sim, de tela fina<br>e de tubo",
                                                                                "Não"])
        # Adicionando imagens
        img_7 = Image.open("images/moradia-img07-televisao.png")
        img_8 = Image.open("images/moradia-img08-televisao.png")
        fig.add_layout_image(dict(source=img_7, x=0.55, y=0.55))
        fig.add_layout_image(dict(source=img_8, x=0.85, y=0.55))
        fig.update_layout_images(dict(xref="paper", yref="paper", sizex=0.3, sizey=0.3, xanchor="right", yanchor="bottom"))

        fig.add_annotation(text='Fonte: <a href="https://www.flaticon.com/br/icones-gratis/televisao">Televisão ícones criados por Freepik - Flaticon</a>'
                        '<br>Fonte: <a href="https://www.flaticon.com/br/icones-gratis/televisao">Televisão ícones criados por Vignesh Oviyan - Flaticon</a>',
                        align="left", xref="paper", yref = "paper", x=1, y=-0.35, showarrow=False, font_size=10)
        st.plotly_chart(fig)

    cols_dom_pc_net = st.columns(2)
    with cols_dom_pc_net[0]:
        # Domicílios com PC
        total = dados.shape[0]
        labels = ["Sim", "Não"]
        tem_pc = dados.query("V516_first == 'Sim'").shape[0]
        values = [tem_pc/total, 1 - tem_pc/total]

        # Domicílios com acesso à internet
        tem_internet = dados.query("V517_first == 'Sim'").shape[0]
        values_2 = [tem_internet/total, 1 - tem_internet/total]

        # Domicílios com acesso à internet móvel
        tem_internet_movel = dados.query("V518_first == 'Sim'").shape[0]
        values_3 = [tem_internet_movel/total, 1 - tem_internet_movel/total]

        from plotly.subplots import make_subplots

        fig = make_subplots(1, 3, specs=[[{'type':'domain'}, {'type':'domain'}, {'type':'domain'}]])
        fig.add_trace(go.Pie(labels=labels, values=values, marker_colors=["#001932","#b3bac2"], hole = 0.6, rotation = 180), 1, 1)
        fig.add_trace(go.Pie(labels=labels, values=values_2, marker_colors=["#001932","#b3bac2"], hole = 0.6, rotation = 0), 1, 2)
        fig.add_trace(go.Pie(labels=labels, values=values_3, marker_colors=["#001932","#b3bac2"], hole = 0.6, rotation = 0), 1, 3)

        #Ajustando o layout do gráfico
        fig.update_layout(width=700, height=400, font_family = 'Open Sans', font_color= "black", title_font_color= "black",
                        title_font_size=24, title_text='Domicílios com computador e acesso à internet' + 
                        '<br><sup size=1 style="color:#555655">Segundo o PSE 2020</sup>',
                        showlegend=False, 
                        annotations=[dict(text=f'<b>{tem_pc/total*100:.1f}%</b>', x=0.11, y=0.4, font_size=18, showarrow=False),
                                    dict(text=f'<b>{tem_internet/total*100:.1f}%</b>', x=0.5, y=0.4, font_size=18, showarrow=False),
                                    dict(text=f'<b>{tem_internet_movel/total*100:.1f}%</b>', x=0.89, y=0.4, font_size=18, showarrow=False)]
                                    )

        fig.update_traces(hoverinfo='label+percent', textinfo='none')

        img_9 = Image.open("images/moradia-img09-pc.png")
        img_10 = Image.open("images/moradia-img10-internet.png")
        img_11 = Image.open("images/moradia-img11-internet_movel.png")
        fig.add_layout_image(dict(source=img_9, x=0.15, y=0.55))
        fig.add_layout_image(dict(source=img_10, x=0.5, y=0.55))
        fig.add_layout_image(dict(source=img_11, x=0.86, y=0.55))
        fig.update_layout_images(dict(xref="paper", yref="paper", sizex=0.2, sizey=0.2, xanchor="center", yanchor="middle"))

        fig.add_annotation(text='Fonte: <a href="https://www.flaticon.com/br/icones-gratis/computador">Computador ícones criados por Freepik - Flaticon</a>'
                        '<br>Fonte: <a href="https://www.flaticon.com/br/icones-gratis/modem">Modem ícones criados por Uniconlabs - Flaticon</a>'
                        '<br>Fonte: <a href="https://www.flaticon.com/br/icones-gratis/wifi-gratis">Wifi grátis ícones criados por Kalashnyk - Flaticon</a>',
                        align="left", xref="paper", yref = "paper", x=1, y=-0.3, showarrow=False, font_size=10)
        st.plotly_chart(fig)
    with cols_dom_pc_net[1]:
        st.markdown('''<ul class="font-text-destaques">
                    <br><br>
                        <li> O <font color='red'><b>computador e/ou notebook</b></font>, bens que facilitam a operação de funcionamentos para a realização social
                        dos indivíduos, <font color='red'><b>estão presentes em 46,3% dos domicílios</b></font> (por volta de 303 domicílios). Esse número é 
                        superior à média nacional de <b>44,1%</b>, mas bem inferior a média do estado que tem <b>52,3%</b>.
                        </li>
                    <br>
                        <li> Observando o gráfico ao lado, podemos notar o <font color='red'><b> acesso à internet de banda larga fixa presente em 72% das moradias
                        </b></font>, ou seja, 471 domicílios pesquisados, a média nacional é de <b>75,9%</b>. Em relação ao <font color='red'><b> acesso à internet 
                        móvel, 71,7% dos domicílios declaram possuir</b></font>. Esse número é bem abaixo da média nacional e da região Sudeste (<b>80,2%</b> e 
                        <b>84,8%</b>).
                        </li>
                    </ul>''', unsafe_allow_html=True)

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
st.markdown(css, unsafe_allow_html=True)