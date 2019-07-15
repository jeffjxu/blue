import requests
import lxml
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np

# https://www.springfieldspringfield.co.uk/view_episode_scripts.php?tv-show=friends&episode=s01e01
URL = "https://www.springfieldspringfield.co.uk/view_episode_scripts.php?"
tv_show = "tv-show="
episode = "&episode="
season_num = 1
episode_num = 1

title = input("What show would you like?")
tv_show1 = tv_show + title.replace(' ', '-')

title2 = input("What show would you like?")
tv_show2 = tv_show + title2.replace(' ', '-')

title3 = input("What show would you like?")
tv_show3 = tv_show + title3.replace(' ', '-')

list_of_shows = [tv_show1]

df = pd.DataFrame(columns=['Lines', 'Season', 'Episode'])

i = 0

while season_num < 3:  # Looping through to get season_num transcripts
    try:
        # Getting the html from site and extracting specific part with transcript
        print(URL + list_of_shows[i] + episode + 's' + str(season_num).zfill(2) + 'e' + str(episode_num).zfill(2))
        resp = requests.get(URL + list_of_shows[i] + episode + 's' + str(season_num).zfill(2) + 'e' + str(episode_num).zfill(2))
        soup = BeautifulSoup(resp.content, features='lxml')
        script = soup.find("div", {'class':'scrolling-script-container'}).get_text()
        script = re.sub('\\s+', ' ', script)
        script = script.replace('-', '').replace('?', '.').replace('!', '.').replace(',', '').replace('"', '')
        list_of_lines = script.split('. ')
        list_of_lines.remove(list_of_lines[0])

        # Creating a new data frame and appending to df each line in transcript
        for line in list_of_lines:
            if 10 < len(line.split(' ')) < 20:
                new_record = {"Lines": line, "Season": season_num, "Episode": episode_num}
                df = df.append(new_record, ignore_index=True)

        episode_num += 1
    except:
        season_num += 1
        episode_num = 1

    df['Lines'].replace('', np.nan, inplace=True)
    df['Lines'].replace('.', np.nan, inplace=True)
    df.dropna(subset=['Lines'], inplace=True)

season_num = 1
episode_num = 1

# writing transcripts to file in csv form
with open("/Users/Wendy.Hu2@ibm.com/Documents/transcript.csv", 'w') as file:
        file.write(df.to_csv())
