import json
from operator import itemgetter

with open('steam.json', 'r') as steamfile:
    data = json.load(steamfile)

    def sort():
        sortkey = input('sortkey')
        data.sort(key=itemgetter(sortkey))
        count = 0
        for game in data:
            print(game)
            count += 1
        print(count)
    sort()
