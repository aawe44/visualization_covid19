import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv(
    "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv",
    dtype={'fips': 'str'}
)

all_states = set(df["state"])
all_dates = sorted(list(set(df["date"])))

today = all_dates[-1]

date_to_AllState = []

n = len(all_dates)

cases_by_state = {}
df_today = df[df["date"] == today]

for state in all_states:
    cases_by_state[state] = sum(df_today[df_today["state"] == state]["cases"])

all_states = list(all_states)
all_states.sort()
cases = [cases_by_state[x] for x in all_states]

all_states.sort(key=lambda state: -cases_by_state[state])
cases.sort(key=lambda x: -x)

state_top5 = all_states[:5]
state_top5.append("Other states")
today = "2020-03-15"
idx = 0
for i, date in enumerate(all_dates):
    if date == today:
        idx = i
        break
all_dates = all_dates[idx:]

date_to_AllState = []

n = len(all_dates)
import collections

for i in range(n):
    today = all_dates[i]
    cases_by_state = collections.defaultdict(int)
    df_today = df[df["date"] == today]

    for state in all_states:
        if state in state_top5:
            cases_by_state[state] = sum(df_today[df_today["state"] == state]["cases"])
        else:
            cases_by_state["Other states"] += sum(df_today[df_today["state"] == state]["cases"])

    cases = [cases_by_state[x] for x in state_top5[::-1]]

    date_to_AllState.append(cases)

rev = np.array(date_to_AllState).transpose()

plt.figure(figsize=(16, 9))
pal = sns.color_palette("Set1")

plt.stackplot(all_dates, rev, labels=state_top5[::-1], colors=pal, alpha=0.5)

plt.xlabel('Date')
plt.ylabel('Cases')
plt.title("Stackplot of cases by state")
plt.legend(loc="upper left")

ax = plt.gca()
ax.set_xticklabels([all_dates[i][-5:] if i % 10 == 0 else "" for i in range(len(all_dates))])

plt.savefig(fname="plot_stack.png")
plt.show()
