
#############################################################
ORIG_HITTER_DATA = 'DATA\\Hitter Data\\ORIGINAL'
TRANS_HITTER_DATA = 'DATA\\Hitter Data\\TRANSFORMED'

ORIG_SCHEDULES = 'DATA\\Schedules and Results\\Original'
TRANS_SCHEDULES = 'DATA\\Schedules and Results\\Transformed'

ORIG_PITCHER_DATA = 'DATA\Pitcher Data\\ORIGINAL'
TRANS_PITCHER_DATA = 'DATA\Pitcher Data\\TRANSFORMED'

PARK_DATA = 'DATA\Park Scores'

ORIG_HITTER_CAREER = 'DATA\\Hitter Career Data'
GAME_LOGS = 'DATA\\Game Logs'

OUTPUT = 'MODEL_OUTPUT'

R_FOLDER = '_With R'
#############################################################

#FEATURES = ['AB','platoon','era','whip','h9','hr9','bb9','so9','is_home']
FEATURES = ['AB','era','platoon','is_home','Park_R','Park_HR']
TARGET = 'FANTASY_PTS'

#############################################################

#Reconcile abbrev differences in BaseballMusings.com and BaseballReference.com
baseballRef_to_baseballMus = {
    'ARI': 'ARI',
    'ATL': 'ATL',
    'BAL': 'BAL',
    'BOS': 'BOS',
    'CHC': 'CHN',
    'CHW': 'CHA',
    'CIN': 'CIN',
    'CLE': 'CLE',
    'COL': 'COL',
    'DET': 'DET',
    'HOU': 'HOU',
    'KCR': 'KCA',
    'LAA': 'LAA',
    'LAD': 'LAN',
    'MIA': 'MIA',
    'MIL': 'MIL',
    'MIN': 'MIN',
    'NYM': 'NYN',
    'NYY': 'NYA',
    'OAK': 'OAK',
    'PHI': 'PHI',
    'PIT': 'PIT',
    'SDP': 'SDN', 
    'SEA': 'SEA',
    'SFG': 'SFN',
    'STL': 'SLN',
    'TBR': 'TBA',
    'TEX': 'TEX',
    'TOR': 'TOR',
    'WSN': 'WSH'
    }
#############################################################

players_urls0 = {
    'Mookie_Betts':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=11%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=13611',
    'Brock_Holt':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=11%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9345',
    'Ortiz':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=11%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=745',
    'Travis_Shaw':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=11%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11982',
    'Dustin_Pedroia':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=11%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=8370',
    'Jackie_Bradley':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=11%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12984',
    'Coco_Crisp':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=11%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=1572',
    'Xander':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=11%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12161',
    'Bryce_Harper':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=11%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11579',
    'Kev_Pillar':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=11%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12434',
    'Granderson':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4747',
    'A_Gonzalez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=11%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=1908',
    'Jayson_Werth':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F30%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=1327',
    'Brad_Miller':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=11%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12775',
    'Buster_Posey':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9166',
    'Chris_Carter':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9911',
    'Kris_Bryant':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=15429',
    'Altuve':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5417',
    'Cano':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3269',
    'Yasmany_Tomas':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=17171',
    'Justin_Turner':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5235',
    'Wil_Myers':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10047',
    'Howie_Kendrick':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4229',
    'Jacoby':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4727',
    'Edwin_Encarnacion':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=2151',
    'Mike_Napoli':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3057',
    'Todd_Frazier':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=785',
    'Brett_gardner':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9927',
    'Yonder_Alonso':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=2530',
    'Carlos_Santana':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=2396',
    'Iglesias':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10231',
    'Elvis_Andrus':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=8709',
    'Manny_Machado':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11493',
    'Jose_Abreu':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=15676',
    'Ian_Kinsler':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=6195',
    'Dozier':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F07%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9810',
    'Schoop':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F25%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11265',
    'Carlos_Correa':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F08%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=14162',
    'Joey_Votto':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F04%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4314',
    'Charlie_Blackmon':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F07%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=7859',
    'Starling_Marte':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F26%2F2016&EndDate=09%2F27%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9241',
    'Ryan_Braun':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=01%2F25%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3410',
    'Espinosa':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9219',
    'Chase_Utley':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=1679',
    'Denard_Span':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=8347',
    'McCutchen':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F04%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9847',
    'Dexter_Fowler':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F02%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4062',
     "Miguel_Cabrera":
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=1744',
    'Melky Cabrera':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4022',
    'Keon_Broxton':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=4%2F01%2F2016&EndDate=09%2F16%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9253',
    'Jose_Ramirez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=13510',
    'JD_Martinez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=6184',
    'Yunel_Escobar':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4191',
    'Francisco_Lindor':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12916',
    'Adrian_Beltre':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=639',
    'Carlos_Beltran':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=589',
    'Victor_Martinez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=393',
    'Nelson_Cruz':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=2434',
    'Hanley_Ramirez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F02%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=8001',
    'Ian_Desmond':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F02%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=6885',
    'Adam Eaton':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11205',
    'Josh_Donaldson':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5038',
    'Kyle_Seager':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9785',
    'Didi_Gregorius':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=6012',
    'Jason_Kipnis':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9776',
    'Cheslor_Cuthbert':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10473',
    'Evan_Longoria':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9368',
    'Rougned_Odor':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12282',
    'Kole_Calhoun':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11200',
    'Starlin_Castro':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4579',
    'Albert_Pujols':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F02%2F2016&EndDate=10%2F26%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=1177',
    'DJ_LeMahieu':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=09%2F30%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9874',
    'Daniel_Murphy':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4316',
    'Jean_Segura':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5933',
    'Corey_Seager':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F02%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=13624',
    'Yadier_Molina':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F02%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=7007',
    'Wilson_Ramos':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F02%2F2016&EndDate=09%2F26%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=1433',
    'Martin_Prado':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3312',
    'JT_Realmuto':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F02%2F2016&EndDate=09%2F30%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11739',
    'Freddie_Freeman':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5361',
    'Carlos_Gonzalez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=7287',
    'Christian_Yelich':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11477',
    'Paul_Goldschmidt':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9218',
    'Nolan_Arenado':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9777',
    'Cesar_Hernandez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10556',
    'Anthony_Rizzo':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3473',
    'Ender_Inciarte':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4922',
    'Brandon_Phillips':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F27%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=791',
    'Odubel_Herrera':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11476',
    'Jonathan_Villar':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10071',
    'Josh_Harrison':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=09%2F10%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=8202',
    'Asdrubal_Cabrera':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F08%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4962',
    'Yoenis_Cespedes':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F28%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=13110',
    'Angel_Pagan':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F03%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=2918',
    'Brandon_Belt':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F31%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10264',
    'Brandon_Crawford':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F27%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5343',
    'Stephen_Piscotty':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F21%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=13367',
    'Adonis_Garcia':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F19%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=13777',
    'Ben_Zobrist':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=7435',
    'Matt_Carpenter':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F04%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=8090',
    'Anthony_Rendon':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F21%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12861',
    'Nick_Markakis':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F03%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5930',
    'Matt_Kemp':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F28%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5631',
    'Jarrod_Dyson':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F07%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4866',
    'Dee_Gordon':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F06%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=8203',
    'Billy_Hamilton':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F03%2F2016&EndDate=09%2F04%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10199',
    'Rajai_Davis':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F14%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3708',
    'Hernan_Perez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F09%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5751',
    'Trea_Turner':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F21%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=16252',
    'Mike_Trout':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F08%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10155',
    'Leonys_Martin':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F02%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11846',
    'Chris_Owings':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F03%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10030',
    'Kevin_Kiermaier':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F30%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11038',
    'Jose_Peraza':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F10%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=13593',
    'Gregory_Polanco':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F10%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12907',
    'Mark_Trumbo':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F11%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=6876',
    'Khris_Davis':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9112',
    'Jake_Lamb':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F07%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=13329',
    'Jay_Bruce':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F27%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9892',
    'Jonathan_Lucroy':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F21%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=7870',
    'Adam_Duvall':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F26%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10950',
    'Michael_Saunders':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F25%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9981',
    'Corey_Dickerson':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F22%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10762',
    'Kendrys_Morales':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F23%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=8610',
    'Justin_Upton':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F02%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5222',
    'Chris_Davis':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F26%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9272',
    'George_Springer':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F16%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12856',
    'Marcell_Ozuna':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F30%2F2016&EndDate=09%2F30%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10324',
    'Jose_Bautista':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F04%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=1887',
    'Freddy_Galvis':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F05%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=6609',
    'Maikel_Franco':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F02%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12179',
    'Marcus_Semien':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F04%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12533',
    'Eugenio_Suarez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F04%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12552',
    'Alcides_Escobar':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F03%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=6310',
    'Adam_Jones':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F14%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=6368',
    'Eric_Hosmer':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F06%2F2016&EndDate=09%2F30%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3516',
    'Brandon_Moss':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F06%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4467',
    'Jedd_Gyorko':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10816',
    'Giancarlo_Stanton':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F08%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4949',
    'Yasmani_Grandal':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F02%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11368',
    'Trevor_Story':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F04%2F2016&EndDate=09%2F30%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12564',
    'Ryan_Hanigan':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F09%2F2016&EndDate=09%2F29%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4952',
    'Ryan_Howard':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=2154',
    'Joc_Pederson':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11899',
    'Randal_Grichuk':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F28%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10243',
    'Neil_Walker':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F01%2F2016&EndDate=08%2F27%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=7539',
    'Tommy_Joseph':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F13%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10349',
    'Addison_Russell':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F21%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=14106',
    'Jung-ho Kang':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F08%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=17182',
    'Matt_Holiday':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F16%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=1873',
    'Ryan_Schimpf':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F14%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9953',
    'Sean_Rodriguez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F19%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=6589',
    'Aledmys_Diaz':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F05%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=15937',
    'Zack_Cozart':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F07%2F2016&EndDate=09%2F10%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=2616',
    'Wilmer_Flores':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F06%2F2016&EndDate=09%2F10%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5827',
    'Matt_Adams':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F20%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9393',
    'Cameron_Rupp':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F10%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11146',
    'Brandon_Drury':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11615',
    'Ryan_Zimmerman':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4220',
    'Yangervis_Solarte':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F02%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5352',
    'Justin_Bour':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F05%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9744',
    'Mark_Reynolds':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F16%2F2016&EndDate=09%2F18%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=7619',
    'Welington_Castillo':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F11%2F2016&EndDate=09%2F30%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3256',
    'Derek_Norris':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F21%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=6867',
    'Scooter_Gennett':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F03%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10339',
    'Javier_Baez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F05%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12979',
    'Hunter_Pence':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F28%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=8252',
    'Matt_Joyce':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F05%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3353',
    'Adam_Rosales':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F09%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9682',
    'Pedro_Alvarez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F16%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=2495',
    'Salvador_Perez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F10%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=7304',
    'Brain_McCann':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F10%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4810',
    'Russell_Martin':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F05%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4616',
    'Adam_Lind':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F02%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=8027',
    'Logan_Forsythe':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F04%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=7185',
    'Gary_Sanchez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F03%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11442',
    'Nomar_Mazara':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F10%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=14553',
    'Alex_Gordon':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F02%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5209',
    'Matt_Wieters':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F29%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4298',
    'Steven_Souza':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F13%2F2016&EndDate=09%2F18%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5667',
    'Max_Kepler':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F27%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12144',
    'Stephen_Vogt':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F06%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5000',
    'Evan_Gattis':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F03%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11003',
    'Troy_Tulowitzki':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F30%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3531',
    'Nick_Castellanos':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11737',
    'Seth_Smith':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F16%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=7331',
    'C.J._Cron':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F03%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12546',
    'Mark_Teixeira':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=1281',
    'Colby_Rasmus':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F07%2F2016&EndDate=09%2F18%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9893',
    'Jefry_Marte':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F05%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5107',
    'Franklin_Gutierrez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F31%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3255',
    'Chase_Headley':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F15%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4720',
    'Justin_Smoak':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F23%2F2016&EndDate=09%2F30%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9054',
    'Logan_Morrison':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F27%2F2016&EndDate=09%2F11%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9205',
    'Tyler_Naquin':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F05%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=13359',
    'Dae-Ho_Lee':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F04%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=18722',
    'Carlos_Gomez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F13%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4881',
    'Steve_Pearce':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F01%2F2016&EndDate=09%2F12%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9957',
    'Luis_Valbuena':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F02%2F2016&EndDate=07%2F26%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4969',
    'Marwin_Gonzalez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F06%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5497',
    'Ryon_Healy':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F15%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=15447',
    'Jarrod_Salty':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F02%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5557',
    'Trevor_Plouffe':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F21%2F2016&EndDate=09%2F06%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=7462',
    'Eduardo_Nunez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F19%2F2016&EndDate=09%2F25%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=6848',
    'Brett_Lawrie':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F05%2F2016&EndDate=07%2F21%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5247',
    'Avisail_Garcia':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F31%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5760',
    'James_McCann':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12859',
    'Mike_Zunino':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F12%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=13265',
    'Byung-Ho_Park':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F04%2F2016&EndDate=06%2F28%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=18497',
    'Joe_Mauer':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=09%2F25%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=1857',
    'Jason_Castro':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F22%2F2016&EndDate=09%2F30%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=8722',
    'Robbie_Grossman':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F24%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5254',
    'Devon_Travis':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=13862',
    'Eddie_Rosario':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F06%2F2016&EndDate=09%2F17%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12155',
    'Byron_Buxton':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F14%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=14161',
    'Alex_Rodriguez':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F08%2F2016&EndDate=08%2F12%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=1274',
    'JJ_Hardy':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F04%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3797',
    'Chris_Young':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F18%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3882',
    'Lorenzo_Cain':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F16%2F2016&EndDate=09%2F09%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9077',
    'Brandon_Guyer':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F06%2F2016&EndDate=09%2F30%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=2636',
    'Yan_Gomes':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F17%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9627',
    'Tim_Anderson':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F10%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=15172',
    'Prince_Fielder':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F13%2F2016&EndDate=07%2F18%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4613',
    'Kurt_Suzuki':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F12%2F2016&EndDate=09%2F27%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=8259',
    'Sandy_Leon':
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F14%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5273',
    'Domingo_Santana': 
    'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10348',
    'Kirk_Nieuwenhuis': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=02%2F07%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=6400',
    'Martin_Maldonado': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F03%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=6887',
    'Michael_Bourn': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F30%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=6387',
    'Tyler_Flowers': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F03%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9134',
    'Jace_Peterson': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F25%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12325',
    'Erick_Aybar': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F16%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4082',
    'Matt_Wieters': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F29%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4298',
    'David_Ross': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F29%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=1551',
    'Miguel_Montero': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F06%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3364',
    'Jason_Heyward': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4940',
    'Dioner_Navarro': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F07%2F2016&EndDate=09%2F30%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3179',
    'Tyler_Saladino': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F10%2F2016&EndDate=09%2F21%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10807',
    'Austin_Jackson': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=04%2F01%2F2016&EndDate=06%2F09%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=9848',
    'Jimmy_Rollins': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F17%2F2016&EndDate=06%2F08%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=971',
    'Tucker_Barnhart': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F03%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10200',
    'Scott_Schebler': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F05%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12225',
    'Juan_Uribe': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F08%2F2016&EndDate=07%2F30%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=454',
    'Lonnie_Chisenhall': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F27%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=7571',
    'Roberto_Perez': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F10%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=2900',
    'Abraham_Almonte': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F30%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5486',
    'Cristhian_Adames': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F29%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=6013',
    'Nick_Hundley': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F04%2F2016&EndDate=09%2F30%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3376',
    'Gerardo_Parra': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F13%2F2016&EndDate=09%2F29%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=8553',
    'Cameron_Maybin': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F17%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5223',
    'Andrew_Romine': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F24%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=1159',
    'Jake_Marisnick': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F23%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11339',
    'Paulo_Orlando': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F09%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=8628',
    'Andrelton_Simmons': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F02%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10847',
    'Gregorio_Petit': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F18%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3812',
    'Johnny_Giavotella': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F05%2F2016&EndDate=08%2F14%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=6740',
    'Ichiro_Suzuki': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F02%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=1101',
    'Adeiny_Hechavarria': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F04%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=10459',
    'James_Loney': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F04%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4556',
    'Rene_Rivera': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F22%2F2016&EndDate=09%2F30%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3648',
    'Jose_Reyes': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F10%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=1736',
    'Josh_Reddick': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F31%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3892',
    'Jed_Lowrie': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F15%2F2016&EndDate=08%2F03%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4418',
    'Peter_Bourjos': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F03%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=2578',
    'John_Jaso': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F06%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5887',
    'Francisco_Cervelli': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F18%2F2016&EndDate=09%2F27%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5275',
    'Jordy_Mercer': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F29%2F2016&EndDate=09%2F29%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=6547',
    'Travis_Jankowski': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F21%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=13768',
    'Jon_Jay': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F26%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5227',
    'Alexei_Ramirez': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F31%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=5133',
    'Joe_Panik': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F22%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=11936',
    'Nori_Aoki': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F06%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=13075',
    'Chris_Iannetta': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F27%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=8267',
    'Kolten_Wong': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F16%2F2016&EndDate=09%2F30%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=12532',
    'Jhonny_Peralta': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F12%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=1738',
    'Shin-soo_Choo': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F21%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3174',
    'Mitch_Moreland': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F29%2F2016&EndDate=10%2F01%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3086',
    'Robinson_Chirinos': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F18%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=3142',
    'Darwin_Barney': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F12%2F2016&EndDate=09%2F28%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=2430',
    'Ben_Revere': 'http://www.baseballmusings.com/cgi-bin/PlayerInfo.py?StartDate=03%2F07%2F2016&EndDate=10%2F02%2F2016&GameType=all&PlayedFor=0&PlayedVs=0&Park=0&PlayerID=4712'
    
    
    
    }
#need to get all the urls and then scrape for career data
players_career_data0 = {
    'Mookie_Betts': 'http://www.baseball-reference.com/players/b/bettsmo01.shtml',
    'Brock_Holt': 'http://www.baseball-reference.com/players/h/holtbr01.shtml',
    'Ortiz': 'http://www.baseball-reference.com/players/o/ortizda01.shtml',
    'Travis_Shaw':'http://www.baseball-reference.com/players/s/shawtr01.shtml',
    'Dustin_Pedroia':'http://www.baseball-reference.com/players/p/pedrodu01.shtml',
    'Jackie_Bradley':'http://www.baseball-reference.com/players/b/bradlja02.shtml',
    'Coco_Crisp':'http://www.baseball-reference.com/players/c/crispco01.shtml',
    'Xander': 'http://www.baseball-reference.com/players/b/bogaexa01.shtml',
    'Bryce_Harper': 'http://www.baseball-reference.com/players/h/harpebr03.shtml',
    'Kev_Pillar': 'http://www.baseball-reference.com/players/p/pillake01.shtml',
    'Granderson': 'http://www.baseball-reference.com/players/g/grandcu01.shtml',
    'A_Gonzalez': 'http://www.baseball-reference.com/players/g/gonzaad01.shtml',
    'Jayson_Werth': 'http://www.baseball-reference.com/players/w/werthja01.shtml',
    'Brad_Miller': 'http://www.baseball-reference.com/players/m/millebr02.shtml',
    'Buster_Posey': 'http://www.baseball-reference.com/players/p/poseybu01.shtml',
    'Chris_Carter': 'http://www.baseball-reference.com/players/c/cartech02.shtml',
    'Kris_Bryant': 'http://www.baseball-reference.com/players/b/bryankr01.shtml',
    'Altuve':'http://www.baseball-reference.com/players/a/altuvjo01.shtml',
    'Cano':'http://www.baseball-reference.com/players/c/canoro01.shtml',
    'Yasmany_Tomas': 'http://www.baseball-reference.com/players/t/tomasya01.shtml',
    'Justin_Turner':'http://www.baseball-reference.com/players/t/turneju01.shtml',
    'Wil_Myers': 'http://www.baseball-reference.com/players/m/myerswi01.shtml',
    'Howie_Kendrick': 'http://www.baseball-reference.com/players/k/kendrho01.shtml',
    'Jacoby': 'http://www.baseball-reference.com/players/e/ellsbja01.shtml',
    'Edwin_Encarnacion': 'http://www.baseball-reference.com/players/e/encared01.shtml',
    'Mike_Napoli': 'http://www.baseball-reference.com/players/n/napolmi01.shtml',
    'Todd_Frazier': 'http://www.baseball-reference.com/players/f/frazito01.shtml',
    'Brett_gardner': 'http://www.baseball-reference.com/players/g/gardnbr01.shtml',
    'Yonder_Alonso': 'http://www.baseball-reference.com/players/a/alonsyo01.shtml',
    'Carlos_Santana': 'http://www.baseball-reference.com/players/s/santaca01.shtml',
    'Iglesias': 'http://www.baseball-reference.com/players/i/iglesjo01.shtml',
    'Elvis_Andrus':'http://www.baseball-reference.com/players/a/andruel01.shtml',
    'Manny_Machado':'http://www.baseball-reference.com/players/m/machama01.shtml',
    'Jose_Abreu':'http://www.baseball-reference.com/players/a/abreujo02.shtml',
    'Ian_Kinsler':'http://www.baseball-reference.com/players/k/kinslia01.shtml',
    'Dozier':'http://www.baseball-reference.com/players/d/doziebr01.shtml',
    'Schoop':'http://www.baseball-reference.com/players/s/schoojo01.shtml',
    'Carlos_Correa':'http://www.baseball-reference.com/players/c/correca01.shtml',
    'Joey_Votto':'http://www.baseball-reference.com/players/v/vottojo01.shtml',
    'Charlie_Blackmon':'http://www.baseball-reference.com/players/b/blackch02.shtml',
    'Starling_Marte':'http://www.baseball-reference.com/players/m/martest01.shtml',
    'Ryan_Braun':'http://www.baseball-reference.com/players/b/braunry02.shtml',
    'Espinosa':'http://www.baseball-reference.com/players/e/espinda01.shtml',
    'Chase_Utley':'http://www.baseball-reference.com/players/u/utleych01.shtml',
    'Denard_Span':'http://www.baseball-reference.com/players/s/spande01.shtml',
    'McCutchen':'http://www.baseball-reference.com/players/m/mccutan01.shtml',
    'Dexter_Fowler':'http://www.baseball-reference.com/players/f/fowlede01.shtml',
    'Miguel_Cabrera':'http://www.baseball-reference.com/players/c/cabremi01.shtml',
    'Melky Cabrera':'http://www.baseball-reference.com/players/c/cabreme01.shtml',
    'Keon_Broxton':'http://www.baseball-reference.com/players/b/broxtke01.shtml',
    'Jose_Ramirez':'http://www.baseball-reference.com/players/r/ramirjo01.shtml',
    'JD_Martinez':'http://www.baseball-reference.com/players/m/martijd02.shtml',
    'Yunel_Escobar':'http://www.baseball-reference.com/players/e/escobyu01.shtml',
    'Francisco_Lindor':'http://www.baseball-reference.com/players/l/lindofr01.shtml',
    'Adrian_Beltre':'http://www.baseball-reference.com/players/b/beltrad01.shtml',
    'Carlos_Beltran':'http://www.baseball-reference.com/players/b/beltrca01.shtml',
    'Victor_Martinez':'http://www.baseball-reference.com/players/m/martivi01.shtml',
    'Nelson_Cruz':'http://www.baseball-reference.com/players/c/cruzne02.shtml',
    'Hanley_Ramirez':'http://www.baseball-reference.com/players/r/ramirha01.shtml',
    'Ian_Desmond':'http://www.baseball-reference.com/players/d/desmoia01.shtml',
    'Adam Eaton': 'http://www.baseball-reference.com/players/e/eatonad02.shtml',
    'Josh_Donaldson': 'http://www.baseball-reference.com/players/d/donaljo02.shtml',
    'Kyle_Seager': 'http://www.baseball-reference.com/players/s/seageky01.shtml',
    'Didi_Gregorius': 'http://www.baseball-reference.com/players/g/gregodi01.shtml',
    'Jason_Kipnis': 'http://www.baseball-reference.com/players/k/kipnija01.shtml',
    'Cheslor_Cuthbert': 'http://www.baseball-reference.com/players/c/cuthbch01.shtml',
    'Evan_Longoria': 'http://www.baseball-reference.com/players/l/longoev01.shtml',
    'Rougned_Odor':'http://www.baseball-reference.com/players/o/odorro01.shtml',
    'Kole_Calhoun':'http://www.baseball-reference.com/players/c/calhoko01.shtml',
    'Starlin_Castro':'http://www.baseball-reference.com/players/c/castrst01.shtml',
    'Albert_Pujols':'http://www.baseball-reference.com/players/p/pujolal01.shtml',
    'DJ_LeMahieu':'http://www.baseball-reference.com/players/l/lemahdj01.shtml',
    'Daniel_Murphy': 'http://www.baseball-reference.com/players/m/murphda08.shtml',
    'Jean_Segura': 'http://www.baseball-reference.com/players/s/segurje01.shtml',
    'Corey_Seager': 'http://www.baseball-reference.com/players/s/seageco01.shtml',
    'Yadier_Molina': 'http://www.baseball-reference.com/players/m/molinya01.shtml',
    'Wilson_Ramos':'http://www.baseball-reference.com/players/r/ramoswi01.shtml',
    'Martin_Prado':'http://www.baseball-reference.com/players/p/pradoma01.shtml',
    'JT_Realmuto':'http://www.baseball-reference.com/players/r/realmjt01.shtml',
    'Freddie_Freeman':'http://www.baseball-reference.com/players/f/freemfr01.shtml',
    'Carlos_Gonzalez':'http://www.baseball-reference.com/players/g/gonzaca01.shtml',
    'Christian_Yelich': 'http://www.baseball-reference.com/players/y/yelicch01.shtml',
    'Paul_Goldschmidt': 'http://www.baseball-reference.com/players/g/goldspa01.shtml',
    'Nolan_Arenado': 'http://www.baseball-reference.com/players/a/arenano01.shtml',
    'Cesar_Hernandez': 'http://www.baseball-reference.com/players/h/hernace02.shtml',
    'Anthony_Rizzo': 'http://www.baseball-reference.com/players/r/rizzoan01.shtml',
    'Ender_Inciarte': 'http://www.baseball-reference.com/players/i/inciaen01.shtml',
    'Brandon_Phillips': 'http://www.baseball-reference.com/players/p/phillbr01.shtml',
    'Odubel_Herrera': 'http://www.baseball-reference.com/players/h/herreod01.shtml',
    'Jonathan_Villar': 'http://www.baseball-reference.com/players/v/villajo01.shtml',
    'Josh_Harrison': 'http://www.baseball-reference.com/players/h/harrijo05.shtml',
    'Asdrubal_Cabrera': 'http://www.baseball-reference.com/players/c/cabreas01.shtml',
    'Yoenis_Cespedes': 'http://www.baseball-reference.com/players/c/cespeyo01.shtml',
    'Angel_Pagan': 'http://www.baseball-reference.com/players/p/paganan01.shtml',
    'Brandon_Belt': 'http://www.baseball-reference.com/players/b/beltbr01.shtml',
    'Brandon_Crawford': 'http://www.baseball-reference.com/players/c/crawfbr01.shtml',
    'Stephen_Piscotty': 'http://www.baseball-reference.com/players/p/piscost01.shtml',
    'Adonis_Garcia': 'http://www.baseball-reference.com/players/g/garciad01.shtml',
    'Ben_Zobrist': 'http://www.baseball-reference.com/players/z/zobribe01.shtml',
    'Matt_Carpenter': 'http://www.baseball-reference.com/players/c/carpema01.shtml',
    'Anthony_Rendon': 'http://www.baseball-reference.com/players/r/rendoan01.shtml',
    'Nick_Markakis': 'http://www.baseball-reference.com/players/m/markani01.shtml',
    'Matt_Kemp': 'http://www.baseball-reference.com/players/k/kempma01.shtml',
    'Jarrod_Dyson': 'http://www.baseball-reference.com/players/d/dysonja01.shtml',
    'Dee_Gordon': 'http://www.baseball-reference.com/players/g/gordode01.shtml',
    'Billy_Hamilton': 'http://www.baseball-reference.com/players/h/hamilbi02.shtml',
    'Rajai_Davis': 'http://www.baseball-reference.com/players/d/davisra01.shtml',
    'Hernan_Perez': 'http://www.baseball-reference.com/players/p/perezhe01.shtml',
    'Trea_Turner': 'http://www.baseball-reference.com/players/t/turnetr01.shtml',
    'Mike_Trout': 'http://www.baseball-reference.com/players/t/troutmi01.shtml',
    'Leonys_Martin': 'http://www.baseball-reference.com/players/m/martile01.shtml',
    'Chris_Owings': 'http://www.baseball-reference.com/players/o/owingch01.shtml',
    'Kevin_Kiermaier': 'http://www.baseball-reference.com/players/k/kiermke01.shtml',
    'Jose_Peraza':'http://www.baseball-reference.com/players/p/perazjo01.shtml',
    'Gregory_Polanco': 'http://www.baseball-reference.com/players/p/polangr01.shtml',
    'Mark_Trumbo': 'http://www.baseball-reference.com/players/t/trumbma01.shtml',
    'Khris_Davis': 'http://www.baseball-reference.com/players/d/daviskh01.shtml',
    'Jake_Lamb': 'http://www.baseball-reference.com/players/l/lambja01.shtml',
    'Jay_Bruce': 'http://www.baseball-reference.com/players/b/bruceja01.shtml',
    'Jonathan_Lucroy': 'http://www.baseball-reference.com/players/l/lucrojo01.shtml',
    'Adam_Duvall': 'http://www.baseball-reference.com/players/d/duvalad01.shtml',
    'Michael_Saunders': 'http://www.baseball-reference.com/players/s/saundmi01.shtml',
    'Corey_Dickerson': 'http://www.baseball-reference.com/players/d/dickeco01.shtml',
    'Kendrys_Morales': 'http://www.baseball-reference.com/players/m/moralke01.shtml',
    'Justin_Upton': 'http://www.baseball-reference.com/players/u/uptonju01.shtml',
    'Chris_Davis': 'http://www.baseball-reference.com/players/d/davisch02.shtml',
    'George_Springer': 'http://www.baseball-reference.com/players/s/springe01.shtml',
    'Marcell_Ozuna': 'http://www.baseball-reference.com/players/o/ozunama01.shtml',
    'Jose_Bautista': 'http://www.baseball-reference.com/players/b/bautijo02.shtml',
    'Freddy_Galvis': 'http://www.baseball-reference.com/players/g/galvifr01.shtml',
    'Maikel_Franco': 'http://www.baseball-reference.com/players/f/francma02.shtml',
    'Marcus_Semien': 'http://www.baseball-reference.com/players/s/semiema01.shtml',
    'Eugenio_Suarez': 'http://www.baseball-reference.com/players/s/suareeu01.shtml',
    'Alcides_Escobar': 'http://www.baseball-reference.com/players/e/escobal02.shtml',
    'Adam_Jones': 'http://www.baseball-reference.com/players/j/jonesad01.shtml',
    'Eric_Hosmer': 'http://www.baseball-reference.com/players/h/hosmeer01.shtml',
    'Brandon_Moss': 'http://www.baseball-reference.com/players/m/mossbr01.shtml',
    'Jedd_Gyorko': 'http://www.baseball-reference.com/players/g/gyorkje01.shtml',
    'Giancarlo_Stanton': 'http://www.baseball-reference.com/players/s/stantmi03.shtml',
    'Yasmani_Grandal': 'http://www.baseball-reference.com/players/g/grandya01.shtml',
    'Trevor_Story': 'http://www.baseball-reference.com/players/s/storytr01.shtml',
    'Ryan_Hanigan': 'http://www.baseball-reference.com/players/h/hanigry01.shtml',
    'Ryan_Howard': 'http://www.baseball-reference.com/players/h/howarry01.shtml',
    'Joc_Pederson': 'http://www.baseball-reference.com/players/p/pederjo01.shtml',
    'Randal_Grichuk': 'http://www.baseball-reference.com/players/g/grichra01.shtml',
    'Neil_Walker': 'http://www.baseball-reference.com/players/w/walkene01.shtml',
    'Tommy_Joseph': 'http://www.baseball-reference.com/players/j/josepto01.shtml',
    'Addison_Russell': 'http://www.baseball-reference.com/players/r/russead02.shtml',
    'Jung-ho Kang': 'http://www.baseball-reference.com/players/k/kangju01.shtml',
    'Matt_Holiday': 'http://www.baseball-reference.com/players/h/hollima01.shtml',
    'Ryan_Schimpf': 'http://www.baseball-reference.com/players/s/schimry01.shtml',
    'Sean_Rodriguez': 'http://www.baseball-reference.com/players/r/rodrise01.shtml',
    'Aledmys_Diaz': 'http://www.baseball-reference.com/players/d/diazal02.shtml',
    'Zack_Cozart': 'http://www.baseball-reference.com/players/c/cozarza01.shtml',
    'Wilmer_Flores': 'http://www.baseball-reference.com/players/f/florewi01.shtml',
    'Matt_Adams': 'http://www.baseball-reference.com/players/a/adamsma01.shtml',
    'Cameron_Rupp': 'http://www.baseball-reference.com/players/r/ruppca01.shtml',
    'Brandon_Drury': 'http://www.baseball-reference.com/players/d/drurybr01.shtml',
    'Ryan_Zimmerman': 'http://www.baseball-reference.com/players/z/zimmery01.shtml',
    'Yangervis_Solarte': 'http://www.baseball-reference.com/players/s/solarya01.shtml',
    'Justin_Bour': 'http://www.baseball-reference.com/players/b/bourju01.shtml',
    'Mark_Reynolds': 'http://www.baseball-reference.com/players/r/reynoma01.shtml',
    'Welington_Castillo': 'http://www.baseball-reference.com/players/c/castiwe01.shtml',
    'Derek_Norris': 'http://www.baseball-reference.com/players/n/norride01.shtml',
    'Scooter_Gennett': 'http://www.baseball-reference.com/players/g/gennesc01.shtml',
    'Javier_Baez': 'http://www.baseball-reference.com/players/b/baezja01.shtml',
    'Hunter_Pence': 'http://www.baseball-reference.com/players/p/pencehu01.shtml',
    'Matt_Joyce': 'http://www.baseball-reference.com/players/j/joycema01.shtml',
    'Adam_Rosales': 'http://www.baseball-reference.com/players/r/rosalad01.shtml',
    'Pedro_Alvarez': 'http://www.baseball-reference.com/players/a/alvarpe01.shtml',
    'Salvador_Perez': 'http://www.baseball-reference.com/players/p/perezsa02.shtml',
    'Brain_McCann': 'http://www.baseball-reference.com/players/m/mccanbr01.shtml',
    'Russell_Martin': 'http://www.baseball-reference.com/players/m/martiru01.shtml',
    'Adam_Lind': 'http://www.baseball-reference.com/players/l/lindad01.shtml',
    'Logan_Forsythe': 'http://www.baseball-reference.com/players/f/forsylo01.shtml',
    'Gary_Sanchez': 'http://www.baseball-reference.com/players/s/sanchga02.shtml',
    'Nomar_Mazara': 'http://www.baseball-reference.com/players/m/mazarno01.shtml',
    'Alex_Gordon': 'http://www.baseball-reference.com/players/g/gordoal01.shtml',
    'Matt_Wieters': 'http://www.baseball-reference.com/players/w/wietema01.shtml',
    'Steven_Souza': 'http://www.baseball-reference.com/players/s/souzast01.shtml',
    'Max_Kepler': 'http://www.baseball-reference.com/players/k/keplema01.shtml',
    'Stephen_Vogt': 'http://www.baseball-reference.com/players/v/vogtst01.shtml',
    'Evan_Gattis': 'http://www.baseball-reference.com/players/g/gattiev01.shtml',
    'Troy_Tulowitzki': 'http://www.baseball-reference.com/players/t/tulowtr01.shtml',
    'Nick_Castellanos': 'http://www.baseball-reference.com/players/c/casteni01.shtml',
    'Seth_Smith': 'http://www.baseball-reference.com/players/s/smithse01.shtml',
    'C.J._Cron': 'http://www.baseball-reference.com/players/c/croncj01.shtml',
    'Mark_Teixeira': 'http://www.baseball-reference.com/players/t/teixema01.shtml',
    'Colby_Rasmus': 'http://www.baseball-reference.com/players/r/rasmuco01.shtml',
    'Jefry_Marte': 'http://www.baseball-reference.com/players/m/marteje01.shtml',
    'Franklin_Gutierrez': 'http://www.baseball-reference.com/players/g/gutiefr01.shtml',
    'Chase_Headley': 'http://www.baseball-reference.com/players/h/headlch01.shtml',
    'Justin_Smoak': 'http://www.baseball-reference.com/players/s/smoakju01.shtml',
    'Logan_Morrison': 'http://www.baseball-reference.com/players/m/morrilo01.shtml',
    'Tyler_Naquin': 'http://www.baseball-reference.com/players/n/naquity01.shtml',
    'Dae-Ho_Lee': 'http://www.baseball-reference.com/players/l/leeda02.shtml',
    'Carlos_Gomez': 'http://www.baseball-reference.com/players/g/gomezca01.shtml',
    'Steve_Pearce': 'http://www.baseball-reference.com/players/p/pearcst01.shtml',
    'Luis_Valbuena': 'http://www.baseball-reference.com/players/v/valbulu01.shtml',
    'Marwin_Gonzalez': 'http://www.baseball-reference.com/players/g/gonzama01.shtml',
    'Ryon_Healy': 'http://www.baseball-reference.com/players/h/healyry01.shtml',
    'Jarrod_Salty': 'http://www.baseball-reference.com/players/s/saltaja01.shtml',
    'Trevor_Plouffe': 'http://www.baseball-reference.com/players/p/plouftr01.shtml',
    'Eduardo_Nunez': 'http://www.baseball-reference.com/players/n/nunezed02.shtml',
    'Brett_Lawrie': 'http://www.baseball-reference.com/players/l/lawribr01.shtml',
    'Avisail_Garcia': 'http://www.baseball-reference.com/players/g/garciav01.shtml',
    'James_McCann': 'http://www.baseball-reference.com/players/m/mccanja02.shtml',
    'Mike_Zunino': 'http://www.baseball-reference.com/players/z/zuninmi01.shtml',
    'Byung-Ho_Park': 'http://www.baseball-reference.com/players/p/parkby01.shtml',
    'Joe_Mauer': 'http://www.baseball-reference.com/players/m/mauerjo01.shtml',
    'Jason_Castro': 'http://www.baseball-reference.com/players/c/castrja01.shtml',
    'Robbie_Grossman': 'http://www.baseball-reference.com/players/g/grossro01.shtml',
    'Devon_Travis': 'http://www.baseball-reference.com/players/t/travide01.shtml',
    'Eddie_Rosario': 'http://www.baseball-reference.com/players/r/rosared01.shtml',
    'Byron_Buxton': 'http://www.baseball-reference.com/players/b/buxtoby01.shtml',
    'Alex_Rodriguez': 'http://www.baseball-reference.com/players/r/rodrial01.shtml',
    'JJ_Hardy': 'http://www.baseball-reference.com/players/h/hardyjj01.shtml',
    'Chris_Young': 'http://www.baseball-reference.com/players/y/youngch04.shtml',
    'Lorenzo_Cain': 'http://www.baseball-reference.com/players/c/cainlo01.shtml',
    'Brandon_Guyer': 'http://www.baseball-reference.com/players/g/guyerbr01.shtml',
    'Yan_Gomes': 'http://www.baseball-reference.com/players/g/gomesya01.shtml',
    'Tim_Anderson': 'http://www.baseball-reference.com/players/a/anderti01.shtml',
    'Prince_Fielder': 'http://www.baseball-reference.com/players/f/fieldpr01.shtml',
    'Kurt_Suzuki': 'http://www.baseball-reference.com/players/s/suzukku01.shtml',
    'Sandy_Leon': 'http://www.baseball-reference.com/players/l/leonsa01.shtml',
    'Domingo_Santana': 'http://www.baseball-reference.com/players/s/santado01.shtml',
    'Kirk_Nieuwenhuis': 'http://www.baseball-reference.com/players/n/nieuwki01.shtml',
    'Martin_Maldonado': 'http://www.baseball-reference.com/players/m/maldoma01.shtml',
    'Michael_Bourn': 'http://www.baseball-reference.com/players/b/bournmi01.shtml',
    'Tyler_Flowers': 'http://www.baseball-reference.com/players/f/flowety01.shtml',
    'Jace_Peterson': 'http://www.baseball-reference.com/players/p/peterja01.shtml',
    'Erick_Aybar': 'http://www.baseball-reference.com/players/a/aybarer01.shtml',
    'Matt_Wieters': 'http://www.baseball-reference.com/players/w/wietema01.shtml',
    'David_Ross': 'http://www.baseball-reference.com/players/r/rossda01.shtml',
    'Miguel_Montero': 'http://www.baseball-reference.com/players/m/montemi01.shtml',
    'Jason_Heyward': 'http://www.baseball-reference.com/players/h/heywaja01.shtml',
    'Dioner_Navarro': 'http://www.baseball-reference.com/players/n/navardi01.shtml',
    'Tyler_Saladino': 'http://www.baseball-reference.com/players/s/saladty01.shtml',
    'Austin_Jackson': 'http://www.baseball-reference.com/players/j/jacksau01.shtml',
    'Jimmy_Rollins': 'http://www.baseball-reference.com/players/r/rolliji01.shtml',
    'Tucker_Barnhart': 'http://www.baseball-reference.com/players/b/barnhtu01.shtml',
    'Scott_Schebler': 'http://www.baseball-reference.com/players/s/schebsc01.shtml',
    'Juan_Uribe': 'http://www.baseball-reference.com/players/u/uribeju01.shtml',
    'Lonnie_Chisenhall': 'http://www.baseball-reference.com/players/c/chiselo01.shtml',
    'Roberto_Perez': 'http://www.baseball-reference.com/players/p/perezro02.shtml',
    'Abraham_Almonte': 'http://www.baseball-reference.com/players/a/almonab01.shtml',
    'Cristhian_Adames': 'http://www.baseball-reference.com/players/a/adamecr01.shtml',
    'Nick_Hundley': 'http://www.baseball-reference.com/players/h/hundlni01.shtml',
    'Gerardo_Parra': 'http://www.baseball-reference.com/players/p/parrage01.shtml',
    'Cameron_Maybin': 'http://www.baseball-reference.com/players/m/maybica01.shtml',
    'Andrew_Romine': 'http://www.baseball-reference.com/players/r/rominan01.shtml',
    'Jake_Marisnick': 'http://www.baseball-reference.com/players/m/marisja01.shtml',
    'Paulo_Orlando': 'http://www.baseball-reference.com/players/o/orlanpa01.shtml',
    'Andrelton_Simmons': 'http://www.baseball-reference.com/players/s/simmoan01.shtml',
    'Gregorio_Petit': 'http://www.baseball-reference.com/players/p/petitgr01.shtml',
    'Johnny_Giavotella': 'http://www.baseball-reference.com/players/g/giavojo01.shtml',
    'Ichiro_Suzuki': 'http://www.baseball-reference.com/players/s/suzukic01.shtml',
    'Adeiny_Hechavarria': 'http://www.baseball-reference.com/players/h/hechaad01.shtml',
    'James_Loney': 'http://www.baseball-reference.com/players/l/loneyja01.shtml',
    'Rene_Rivera': 'http://www.baseball-reference.com/players/r/riverre01.shtml',
    'Jose_Reyes': 'http://www.baseball-reference.com/players/r/reyesjo01.shtml',
    'Josh_Reddick': 'http://www.baseball-reference.com/players/r/reddijo01.shtml',
    'Jed_Lowrie': 'http://www.baseball-reference.com/players/l/lowrije01.shtml',
    'Peter_Bourjos': 'http://www.baseball-reference.com/players/b/bourjpe01.shtml',
    'John_Jaso': 'http://www.baseball-reference.com/players/j/jasojo01.shtml',
    'Francisco_Cervelli': 'http://www.baseball-reference.com/players/c/cervefr01.shtml',
    'Jordy_Mercer': 'http://www.baseball-reference.com/players/m/mercejo03.shtml',
    'Travis_Jankowski': 'http://www.baseball-reference.com/players/j/jankotr01.shtml',
    'Jon_Jay': 'http://www.baseball-reference.com/players/j/jayjo02.shtml',
    'Alexei_Ramirez': 'http://www.baseball-reference.com/players/r/ramiral03.shtml',
    'Joe_Panik': 'http://www.baseball-reference.com/players/p/panikjo01.shtml',
    'Nori_Aoki': 'http://www.baseball-reference.com/players/a/aokino01.shtml',
    'Chris_Iannetta': 'http://www.baseball-reference.com/players/i/iannech01.shtml',
    'Kolten_Wong': 'http://www.baseball-reference.com/players/w/wongko01.shtml',
    'Jhonny_Peralta': 'http://www.baseball-reference.com/players/p/peraljh01.shtml',
    'Shin-soo_Choo': 'http://www.baseball-reference.com/players/c/choosh01.shtml',
    'Mitch_Moreland': 'http://www.baseball-reference.com/players/m/morelmi01.shtml',
    'Robinson_Chirinos': 'http://www.baseball-reference.com/players/c/chiriro01.shtml',
    'Darwin_Barney': 'http://www.baseball-reference.com/players/b/barneda01.shtml',
    'Ben_Revere': 'http://www.baseball-reference.com/players/r/reverbe01.shtml'
    
    }

players_game_logs0 = {
'Juan_Uribe': 'http://www.baseball-reference.com/players/gl.cgi?id=uribeju01&t=b&year=2016',
'Robbie_Grossman': 'http://www.baseball-reference.com/players/gl.cgi?id=grossro01&t=b&year=2016',
'Anthony_Rendon': 'http://www.baseball-reference.com/players/gl.cgi?id=rendoan01&t=b&year=2016',
'Mookie_Betts': 'http://www.baseball-reference.com/players/gl.cgi?id=bettsmo01&t=b&year=2016',
'Howie_Kendrick': 'http://www.baseball-reference.com/players/gl.cgi?id=kendrho01&t=b&year=2016',
'Nick_Castellanos': 'http://www.baseball-reference.com/players/gl.cgi?id=casteni01&t=b&year=2016',
'Abraham_Almonte': 'http://www.baseball-reference.com/players/gl.cgi?id=almonab01&t=b&year=2016',
'Russell_Martin': 'http://www.baseball-reference.com/players/gl.cgi?id=martiru01&t=b&year=2016',
'Ortiz': 'http://www.baseball-reference.com/players/gl.cgi?id=ortizda01&t=b&year=2016',
'Jason_Castro': 'http://www.baseball-reference.com/players/gl.cgi?id=castrja01&t=b&year=2016',
'Sean_Rodriguez': 'http://www.baseball-reference.com/players/gl.cgi?id=rodrise01&t=b&year=2016',
'Byung-Ho_Park': 'http://www.baseball-reference.com/players/gl.cgi?id=parkby01&t=b&year=2016',
'Brandon_Crawford': 'http://www.baseball-reference.com/players/gl.cgi?id=crawfbr01&t=b&year=2016',
'Todd_Frazier': 'http://www.baseball-reference.com/players/gl.cgi?id=frazito01&t=b&year=2016',
'Stephen_Piscotty': 'http://www.baseball-reference.com/players/gl.cgi?id=piscost01&t=b&year=2016',
'Scott_Schebler': 'http://www.baseball-reference.com/players/gl.cgi?id=schebsc01&t=b&year=2016',
'Ian_Desmond': 'http://www.baseball-reference.com/players/gl.cgi?id=desmoia01&t=b&year=2016',
'Nick_Markakis': 'http://www.baseball-reference.com/players/gl.cgi?id=markani01&t=b&year=2016',
'Wilson_Ramos': 'http://www.baseball-reference.com/players/gl.cgi?id=ramoswi01&t=b&year=2016',
'Xander': 'http://www.baseball-reference.com/players/gl.cgi?id=bogaexa01&t=b&year=2016',
'Wil_Myers': 'http://www.baseball-reference.com/players/gl.cgi?id=myerswi01&t=b&year=2016',
'Martin_Prado': 'http://www.baseball-reference.com/players/gl.cgi?id=pradoma01&t=b&year=2016',
'Chris_Davis': 'http://www.baseball-reference.com/players/gl.cgi?id=davisch02&t=b&year=2016',
'Cameron_Rupp': 'http://www.baseball-reference.com/players/gl.cgi?id=ruppca01&t=b&year=2016',
'Dae-Ho_Lee': 'http://www.baseball-reference.com/players/gl.cgi?id=leeda02&t=b&year=2016',
'Coco_Crisp': 'http://www.baseball-reference.com/players/gl.cgi?id=crispco01&t=b&year=2016',
'Addison_Russell': 'http://www.baseball-reference.com/players/gl.cgi?id=russead02&t=b&year=2016',
'Jonathan_Villar': 'http://www.baseball-reference.com/players/gl.cgi?id=villajo01&t=b&year=2016',
'Francisco_Lindor': 'http://www.baseball-reference.com/players/gl.cgi?id=lindofr01&t=b&year=2016',
'Kevin_Kiermaier': 'http://www.baseball-reference.com/players/gl.cgi?id=kiermke01&t=b&year=2016',
'Rajai_Davis': 'http://www.baseball-reference.com/players/gl.cgi?id=davisra01&t=b&year=2016',
'Zack_Cozart': 'http://www.baseball-reference.com/players/gl.cgi?id=cozarza01&t=b&year=2016',
'Jonathan_Lucroy': 'http://www.baseball-reference.com/players/gl.cgi?id=lucrojo01&t=b&year=2016',
'Chris_Owings': 'http://www.baseball-reference.com/players/gl.cgi?id=owingch01&t=b&year=2016',
'Jefry_Marte': 'http://www.baseball-reference.com/players/gl.cgi?id=marteje01&t=b&year=2016',
'Kirk_Nieuwenhuis': 'http://www.baseball-reference.com/players/gl.cgi?id=nieuwki01&t=b&year=2016',
'Ian_Kinsler': 'http://www.baseball-reference.com/players/gl.cgi?id=kinslia01&t=b&year=2016',
'Kyle_Seager': 'http://www.baseball-reference.com/players/gl.cgi?id=seageky01&t=b&year=2016',
'Jose_Bautista': 'http://www.baseball-reference.com/players/gl.cgi?id=bautijo02&t=b&year=2016',
'Eric_Hosmer': 'http://www.baseball-reference.com/players/gl.cgi?id=hosmeer01&t=b&year=2016',
'Mark_Teixeira': 'http://www.baseball-reference.com/players/gl.cgi?id=teixema01&t=b&year=2016',
'Trea_Turner': 'http://www.baseball-reference.com/players/gl.cgi?id=turnetr01&t=b&year=2016',
'Jose_Ramirez': 'http://www.baseball-reference.com/players/gl.cgi?id=ramirjo01&t=b&year=2016',
'Avisail_Garcia': 'http://www.baseball-reference.com/players/gl.cgi?id=garciav01&t=b&year=2016',
'Jarrod_Salty': 'http://www.baseball-reference.com/players/gl.cgi?id=saltaja01&t=b&year=2016',
'Marcell_Ozuna': 'http://www.baseball-reference.com/players/gl.cgi?id=ozunama01&t=b&year=2016',
'Adam_Lind': 'http://www.baseball-reference.com/players/gl.cgi?id=lindad01&t=b&year=2016',
'Logan_Morrison': 'http://www.baseball-reference.com/players/gl.cgi?id=morrilo01&t=b&year=2016',
'Gerardo_Parra': 'http://www.baseball-reference.com/players/gl.cgi?id=parrage01&t=b&year=2016',
'Domingo_Santana': 'http://www.baseball-reference.com/players/gl.cgi?id=santado01&t=b&year=2016',
'Yasmani_Grandal': 'http://www.baseball-reference.com/players/gl.cgi?id=grandya01&t=b&year=2016',
'Pedro_Alvarez': 'http://www.baseball-reference.com/players/gl.cgi?id=alvarpe01&t=b&year=2016',
'Starling_Marte': 'http://www.baseball-reference.com/players/gl.cgi?id=martest01&t=b&year=2016',
'Adam_Rosales': 'http://www.baseball-reference.com/players/gl.cgi?id=rosalad01&t=b&year=2016',
'Chris_Carter': 'http://www.baseball-reference.com/players/gl.cgi?id=cartech02&t=b&year=2016',
'Justin_Upton': 'http://www.baseball-reference.com/players/gl.cgi?id=uptonju01&t=b&year=2016',
'Jay_Bruce': 'http://www.baseball-reference.com/players/gl.cgi?id=bruceja01&t=b&year=2016',
'Yunel_Escobar': 'http://www.baseball-reference.com/players/gl.cgi?id=escobyu01&t=b&year=2016',
'Adam_Jones': 'http://www.baseball-reference.com/players/gl.cgi?id=jonesad01&t=b&year=2016',
'Michael_Saunders': 'http://www.baseball-reference.com/players/gl.cgi?id=saundmi01&t=b&year=2016',
'Yasmany_Tomas': 'http://www.baseball-reference.com/players/gl.cgi?id=tomasya01&t=b&year=2016',
'Justin_Turner': 'http://www.baseball-reference.com/players/gl.cgi?id=turneju01&t=b&year=2016',
'Matt_Adams': 'http://www.baseball-reference.com/players/gl.cgi?id=adamsma01&t=b&year=2016',
'Marwin_Gonzalez': 'http://www.baseball-reference.com/players/gl.cgi?id=gonzama01&t=b&year=2016',
'Jimmy_Rollins': 'http://www.baseball-reference.com/players/gl.cgi?id=rolliji01&t=b&year=2016',
'George_Springer': 'http://www.baseball-reference.com/players/gl.cgi?id=springe01&t=b&year=2016',
'Brock_Holt': 'http://www.baseball-reference.com/players/gl.cgi?id=holtbr01&t=b&year=2016',
'Mark_Trumbo': 'http://www.baseball-reference.com/players/gl.cgi?id=trumbma01&t=b&year=2016',
'Yangervis_Solarte': 'http://www.baseball-reference.com/players/gl.cgi?id=solarya01&t=b&year=2016',
'C.J._Cron': 'http://www.baseball-reference.com/players/gl.cgi?id=croncj01&t=b&year=2016',
'Carlos_Beltran': 'http://www.baseball-reference.com/players/gl.cgi?id=beltrca01&t=b&year=2016',
'Freddy_Galvis': 'http://www.baseball-reference.com/players/gl.cgi?id=galvifr01&t=b&year=2016',
'Dexter_Fowler': 'http://www.baseball-reference.com/players/gl.cgi?id=fowlede01&t=b&year=2016',
'Nomar_Mazara': 'http://www.baseball-reference.com/players/gl.cgi?id=mazarno01&t=b&year=2016',
'Matt_Carpenter': 'http://www.baseball-reference.com/players/gl.cgi?id=carpema01&t=b&year=2016',
'Dozier': 'http://www.baseball-reference.com/players/gl.cgi?id=doziebr01&t=b&year=2016',
'JD_Martinez': 'http://www.baseball-reference.com/players/gl.cgi?id=martijd02&t=b&year=2016',
'Adam Eaton': 'http://www.baseball-reference.com/players/gl.cgi?id=eatonad02&t=b&year=2016',
'Jose_Abreu': 'http://www.baseball-reference.com/players/gl.cgi?id=abreujo02&t=b&year=2016',
'Kurt_Suzuki': 'http://www.baseball-reference.com/players/gl.cgi?id=suzukku01&t=b&year=2016',
'Matt_Holiday': 'http://www.baseball-reference.com/players/gl.cgi?id=hollima01&t=b&year=2016',
'Austin_Jackson': 'http://www.baseball-reference.com/players/gl.cgi?id=jacksau01&t=b&year=2016',
'Josh_Donaldson': 'http://www.baseball-reference.com/players/gl.cgi?id=donaljo02&t=b&year=2016',
'JJ_Hardy': 'http://www.baseball-reference.com/players/gl.cgi?id=hardyjj01&t=b&year=2016',
'Carlos_Correa': 'http://www.baseball-reference.com/players/gl.cgi?id=correca01&t=b&year=2016',
'Hunter_Pence': 'http://www.baseball-reference.com/players/gl.cgi?id=pencehu01&t=b&year=2016',
'Carlos_Gonzalez': 'http://www.baseball-reference.com/players/gl.cgi?id=gonzaca01&t=b&year=2016',
'Evan_Gattis': 'http://www.baseball-reference.com/players/gl.cgi?id=gattiev01&t=b&year=2016',
'Melky Cabrera': 'http://www.baseball-reference.com/players/gl.cgi?id=cabreme01&t=b&year=2016',
'Nick_Hundley': 'http://www.baseball-reference.com/players/gl.cgi?id=hundlni01&t=b&year=2016',
'Steve_Pearce': 'http://www.baseball-reference.com/players/gl.cgi?id=pearcst01&t=b&year=2016',
'Elvis_Andrus': 'http://www.baseball-reference.com/players/gl.cgi?id=andruel01&t=b&year=2016',
'Chase_Headley': 'http://www.baseball-reference.com/players/gl.cgi?id=headlch01&t=b&year=2016',
'Mark_Reynolds': 'http://www.baseball-reference.com/players/gl.cgi?id=reynoma01&t=b&year=2016',
'Joe_Mauer': 'http://www.baseball-reference.com/players/gl.cgi?id=mauerjo01&t=b&year=2016',
'Tyler_Naquin': 'http://www.baseball-reference.com/players/gl.cgi?id=naquity01&t=b&year=2016',
'Starlin_Castro': 'http://www.baseball-reference.com/players/gl.cgi?id=castrst01&t=b&year=2016',
'Charlie_Blackmon': 'http://www.baseball-reference.com/players/gl.cgi?id=blackch02&t=b&year=2016',
'Billy_Hamilton': 'http://www.baseball-reference.com/players/gl.cgi?id=hamilbi02&t=b&year=2016',
'Gregory_Polanco': 'http://www.baseball-reference.com/players/gl.cgi?id=polangr01&t=b&year=2016',
'Rougned_Odor': 'http://www.baseball-reference.com/players/gl.cgi?id=odorro01&t=b&year=2016',
'Dee_Gordon': 'http://www.baseball-reference.com/players/gl.cgi?id=gordode01&t=b&year=2016',
'Tyler_Saladino': 'http://www.baseball-reference.com/players/gl.cgi?id=saladty01&t=b&year=2016',
'Chase_Utley': 'http://www.baseball-reference.com/players/gl.cgi?id=utleych01&t=b&year=2016',
'Matt_Wieters': 'http://www.baseball-reference.com/players/gl.cgi?id=wietema01&t=b&year=2016',
'Erick_Aybar': 'http://www.baseball-reference.com/players/gl.cgi?id=aybarer01&t=b&year=2016',
'Miguel_Montero': 'http://www.baseball-reference.com/players/gl.cgi?id=montemi01&t=b&year=2016',
'Tucker_Barnhart': 'http://www.baseball-reference.com/players/gl.cgi?id=barnhtu01&t=b&year=2016',
'Trevor_Story': 'http://www.baseball-reference.com/players/gl.cgi?id=storytr01&t=b&year=2016',
'Steven_Souza': 'http://www.baseball-reference.com/players/gl.cgi?id=souzast01&t=b&year=2016',
'Jason_Heyward': 'http://www.baseball-reference.com/players/gl.cgi?id=heywaja01&t=b&year=2016',
'Schoop': 'http://www.baseball-reference.com/players/gl.cgi?id=schoojo01&t=b&year=2016',
'Brandon_Guyer': 'http://www.baseball-reference.com/players/gl.cgi?id=guyerbr01&t=b&year=2016',
'Eugenio_Suarez': 'http://www.baseball-reference.com/players/gl.cgi?id=suareeu01&t=b&year=2016',
'Byron_Buxton': 'http://www.baseball-reference.com/players/gl.cgi?id=buxtoby01&t=b&year=2016',
'Corey_Seager': 'http://www.baseball-reference.com/players/gl.cgi?id=seageco01&t=b&year=2016',
'Cano': 'http://www.baseball-reference.com/players/gl.cgi?id=canoro01&t=b&year=2016',
'Yan_Gomes': 'http://www.baseball-reference.com/players/gl.cgi?id=gomesya01&t=b&year=2016',
'Odubel_Herrera': 'http://www.baseball-reference.com/players/gl.cgi?id=herreod01&t=b&year=2016',
'Edwin_Encarnacion': 'http://www.baseball-reference.com/players/gl.cgi?id=encared01&t=b&year=2016',
'Giancarlo_Stanton': 'http://www.baseball-reference.com/players/gl.cgi?id=stantmi03&t=b&year=2016',
'Max_Kepler': 'http://www.baseball-reference.com/players/gl.cgi?id=keplema01&t=b&year=2016',
'Jake_Lamb': 'http://www.baseball-reference.com/players/gl.cgi?id=lambja01&t=b&year=2016',
'Eddie_Rosario': 'http://www.baseball-reference.com/players/gl.cgi?id=rosared01&t=b&year=2016',
'Matt_Kemp': 'http://www.baseball-reference.com/players/gl.cgi?id=kempma01&t=b&year=2016',
'Mike_Napoli': 'http://www.baseball-reference.com/players/gl.cgi?id=napolmi01&t=b&year=2016',
'Hernan_Perez': 'http://www.baseball-reference.com/players/gl.cgi?id=perezhe01&t=b&year=2016',
'Iglesias': 'http://www.baseball-reference.com/players/gl.cgi?id=iglesjo01&t=b&year=2016',
'Daniel_Murphy': 'http://www.baseball-reference.com/players/gl.cgi?id=murphda08&t=b&year=2016',
'Cheslor_Cuthbert': 'http://www.baseball-reference.com/players/gl.cgi?id=cuthbch01&t=b&year=2016',
'Ryan_Hanigan': 'http://www.baseball-reference.com/players/gl.cgi?id=hanigry01&t=b&year=2016',
'Adam_Duvall': 'http://www.baseball-reference.com/players/gl.cgi?id=duvalad01&t=b&year=2016',
'Randal_Grichuk': 'http://www.baseball-reference.com/players/gl.cgi?id=grichra01&t=b&year=2016',
'Jose_Peraza': 'http://www.baseball-reference.com/players/gl.cgi?id=perazjo01&t=b&year=2016',
'Brain_McCann': 'http://www.baseball-reference.com/players/gl.cgi?id=mccanbr01&t=b&year=2016',
'Angel_Pagan': 'http://www.baseball-reference.com/players/gl.cgi?id=paganan01&t=b&year=2016',
'Mike_Zunino': 'http://www.baseball-reference.com/players/gl.cgi?id=zuninmi01&t=b&year=2016',
'Michael_Bourn': 'http://www.baseball-reference.com/players/gl.cgi?id=bournmi01&t=b&year=2016',
'Jedd_Gyorko': 'http://www.baseball-reference.com/players/gl.cgi?id=gyorkje01&t=b&year=2016',
'Jayson_Werth': 'http://www.baseball-reference.com/players/gl.cgi?id=werthja01&t=b&year=2016',
'Logan_Forsythe': 'http://www.baseball-reference.com/players/gl.cgi?id=forsylo01&t=b&year=2016',
'Ryan_Howard': 'http://www.baseball-reference.com/players/gl.cgi?id=howarry01&t=b&year=2016',
'Brandon_Drury': 'http://www.baseball-reference.com/players/gl.cgi?id=drurybr01&t=b&year=2016',
'Javier_Baez': 'http://www.baseball-reference.com/players/gl.cgi?id=baezja01&t=b&year=2016',
'Brandon_Belt': 'http://www.baseball-reference.com/players/gl.cgi?id=beltbr01&t=b&year=2016',
'Salvador_Perez': 'http://www.baseball-reference.com/players/gl.cgi?id=perezsa02&t=b&year=2016',
'Keon_Broxton': 'http://www.baseball-reference.com/players/gl.cgi?id=broxtke01&t=b&year=2016',
'Travis_Shaw': 'http://www.baseball-reference.com/players/gl.cgi?id=shawtr01&t=b&year=2016',
'Nelson_Cruz': 'http://www.baseball-reference.com/players/gl.cgi?id=cruzne02&t=b&year=2016',
'Jarrod_Dyson': 'http://www.baseball-reference.com/players/gl.cgi?id=dysonja01&t=b&year=2016',
'Neil_Walker': 'http://www.baseball-reference.com/players/gl.cgi?id=walkene01&t=b&year=2016',
'Maikel_Franco': 'http://www.baseball-reference.com/players/gl.cgi?id=francma02&t=b&year=2016',
'Albert_Pujols': 'http://www.baseball-reference.com/players/gl.cgi?id=pujolal01&t=b&year=2016',
'Sandy_Leon': 'http://www.baseball-reference.com/players/gl.cgi?id=leonsa01&t=b&year=2016',
'Tommy_Joseph': 'http://www.baseball-reference.com/players/gl.cgi?id=josepto01&t=b&year=2016',
'Adonis_Garcia': 'http://www.baseball-reference.com/players/gl.cgi?id=garciad01&t=b&year=2016',
'Trevor_Plouffe': 'http://www.baseball-reference.com/players/gl.cgi?id=plouftr01&t=b&year=2016',
'Cristhian_Adames': 'http://www.baseball-reference.com/players/gl.cgi?id=adamecr01&t=b&year=2016',
'A_Gonzalez': 'http://www.baseball-reference.com/players/gl.cgi?id=gonzaad01&t=b&year=2016',
'Kendrys_Morales': 'http://www.baseball-reference.com/players/gl.cgi?id=moralke01&t=b&year=2016',
'Espinosa': 'http://www.baseball-reference.com/players/gl.cgi?id=espinda01&t=b&year=2016',
'Welington_Castillo': 'http://www.baseball-reference.com/players/gl.cgi?id=castiwe01&t=b&year=2016',
'Matt_Joyce': 'http://www.baseball-reference.com/players/gl.cgi?id=joycema01&t=b&year=2016',
'Lonnie_Chisenhall': 'http://www.baseball-reference.com/players/gl.cgi?id=chiselo01&t=b&year=2016',
'Justin_Bour': 'http://www.baseball-reference.com/players/gl.cgi?id=bourju01&t=b&year=2016',
'Roberto_Perez': 'http://www.baseball-reference.com/players/gl.cgi?id=perezro02&t=b&year=2016',
'Troy_Tulowitzki': 'http://www.baseball-reference.com/players/gl.cgi?id=tulowtr01&t=b&year=2016',
'Jackie_Bradley': 'http://www.baseball-reference.com/players/gl.cgi?id=bradlja02&t=b&year=2016',
'Brett_gardner': 'http://www.baseball-reference.com/players/gl.cgi?id=gardnbr01&t=b&year=2016',
'Alex_Gordon': 'http://www.baseball-reference.com/players/gl.cgi?id=gordoal01&t=b&year=2016',
'Tyler_Flowers': 'http://www.baseball-reference.com/players/gl.cgi?id=flowety01&t=b&year=2016',
'Jace_Peterson': 'http://www.baseball-reference.com/players/gl.cgi?id=peterja01&t=b&year=2016',
'Yadier_Molina': 'http://www.baseball-reference.com/players/gl.cgi?id=molinya01&t=b&year=2016',
'Yoenis_Cespedes': 'http://www.baseball-reference.com/players/gl.cgi?id=cespeyo01&t=b&year=2016',
'Martin_Maldonado': 'http://www.baseball-reference.com/players/gl.cgi?id=maldoma01&t=b&year=2016',
'Ender_Inciarte': 'http://www.baseball-reference.com/players/gl.cgi?id=inciaen01&t=b&year=2016',
'Ben_Zobrist': 'http://www.baseball-reference.com/players/gl.cgi?id=zobribe01&t=b&year=2016',
'Joc_Pederson': 'http://www.baseball-reference.com/players/gl.cgi?id=pederjo01&t=b&year=2016',
'Brad_Miller': 'http://www.baseball-reference.com/players/gl.cgi?id=millebr02&t=b&year=2016',
'Colby_Rasmus': 'http://www.baseball-reference.com/players/gl.cgi?id=rasmuco01&t=b&year=2016',
'Manny_Machado': 'http://www.baseball-reference.com/players/gl.cgi?id=machama01&t=b&year=2016',
'Brandon_Moss': 'http://www.baseball-reference.com/players/gl.cgi?id=mossbr01&t=b&year=2016',
'Devon_Travis': 'http://www.baseball-reference.com/players/gl.cgi?id=travide01&t=b&year=2016',
'Bryce_Harper': 'http://www.baseball-reference.com/players/gl.cgi?id=harpebr03&t=b&year=2016',
'Asdrubal_Cabrera': 'http://www.baseball-reference.com/players/gl.cgi?id=cabreas01&t=b&year=2016',
'Seth_Smith': 'http://www.baseball-reference.com/players/gl.cgi?id=smithse01&t=b&year=2016',
'Brett_Lawrie': 'http://www.baseball-reference.com/players/gl.cgi?id=lawribr01&t=b&year=2016',
'McCutchen': 'http://www.baseball-reference.com/players/gl.cgi?id=mccutan01&t=b&year=2016',
'Alex_Rodriguez': 'http://www.baseball-reference.com/players/gl.cgi?id=rodrial01&t=b&year=2016',
'JT_Realmuto': 'http://www.baseball-reference.com/players/gl.cgi?id=realmjt01&t=b&year=2016',
'Tim_Anderson': 'http://www.baseball-reference.com/players/gl.cgi?id=anderti01&t=b&year=2016',
'Jacoby': 'http://www.baseball-reference.com/players/gl.cgi?id=ellsbja01&t=b&year=2016',
'Freddie_Freeman': 'http://www.baseball-reference.com/players/gl.cgi?id=freemfr01&t=b&year=2016',
'David_Ross': 'http://www.baseball-reference.com/players/gl.cgi?id=rossda01&t=b&year=2016',
'Ryan_Braun': 'http://www.baseball-reference.com/players/gl.cgi?id=braunry02&t=b&year=2016',
'Yonder_Alonso': 'http://www.baseball-reference.com/players/gl.cgi?id=alonsyo01&t=b&year=2016',
'Buster_Posey': 'http://www.baseball-reference.com/players/gl.cgi?id=poseybu01&t=b&year=2016',
'Carlos_Gomez': 'http://www.baseball-reference.com/players/gl.cgi?id=gomezca01&t=b&year=2016',
'Evan_Longoria': 'http://www.baseball-reference.com/players/gl.cgi?id=longoev01&t=b&year=2016',
'DJ_LeMahieu': 'http://www.baseball-reference.com/players/gl.cgi?id=lemahdj01&t=b&year=2016',
'Denard_Span': 'http://www.baseball-reference.com/players/gl.cgi?id=spande01&t=b&year=2016',
'Justin_Smoak': 'http://www.baseball-reference.com/players/gl.cgi?id=smoakju01&t=b&year=2016',
'Hanley_Ramirez': 'http://www.baseball-reference.com/players/gl.cgi?id=ramirha01&t=b&year=2016',
'Luis_Valbuena': 'http://www.baseball-reference.com/players/gl.cgi?id=valbulu01&t=b&year=2016',
'Mike_Trout': 'http://www.baseball-reference.com/players/gl.cgi?id=troutmi01&t=b&year=2016',
'Franklin_Gutierrez': 'http://www.baseball-reference.com/players/gl.cgi?id=gutiefr01&t=b&year=2016',
'Jason_Kipnis': 'http://www.baseball-reference.com/players/gl.cgi?id=kipnija01&t=b&year=2016',
'Jean_Segura': 'http://www.baseball-reference.com/players/gl.cgi?id=segurje01&t=b&year=2016',
'Josh_Harrison': 'http://www.baseball-reference.com/players/gl.cgi?id=harrijo05&t=b&year=2016',
'Corey_Dickerson': 'http://www.baseball-reference.com/players/gl.cgi?id=dickeco01&t=b&year=2016',
'James_McCann': 'http://www.baseball-reference.com/players/gl.cgi?id=mccanja02&t=b&year=2016',
'Ryan_Zimmerman': 'http://www.baseball-reference.com/players/gl.cgi?id=zimmery01&t=b&year=2016',
'Dioner_Navarro': 'http://www.baseball-reference.com/players/gl.cgi?id=navardi01&t=b&year=2016',
'Marcus_Semien': 'http://www.baseball-reference.com/players/gl.cgi?id=semiema01&t=b&year=2016',
'Paul_Goldschmidt': 'http://www.baseball-reference.com/players/gl.cgi?id=goldspa01&t=b&year=2016',
'Dustin_Pedroia': 'http://www.baseball-reference.com/players/gl.cgi?id=pedrodu01&t=b&year=2016',
'Prince_Fielder': 'http://www.baseball-reference.com/players/gl.cgi?id=fieldpr01&t=b&year=2016',
'Brandon_Phillips': 'http://www.baseball-reference.com/players/gl.cgi?id=phillbr01&t=b&year=2016',
'Kris_Bryant': 'http://www.baseball-reference.com/players/gl.cgi?id=bryankr01&t=b&year=2016',
'Didi_Gregorius': 'http://www.baseball-reference.com/players/gl.cgi?id=gregodi01&t=b&year=2016',
'Leonys_Martin': 'http://www.baseball-reference.com/players/gl.cgi?id=martile01&t=b&year=2016',
'Khris_Davis': 'http://www.baseball-reference.com/players/gl.cgi?id=daviskh01&t=b&year=2016',
'Ryon_Healy': 'http://www.baseball-reference.com/players/gl.cgi?id=healyry01&t=b&year=2016',
'Adrian_Beltre': 'http://www.baseball-reference.com/players/gl.cgi?id=beltrad01&t=b&year=2016',
'Scooter_Gennett': 'http://www.baseball-reference.com/players/gl.cgi?id=gennesc01&t=b&year=2016',
'Miguel_Cabrera': 'http://www.baseball-reference.com/players/gl.cgi?id=cabremi01&t=b&year=2016',
'Aledmys_Diaz': 'http://www.baseball-reference.com/players/gl.cgi?id=diazal02&t=b&year=2016',
'Victor_Martinez': 'http://www.baseball-reference.com/players/gl.cgi?id=martivi01&t=b&year=2016',
'Anthony_Rizzo': 'http://www.baseball-reference.com/players/gl.cgi?id=rizzoan01&t=b&year=2016',
'Stephen_Vogt': 'http://www.baseball-reference.com/players/gl.cgi?id=vogtst01&t=b&year=2016',
'Carlos_Santana': 'http://www.baseball-reference.com/players/gl.cgi?id=santaca01&t=b&year=2016',
'Lorenzo_Cain': 'http://www.baseball-reference.com/players/gl.cgi?id=cainlo01&t=b&year=2016',
'Ryan_Schimpf': 'http://www.baseball-reference.com/players/gl.cgi?id=schimry01&t=b&year=2016',
'Alcides_Escobar': 'http://www.baseball-reference.com/players/gl.cgi?id=escobal02&t=b&year=2016',
'Wilmer_Flores': 'http://www.baseball-reference.com/players/gl.cgi?id=florewi01&t=b&year=2016',
'Eduardo_Nunez': 'http://www.baseball-reference.com/players/gl.cgi?id=nunezed02&t=b&year=2016',
'Christian_Yelich': 'http://www.baseball-reference.com/players/gl.cgi?id=yelicch01&t=b&year=2016',
'Altuve': 'http://www.baseball-reference.com/players/gl.cgi?id=altuvjo01&t=b&year=2016',
'Jung-ho Kang': 'http://www.baseball-reference.com/players/gl.cgi?id=kangju01&t=b&year=2016',
'Granderson': 'http://www.baseball-reference.com/players/gl.cgi?id=grandcu01&t=b&year=2016',
'Derek_Norris': 'http://www.baseball-reference.com/players/gl.cgi?id=norride01&t=b&year=2016',
'Cesar_Hernandez': 'http://www.baseball-reference.com/players/gl.cgi?id=hernace02&t=b&year=2016',
'Joey_Votto': 'http://www.baseball-reference.com/players/gl.cgi?id=vottojo01&t=b&year=2016',
'Kev_Pillar': 'http://www.baseball-reference.com/players/gl.cgi?id=pillake01&t=b&year=2016',
'Kole_Calhoun': 'http://www.baseball-reference.com/players/gl.cgi?id=calhoko01&t=b&year=2016',
'Nolan_Arenado': 'http://www.baseball-reference.com/players/gl.cgi?id=arenano01&t=b&year=2016',
'Chris_Young': 'http://www.baseball-reference.com/players/gl.cgi?id=youngch04&t=b&year=2016',
'Gary_Sanchez': 'http://www.baseball-reference.com/players/gl.cgi?id=sanchga02&t=b&year=2016',
'Cameron_Maybin': 'http://www.baseball-reference.com/players/gl.cgi?id=maybica01&t=b&year=2016',
'Andrew_Romine': 'http://www.baseball-reference.com/players/gl.cgi?id=rominan01&t=b&year=2016',
    'Jake_Marisnick':'http://www.baseball-reference.com/players/gl.cgi?id=marisja01&t=b&year=2016',
    'Paulo_Orlando': 'http://www.baseball-reference.com/players/gl.cgi?id=orlanpa01&t=b&year=2016',
    'Andrelton_Simmons': 'http://www.baseball-reference.com/players/gl.cgi?id=simmoan01&t=b&year=2016',
    'Gregorio_Petit':'http://www.baseball-reference.com/players/gl.cgi?id=petitgr01&t=b&year=2016',
    'Johnny_Giavotella': 'http://www.baseball-reference.com/players/gl.cgi?id=giavojo01&t=b&year=2016',
    'Ichiro_Suzuki': 'http://www.baseball-reference.com/players/gl.cgi?id=suzukic01&t=b&year=2016',
    'Adeiny_Hechavarria': 'http://www.baseball-reference.com/players/gl.cgi?id=hechaad01&t=b&year=2016',
    'James_Loney': 'http://www.baseball-reference.com/players/gl.cgi?id=loneyja01&t=b&year=2016',
    'Rene_Rivera': 'http://www.baseball-reference.com/players/gl.cgi?id=riverre01&t=b&year=2016',
    'Jose_Reyes': 'http://www.baseball-reference.com/players/gl.cgi?id=reyesjo01&t=b&year=2016',
    'Josh_Reddick':'http://www.baseball-reference.com/players/gl.cgi?id=reddijo01&t=b&year=2016',
    'Jed_Lowrie': 'http://www.baseball-reference.com/players/gl.cgi?id=lowrije01&t=b&year=2016',
    'Peter_Bourjos': 'http://www.baseball-reference.com/players/gl.cgi?id=bourjpe01&t=b&year=2016',
    'John_Jaso': 'http://www.baseball-reference.com/players/gl.cgi?id=jasojo01&t=b&year=2016',
    'Francisco_Cervelli': 'http://www.baseball-reference.com/players/gl.cgi?id=cervefr01&t=b&year=2016',
    'Jordy_Mercer': 'http://www.baseball-reference.com/players/gl.cgi?id=mercejo03&t=b&year=2016',
    'Travis_Jankowski': 'http://www.baseball-reference.com/players/gl.cgi?id=jankotr01&t=b&year=2016',
    'Jon_Jay':'http://www.baseball-reference.com/players/gl.cgi?id=jayjo02&t=b&year=2016',
    'Alexei_Ramirez': 'http://www.baseball-reference.com/players/gl.cgi?id=ramiral03&t=b&year=2016',
    'Joe_Panik':'http://www.baseball-reference.com/players/gl.cgi?id=panikjo01&t=b&year=2016',
    'Nori_Aoki': 'http://www.baseball-reference.com/players/gl.cgi?id=aokino01&t=b&year=2016',
    'Chris_Iannetta': 'http://www.baseball-reference.com/players/gl.cgi?id=iannech01&t=b&year=2016',
    'Kolten_Wong':'http://www.baseball-reference.com/players/gl.cgi?id=wongko01&t=b&year=2016',
    'Jhonny_Peralta': 'http://www.baseball-reference.com/players/gl.cgi?id=peraljh01&t=b&year=2016',
    'Shin-soo_Choo': 'http://www.baseball-reference.com/players/gl.cgi?id=choosh01&t=b&year=2016',
    'Mitch_Moreland': 'http://www.baseball-reference.com/players/gl.cgi?id=morelmi01&t=b&year=2016',
    'Robinson_Chirinos': 'http://www.baseball-reference.com/players/gl.cgi?id=chiriro01&t=b&year=2016',
    'Darwin_Barney': 'http://www.baseball-reference.com/players/gl.cgi?id=barneda01&t=b&year=2016',
    'Ben_Revere': 'http://www.baseball-reference.com/players/gl.cgi?id=reverbe01&t=b&year=2016'
    }

####################################################

#These have not yet been scraped
players_urls = {

     
}

players_career_data = {
    
    
}

players_game_logs = {
    
}

players_career_v_pitcher = {
 'A_Gonzalez': 'http://www.baseball-reference.com/players/split.cgi?id=gonzaad01&year=Career&t=b',
 'Abraham_Almonte': 'http://www.baseball-reference.com/players/split.cgi?id=almonab01&year=Career&t=b',
 'Adam Eaton': 'http://www.baseball-reference.com/players/split.cgi?id=eatonad02&year=Career&t=b',
 'Adam_Duvall': 'http://www.baseball-reference.com/players/split.cgi?id=duvalad01&year=Career&t=b',
 'Adam_Jones': 'http://www.baseball-reference.com/players/split.cgi?id=jonesad01&year=Career&t=b',
 'Adam_Lind': 'http://www.baseball-reference.com/players/split.cgi?id=lindad01&year=Career&t=b',
 'Adam_Rosales': 'http://www.baseball-reference.com/players/split.cgi?id=rosalad01&year=Career&t=b',
 'Addison_Russell': 'http://www.baseball-reference.com/players/split.cgi?id=russead02&year=Career&t=b',
 'Adeiny_Hechavarria': 'http://www.baseball-reference.com/players/split.cgi?id=hechaad01&year=Career&t=b',
 'Adonis_Garcia': 'http://www.baseball-reference.com/players/split.cgi?id=garciad01&year=Career&t=b',
 'Adrian_Beltre': 'http://www.baseball-reference.com/players/split.cgi?id=beltrad01&year=Career&t=b',
 'Albert_Pujols': 'http://www.baseball-reference.com/players/split.cgi?id=pujolal01&year=Career&t=b',
 'Alcides_Escobar': 'http://www.baseball-reference.com/players/split.cgi?id=escobal02&year=Career&t=b',
 'Aledmys_Diaz': 'http://www.baseball-reference.com/players/split.cgi?id=diazal02&year=Career&t=b',
 'Alex_Gordon': 'http://www.baseball-reference.com/players/split.cgi?id=gordoal01&year=Career&t=b',
 'Alex_Rodriguez': 'http://www.baseball-reference.com/players/split.cgi?id=rodrial01&year=Career&t=b',
 'Alexei_Ramirez': 'http://www.baseball-reference.com/players/split.cgi?id=ramiral03&year=Career&t=b',
 'Altuve': 'http://www.baseball-reference.com/players/split.cgi?id=altuvjo01&year=Career&t=b',
 'Andrelton_Simmons': 'http://www.baseball-reference.com/players/split.cgi?id=simmoan01&year=Career&t=b',
 'Andrew_Romine': 'http://www.baseball-reference.com/players/split.cgi?id=rominan01&year=Career&t=b',
 'Angel_Pagan': 'http://www.baseball-reference.com/players/split.cgi?id=paganan01&year=Career&t=b',
 'Anthony_Rendon': 'http://www.baseball-reference.com/players/split.cgi?id=rendoan01&year=Career&t=b',
 'Anthony_Rizzo': 'http://www.baseball-reference.com/players/split.cgi?id=rizzoan01&year=Career&t=b',
 'Asdrubal_Cabrera': 'http://www.baseball-reference.com/players/split.cgi?id=cabreas01&year=Career&t=b',
 'Austin_Jackson': 'http://www.baseball-reference.com/players/split.cgi?id=jacksau01&year=Career&t=b',
 'Avisail_Garcia': 'http://www.baseball-reference.com/players/split.cgi?id=garciav01&year=Career&t=b',
 'Ben_Revere': 'http://www.baseball-reference.com/players/split.cgi?id=reverbe01&year=Career&t=b',
 'Ben_Zobrist': 'http://www.baseball-reference.com/players/split.cgi?id=zobribe01&year=Career&t=b',
 'Billy_Hamilton': 'http://www.baseball-reference.com/players/split.cgi?id=hamilbi02&year=Career&t=b',
 'Brad_Miller': 'http://www.baseball-reference.com/players/split.cgi?id=millebr02&year=Career&t=b',
 'Brain_McCann': 'http://www.baseball-reference.com/players/split.cgi?id=mccanbr01&year=Career&t=b',
 'Brandon_Belt': 'http://www.baseball-reference.com/players/split.cgi?id=beltbr01&year=Career&t=b',
 'Brandon_Crawford': 'http://www.baseball-reference.com/players/split.cgi?id=crawfbr01&year=Career&t=b',
 'Brandon_Drury': 'http://www.baseball-reference.com/players/split.cgi?id=drurybr01&year=Career&t=b',
 'Brandon_Guyer': 'http://www.baseball-reference.com/players/split.cgi?id=guyerbr01&year=Career&t=b',
 'Brandon_Moss': 'http://www.baseball-reference.com/players/split.cgi?id=mossbr01&year=Career&t=b',
 'Brandon_Phillips': 'http://www.baseball-reference.com/players/split.cgi?id=phillbr01&year=Career&t=b',
 'Brett_Lawrie': 'http://www.baseball-reference.com/players/split.cgi?id=lawribr01&year=Career&t=b',
 'Brett_gardner': 'http://www.baseball-reference.com/players/split.cgi?id=gardnbr01&year=Career&t=b',
 'Brock_Holt': 'http://www.baseball-reference.com/players/split.cgi?id=holtbr01&year=Career&t=b',
 'Bryce_Harper': 'http://www.baseball-reference.com/players/split.cgi?id=harpebr03&year=Career&t=b',
 'Buster_Posey': 'http://www.baseball-reference.com/players/split.cgi?id=poseybu01&year=Career&t=b',
 'Byron_Buxton': 'http://www.baseball-reference.com/players/split.cgi?id=buxtoby01&year=Career&t=b',
 'Byung-Ho_Park': 'http://www.baseball-reference.com/players/split.cgi?id=parkby01&year=Career&t=b',
 'C.J._Cron': 'http://www.baseball-reference.com/players/split.cgi?id=croncj01&year=Career&t=b',
 'Cameron_Maybin': 'http://www.baseball-reference.com/players/split.cgi?id=maybica01&year=Career&t=b',
 'Cameron_Rupp': 'http://www.baseball-reference.com/players/split.cgi?id=ruppca01&year=Career&t=b',
 'Cano': 'http://www.baseball-reference.com/players/split.cgi?id=canoro01&year=Career&t=b',
 'Carlos_Beltran': 'http://www.baseball-reference.com/players/split.cgi?id=beltrca01&year=Career&t=b',
 'Carlos_Correa': 'http://www.baseball-reference.com/players/split.cgi?id=correca01&year=Career&t=b',
 'Carlos_Gomez': 'http://www.baseball-reference.com/players/split.cgi?id=gomezca01&year=Career&t=b',
 'Carlos_Gonzalez': 'http://www.baseball-reference.com/players/split.cgi?id=gonzaca01&year=Career&t=b',
 'Carlos_Santana': 'http://www.baseball-reference.com/players/split.cgi?id=santaca01&year=Career&t=b',
 'Cesar_Hernandez': 'http://www.baseball-reference.com/players/split.cgi?id=hernace02&year=Career&t=b',
 'Charlie_Blackmon': 'http://www.baseball-reference.com/players/split.cgi?id=blackch02&year=Career&t=b',
 'Chase_Headley': 'http://www.baseball-reference.com/players/split.cgi?id=headlch01&year=Career&t=b',
 'Chase_Utley': 'http://www.baseball-reference.com/players/split.cgi?id=utleych01&year=Career&t=b',
 'Cheslor_Cuthbert': 'http://www.baseball-reference.com/players/split.cgi?id=cuthbch01&year=Career&t=b',
 'Chris_Carter': 'http://www.baseball-reference.com/players/split.cgi?id=cartech02&year=Career&t=b',
 'Chris_Davis': 'http://www.baseball-reference.com/players/split.cgi?id=davisch02&year=Career&t=b',
 'Chris_Iannetta': 'http://www.baseball-reference.com/players/split.cgi?id=iannech01&year=Career&t=b',
 'Chris_Owings': 'http://www.baseball-reference.com/players/split.cgi?id=owingch01&year=Career&t=b',
 'Chris_Young': 'http://www.baseball-reference.com/players/split.cgi?id=youngch04&year=Career&t=b',
 'Christian_Yelich': 'http://www.baseball-reference.com/players/split.cgi?id=yelicch01&year=Career&t=b',
 'Coco_Crisp': 'http://www.baseball-reference.com/players/split.cgi?id=crispco01&year=Career&t=b',
 'Colby_Rasmus': 'http://www.baseball-reference.com/players/split.cgi?id=rasmuco01&year=Career&t=b',
 'Corey_Dickerson': 'http://www.baseball-reference.com/players/split.cgi?id=dickeco01&year=Career&t=b',
 'Corey_Seager': 'http://www.baseball-reference.com/players/split.cgi?id=seageco01&year=Career&t=b',
 'Cristhian_Adames': 'http://www.baseball-reference.com/players/split.cgi?id=adamecr01&year=Career&t=b',
 'DJ_LeMahieu': 'http://www.baseball-reference.com/players/split.cgi?id=lemahdj01&year=Career&t=b',
 'Dae-Ho_Lee': 'http://www.baseball-reference.com/players/split.cgi?id=leeda02&year=Career&t=b',
 'Daniel_Murphy': 'http://www.baseball-reference.com/players/split.cgi?id=murphda08&year=Career&t=b',
 'Darwin_Barney': 'http://www.baseball-reference.com/players/split.cgi?id=barneda01&year=Career&t=b',
 'David_Ross': 'http://www.baseball-reference.com/players/split.cgi?id=rossda01&year=Career&t=b',
 'Dee_Gordon': 'http://www.baseball-reference.com/players/split.cgi?id=gordode01&year=Career&t=b',
 'Denard_Span': 'http://www.baseball-reference.com/players/split.cgi?id=spande01&year=Career&t=b',
 'Derek_Norris': 'http://www.baseball-reference.com/players/split.cgi?id=norride01&year=Career&t=b',
 'Devon_Travis': 'http://www.baseball-reference.com/players/split.cgi?id=travide01&year=Career&t=b',
 'Dexter_Fowler': 'http://www.baseball-reference.com/players/split.cgi?id=fowlede01&year=Career&t=b',
 'Didi_Gregorius': 'http://www.baseball-reference.com/players/split.cgi?id=gregodi01&year=Career&t=b',
 'Dioner_Navarro': 'http://www.baseball-reference.com/players/split.cgi?id=navardi01&year=Career&t=b',
 'Domingo_Santana': 'http://www.baseball-reference.com/players/split.cgi?id=santado01&year=Career&t=b',
 'Dozier': 'http://www.baseball-reference.com/players/split.cgi?id=doziebr01&year=Career&t=b',
 'Dustin_Pedroia': 'http://www.baseball-reference.com/players/split.cgi?id=pedrodu01&year=Career&t=b',
 'Eddie_Rosario': 'http://www.baseball-reference.com/players/split.cgi?id=rosared01&year=Career&t=b',
 'Eduardo_Nunez': 'http://www.baseball-reference.com/players/split.cgi?id=nunezed02&year=Career&t=b',
 'Edwin_Encarnacion': 'http://www.baseball-reference.com/players/split.cgi?id=encared01&year=Career&t=b',
 'Elvis_Andrus': 'http://www.baseball-reference.com/players/split.cgi?id=andruel01&year=Career&t=b',
 'Ender_Inciarte': 'http://www.baseball-reference.com/players/split.cgi?id=inciaen01&year=Career&t=b',
 'Eric_Hosmer': 'http://www.baseball-reference.com/players/split.cgi?id=hosmeer01&year=Career&t=b',
 'Erick_Aybar': 'http://www.baseball-reference.com/players/split.cgi?id=aybarer01&year=Career&t=b',
 'Espinosa': 'http://www.baseball-reference.com/players/split.cgi?id=espinda01&year=Career&t=b',
 'Eugenio_Suarez': 'http://www.baseball-reference.com/players/split.cgi?id=suareeu01&year=Career&t=b',
 'Evan_Gattis': 'http://www.baseball-reference.com/players/split.cgi?id=gattiev01&year=Career&t=b',
 'Evan_Longoria': 'http://www.baseball-reference.com/players/split.cgi?id=longoev01&year=Career&t=b',
 'Francisco_Cervelli': 'http://www.baseball-reference.com/players/split.cgi?id=cervefr01&year=Career&t=b',
 'Francisco_Lindor': 'http://www.baseball-reference.com/players/split.cgi?id=lindofr01&year=Career&t=b',
 'Franklin_Gutierrez': 'http://www.baseball-reference.com/players/split.cgi?id=gutiefr01&year=Career&t=b',
 'Freddie_Freeman': 'http://www.baseball-reference.com/players/split.cgi?id=freemfr01&year=Career&t=b',
 'Freddy_Galvis': 'http://www.baseball-reference.com/players/split.cgi?id=galvifr01&year=Career&t=b',
 'Gary_Sanchez': 'http://www.baseball-reference.com/players/split.cgi?id=sanchga02&year=Career&t=b',
 'George_Springer': 'http://www.baseball-reference.com/players/split.cgi?id=springe01&year=Career&t=b',
 'Gerardo_Parra': 'http://www.baseball-reference.com/players/split.cgi?id=parrage01&year=Career&t=b',
 'Giancarlo_Stanton': 'http://www.baseball-reference.com/players/split.cgi?id=stantmi03&year=Career&t=b',
 'Granderson': 'http://www.baseball-reference.com/players/split.cgi?id=grandcu01&year=Career&t=b',
 'Gregorio_Petit': 'http://www.baseball-reference.com/players/split.cgi?id=petitgr01&year=Career&t=b',
 'Gregory_Polanco': 'http://www.baseball-reference.com/players/split.cgi?id=polangr01&year=Career&t=b',
 'Hanley_Ramirez': 'http://www.baseball-reference.com/players/split.cgi?id=ramirha01&year=Career&t=b',
 'Hernan_Perez': 'http://www.baseball-reference.com/players/split.cgi?id=perezhe01&year=Career&t=b',
 'Howie_Kendrick': 'http://www.baseball-reference.com/players/split.cgi?id=kendrho01&year=Career&t=b',
 'Hunter_Pence': 'http://www.baseball-reference.com/players/split.cgi?id=pencehu01&year=Career&t=b',
 'Ian_Desmond': 'http://www.baseball-reference.com/players/split.cgi?id=desmoia01&year=Career&t=b',
 'Ian_Kinsler': 'http://www.baseball-reference.com/players/split.cgi?id=kinslia01&year=Career&t=b',
 'Ichiro_Suzuki': 'http://www.baseball-reference.com/players/split.cgi?id=suzukic01&year=Career&t=b',
 'Iglesias': 'http://www.baseball-reference.com/players/split.cgi?id=iglesjo01&year=Career&t=b',
 'JD_Martinez': 'http://www.baseball-reference.com/players/split.cgi?id=martijd02&year=Career&t=b',
 'JJ_Hardy': 'http://www.baseball-reference.com/players/split.cgi?id=hardyjj01&year=Career&t=b',
 'JT_Realmuto': 'http://www.baseball-reference.com/players/split.cgi?id=realmjt01&year=Career&t=b',
 'Jace_Peterson': 'http://www.baseball-reference.com/players/split.cgi?id=peterja01&year=Career&t=b',
 'Jackie_Bradley': 'http://www.baseball-reference.com/players/split.cgi?id=bradlja02&year=Career&t=b',
 'Jacoby': 'http://www.baseball-reference.com/players/split.cgi?id=ellsbja01&year=Career&t=b',
 'Jake_Lamb': 'http://www.baseball-reference.com/players/split.cgi?id=lambja01&year=Career&t=b',
 'Jake_Marisnick': 'http://www.baseball-reference.com/players/split.cgi?id=marisja01&year=Career&t=b',
 'James_Loney': 'http://www.baseball-reference.com/players/split.cgi?id=loneyja01&year=Career&t=b',
 'James_McCann': 'http://www.baseball-reference.com/players/split.cgi?id=mccanja02&year=Career&t=b',
 'Jarrod_Dyson': 'http://www.baseball-reference.com/players/split.cgi?id=dysonja01&year=Career&t=b',
 'Jarrod_Salty': 'http://www.baseball-reference.com/players/split.cgi?id=saltaja01&year=Career&t=b',
 'Jason_Castro': 'http://www.baseball-reference.com/players/split.cgi?id=castrja01&year=Career&t=b',
 'Jason_Heyward': 'http://www.baseball-reference.com/players/split.cgi?id=heywaja01&year=Career&t=b',
 'Jason_Kipnis': 'http://www.baseball-reference.com/players/split.cgi?id=kipnija01&year=Career&t=b',
 'Javier_Baez': 'http://www.baseball-reference.com/players/split.cgi?id=baezja01&year=Career&t=b',
 'Jay_Bruce': 'http://www.baseball-reference.com/players/split.cgi?id=bruceja01&year=Career&t=b',
 'Jayson_Werth': 'http://www.baseball-reference.com/players/split.cgi?id=werthja01&year=Career&t=b',
 'Jean_Segura': 'http://www.baseball-reference.com/players/split.cgi?id=segurje01&year=Career&t=b',
 'Jed_Lowrie': 'http://www.baseball-reference.com/players/split.cgi?id=lowrije01&year=Career&t=b',
 'Jedd_Gyorko': 'http://www.baseball-reference.com/players/split.cgi?id=gyorkje01&year=Career&t=b',
 'Jefry_Marte': 'http://www.baseball-reference.com/players/split.cgi?id=marteje01&year=Career&t=b',
 'Jhonny_Peralta': 'http://www.baseball-reference.com/players/split.cgi?id=peraljh01&year=Career&t=b',
 'Jimmy_Rollins': 'http://www.baseball-reference.com/players/split.cgi?id=rolliji01&year=Career&t=b',
 'Joc_Pederson': 'http://www.baseball-reference.com/players/split.cgi?id=pederjo01&year=Career&t=b',
 'Joe_Mauer': 'http://www.baseball-reference.com/players/split.cgi?id=mauerjo01&year=Career&t=b',
 'Joe_Panik': 'http://www.baseball-reference.com/players/split.cgi?id=panikjo01&year=Career&t=b',
 'Joey_Votto': 'http://www.baseball-reference.com/players/split.cgi?id=vottojo01&year=Career&t=b',
 'John_Jaso': 'http://www.baseball-reference.com/players/split.cgi?id=jasojo01&year=Career&t=b',
 'Johnny_Giavotella': 'http://www.baseball-reference.com/players/split.cgi?id=giavojo01&year=Career&t=b',
 'Jon_Jay': 'http://www.baseball-reference.com/players/split.cgi?id=jayjo02&year=Career&t=b',
 'Jonathan_Lucroy': 'http://www.baseball-reference.com/players/split.cgi?id=lucrojo01&year=Career&t=b',
 'Jonathan_Villar': 'http://www.baseball-reference.com/players/split.cgi?id=villajo01&year=Career&t=b',
 'Jordy_Mercer': 'http://www.baseball-reference.com/players/split.cgi?id=mercejo03&year=Career&t=b',
 'Jose_Abreu': 'http://www.baseball-reference.com/players/split.cgi?id=abreujo02&year=Career&t=b',
 'Jose_Bautista': 'http://www.baseball-reference.com/players/split.cgi?id=bautijo02&year=Career&t=b',
 'Jose_Peraza': 'http://www.baseball-reference.com/players/split.cgi?id=perazjo01&year=Career&t=b',
 'Jose_Ramirez': 'http://www.baseball-reference.com/players/split.cgi?id=ramirjo01&year=Career&t=b',
 'Jose_Reyes': 'http://www.baseball-reference.com/players/split.cgi?id=reyesjo01&year=Career&t=b',
 'Josh_Donaldson': 'http://www.baseball-reference.com/players/split.cgi?id=donaljo02&year=Career&t=b',
 'Josh_Harrison': 'http://www.baseball-reference.com/players/split.cgi?id=harrijo05&year=Career&t=b',
 'Josh_Reddick': 'http://www.baseball-reference.com/players/split.cgi?id=reddijo01&year=Career&t=b',
 'Juan_Uribe': 'http://www.baseball-reference.com/players/split.cgi?id=uribeju01&year=Career&t=b',
 'Jung-ho Kang': 'http://www.baseball-reference.com/players/split.cgi?id=kangju01&year=Career&t=b',
 'Justin_Bour': 'http://www.baseball-reference.com/players/split.cgi?id=bourju01&year=Career&t=b',
 'Justin_Smoak': 'http://www.baseball-reference.com/players/split.cgi?id=smoakju01&year=Career&t=b',
 'Justin_Turner': 'http://www.baseball-reference.com/players/split.cgi?id=turneju01&year=Career&t=b',
 'Justin_Upton': 'http://www.baseball-reference.com/players/split.cgi?id=uptonju01&year=Career&t=b',
 'Kendrys_Morales': 'http://www.baseball-reference.com/players/split.cgi?id=moralke01&year=Career&t=b',
 'Keon_Broxton': 'http://www.baseball-reference.com/players/split.cgi?id=broxtke01&year=Career&t=b',
 'Kev_Pillar': 'http://www.baseball-reference.com/players/split.cgi?id=pillake01&year=Career&t=b',
 'Kevin_Kiermaier': 'http://www.baseball-reference.com/players/split.cgi?id=kiermke01&year=Career&t=b',
 'Khris_Davis': 'http://www.baseball-reference.com/players/split.cgi?id=daviskh01&year=Career&t=b',
 'Kirk_Nieuwenhuis': 'http://www.baseball-reference.com/players/split.cgi?id=nieuwki01&year=Career&t=b',
 'Kole_Calhoun': 'http://www.baseball-reference.com/players/split.cgi?id=calhoko01&year=Career&t=b',
 'Kolten_Wong': 'http://www.baseball-reference.com/players/split.cgi?id=wongko01&year=Career&t=b',
 'Kris_Bryant': 'http://www.baseball-reference.com/players/split.cgi?id=bryankr01&year=Career&t=b',
 'Kurt_Suzuki': 'http://www.baseball-reference.com/players/split.cgi?id=suzukku01&year=Career&t=b',
 'Kyle_Seager': 'http://www.baseball-reference.com/players/split.cgi?id=seageky01&year=Career&t=b',
 'Leonys_Martin': 'http://www.baseball-reference.com/players/split.cgi?id=martile01&year=Career&t=b',
 'Logan_Forsythe': 'http://www.baseball-reference.com/players/split.cgi?id=forsylo01&year=Career&t=b',
 'Logan_Morrison': 'http://www.baseball-reference.com/players/split.cgi?id=morrilo01&year=Career&t=b',
 'Lonnie_Chisenhall': 'http://www.baseball-reference.com/players/split.cgi?id=chiselo01&year=Career&t=b',
 'Lorenzo_Cain': 'http://www.baseball-reference.com/players/split.cgi?id=cainlo01&year=Career&t=b',
 'Luis_Valbuena': 'http://www.baseball-reference.com/players/split.cgi?id=valbulu01&year=Career&t=b',
 'Maikel_Franco': 'http://www.baseball-reference.com/players/split.cgi?id=francma02&year=Career&t=b',
 'Manny_Machado': 'http://www.baseball-reference.com/players/split.cgi?id=machama01&year=Career&t=b',
 'Marcell_Ozuna': 'http://www.baseball-reference.com/players/split.cgi?id=ozunama01&year=Career&t=b',
 'Marcus_Semien': 'http://www.baseball-reference.com/players/split.cgi?id=semiema01&year=Career&t=b',
 'Mark_Reynolds': 'http://www.baseball-reference.com/players/split.cgi?id=reynoma01&year=Career&t=b',
 'Mark_Teixeira': 'http://www.baseball-reference.com/players/split.cgi?id=teixema01&year=Career&t=b',
 'Mark_Trumbo': 'http://www.baseball-reference.com/players/split.cgi?id=trumbma01&year=Career&t=b',
 'Martin_Maldonado': 'http://www.baseball-reference.com/players/split.cgi?id=maldoma01&year=Career&t=b',
 'Martin_Prado': 'http://www.baseball-reference.com/players/split.cgi?id=pradoma01&year=Career&t=b',
 'Marwin_Gonzalez': 'http://www.baseball-reference.com/players/split.cgi?id=gonzama01&year=Career&t=b',
 'Matt_Adams': 'http://www.baseball-reference.com/players/split.cgi?id=adamsma01&year=Career&t=b',
 'Matt_Carpenter': 'http://www.baseball-reference.com/players/split.cgi?id=carpema01&year=Career&t=b',
 'Matt_Holiday': 'http://www.baseball-reference.com/players/split.cgi?id=hollima01&year=Career&t=b',
 'Matt_Joyce': 'http://www.baseball-reference.com/players/split.cgi?id=joycema01&year=Career&t=b',
 'Matt_Kemp': 'http://www.baseball-reference.com/players/split.cgi?id=kempma01&year=Career&t=b',
 'Matt_Wieters': 'http://www.baseball-reference.com/players/split.cgi?id=wietema01&year=Career&t=b',
 'Max_Kepler': 'http://www.baseball-reference.com/players/split.cgi?id=keplema01&year=Career&t=b',
 'McCutchen': 'http://www.baseball-reference.com/players/split.cgi?id=mccutan01&year=Career&t=b',
 'Melky Cabrera': 'http://www.baseball-reference.com/players/split.cgi?id=cabreme01&year=Career&t=b',
 'Michael_Bourn': 'http://www.baseball-reference.com/players/split.cgi?id=bournmi01&year=Career&t=b',
 'Michael_Saunders': 'http://www.baseball-reference.com/players/split.cgi?id=saundmi01&year=Career&t=b',
 'Miguel_Cabrera': 'http://www.baseball-reference.com/players/split.cgi?id=cabremi01&year=Career&t=b',
 'Miguel_Montero': 'http://www.baseball-reference.com/players/split.cgi?id=montemi01&year=Career&t=b',
 'Mike_Napoli': 'http://www.baseball-reference.com/players/split.cgi?id=napolmi01&year=Career&t=b',
 'Mike_Trout': 'http://www.baseball-reference.com/players/split.cgi?id=troutmi01&year=Career&t=b',
 'Mike_Zunino': 'http://www.baseball-reference.com/players/split.cgi?id=zuninmi01&year=Career&t=b',
 'Mitch_Moreland': 'http://www.baseball-reference.com/players/split.cgi?id=morelmi01&year=Career&t=b',
 'Mookie_Betts': 'http://www.baseball-reference.com/players/split.cgi?id=bettsmo01&year=Career&t=b',
 'Neil_Walker': 'http://www.baseball-reference.com/players/split.cgi?id=walkene01&year=Career&t=b',
 'Nelson_Cruz': 'http://www.baseball-reference.com/players/split.cgi?id=cruzne02&year=Career&t=b',
 'Nick_Castellanos': 'http://www.baseball-reference.com/players/split.cgi?id=casteni01&year=Career&t=b',
 'Nick_Hundley': 'http://www.baseball-reference.com/players/split.cgi?id=hundlni01&year=Career&t=b',
 'Nick_Markakis': 'http://www.baseball-reference.com/players/split.cgi?id=markani01&year=Career&t=b',
 'Nolan_Arenado': 'http://www.baseball-reference.com/players/split.cgi?id=arenano01&year=Career&t=b',
 'Nomar_Mazara': 'http://www.baseball-reference.com/players/split.cgi?id=mazarno01&year=Career&t=b',
 'Nori_Aoki': 'http://www.baseball-reference.com/players/split.cgi?id=aokino01&year=Career&t=b',
 'Odubel_Herrera': 'http://www.baseball-reference.com/players/split.cgi?id=herreod01&year=Career&t=b',
 'Ortiz': 'http://www.baseball-reference.com/players/split.cgi?id=ortizda01&year=Career&t=b',
 'Paul_Goldschmidt': 'http://www.baseball-reference.com/players/split.cgi?id=goldspa01&year=Career&t=b',
 'Paulo_Orlando': 'http://www.baseball-reference.com/players/split.cgi?id=orlanpa01&year=Career&t=b',
 'Pedro_Alvarez': 'http://www.baseball-reference.com/players/split.cgi?id=alvarpe01&year=Career&t=b',
 'Peter_Bourjos': 'http://www.baseball-reference.com/players/split.cgi?id=bourjpe01&year=Career&t=b',
 'Prince_Fielder': 'http://www.baseball-reference.com/players/split.cgi?id=fieldpr01&year=Career&t=b',
 'Rajai_Davis': 'http://www.baseball-reference.com/players/split.cgi?id=davisra01&year=Career&t=b',
 'Randal_Grichuk': 'http://www.baseball-reference.com/players/split.cgi?id=grichra01&year=Career&t=b',
 'Rene_Rivera': 'http://www.baseball-reference.com/players/split.cgi?id=riverre01&year=Career&t=b',
 'Robbie_Grossman': 'http://www.baseball-reference.com/players/split.cgi?id=grossro01&year=Career&t=b',
 'Roberto_Perez': 'http://www.baseball-reference.com/players/split.cgi?id=perezro02&year=Career&t=b',
 'Robinson_Chirinos': 'http://www.baseball-reference.com/players/split.cgi?id=chiriro01&year=Career&t=b',
 'Rougned_Odor': 'http://www.baseball-reference.com/players/split.cgi?id=odorro01&year=Career&t=b',
 'Russell_Martin': 'http://www.baseball-reference.com/players/split.cgi?id=martiru01&year=Career&t=b',
 'Ryan_Braun': 'http://www.baseball-reference.com/players/split.cgi?id=braunry02&year=Career&t=b',
 'Ryan_Hanigan': 'http://www.baseball-reference.com/players/split.cgi?id=hanigry01&year=Career&t=b',
 'Ryan_Howard': 'http://www.baseball-reference.com/players/split.cgi?id=howarry01&year=Career&t=b',
 'Ryan_Schimpf': 'http://www.baseball-reference.com/players/split.cgi?id=schimry01&year=Career&t=b',
 'Ryan_Zimmerman': 'http://www.baseball-reference.com/players/split.cgi?id=zimmery01&year=Career&t=b',
 'Ryon_Healy': 'http://www.baseball-reference.com/players/split.cgi?id=healyry01&year=Career&t=b',
 'Salvador_Perez': 'http://www.baseball-reference.com/players/split.cgi?id=perezsa02&year=Career&t=b',
 'Sandy_Leon': 'http://www.baseball-reference.com/players/split.cgi?id=leonsa01&year=Career&t=b',
 'Schoop': 'http://www.baseball-reference.com/players/split.cgi?id=schoojo01&year=Career&t=b',
 'Scooter_Gennett': 'http://www.baseball-reference.com/players/split.cgi?id=gennesc01&year=Career&t=b',
 'Scott_Schebler': 'http://www.baseball-reference.com/players/split.cgi?id=schebsc01&year=Career&t=b',
 'Sean_Rodriguez': 'http://www.baseball-reference.com/players/split.cgi?id=rodrise01&year=Career&t=b',
 'Seth_Smith': 'http://www.baseball-reference.com/players/split.cgi?id=smithse01&year=Career&t=b',
 'Shin-soo_Choo': 'http://www.baseball-reference.com/players/split.cgi?id=choosh01&year=Career&t=b',
 'Starlin_Castro': 'http://www.baseball-reference.com/players/split.cgi?id=castrst01&year=Career&t=b',
 'Starling_Marte': 'http://www.baseball-reference.com/players/split.cgi?id=martest01&year=Career&t=b',
 'Stephen_Piscotty': 'http://www.baseball-reference.com/players/split.cgi?id=piscost01&year=Career&t=b',
 'Stephen_Vogt': 'http://www.baseball-reference.com/players/split.cgi?id=vogtst01&year=Career&t=b',
 'Steve_Pearce': 'http://www.baseball-reference.com/players/split.cgi?id=pearcst01&year=Career&t=b',
 'Steven_Souza': 'http://www.baseball-reference.com/players/split.cgi?id=souzast01&year=Career&t=b',
 'Tim_Anderson': 'http://www.baseball-reference.com/players/split.cgi?id=anderti01&year=Career&t=b',
 'Todd_Frazier': 'http://www.baseball-reference.com/players/split.cgi?id=frazito01&year=Career&t=b',
 'Tommy_Joseph': 'http://www.baseball-reference.com/players/split.cgi?id=josepto01&year=Career&t=b',
 'Travis_Jankowski': 'http://www.baseball-reference.com/players/split.cgi?id=jankotr01&year=Career&t=b',
 'Travis_Shaw': 'http://www.baseball-reference.com/players/split.cgi?id=shawtr01&year=Career&t=b',
 'Trea_Turner': 'http://www.baseball-reference.com/players/split.cgi?id=turnetr01&year=Career&t=b',
 'Trevor_Plouffe': 'http://www.baseball-reference.com/players/split.cgi?id=plouftr01&year=Career&t=b',
 'Trevor_Story': 'http://www.baseball-reference.com/players/split.cgi?id=storytr01&year=Career&t=b',
 'Troy_Tulowitzki': 'http://www.baseball-reference.com/players/split.cgi?id=tulowtr01&year=Career&t=b',
 'Tucker_Barnhart': 'http://www.baseball-reference.com/players/split.cgi?id=barnhtu01&year=Career&t=b',
 'Tyler_Flowers': 'http://www.baseball-reference.com/players/split.cgi?id=flowety01&year=Career&t=b',
 'Tyler_Naquin': 'http://www.baseball-reference.com/players/split.cgi?id=naquity01&year=Career&t=b',
 'Tyler_Saladino': 'http://www.baseball-reference.com/players/split.cgi?id=saladty01&year=Career&t=b',
 'Victor_Martinez': 'http://www.baseball-reference.com/players/split.cgi?id=martivi01&year=Career&t=b',
 'Welington_Castillo': 'http://www.baseball-reference.com/players/split.cgi?id=castiwe01&year=Career&t=b',
 'Wil_Myers': 'http://www.baseball-reference.com/players/split.cgi?id=myerswi01&year=Career&t=b',
 'Wilmer_Flores': 'http://www.baseball-reference.com/players/split.cgi?id=florewi01&year=Career&t=b',
 'Wilson_Ramos': 'http://www.baseball-reference.com/players/split.cgi?id=ramoswi01&year=Career&t=b',
 'Xander': 'http://www.baseball-reference.com/players/split.cgi?id=bogaexa01&year=Career&t=b',
 'Yadier_Molina': 'http://www.baseball-reference.com/players/split.cgi?id=molinya01&year=Career&t=b',
 'Yan_Gomes': 'http://www.baseball-reference.com/players/split.cgi?id=gomesya01&year=Career&t=b',
 'Yangervis_Solarte': 'http://www.baseball-reference.com/players/split.cgi?id=solarya01&year=Career&t=b',
 'Yasmani_Grandal': 'http://www.baseball-reference.com/players/split.cgi?id=grandya01&year=Career&t=b',
 'Yasmany_Tomas': 'http://www.baseball-reference.com/players/split.cgi?id=tomasya01&year=Career&t=b',
 'Yoenis_Cespedes': 'http://www.baseball-reference.com/players/split.cgi?id=cespeyo01&year=Career&t=b',
 'Yonder_Alonso': 'http://www.baseball-reference.com/players/split.cgi?id=alonsyo01&year=Career&t=b',
 'Yunel_Escobar': 'http://www.baseball-reference.com/players/split.cgi?id=escobyu01&year=Career&t=b',
 'Zack_Cozart': 'http://www.baseball-reference.com/players/split.cgi?id=cozarza01&year=Career&t=b'
 }









