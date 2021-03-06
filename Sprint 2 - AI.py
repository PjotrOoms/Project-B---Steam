#  ---Imports-----------------------------------------------------------------------------------------------------------
from tkinter import *
import json
import pandas as pd
import requests

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
list_name2 = df.iloc[0:30000, 1].values

#  ---Lists-------------------------------------------------------------------------------------------------------------
list_games = []
list_games.extend(list_name2)
list_games2 = []
list_games2.extend(list_name2)
list_prices2 = []
list_prices2.extend(list_price)
#  ---Counter-----------------------------------------------------------------------------------------------------------
index1 = 0
index2 = 10

#  ---Sort-Functions----------------------------------------------------------------------------------------------------
def merge_sort(lst, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index) // 2
    merge_sort(lst, left_index, middle)
    merge_sort(lst, middle + 1, right_index)
    merge(lst, left_index, right_index, middle)

def merge(lst, left_index, right_index, middle):
    left_sublist = lst[left_index:middle + 1]
    right_sublist = lst[middle + 1:right_index + 1]
    left_sublist_index = 0
    right_sublist_index = 0
    sorted_index = left_index

    while left_sublist_index < len(left_sublist) and right_sublist_index < len(right_sublist):
        if left_sublist[left_sublist_index] <= right_sublist[right_sublist_index]:
            lst[sorted_index] = left_sublist[left_sublist_index]
            left_sublist_index = left_sublist_index + 1
        else:
            lst[sorted_index] = right_sublist[right_sublist_index]
            right_sublist_index = right_sublist_index + 1
        sorted_index = sorted_index + 1

    while left_sublist_index < len(left_sublist):
        lst[sorted_index] = left_sublist[left_sublist_index]
        left_sublist_index = left_sublist_index + 1
        sorted_index = sorted_index + 1

    while right_sublist_index < len(right_sublist):
        lst[sorted_index] = right_sublist[right_sublist_index]
        right_sublist_index = right_sublist_index + 1
        sorted_index = sorted_index + 1

# ---Search-Functions----------------------------------------------------------------------------------------------------
def binary_search_recursive(lst, target):
    """ Returns of het element in de lijst voorkomt (true or false) """
    midden = len(lst) // 2
    if target == lst[midden]:
        return True
    elif len(lst) == 1 and target != lst[0]:
        return False
    elif target < lst[midden]:
        new_lst = lst[:midden]
        return binary_search_recursive(new_lst, target)
    elif target > lst[midden]:
        new_lst = lst[midden:]
        return binary_search_recursive(new_lst, target)

#  ---Stats-Functions---------------------------------------------------------------------------------------------------
def mean(lst):
    """ Returns het gemiddelde (float) van de lijst lst. """
    avg = sum(lst) / len(lst)
    return round(avg, 2)

def mode(lst):
    """ Returns een gesorteerde lijst (list) van de modi van lijst lst. """
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
    return modi

def rnge(lst):
    """ Returns het bereik (int) van de lijst lst. """
    index = len(lst) - 1
    merge_sort(lst, 0, len(lst) - 1)
    hoog = lst[index]
    laag = lst[0]
    return hoog - laag

#  ---Tkinter-Functions-------------------------------------------------------------------------------------------------
def sort_games(a, b):
    text_box1.delete("1.0", "end")
    merge_sort(list_games, 0, len(list_games) - 1)
    for x in list_games[a:b]:
        text_box1.insert("end-1c", f'{x}\n')

def search_games():
    search = text_box_search.get("1.0", 'end-1c')
    search2 = str(search)
    text_box_search.delete("1.0", "end")
    merge_sort(list_games2, 0, len(list_games2) - 1)
    a = binary_search_recursive(list_games2, f'{search2}')
    if a:
        text_box_search.insert("end-1c", f'Dit spel is beschikbaar\nop Steam!\n')
    else:
        text_box_search.insert("end-1c", f'Dit spel is helaas niet\nbeschikbaar op Steam...\n')

def pref_page():
    global index1, index2
    index1 -= 10
    index2 -= 10
    sort_games(index1, index2)

def next_page():
    global index1, index2
    index1 += 10
    index2 += 10
    sort_games(index1, index2)

def toon_gem():
    text_box2.delete("1.0", "end")
    text_box2.insert("end-1c", f'Gemiddelde prijs van een game is\n{mean(list_prices2)}\n')

def toon_modus():
    text_box2.delete("1.0", "end")
    for x in mode(list_genres):
        text_box2.insert("end-1c", f'Het meest voorkomende genre op steam is\n{x}\n')

def toon_rnge():
    text_box2.delete("1.0", "end")
    text_box2.insert("end-1c", f'Het goedkoopste spel is gratis en\nhet duurste spel is\n{rnge(list_prices2)}\n')

def toon_vr():
    for friend in selectedfriends:
        friendname = steamname(friend)
        status = personastate(friend)
        if status == 1:
            text_box3.insert("end-1c", f'{friendname} is online\n')
        else:
            text_box3.insert("end-1c", f'{friendname} is offline\n')

def afsluiten1():
    root_2.destroy()

def afsluiten2():
    root_3.destroy()

def afsluiten3():
    root_4.destroy()

def games():
    global text_box1, root_2, text_box_search
    root_2 = Toplevel(root_dashboard)
    root_2.geometry("600x400")
    root_2.title("STEAM Games")

    #  Label spel
    available_label = Label(root_2, text="Games:")
    available_label.place(x=20, y=10)

    #  Label uitleg
    name_label = Label(root_2, text='Toon de eerste 10 spellen,\ngesorteerd op naam:')
    name_label.place(x=20, y=220)

    #  Label zoeken
    search_label = Label(root_2, text='Vul hieronder het spel\nin wat u wilt zoeken')
    search_label.place(x=300, y=220)

    #  Tekstvak spel
    text_box1 = Text(root_2, width=70, height=10)
    text_box1.place(x=20, y=40)
    text_box1.delete("1.0", "end")
    for x in list_name:
        text_box1.insert("end-1c", f'{x}\n')

    #  Tektstvak zoeken
    text_box_search = Text(root_2, width=30, height=4)
    text_box_search.place(x=300, y=270)
    text_box1.delete("1.0", "end")

    #  Toon games button
    name_btn = Button(root_2, text="Sorteer", command=lambda: sort_games(index1, index2))
    name_btn.place(x=20, y=270, width=60)

    #  Previous page button
    prev_btn = Button(root_2, text="Vorige pagina", command=pref_page)
    prev_btn.place(x=50, y=310, width=100)

    #  Next page button
    next_btn = Button(root_2, text="Volgende pagina", command=next_page)
    next_btn.place(x=160, y=310, width=100)

    #  Search button
    search_btn = Button(root_2, text="Zoeken", command=search_games)
    search_btn.place(x=500, y=230, width=60)

    #  Afsluiten button
    afs_btn = Button(root_2, text="Afsluiten", command=afsluiten1)
    afs_btn.place(x=490, y=360, width=100)


def stats():
    global text_box2, root_3
    root_3 = Toplevel(root_dashboard)
    root_3.geometry("400x300")
    root_3.title("STEAM Stats")

    #  Label stats
    stats_label = Label(root_3, text='Toon de')
    stats_label.place(x=20, y=140)

    #  Textvak stats
    text_box2 = Text(root_3, width=40, height=6)
    text_box2.place(x=20, y=20)

    #  Toon gemiddelde prijs button
    avg_btn = Button(root_3, text="Gemiddelde prijs", command=toon_gem)
    avg_btn.place(x=15, y=170, width=100)

    #  Toon modus genres button
    mod_btn = Button(root_3, text="Modus van alle genres", command=toon_modus)
    mod_btn.place(x=130, y=170, width=130)

    #  Toon modus genres button
    mod_btn = Button(root_3, text="Price range", command=toon_rnge)
    mod_btn.place(x=280, y=170, width=100)

    #  Afsluiten button
    afs_btn = Button(root_3, text="Afsluiten", command=afsluiten2)
    afs_btn.place(x=290, y=260, width=100)

def friends_gui():
    global text_box3, root_4
    root_4 = Toplevel(root_dashboard)
    root_4.geometry("600x400")
    root_4.title("STEAM Friends")
    #  Label vrienden
    friends_label = Label(root_4, text="Vrienden:")
    friends_label.place(x=20, y=20)

    #  Textvak vrienden
    text_box3 = Text(root_4, width=60, height=12)
    text_box3.place(x=100, y=20)

    #  Afsluiten button
    afs_btn = Button(root_4, text="Afsluiten", command=afsluiten3)
    afs_btn.place(x=450, y=300, width=130)
    toon_vr()

#  ---Steam-API-Functions------------------------------------------------------------------------------------------------
def personastate(steamid):
    url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=68A6A5CD1D0EE6576FCBE1486E405D46&steamids=' + str(steamid)
    response = requests.get(url)
    data = json.loads(response.text)
    status = data['response']['players'][0]['personastate']
    if status == 1:
        return 1
    if status != 1:
        return 0

def friends(steamid):
    url = 'http://api.steampowered.com/ISteamUser/GetFriendList/v0001/?key=68A6A5CD1D0EE6576FCBE1486E405D46&steamid=' + str(steamid) + "&relationship=friend"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['friendslist']['friends']

def steamname(steamid):
    url = 'http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=68A6A5CD1D0EE6576FCBE1486E405D46&steamids=' + str(steamid)
    response = requests.get(url)
    data = json.loads(response.text)
    return data['response']['players'][0]['personaname']

steamid = '76561198371968392'
selectedfriends = friends(steamid)[:10]

#  ---Dashboard---------------------------------------------------------------------------------------------------------
root_dashboard = Tk()
root_dashboard.geometry("400x300")
root_dashboard.title("STEAM Dashboard")

#  Label bericht
dashboard_label = Label(root_dashboard, text='Welkom bij het dashboard\nMaak een keuze')
dashboard_label.place(x=130, y=20)

#  Games button
games_btn = Button(root_dashboard, text="Games", command=games)
games_btn.place(x=20, y=100, width=60)

#  Stats button
stats_btn = Button(root_dashboard, text="Stats", command=stats)
stats_btn.place(x=20, y=200, width=60)

#  Friends button
fr_btn = Button(root_dashboard, text="Friends", command=friends_gui)
fr_btn.place(x=200, y=100, width=60)

#  ---Run---------------------------------------------------------------------------------------------------------------
mainloop()
