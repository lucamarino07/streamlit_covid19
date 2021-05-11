
import streamlit as st
import pandas as pd

from datetime import datetime

url = "https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-regioni/dpc-covid19-ita-regioni-latest.csv"
df = pd.read_csv(url, parse_dates=['data'])


st.title("COVID-19 NELLE REGIONI ITALIANE 🦠")

st.header("Seleziona una regione per visualizzare un riepilogo dei dati")




# col1.select_slider('REGIONE')


df = df.rename(columns={'long': 'lon'})


regione = st.selectbox('REGIONE', options=list(df['denominazione_regione']))



df_regione = df[df['denominazione_regione'] == regione]
st.map(df_regione[['lon', 'lat']], zoom=7)
col1, col2 = st.beta_columns(2)
# st.dataframe(df_regione)
col1.write(f"🔘 Casi Totali: {df_regione['totale_casi'].values[0]}")
col1.write(f"🔘 Nuovi Positivi: {df_regione['nuovi_positivi'].values[0]}")
col1.write(f"🔘 Tamponi Effettuati: {df_regione['tamponi'].values[0]}")


col2.write(f"🟢 Guariti: {df_regione['dimessi_guariti'].values[0]}")
col2.write(f"🟠 Terapia Intensiva: {df_regione['terapia_intensiva'].values[0]}")
col2.write(f"🔴 Deceduti: {df_regione['deceduti'].values[0]}")



# st.write("Prova Form")

# form = st.form(key='my_form')
# nome = form.text_input(label='Nome')
# cognome = form.text_input(label='Cognome')
# submit = form.form_submit_button(label='Submit', )


# if submit:
#     st.header(f"Ciao {nome} {cognome}")

# df = pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv", parse_dates=['data'])


# df_result = pd.DataFrame(columns=['data', 'y', 'tipologia', 'giorni'])

# data_inizio = st.date_input("Data Inizio")





# for index, row in df.iterrows():

#     df_result = df_result.append({
#         'data': row['data'],
#         'y': row['totale_casi'],
#         'tipologia': 'Casi totali',
#         'giorni': index + 1
#     }, ignore_index=True)

# for index, row in df.iterrows():
#     df_result = df_result.append({
#         'data': row['data'],
#         'y': row['totale_positivi'],
#         'tipologia': 'Totale positivi',
#         'giorni': index + 1
#     }, ignore_index=True)

# for index, row in df.iterrows():
#     df_result = df_result.append({
#         'data': row['data'],
#         'y': row['dimessi_guariti'],
#         'tipologia': 'Guariti',
#         'giorni': index + 1
#     }, ignore_index=True)
# for index, row in df.iterrows():
#     df_result = df_result.append({
#         'data': row['data'],
#         'y': row['deceduti'],
#         'tipologia': 'Deceduti',
#         'giorni': index + 1
#     }, ignore_index=True)

# st.dataframe(df_result)




# a = df_result[df_result['data'] == data_inizio]
# st.dataframe(a)




# fig = px.bar(df_result, x="y", y="tipologia", color='tipologia',
#   animation_frame='giorni', animation_group="tipologia",orientation='h', range_x=[0, max(df_result['y'])], labels='y')

# st.plotly_chart(fig)
# fig.show()
