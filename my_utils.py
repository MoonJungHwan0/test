
def connet_mysql(db):
    conn = pymysql.connect(host='localhost', user='root', password='1234', db=db,
                           charset='utf8')
    return conn

def mysql_execute(query, conn):
    cursor_mysql = conn.cursor()
    cursor_mysql.execute(query)
    result = cursor_mysql.fetchall()
    return result

def mysql_execute_dict(query, conn):
    cursor_mysql = conn.cursor(cursor = pymysql.cursors.DictCursor)
    cursor_mysql.execute(query)
    result = cursor_mysql.fetchall()
    return result

def df_creater(url):
    url = url.replace('(인증키)',seoul_api_key).replace('xml','json').replace('/5/','/1000/')
    res = requests.get(url).json()
    key = list(res.keys())[0]
    data = res[key]['row']
    df = pd.DataFrame(data)
    return df

def my_get_puuid(user):
    my_url =f'https://kr.api.riotgames.com/lol/summoner/v4/summoners/by-name/{user}?api_key={riot_api_key}'
    my_res = requests.get(my_url).json()
    my_puuid = my_res['puuid']
    return my_puuid

def my_get_matchId(puuid,num):
    my_url2=f'https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?type=ranked&start=0&count={num}&api_key={riot_api_key}'
    my_res_matchId = requests.get(my_url2).json()
    return my_res_matchId

def my_get_match(match_one):
    my_url3 = f'https://asia.api.riotgames.com/lol/match/v5/matches/{match_one}?api_key={riot_api_key}'
    my_res_match = requests.get(my_url3).json()
    return my_res_match

def my_get_match_timeline(match_one):
    my_url4 = f'https://asia.api.riotgames.com/lol/match/v5/matches/{match_one}/timeline?api_key={riot_api_key}'
    my_res_match_timeline = requests.get(my_url4).json()
    return my_res_match_timeline

print('git test')
print('git2 test')