import pandas as pd
import matplotlib.pyplot as plt
from pywaffle import Waffle
import get_covid19_data

target_day = "2020-06-13"
all_states, cases = get_covid19_data.search(target_day)

top_k = 8
state_top5 = all_states[:top_k]
state_top5.append("Other states")

cases_top5 = cases[:top_k]
cases_top5.append(sum(cases[top_k:]))

n_block = 200
d = sum(cases_top5) // n_block
normal = [v // d for v in cases_top5]

fig = plt.figure(
    FigureClass=Waffle,
    plots={
        '111': {
            'values': normal,
            'labels': [f"{state}, {cases//10**3}k" for state, cases in zip(state_top5, cases_top5)],
            'legend': {'loc': 'upper left', 'bbox_to_anchor': (1.05, 1), 'fontsize': 12},
            'title': {'label': f'# Cases by State on {target_day}', 'loc': 'center', 'fontsize': 18}
        },
    },

    rows=7,
    cmap_name="tab10",
    figsize=(16, 9)
)
plt.savefig(fname="plot_waffle.png")
plt.show()
