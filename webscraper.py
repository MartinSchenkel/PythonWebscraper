from selenium import webdriver

class RocketLeagueStats:
    wins = 0 # Number of wins
    goalShotRatio = 0.0 # How many shots did score ratio
    goals = 0 # Number of goals
    shots = 0 # Number of shots
    assists = 0 # Number of Assists
    saves = 0 # Number of saves
    mvps = 0 # Number of MVPS
    
    rank1s = '' # Name of the Rank and Div
    mmr1s = 0 # Rating
    rank2s = ''  # Name of the Rank and Div
    mmr2s = 0 # Rating
    rank3s = '' # Name of the Rank and Div
    mmr3s = 0 # Rating

class ValorantStats:
    adr = 0.0 # Damage per round
    kr = 0.0 # Kills per round
    kd = 0.0 # Kill Death Ratio
    hsper = 0 # Headshot Percentage
    winper = 0.0 # Win Percentage
    wins = 0 # Number of wins
    kills = 0 # Number of Kills
    deaths = 0 # Number of deaths
    assists = 0 # Number of assists
    headshots = 0 # Number of Headshots
    aces = 0 # Number of Aces
    topAgent = '' # Name of most played agent
    topWeapon = '' # Name of weapon you scored the most kills with
    rating = '' # Name of the rank

class CSGOStats:
    wins = 0 # Number of wins
    kd = 0.0 # Kill Death Ratio
    kills = 0 # Number of kills
    winper = 0.0 # Win Percentage
    mvp = 0 # Number of MVPs
    shotacc = 0.0 # Shot Accuracy
    moneyearned = 0 # Total Money Earned
    topWeapon = '' # Name of most used weapon

class LeagueOfLegendsStats:
    soloqrank = '' # Solo/Duo Rank
    flexqrank = '' # Flex Queue Rank

class User:
    userName = ''
    rocketLeagueURL = ''
    valorantURL = ''
    csgoURL = ''
    csgoWeaponURL = ''
    leagueOfLegendsURL = ''

    rlStats = None
    valStats = None
    csgoStats = None
    lolStats = None
    def __init__(self):
        self.rlStats = RocketLeagueStats()
        self.valStats = ValorantStats()
        self.csgoStats = CSGOStats()
        self.lolStats = LeagueOfLegendsStats()

jonas = User()
jonas.userName = 'Botsling'
jonas.csgoURL = 'https://tracker.gg/csgo/profile/steam/76561198195955675/overview'
jonas.csgoWeaponURL = 'https://tracker.gg/csgo/profile/steam/76561198195955675/weapons'

timo = User()
timo.userName = 'Breyy'
timo.rocketLeagueURL = 'https://rocketleague.tracker.network/rocket-league/profile/steam/76561198253573914/overview'
timo.csgoURL = 'https://tracker.gg/csgo/profile/steam/76561198253573914/overview'
timo.csgoWeaponURL = 'https://tracker.gg/csgo/profile/steam/76561198253573914/weapons'
timo.leagueOfLegendsURL = "https://euw.op.gg/summoner/userName=breyy"

martin = User()
martin.userName = 'Maddisch'
martin.rocketLeagueURL = 'https://rocketleague.tracker.network/rocket-league/profile/steam/76561198108703096/overview'
martin.valorantURL = 'https://tracker.gg/valorant/profile/riot/Maddisch%231337/overview?playlist=competitive'
martin.csgoURL = 'https://tracker.gg/csgo/profile/steam/76561198108703096/overview'
martin.csgoWeaponURL = 'https://tracker.gg/csgo/profile/steam/76561198108703096/weapons'
martin.leagueOfLegendsURL = 'https://euw.op.gg/summoner/userName=KiddingYouAgain'

matti = User()
matti.userName = 'Maku'
matti.rocketLeagueURL = 'https://rocketleague.tracker.network/rocket-league/profile/steam/76561198353651815/overview'
# TODO MATTIS CSGO DATEN 

aaron = User()
aaron.userName = 'Mistersauber'
# TODO AARONS CSGO DATEN

patrick = User()
patrick.userName = 'Pattifix'
patrick.rocketLeagueURL = 'https://rocketleague.tracker.network/rocket-league/profile/steam/76561198143048248/overview'
patrick.csgoURL = "https://tracker.gg/csgo/profile/steam/76561198143048248/overview"
patrick.csgoWeaponURL = "https://tracker.gg/csgo/profile/steam/76561198143048248/weapons"
patrick.leagueOfLegendsURL = "https://euw.op.gg/summoner/userName=pattifix"

christoph = User()
christoph.userName = 'Rainingstorm'
christoph.rocketLeagueURL = 'https://rocketleague.tracker.network/rocket-league/profile/steam/76561198277203357/overview'
# TODO SICKINGS CSGO DATEN
christoph.leagueOfLegendsURL = "https://euw.op.gg/summoner/userName=o0rainingstorm0o"

malte = User()
malte.userName = 'Stachosson'
malte.valorantURL = "https://tracker.gg/valorant/profile/riot/StachoKuhlmann%234447/overview"
malte.csgoURL = 'https://tracker.gg/csgo/profile/steam/76561198143960916/overview'
malte.csgoWeaponURL = 'https://tracker.gg/csgo/profile/steam/76561198143960916/weapons'
malte.leagueOfLegendsURL = "https://euw.op.gg/summoner/userName=stachokuhlmann"

janko = User()
janko.userName = 'Stathogon'
janko.valorantURL = "https://tracker.gg/valorant/profile/riot/Stathogon%23EUW/overview"
janko.csgoURL = 'https://tracker.gg/csgo/profile/steam/76561198092006241/overview'
janko.csgoWeaponURL = 'https://tracker.gg/csgo/profile/steam/76561198092006241/weapons'
janko.leagueOfLegendsURL = "https://euw.op.gg/summoner/userName=stathogon"


users = [jonas, timo, martin, matti, aaron, patrick, christoph, malte, janko]

def getRocketLeagueStats():

    for u in users:
        if u.rocketLeagueURL != '':
            browser.get(u.rocketLeagueURL)
            u.rlStats.wins = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/aside/div[2]/div/div[1]/div/div[2]/span[2]').text
            u.rlStats.goalShotRatio = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/aside/div[2]/div/div[2]/div/div[2]/span[2]').text
            u.rlStats.goals = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/aside/div[2]/div/div[3]/div/div[2]/span[2]').text
            u.rlStats.shots = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/aside/div[2]/div/div[4]/div/div[2]/span[2]').text
            u.rlStats.assists = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/aside/div[2]/div/div[5]/div/div[2]/span[2]').text
            u.rlStats.saves = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/aside/div[2]/div/div[6]/div/div[2]/span[2]').text
            u.rlStats.mvps = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/aside/div[2]/div/div[7]/div/div[2]/span[2]').text
            u.rlStats.rank1s = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/div[2]').text
            u.rlStats.mmr1s = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[2]/td[3]/div/div[2]/div[1]/div').text
            u.rlStats.rank2s = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[3]/td[2]/div[2]').text
            u.rlStats.mmr2s = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[3]/td[3]/div/div[2]/div[1]/div').text
            u.rlStats.rank3s = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[4]/td[2]/div[2]').text
            u.rlStats.mmr3s = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div/div/div[1]/div[2]/table/tbody/tr[4]/td[3]/div/div[2]/div[1]/div').text
            
            u.rlStats.wins  = int(''.join([i for i in str(u.rlStats.wins) if not i == "," and not i == "%"]))
            u.rlStats.goalShotRatio  = float(''.join([i for i in str(u.rlStats.goalShotRatio) if not i == "," and not i == "%"]))
            u.rlStats.goals  = int(''.join([i for i in str(u.rlStats.goals) if not i == "," and not i == "%"]))
            u.rlStats.shots  = int(''.join([i for i in str(u.rlStats.shots) if not i == "," and not i == "%"]))
            u.rlStats.assists  = int(''.join([i for i in str(u.rlStats.assists) if not i == "," and not i == "%"]))
            u.rlStats.saves  = int(''.join([i for i in str(u.rlStats.saves) if not i == "," and not i == "%"]))
            u.rlStats.mvps  = int(''.join([i for i in str(u.rlStats.mvps) if not i == "," and not i == "%"]))
            u.rlStats.mmr1s  = int(''.join([i for i in str(u.rlStats.mmr1s) if not i == "," and not i == "%"]))
            u.rlStats.mmr2s  = int(''.join([i for i in str(u.rlStats.mmr2s) if not i == "," and not i == "%"]))
            u.rlStats.mmr3s  = int(''.join([i for i in str(u.rlStats.mmr3s) if not i == "," and not i == "%"]))


            print("----------UserStats------------")
            print(u.userName)
            print(u.rlStats.wins)
            print(u.rlStats.goalShotRatio)
            print(u.rlStats.goals)
            print(u.rlStats.shots)
            print(u.rlStats.assists)
            print(u.rlStats.saves)
            print(u.rlStats.mvps)
            print(u.rlStats.rank1s)
            print(u.rlStats.mmr1s)
            print(u.rlStats.rank2s)
            print(u.rlStats.mmr2s)
            print(u.rlStats.rank3s)
            print(u.rlStats.mmr3s)


def getValorantStats():
    for u in users:
        if u.valorantURL != '':
            browser.get(u.valorantURL)
            u.valStats.adr = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[4]/div[3]/div[1]/div/div[1]/span[2]').text
            u.valStats.kd = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[4]/div[3]/div[2]/div/div[1]/span[2]').text
            u.valStats.hsper = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[4]/div[3]/div[3]/div/div[1]/span[2]').text
            u.valStats.winper = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[4]/div[3]/div[4]/div/div[1]/span[2]').text
            u.valStats.wins = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[4]/div[5]/div[1]/div/div[1]/span[2]').text
            u.valStats.kills = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[4]/div[5]/div[2]/div/div[1]/span[2]').text
            u.valStats.deaths = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[4]/div[5]/div[4]/div/div[1]/span[2]').text
            u.valStats.assists = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[4]/div[5]/div[5]/div/div[1]/span[2]').text
            u.valStats.headshots = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[4]/div[5]/div[3]/div/div[1]/span[2]').text
            u.valStats.aces = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[4]/div[5]/div[9]/div/div[1]/span[2]').text
            u.valStats.topAgent = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[5]/div/div/table/tbody/tr[1]/td[1]/div/span').text
            u.valStats.topWeapon = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[2]/div/div/div[1]/div[1]/div[1]').text
            u.valStats.rating = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[3]/div[4]/div[2]/div[2]/div/div[1]/div[1]/span[2]').text

            u.valStats.adr  = float(''.join([i for i in str(u.valStats.adr) if not i == "," and not i == "%"]))
            u.valStats.kr  = float(''.join([i for i in str(u.valStats.kr) if not i == "," and not i == "%"]))
            u.valStats.kd  = float(''.join([i for i in str(u.valStats.kd) if not i == "," and not i == "%"]))
            u.valStats.hsper  = float(''.join([i for i in str(u.valStats.hsper) if not i == "," and not i == "%"]))
            u.valStats.winper  = float(''.join([i for i in str(u.valStats.winper) if not i == "," and not i == "%"]))
            u.valStats.wins  = int(''.join([i for i in str(u.valStats.wins) if not i == "," and not i == "%"]))
            u.valStats.kills  = int(''.join([i for i in str(u.valStats.kills) if not i == "," and not i == "%"]))
            u.valStats.deaths  = int(''.join([i for i in str(u.valStats.deaths) if not i == "," and not i == "%"]))
            u.valStats.assists  = int(''.join([i for i in str(u.valStats.assists) if not i == "," and not i == "%"]))
            u.valStats.headshots  = int(''.join([i for i in str(u.valStats.headshots) if not i == "," and not i == "%"]))
            u.valStats.aces  = int(''.join([i for i in str(u.valStats.aces) if not i == "," and not i == "%"]))

            print("----------UserStats------------")
            print(u.userName)
            print(u.valStats.adr)
            print(u.valStats.kd)
            print(u.valStats.hsper)
            print(u.valStats.winper)
            print(u.valStats.wins)
            print(u.valStats.kills)
            print(u.valStats.deaths)
            print(u.valStats.assists)
            print(u.valStats.headshots)
            print(u.valStats.aces)
            print(u.valStats.topAgent)
            print(u.valStats.topWeapon)
            print(u.valStats.rating)

def getCSGOStats():
    for u in users:
        if u.csgoURL != '' and u.csgoWeaponURL != '':
            browser.get(u.csgoURL)
            
            u.csgoStats.wins = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div/div/div[1]/div[5]/div[3]/div/div[2]/span[2]').text
            u.csgoStats.kd = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div/div/div[1]/div[3]/div[1]/div/div[2]/span[2]').text
            u.csgoStats.kills = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div/div/div[1]/div[3]/div[2]/div/div[2]/span[2]').text
            u.csgoStats.winper = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div/div/div[1]/div[3]/div[3]/div/div[2]/span[2]').text
            u.csgoStats.mvp = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div/div/div[1]/div[3]/div[4]/div/div[2]/span[2]').text
            u.csgoStats.shotacc = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div/div/div[1]/div[5]/div[8]/div/div[2]/span[2]').text
            u.csgoStats.moneyearned = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div/div/div[1]/div[5]/div[6]/div/div[2]/span[2]').text

            browser.get(u.csgoWeaponURL)
            
            u.csgoStats.topWeapon = browser.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div/main/div[2]/div[3]/div[1]/div/div/div/div[1]/div/div/div[1]/h3').text

            u.csgoStats.wins  = int(''.join([i for i in str(u.csgoStats.wins) if not i == "," and not i == "%"]))
            u.csgoStats.kd  = float(''.join([i for i in str(u.csgoStats.kd) if not i == "," and not i == "%"]))
            u.csgoStats.kills  = int(''.join([i for i in str(u.csgoStats.kills) if not i == "," and not i == "%"]))
            u.csgoStats.winper  = float(''.join([i for i in str(u.csgoStats.winper) if not i == "," and not i == "%"]))
            u.csgoStats.mvp  = int(''.join([i for i in str(u.csgoStats.mvp) if not i == "," and not i == "%"]))
            u.csgoStats.shotacc  = float(''.join([i for i in str(u.csgoStats.shotacc) if not i == "," and not i == "%"]))
            u.csgoStats.moneyearned  = int(''.join([i for i in str(u.csgoStats.moneyearned) if not i == "," and not i == "%"]))


            print("----------UserStats------------")
            print(u.userName)
            print(u.csgoStats.wins)
            print(u.csgoStats.kd)
            print(u.csgoStats.kills)
            print(u.csgoStats.winper)
            print(u.csgoStats.mvp)
            print(u.csgoStats.shotacc)
            print(u.csgoStats.moneyearned)
            print(u.csgoStats.topWeapon)

def getLeagueOfLegendsStats():
    for u in users:
        if u.leagueOfLegendsURL != '':
            browser.get(u.leagueOfLegendsURL)

            u.lolStats.soloqrank = browser.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[1]/div/div[2]/div[2]').text
            u.lolStats.flexqrank = browser.find_element_by_xpath('//*[@id="SummonerLayoutContent"]/div[2]/div[1]/div[2]/div/div[2]').text

            print("----------UserStats------------")
            print(u.userName)
            print(u.lolStats.soloqrank)
            print(u.lolStats.flexqrank)

def writeToJson():
    filePathNameWExt = "./Data.json"

    f = open(filePathNameWExt, "w")
    f.write('[\n')
    for u in users:
        f.write('\t{\n')
        f.write('\t\t"username": "' + u.userName + '",\n')

        f.write('\t\t"rocketleaguestats":\n')
        f.write('\t\t{\n')
        f.write('\t\t\t"wins": ' + str(u.rlStats.wins) + ',\n')
        f.write('\t\t\t"goalshotratio": ' + str(u.rlStats.goalShotRatio) + ',\n')
        f.write('\t\t\t"goals": ' + str(u.rlStats.goals) + ',\n')
        f.write('\t\t\t"shots": ' + str(u.rlStats.shots) + ',\n')
        f.write('\t\t\t"assists": ' + str(u.rlStats.assists) + ',\n')
        f.write('\t\t\t"saves": ' + str(u.rlStats.saves) + ',\n')
        f.write('\t\t\t"mvps": ' + str(u.rlStats.mvps) + ',\n')
        f.write('\t\t\t"rank1s": "' + u.rlStats.rank1s + '",\n')
        f.write('\t\t\t"mmr1s": ' + str(u.rlStats.mmr1s) + ',\n')
        f.write('\t\t\t"rank2s": "' + u.rlStats.rank2s + '",\n')
        f.write('\t\t\t"mmr2s": ' + str(u.rlStats.mmr2s) + ',\n')
        f.write('\t\t\t"rank3s": "' + u.rlStats.rank3s + '",\n')
        f.write('\t\t\t"mmr3s": ' + str(u.rlStats.mmr3s) + '\n')
        f.write('\t\t},\n')

        f.write('\t\t"valorantstats":\n')
        f.write('\t\t{\n')
        f.write('\t\t\t"adr": ' + str(u.valStats.adr) + ',\n')
        f.write('\t\t\t"kr": ' + str(u.valStats.kr) + ',\n')
        f.write('\t\t\t"kd": ' + str(u.valStats.kd) + ',\n')
        f.write('\t\t\t"hsper": ' + str(u.valStats.hsper) + ',\n')
        f.write('\t\t\t"winper": ' + str(u.valStats.winper) + ',\n')
        f.write('\t\t\t"wins": ' + str(u.valStats.wins) + ',\n')
        f.write('\t\t\t"kills": ' + str(u.valStats.kills) + ',\n')
        f.write('\t\t\t"deaths": ' + str(u.valStats.deaths) + ',\n')
        f.write('\t\t\t"assists": ' + str(u.valStats.assists) + ',\n')
        f.write('\t\t\t"headshots": ' + str(u.valStats.headshots) + ',\n')
        f.write('\t\t\t"aces": ' + str(u.valStats.aces) + ',\n')
        f.write('\t\t\t"topagent": "' + u.valStats.topAgent + '",\n')
        f.write('\t\t\t"topweapon": "' + u.valStats.topWeapon + '",\n')
        f.write('\t\t\t"rating": "' + u.valStats.rating + '"\n')
        f.write('\t\t},\n')

        f.write('\t\t"csgostats":\n')
        f.write('\t\t{\n')
        f.write('\t\t\t"wins": ' + str(u.csgoStats.wins) + ',\n')
        f.write('\t\t\t"kd": ' + str(u.csgoStats.kd) + ',\n')
        f.write('\t\t\t"kills": ' + str(u.csgoStats.kills) + ',\n')
        f.write('\t\t\t"winper": ' + str(u.csgoStats.winper) + ',\n')
        f.write('\t\t\t"mvps": ' + str(u.csgoStats.mvp) + ',\n')
        f.write('\t\t\t"shotaccuracy": ' + str(u.csgoStats.shotacc) + ',\n')
        f.write('\t\t\t"moneyearned": ' + str(u.csgoStats.moneyearned) + ',\n')
        f.write('\t\t\t"topWeapon": "' + u.csgoStats.topWeapon + '"\n')
        f.write('\t\t},\n')

        f.write('\t\t"leagueoflegendsstats":\n')
        f.write('\t\t{\n')
        f.write('\t\t\t"soloqrank": "' + u.lolStats.soloqrank + '",\n')
        f.write('\t\t\t"flexqrank": "' + u.lolStats.flexqrank + '"\n')
        f.write('\t\t}\n')

        if u.userName == "Stathogon":
            f.write('\t}\n')
        else:
            f.write('\t},\n')

    
    f.write(']\n')
    f.close()

browser = webdriver.Chrome()

getRocketLeagueStats()
getValorantStats()
getCSGOStats()
getLeagueOfLegendsStats()

writeToJson()

browser.quit()