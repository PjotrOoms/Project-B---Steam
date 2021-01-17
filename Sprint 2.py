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

#  ---Dataframe lists---------------------------------------------------------------------------------------------------
list_name = df.iloc[0:10, 1].values
list_genres = df.iloc[0:30000, 9].values
list_price = df.iloc[0:30000, 17].values


#  ---Stats-Functions---------------------------------------------------------------------------------------------------
def mean(lst):
    """ Return het gemiddelde (float) van de lijst lst. """
    avg = sum(lst) / len(lst)
    return float(avg)

def mode(lst):
    """ Return een gesorteerde lijst (list) van de modi van lijst lst. """
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
    return sorted(modi)

def rnge(lst):
    """ Return het bereik (int) van de lijst lst. """
    index = len(lst) - 1
    lst2 = sorted(lst)
    hoog = lst2[index]
    laag = lst2[0]
    return hoog - laag

#  ---Run---------------------------------------------------------------------------------------------------------------
mean(list_price)        # Gemiddelde prijs van alle spellen op steam
mode(list_genres)       # Meest voorkomende genre op steam
rnge(list_price)        # Het bereik van de prijs, het verschil tussen het duurste en goedkoopste spel

#  ---Tkinter-Functions-------------------------------------------------------------------------------------------------
def toon_naam():
    text_box.delete("1.0", "end")
    for x in list_name:
        text_box.insert("end-1c", f'{x}\n',)

def toon_gem():
    text_box.delete("1.0", "end")
    text_box.insert("end-1c", f'{mean(list_price)}\n', )

def toon_modus():
    text_box.delete("1.0", "end")
    for x in mode(list_genres):
        text_box.insert("end-1c", f'{x}\n', )

def afsluiten():
    text_box.delete("1.0", "end")
    root_steam.destroy()

#  ---Tkinter-GUI-------------------------------------------------------------------------------------------------------
root_steam = Tk()
root_steam.geometry("600x400")
root_steam.title("STEAM Dashboard")

#  Label spel
name_label = Label(root_steam, text="Naam spel:")
name_label.place(x=30, y=20)

#  Label uitleg
name_label = Label(root_steam, text='Toon de eerste 10 spellen, gesorteerd op:')
name_label.place(x=20, y=270)

#  Textvak spel
text_box = Text(root_steam, width=60, height=12)
text_box.place(x=100, y=20)

#  Toon naam button
ber_btn = Button(root_steam, text="Naam", command=toon_naam)
ber_btn.place(x=20, y=300, width=60)

#  Toon gemiddelde prijs button
ber_btn = Button(root_steam, text="Gemiddelde prijs", command=toon_gem)
ber_btn.place(x=110, y=300, width=100)

#  Toon modus genres button
ber_btn = Button(root_steam, text="Modus genres", command=toon_modus)
ber_btn.place(x=250, y=300, width=100)

#  Afsluiten button
afs_btn = Button(root_steam, text="Afsluiten", command=afsluiten)
afs_btn.place(x=450, y=300, width=130)

root_steam.mainloop()
