import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pywaffle import Waffle
from plotly import express as px
from plotly import graph_objs as go

###### Configuração Inicial ######
@st.cache_data
def config_inicial():
    df = pd.read_excel("dados/PSE2020_domicílios.xlsx", sheet_name = "PSE2020_domicílios")
    # Retirando as colunas do ano (todos são 2020) e entrevistador(a)
    cols_a_retirar = ["V100_first", "V101_first", "V106_first", "filter_$"]
    dados = df.drop(columns=cols_a_retirar)
    return dados

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
with tabs[0]:
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
                        <li> Em relação à <font color='red'><b>condição de vida</b></font>, Embu-Guaçu possui indicadores de pobreza
                             e vulnerabilidade abaixo do Brasil (<b>36,99%</b> contra <b>54,38%</b>), porém extremamente 
                             elevado em relação à <b>RMSP</b> e o <b>Estado de São Paulo</b> (<b>22,8%</b> e <b>21,95%</b>). 
                             Praticamente <b>60%</b> das crianças em Embu-Guaçu estão nessas condições adversas.
                        </li>
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
    st.markdown("")
    cols_destaque_contexto = st.columns(2)
    with cols_destaque_contexto[0]:
        st.markdown("<p class='font-text-destaques'>Principais destaques sobre Demografia</p>", unsafe_allow_html=True)
    with cols_destaque_contexto[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> A <font color='red'><b>PSE 2020</b></font> trouxe dados de <b>784</b> alunos da <b>Associação Passos Mágicos</b>.
                             Considerando a população de <b>68.053</b> habitantes em 2020 (SEADE, 2020), a pesquisa representa <b>4% da 
                             população</b> do município.
                        </li>
                        <li> <font color='red'><b>Na faixa entre 5 a 19 anos de idade</b></font> na pesquisa temos <b>1.137</b> crianças e
                             jovens. Considerando os dados apenas nos domicílios entrevistados, <b>353</b> jovens ainda não foram atendidos
                             pela APM. 
                        </li>
                        <li> Extrapolando a população dessa faixa etária para <b>42,5%</b> e uma população de <b>68.053</b> habitantes,
                             <b>28.923</b> seriam de crianças e jovens. <font color='red'><b>Aproximadamente 17.350 crianças e jovens</b></font>
                             como público potencial da APM (<b>60%</b> da população socialmente vulnerável).
                        </li>
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
        pct_mulheres = (100 *mulheres/total).round(0)
        pct_homens = (100 * homens/total).round(0)

        data = {'Mulheres': pct_mulheres, 'Homens': pct_homens}
        fig = plt.figure(FigureClass=Waffle, rows=5, values=data, colors=["#f58334", "#0367b0"],
                        title={'label': 'População total por sexo', 'loc': 'left', 'size':10},
                        labels=[f"{k} ({v:.0f}%)" for k, v in data.items()],
                        legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0},
                        starting_location='NW', block_arranging_style='snake')
        st.pyplot(fig)
    with cols_pop_sexo[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> O recorte da pesquisa engloba <font color='red'><b>4% do total da população</b></font> de Embu-Guaçu, uma amostra considerável.
                        </li>
                        <li> Da população pesquisada, <font color='red'><b>1.452 são mulheres</b></font>, representando aproximadamente <b>54%</b>
                             do total, e <font color='red'><b>1.221 moradores são homens</b></font>, representando <b>46%</b> do total.
                        </li>
                        <li> A <font color='red'><b>proporção entre homens e mulheres</b></font> em Embu-Guaçu em 2020 é de <b>50,5%</b> de mulheres
                     e <b>49,5%</b> de homens. O ligeiro afastamento em relação a pesquisa pode ser explicado pelo recorte socioeconômico.  
                        </li>
                    </ul>''', unsafe_allow_html=True)

    st.markdown('#')
    st.markdown('#')    

    cols_pop_cor_raca = st.columns(2)
    with cols_pop_cor_raca[0]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> Com relação à <font color='red'><b>distribuição da população por raça e cor</b></font>, as proporções da 
                             população total do Brasil se assemelham ao de Embu-Guaçu, que podemos observar na imagem ao lado
                        </li>
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
        pct_mulheres = (100 * domicilio_sexo_resp.loc["Mulheres"]/total).round(0)
        pct_homens = (100 * domicilio_sexo_resp.loc["Homens"]/total).round(0)

        data = {'Mulheres': pct_mulheres, 'Homens': pct_homens}
        fig = plt.figure(FigureClass=Waffle, rows=5, values=data, colors=["#f58334", "#0367b0"],
                title={'label': 'Total de domicílios por sexo do responsável', 'loc': 'left', 'size':10},
                labels=[f"{k} ({v:.0f}%)" for k, v in data.items()],
                legend={'loc': 'lower left', 'bbox_to_anchor': (0, -0.4), 'ncol': len(data), 'framealpha': 0},
                starting_location='NW', block_arranging_style='snake')
        
        st.pyplot(fig)
    with cols_dom_sexo[1]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> Embu-Guaçu tem um total projetado de <b>22.112</b> domicílios em 2020 (SEADE, 2020). Este recorte da pesquisa 
                             engloba <font color='red'><b>3% do total de domicílios</b></font> do município.
                        </li>
                        <li> Dos responsáveis pelo domicílio, <font color='red'><b>354 são mulheres</b></font>, representando aproximadamente <b>54%</b>
                             do total, e <font color='red'><b>300 moradores são homens</b></font>, representando <b>46%</b> do total.
                        </li>
                        <li> A <font color='red'><b>vantagem numérica dos domicílios chefiados por mulheres</b></font> foi destacado nos dados 
                             demográficos dos domicílios entrevistados de Embu-Guaçu, principalmente pelos arranjos familiares.
                        </li>
                    </ul>''', unsafe_allow_html=True)

    st.markdown('#')
    st.markdown('#')

    cols_dom_cor_raca = st.columns(2)
    with cols_dom_cor_raca[0]:
        st.markdown('''<ul class="font-text-destaques">
                        <li> A <font color='red'><b>distribuição por cor e raça dos responsáveis dos domicílios</b></font>, tem relação
                             direta com os dados da população da amostra e, consequentemente, com a proporção da população total do Brasil.
                             Isso evidencia uma homogeneidade dos domicílios quanto a característica dos indivíduos, em que a frequência de
                             domicílios heterogêneos são pouco significativos.
                        </li>
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
                        <li> Observando o gráfico ao lado, com a distribuição dos domicílios na pesquisa, podemos notar <font color='red'><b>uma concentração
                             maior dos domicílios entrevistados com 4 moradores</b></font> tanto na média, quanto na moda e mediana.
                        </li>
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
                        <li> Dos <font color='red'><b>arranjos monoparentais, mais de 90% são de mulheres</b></font>, acima dos <b>83,3%</b> de Embu-Guaçu dada pelo Censo do IBGE em 2010.
                             Dos <font color='red'><b>arranjos de união ou casamento, em 38,6% dos casos a mulher é a responsável pelo domicílio</b></font>.
                        </li>
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