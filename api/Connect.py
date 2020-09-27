from abc import ABC
from github import Github
from configparser import ConfigParser


def get_config(section, keyword):
    config = ConfigParser()
    config.read('config.ini')
    token = config.get(section, keyword)
    return token


class Connect(ABC):
    token = get_config('Auth', 'github_token')
    
    conn = None
    try:
        conn = Github(token)
    except Exception as ex:
        pass
