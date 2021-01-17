#  ---Imports-----------------------------------------------------------------------------------------------------------
from tkinter import *
import json
import pandas as pd

#  ---Reading JSON------------------------------------------------------------------------------------------------------
with open('steam.json', 'r') as steamfile:
    data = json.load(steamfile)

#  ---Pandas Dataframe--------------------------------------------------------------------------------------------------
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 5)
df = pd.DataFrame(data)

#  ---Dataframe lists_--------------------------------------------------------------------------------------------------
list_name = df.iloc[0:50, 1].values
list_genres = df.iloc[0:30000, 9].values
list_price = df.iloc[0:30000, 17].values


#  ---Stats-Functions---------------------------------------------------------------------------------------------------
def mean(lst):
    """ Print het gemiddelde (float) van de lijst lst. """
    avg = sum(lst) / len(lst)  # gemiddelde
    print(float(avg))

def mode(lst):
    """ Print een gesorteerde lijst (list) van de modi van lijst lst. """
    freqs = {}
    for x in lst:
        if x in freqs:
            freqs[x] += 1
        else:
            freqs[x] = 1
    highfreq = max(freqs.values())
    modi = []
    for x, y in freqs.items():
        if y == highfreq:
            modi.append(x)
    print(sorted(modi))

def rnge(lst):
    """ Print het bereik (int) van de lijst lst. """
    index = len(lst) - 1
    lst2 = sorted(lst)
    hoog = lst2[index]
    laag = lst2[0]
    print(hoog - laag)

#  ---Run---------------------------------------------------------------------------------------------------------------
mean(list_price)        # Gemiddelde prijs van alle spellen op steam
mode(list_genres)       # Meest voorkomende genre op steam
rnge(list_price)        # Het bereik van de prijs, het verschil tussen het duurste en goedkoopste spel
