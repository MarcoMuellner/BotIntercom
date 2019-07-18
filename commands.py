from pandas import DataFrame as df
import requests
import json

from BotIntercom.settings import port,qotd_post,punisher_post

def send_qotd_request(position_list : df, g_id : int, g_name : str):
    if 'player_d_id' not in df or 'player_position' not in df:
        raise ValueError("player_d_id and player_position need to exist in Dataframe.")
    send_dict = {'result' : []}
    for p in position_list.iterrows():
        p = p[1]
        send_dict['result'].append([p.player_d_id,p.player_position])
    send_dict['guild_id'] = g_id
    send_dict['guild_name'] = g_name
    send_dict['post_source'] = qotd_post
    try:
        r = requests.post(f'localhost:{port}',data=json.dumps(send_dict))
    except:
        pass

def send_punisher_request(player_id : int, punisher_points : int , g_id : int, g_name : str):
    send_dict = {}
    send_dict['player_id'] = player_id
    send_dict['punisher_points'] = punisher_points
    send_dict['guild_id'] = g_id
    send_dict['guild_name'] = g_name
    send_dict['post_source'] = punisher_post
    try:
        r = requests.post(f'localhost:{port}',data=json.dumps(send_dict))
    except:
        pass