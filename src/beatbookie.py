#Python Translation
#need to edit input 
def beatbookie(data,bet,marg):
	money = [0]
	m = 1
	accuracy = []
	acc = 1
	nGames = len(data)
	bet_games = []
	ids = []
	nValidOdds = 2
	max_odds_arr = []
	mean_odds_arr = []


	for i in nGames:
		score_home = data['home_score'][i]
		score_away = data['away_score'][i]
		if score_home > score_away:
			result = 0
		else:
			result = 1

	averages = (data[['avg_odds_home_win, avg_odds_away_win']][i])
	maximums = (data[['max_odds_home_win, max_odds_away_win']][i])
	counts = (data[['n_odds_home_win','n_odds_away_win']][i])

	earn_margin = (1/averages - marg)*(maximums - 1) #TODO: we dont check whether there is more than 3 odds


	if sum(earn_margin > 0) >= 1: #are there any positive bets?
		bet_result_idx = np.argmax(earn_margin)
		possible_earn = bet*(maximums[bet_result_idx] -1)

		max_odds = maximums[bet_result_idx]
		max_odds_arr.append(max_odds)
		mean_odds = averages[bet_result_idx]
		mean_odds_arr.append(mean_odds)

		ids.append(bet_result_idx)

		if bet_result == result: #if we were right
			money.append(money[i] + possible_earn)
			accuracy.append(1)
		else:
			money.append(money[i] - bet)
			accuracy.append(0)

		bet_games.append(i)

	return money,max_odds_arr,mean_odds_arr,bet_games,ids
