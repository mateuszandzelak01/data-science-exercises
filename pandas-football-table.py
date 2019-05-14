import pandas as pd

prem_table = pd.read_html('https://www.bbc.co.uk/sport/football/premier-league/table')
p_table = prem_table[0]

p_league = p_table.drop(['Unnamed: 1'], axis=1)
print(p_league.head(6))

p_league[['F','A', 'P', 'W', 'D', 'L', 'GD', 'Pts']] = p_league[['F','A', 'P', 'W', 'D', 'L', 'GD', 'Pts']].apply(pd.to_numeric, errors='coerce')

p_league = p_league.drop(p_league.tail(1).index)
p_league.rename(columns={'Unnamed: 0':'Position'}, inplace=True)

p_league['Goal Ratio'] = round(p_league['F']/p_league['A'], 1)
p_league = p_league[['Position','Team', 'P', 'W', 'D', 'L','F','A','Goal Ratio','GD','Pts']]

p_league['Goals/game'] = round((p_league.F / p_league.P), 1)
p_league['Goals conceded/game'] = round((p_league['A'] / p_league['P']), 1)
print(p_league.sort_values(['Goals/game', 'Goal Ratio']).head(5))

goal_differnce = p_league.loc[17, 'GD'] - p_league.loc[16, 'GD']

print('The goal difference between Cardiff and Brighton is ' + str(goal_differnce))