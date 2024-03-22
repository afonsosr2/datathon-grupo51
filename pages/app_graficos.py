import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px 
import plotly.graph_objects as go
import numpy as np

df = pd.read_csv("dados/PEDE_PASSOS_DATASET_FIAP-empilhados.csv", sep=",", encoding="utf-8",engine="python", decimal=".")
df.fillna(0,inplace=True)


# Alunos po ano fonte : PEDE2022
alunos_por_ano = pd.DataFrame({"Ano":["2020","2021","2022"],"Alunos":[727,737,929]})

#grafico 1
fig_1 = px.bar(alunos_por_ano, x='Ano', y='Alunos',
             hover_data=["Alunos"],color=pd.Series('Alunos', index=range(len(alunos_por_ano))),
             labels={'Alunos':'Quantidade de Alunos '}, height=500,width=700)

fig_1.update_layout(
    title="Quantidade de Alunos por Ano ",
    xaxis_title="Ano",
    yaxis_title="Alunos ",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"))

df_media = df.iloc[:,[1,2,3,4,5,6,7,8,9]]

df_2020 = df_media.query("Ano == 2020").query("IAA !=0 ").mean()
df_2021 = df_media.query("Ano == 2021").query("IAA !=0 ").mean()
df_2022 = df_media.query("Ano == 2022").query("IAA !=0 ").mean()

df_2020 = pd.DataFrame(df_2020).T
df_2021 = pd.DataFrame(df_2021).T
df_2022 = pd.DataFrame(df_2022).T


df_medias_1 = pd.concat([df_2020,df_2021,df_2022])
df_medias_1['Ano'] = ["2020","2021","2022"]
df_medias_1


fig_2 = go.Figure()
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IAA, name="IAA",
                    ))
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IEG, name="IEG",
                    ))
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IPS, name="IPS",
                    ))
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IDA, name="IDA",
                    ))
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IPP, name="IPP",
                    ))
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IPV, name="IPV",
                    ))
fig_2.add_trace(go.Scatter(x=df_medias_1.Ano, y=df_medias_1.IAN, name="IAN",
                    ))
#grafico 2 
fig_2.update_layout(
    title="Valores médios dos indicadores",
    xaxis_title="Ano",
    yaxis_title="Média",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"))
fig_2.show()


df_2 = pd.read_csv("dados/PEDE_PASSOS_DATASET_FIAP-original.csv", sep=",", decimal=".", encoding="latin-1")
df_2.fillna(0, inplace=True)


df_notas = df_2.iloc[:,[55,56,57]]
df_notas = df_notas.query("NOTA_PORT_2022 !=0 and NOTA_MAT_2022 !=0")
df_medias = pd.DataFrame(df_notas.mean())
df_medias.reset_index(inplace=True)
df_medias.rename(columns={"index":"notas",0:"media"}, inplace=True)
df_medias



#grafico 3
fig_3 = px.bar(df_medias, x='notas', y='media',color=pd.Series('notas', index=range(len(df_medias))),
             labels={'media':'Médias'}, height=500, width=700)

fig_3.add_hline(4.41,annotation_text="Média Nacional de Português e Matematica ")

fig_3.update_layout(
    title=" Médias Portugues e Matematica ",
    xaxis_title="Materias",
    yaxis_title="Médias",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"))
fig_3.show()


df_virada = df_2[["NOME","PONTO_VIRADA_2022"]]
df_virada = df_virada.query("PONTO_VIRADA_2022 !=0")
df_virada = pd.DataFrame(df_virada.groupby("PONTO_VIRADA_2022")["PONTO_VIRADA_2022"].count())
df_virada.rename(columns={"PONTO_VIRADA_2022":"valores"}, inplace=True)
df_virada.reset_index(inplace=True)
df_virada["%"] = [(749/(749+113))*100,(113/(749+113))*100]
df_virada


#grafico4
fig_4 = px.bar(df_virada, x =df_virada["PONTO_VIRADA_2022"],y = df_virada["%"],color="PONTO_VIRADA_2022", height=500, width=700)

fig_4.update_layout(
    title="Ponto de Virada ",
    xaxis_title="Sim ou Não ",
    yaxis_title="Quantidade ",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"))
fig_4.show()


df_est_univer = pd.DataFrame({"Ano":["2020","2021","2022"],"alunos_unv":[24,49,59],"total_alunos":[727,737,929]})
df_est_univer["%_univer"] =(df_est_univer["alunos_unv"]/df_est_univer["total_alunos"])*100
df_est_univer


fig_5 = px.line(df_est_univer, x='Ano', y='%_univer',color=pd.Series('Ano', index=range(len(df_medias))),
             labels={'%_univer':'Percentual de alunos na universidade'},markers= True, width=700)


#Grafico_5
fig_5.update_layout(
    title=" Percentual de alunos universitários ",
    xaxis_title="Ano",
    yaxis_title="Percentual %",
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"))
fig_5.show()


