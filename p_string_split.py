# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 23:28:00 2024

@author: Nishant
"""

"""
You're working on collecting the text data for a Natural Language Processing(NLP)
 project. You come up with the idea of storing the unique words (case-sensitive)
 with their frequency in a Pandas Series object.

You are given the raw data in form of a string, Write a function which can take a 
string as an input and return the unique words and the corresponding frequency
 in form of a Pandas Series object.

The indices of the series should be the unique words and the values 
should be the frequency of those unique words.

Note that:

String contains no special character.
Always a Non-empty string.
Case sensitive i.e. He and he should be treated as two different word tokens.
Series returned is expected to be sorted by sort_index()for sorting all the words.
(Input Format)
Number of testcases
String with space separated words. (basically a sentence)
(Output Format)
space separated words in first line.
space separated values in the second line.
Sample Input
1
How much wood would a woodchuck chuck if a woodchuck could chuck wood
"""

import pandas as pd

def solve(string):
        freq=string.split('')
        df=pd.DataFrame(data=freq,columns=["words"])
        res=df["words"].value_counts()
        res=res.sort_index()
        return res
    















