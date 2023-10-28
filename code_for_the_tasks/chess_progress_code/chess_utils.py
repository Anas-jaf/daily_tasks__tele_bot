import requests
from secret_variables import owner ,mystudent


def get_user_stats(username=owner):
    headers = {
        'User-Agent': 'python3.11',
    }
    url = f'https://www.chess.com/callback/member/stats/{username}'

    response = requests.get(url, headers=headers)
    
    return response


def get_user_games_puzzles_count(username=mystudent):
    response = get_user_stats(username)
    
    tactics = [i['gameCount'] for i in response.json()['stats'] if i['key'] == 'tactics'][0]
    rapid = [i['gameCount'] for i in response.json()['stats'] if i['key'] == 'rapid'][0]

    return f'{tactics} puzzle , {rapid} game'


print(get_user_games_puzzles_count())