import matplotlib.pyplot as plt
import get_covid19_data

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

plt.title(f"US cases on {target_day}")
plt.savefig(fname="plot_bar.png")

plt.show()
