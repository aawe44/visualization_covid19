import pandas as pd
import matplotlib.pyplot as plt

import sys

from .. import get_covid19_data

# import get_covid19_data

# df = pd.read_csv(
#     "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv",
#     dtype={'fips': 'str'}
# )
# all_states = set(df["state"])
#
# cases_by_state = {}
# df_today = df[df["date"] == "2020-06-13"]
#
# for state in all_states:
#     cases_by_state[state] = sum(df_today[df_today["state"] == state]["cases"])
#
# all_states = list(all_states)
# all_states.sort(key=lambda x: -cases_by_state[x])
# cases = [cases_by_state[x] for x in all_states]

target_day = "2020-06-13"
all_states, cases = get_covid19_data.search(target_day)

colors = plt.get_cmap("Set1").colors

k = 10
state_top_k = all_states[:k]
cases_top_k = cases[:k]

state_top_k.reverse()
state_top_k.append("Other states")

cases_top_k.reverse()
cases_top_k.append(sum(cases[k:]))

plt.figure(figsize=(15, 5))

plt.bar(state_top_k,
        cases_top_k,
        color=colors,
        edgecolor=colors,
        alpha=0.5)
# plt.xticks(rotation="vertical")
plt.title(f"US cases on {target_day}")

plt.show()
