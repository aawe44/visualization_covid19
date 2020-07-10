import squarify
import matplotlib.pyplot as plt
import get_covid19_data

target_day = "2020-06-13"
all_states, cases = get_covid19_data.search(target_day)

top_k = 20
state_top5 = all_states[:top_k]
state_top5.append("Other states")

cases_top5 = cases[:top_k]
cases_top5.append(sum(cases[top_k:]))

state_to_cases = {state: cases for state, cases in zip(state_top5, cases_top5)}

cases_top5.sort()
state_top5.sort(key=lambda x: state_to_cases[x])

set1 = plt.get_cmap("tab20").colors

plt.figure(figsize=(20, 8))

squarify.plot(
    sizes=cases_top5,
    label=state_top5,
    color=set1,
    alpha=.7)
plt.axis('off')
plt.title(f"Treemap of cases to states on {target_day}")
plt.savefig(fname="plot_treemap.png")
plt.show()
