import requests
import json

league_id = 828182
seasonId = 2019

swid = "{6F54577E-8DA7-42DE-BF11-5B2F0B3302F3}"
espn_s2= "AECSnQpVaYbK6Vlw4OQiNkU8K%2BCFRnVLl9gLrjq%2Fc6E9km1gyDHTogLSBLJjOFw35q8id4GBg8uzvyAqrQsJwB7FxaEU%2BfQ1kwVypUqThXCH4QiM80muvx2AYHvSDRWElk0atS3ChTcmEBpy9bWnkU3vOjgDqnPBmr94f8qqanpwtD9kU4qu1t%2Fi3jITm%2FvnyxQajUlLbpFND6MNCz44y84%2BPcsIom045lH4OFFRiyFubM4NFW2hfmkcLDYj8rusvEsehuY%2BRODJcC1eULhIEEIFBnR1RJ2cMFk4HrPFf5BDKA%3D%3D"

curUrl = "https://fantasy.espn.com/apis/v3/games/ffl/seasons/" + str(seasonId) + "/segments/0/leagues/" + str(league_id)

# View params - stats, scoringPeriodID, players_wl, kona_playercard, kona_player_info, proTeamSchedules_wl, kona_game_state, mDraftDetail, mLiveScoring, mMatchupSCore, mPendingTransactions, mPositionalRatings, mRoster, mSettings, mTeam, module, mNav
# Alternate params - rosterForTeamID=num, 
# Other url
# https://fan.api.espn.com/apis/v2/fans/%7B6F54577E-8DA7-42DE-BF11-5B2F0B3302F3%7D?displayEvents=true&displayNow=true&displayRecs=true&displayHiddenPrefs=true&featureFlags=expandAthlete&featureFlags=isolateEvents&recLimit=5

league = requests.get(curUrl, params={'view': 'stats'}, cookies={'espn_s2': espn_s2, 'swid':swid})

with open('stats.txt', 'w') as f:
  print(json.dumps(league.json(), indent=4), file=f)