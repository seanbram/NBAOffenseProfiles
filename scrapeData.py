from nba_api.stats.endpoints import synergyplaytypes
import os
import json

playTypes = ['Transition', 'Isolation', 'PRBallHandler', 'PRRollman', 'Postup','Spotup','Handoff','Cut','OffScreen','OffRebound','Misc']

custom_headers = {
    'Host': 'stats.nba.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
}

for playName in playTypes:
    print(playName)

    play_info = synergyplaytypes.SynergyPlayTypes(play_type_nullable=playName,
    player_or_team_abbreviation='P',
    type_grouping_nullable='offensive', headers=custom_headers)
    data = play_info.get_normalized_dict()
    filename = playName + '.json'
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=2)