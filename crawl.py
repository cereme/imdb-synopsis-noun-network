import csv
import requests
from bs4 import BeautifulSoup

base_url = "https://www.imdb.com/title/%s/plotsummary#synopsis"

def get_movie_targets():
    movie_list = []
    f = open('targets.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    next(rdr)
    for line in rdr:
        movie_list.append(line[1])
    f.close()
    return movie_list

def get_synopsis_from_imdb_id(imdb_id):
    resp = requests.get(base_url % imdb_id)
    bs = BeautifulSoup(resp.content, 'html.parser')
    synopsis = bs.find('ul', {'id': 'plot-synopsis-content'})
    return synopsis.text