from pandas import DataFrame as df
import requests
import json
from typing import List

from BotIntercom.settings import port,qotd_post,punisher_post

def send_qotd_request(position_list : df,question_user_id : int, g_id : int, g_name : str,total_react_list : List[int]):
    if 'player_d_id' not in position_list or 'player_position' not in position_list:
        raise ValueError("player_d_id and player_position need to exist in Dataframe.")
    send_dict = {'result' : []}
    for p in position_list.iterrows():
        p = p[1]
        send_dict['result'].append([int(p.player_d_id),int(p.player_position)])
    send_dict['guild_id'] = g_id
    send_dict['guild_name'] = g_name
    send_dict['post_source'] = qotd_post
    send_dict['question_player_id'] = question_user_id
    send_dict['react_list'] = total_react_list
    r = requests.post(f'http://localhost:{port}',data=json.dumps(send_dict))

def send_punisher_request(player_id : int, punisher_points : int , g_id : int, g_name : str,undo=False):
    send_dict = {}
    send_dict['player_id'] = player_id
    send_dict['punisher_points'] = punisher_points
    send_dict['guild_id'] = g_id
    send_dict['guild_name'] = g_name
    send_dict['post_source'] = punisher_post
    send_dict['undo'] = undo
    r = requests.post(f'http://localhost:{port}',data=json.dumps(send_dict))