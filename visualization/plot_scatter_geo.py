import plotly.express as px
import math
import numpy as np
import pandas as pd

df = pd.read_csv(
    "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv")

maxsize_norm = max(np.log(df["5/18/20"]))
minsize_norm = 0

list_dates = df.columns[4:]
list_other = df.columns[1:4]

# expand stuff
columns = ['Country', 'Lat', 'Long', 'Date', 'Cases', 'CasesLog']
df_expand = pd.DataFrame(columns=columns)
df_expand['Country'] = df_expand['Country'].astype(str)
df_expand['Cases'] = df_expand['Cases'].astype(float)
df_expand['CasesLog'] = df_expand['CasesLog'].astype(float)
list_expandrows = []
for index, row in df.iterrows():
    country = row['Country/Region']
    lat = row['Lat']
    longt = row['Long']
    for date in list_dates:
        # add row into df_expand
        cases = row[date]
        if (row[date] == 0):
            cases_log = 0
        else:
            cases_log = int(math.log(float(row[date])) * 10)
        row_expand = {'Country': country, 'Lat': lat, 'Long': longt, 'Date': date, 'Cases': cases,
                      'CasesLog': cases_log}
        # print(row_expand)
        list_expandrows.append(row_expand)
        # break
    # break
df_expand = df_expand.append(list_expandrows, ignore_index=True)
df_expand['text'] = df_expand['Country'] + ":" + df_expand['Cases'].astype(str)

fig = px.scatter_geo(
    df_expand,
    lon='Long',
    lat='Lat', color="CasesLog",
    hover_data=['Cases'],
    hover_name="Country", size="CasesLog",
    animation_frame="Date",
    projection="natural earth")

fig.update_layout(
    title={'text': 'COVID-19 Global Confirmed Cases',
           'x': 0.5,
           'xanchor': 'center'},
    geo_scope='world', )

fig.show()
