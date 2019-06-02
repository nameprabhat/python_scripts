# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 09:14:44 2018

@author: sunny
"""

animals = { 'a': ['aardvark','aardvark','aardvark','aardvark','aardvark','aardvark'], 'b': ['baboon','aardvark','aardvark','aardvark','aardvark','aardvark','aardvark'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count =0
    for key in aDict.keys():
        count= count+ len(aDict[key])
    return count


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result =None
    count = 0
    for key in aDict.keys():
        if len(aDict[key]) > count:
            count = len(aDict[key])
            result = key
    return result

print('key which has largest value is ',biggest(animals))

print('total number of values in keys are ',how_many(animals))



