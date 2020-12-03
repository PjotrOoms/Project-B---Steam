#  ---Imports-----------------------------------------------------------------------------------------------------------
from tkinter import *
import json
from operator import itemgetter

with open('steam.json', 'r') as steamfile:
    data = json.load(steamfile)

    def naam1():
        game_name = (data[0]['name'])
        text_box.delete("1.0", "end")
        text_box.insert("end-1c", f'{game_name}')


    def sort():
        sortkey = input('sortkey')
        sorted(data, key=itemgetter(sortkey))


#  ---Tkinter-GUI-------------------------------------------------------------------------------------------------------

root_steam = Tk()
root_steam.geometry("600x400")
root_steam.title("STEAM")

#  Label spel
mod_label = Label(root_steam, text="Naam spel:")
mod_label.place(x=30, y=20)

#  Textvak spel
text_box = Text(root_steam, width=60, height=12)
text_box.place(x=100, y=20)

#  Toon naam spel buttton
ber_btn = Button(root_steam, text="Toon spel",  command=naam1)
ber_btn.place(x=20, y=300, width=90)


root_steam.mainloop()
