__author__ = 730574526


import pytest


def invert(dict1 = dict[str, str]) -> dict[str, str]:
    dict2 = []
    for key in dict1:
        dict2[dict1[key]] = key
    return dict2


def favorite_color(dict1 = dict[str, str]) -> str:
    return max(set(list(dict1.values())), key = list(dict1.values()).count)

def count(list = list[str]) -> dict[str, int]:
    dict = []
    for thing in list:
        if thing in dict:
            new_val = dict[thing] + 1
            dict[thing] = new_val
        else:
            dict[thing] = 1
    return dict