from . import user_agents
import random


def get_ua():
    """
    随机提取一个UA
    """
    return random.choice(user_agents)
