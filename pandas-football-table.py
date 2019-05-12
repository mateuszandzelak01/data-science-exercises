import pandas as pd

prem_table = pd.read_html('https://www.bbc.co.uk/sport/football/premier-league/table')
p_table = prem_table[0]

p_league = p_table.drop(['Unnamed: 1'], axis=1)
print(p_league.head(6))

p_league[['F','A', 'P', 'W', 'D', 'L', 'GD', 'Pts']] = p_league[['F','A', 'P', 'W', 'D', 'L', 'GD', 'Pts']].apply(pd.to_numeric, errors='coerce')

p_league.drop(p_league.tail(1).index)
p_league.rename(columns={'Unnamed: 0':'Position'}, inplace=True)


