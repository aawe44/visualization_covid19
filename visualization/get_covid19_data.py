import pandas as pd


def search(target_day):
    df = pd.read_csv(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv",
        dtype={'fips': 'str'}
    )
    all_states = set(df["state"])

    cases_by_state = {}
    df_today = df[df["date"] == target_day]

    for state in all_states:
        cases_by_state[state] = sum(df_today[df_today["state"] == state]["cases"])

    all_states = list(all_states)
    all_states.sort(key=lambda x: -cases_by_state[x])
    cases = [cases_by_state[x] for x in all_states]

    return all_states, cases


