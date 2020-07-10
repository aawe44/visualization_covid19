import bar_chart_race as bcr
import pandas as pd

target_day = "2020-03-15"

df = pd.read_csv(
    "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv",
    dtype={'fips': 'str'}
)

all_states = sorted(list(set(df["state"])))
all_dates = sorted(list(set(df["date"])))

idx = 0
for i, date in enumerate(all_dates):
    if date == target_day:
        idx = i
        break

all_dates = all_dates[idx:]

date_to_AllState = []

n = len(all_dates)

for i in range(n):
    today = all_dates[i]
    cases_by_state = {}
    df_today = df[df["date"] == today]

    for state in all_states:
        cases_by_state[state] = sum(df_today[df_today["state"] == state]["cases"])

    cases = [cases_by_state[x] for x in all_states]
    date_to_AllState.append(cases)

df_date_to_US = pd.DataFrame(date_to_AllState, index=all_dates, columns=all_states)
df_date_to_US = df_date_to_US.fillna(0)

period_length = 200
RaceRunTime = n * period_length / 1000

filename = "bar_chart_race_v1.mp4"
bcr.bar_chart_race(
    df=df_date_to_US,
    n_bars=10,
    period_length=period_length,
    filename=filename,
)
