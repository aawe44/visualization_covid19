import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import get_covid19_data

target_day = "2020-06-13"
all_states, cases = get_covid19_data.search(target_day)

top_k = 4
state_top5 = all_states[:top_k]
state_top5.append("Other states")

cases_top5 = cases[:top_k]
cases_top5.append(sum(cases[top_k:]))

pal = sns.color_palette("husl")
plt.figure(figsize=(16, 9))
plt.pie(
    cases_top5,
    labels=state_top5,
    autopct="%0.0f%%",
    colors=pal,
    textprops=dict(color="w"))

ax = plt.gca()
ax.legend(
    title="States",
    loc="center left",
    bbox_to_anchor=(1, 0, 0.5, 1))

plt.title(f"Pie chart of cases to states on {target_day}")
plt.savefig(fname="plot_pie.png")
plt.show()
